import pandas as pd
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
import numpy as np
from scipy import stats
import statsmodels.stats.multitest as mt
import statsmodels.api as sm


def process_data(data):
       

        # process covariates and design matrix
        
        all_covariates = data.CatCov + data.ConCov

        if not all_covariates or len(data.meta)==1:

                # No covariate provided
                print('You did not input any covariates in CatCov or ConCov parameters, proceeding without them.')
                cov_df=None

        else:


                # check if covariates exist in meta
                if not set(all_covariates).issubset(data.meta.columns):
                    raise ValueError("Invalid elements in CatCov or ConCov. Please check that all covariates names (continuous or categorials) are in the meta DataFrame. ")

                cov_df = data.meta[all_covariates]

                # process categorial covariate
                # drop_first is important to avoid multicollinear
                cov_df = pd.get_dummies(cov_df, columns=data.CatCov, drop_first=True, dtype=int)
                
                
                
        # z scoring
        if data.zscoring:

            # expression data
            # fit a scaler base on the control samples
            scaler = StandardScaler()
            scaler.fit(data.expression_data[data.meta[data.conCol]==0])

            # scale the expression data
            expr = pd.DataFrame(
                scaler.transform(data.expression_data),
                columns=data.expression_data.columns, 
                index=data.expression_data.index
            )
            
            # continuous confounders
            if cov_df is not None and len(data.ConCov)>0:

                # fit a scaler base on the control samples
                scaler = StandardScaler()
                scaler.fit(data.meta.loc[data.meta[data.conCol]==0,data.ConCov])

                # scale the continuous confounders data
                cov_df[data.ConCov] = scaler.transform(data.meta[data.ConCov])
            
        else:  
            expr = data.expression_data
        
        
        #get control and case sample 
        control = data.meta[ data.meta[data.conCol]==0 ].index.values.tolist()
        case = data.meta[ data.meta[data.conCol]==1 ].index.values.tolist()

        return cov_df, expr, control, case
    
    
    
def dyregnet_model(data):
        
        # Fit a model for every edge
        # Detect outliers and calculate zscore and pvalues
        # correct for multiple testing 
        
        # prepare data
        
        if data.cov_df is not None:
            control=pd.merge(data.cov_df.loc[data.control],data.expr, left_index=True, right_index=True).drop_duplicates()
            case=pd.merge(data.cov_df.loc[data.case],data.expr, left_index=True, right_index=True).drop_duplicates()
            covariate_name= list(data.cov_df.columns)
        
        else:
            control=data.expr.loc[data.control]
            case=data.expr.loc[data.case]
            covariate_name=[]
            
        edges = {}
        edges['patient id']=list(case.index.values)
        model_stats = {}
        for tup in tqdm(data.GRN.itertuples()):
                    # pvalues for the same edge for all patients

                    edge = (tup[1],tup[2])
                    
                    # skip self loops
                    if edge[0] != edge[1]:

                        # prepare control for fitting model
                        x_train = control[  [edge[0]] + covariate_name ]
                        x_train = sm.add_constant(x_train, has_constant='add') # add bias
                        y_train = control[edge[1]].values

                        # fit the model
                        model = sm.OLS(y_train, x_train)
                        results = model.fit()
                        
                        model_stats[edge] = [results.rsquared] + list(results.params.values) + list(results.pvalues.values)
                        
                        # get residuals of control
                        resid_control = y_train - results.predict(x_train) 

                        # test data (case or condition)
                        x_test = case[  [edge[0]]+ covariate_name    ]
                        x_test = sm.add_constant(x_test, has_constant='add') # add bias
                        y_test = case[edge[1]].values


                        # define residue for cases
                        resid_case =  y_test - results.predict(x_test)

                        
                        # condition of direction
                        cond = True
                        direction = np.sign(results.params.iloc[1])
                        
                        
                        # two sided p_value as default
                        # if direction_condition is false calculate, two sided p value
                        sides = 2

                        if data.direction_condition: 
                            cond = ( direction * resid_case ) < 0
                            
                            # if direction_condition is true only calculate one sided p value
                            sides = 1

                        
                        # calculate zscore
                        zscore= (resid_case - resid_control.mean()) / resid_control.std()
      


                        # Quality check of the fitness (optionally and must be provided by user)


                        if (data.R2_threshold is not None) and  ( data.R2_threshold > results.rsquared ):
                            # model fit is not that good on training
                            # shrink the zscores
                            edges[edge]= [0.0] * len(zscore)
                            continue

                        #normality test for residuals
                        if  data.normaltest:
                            pv = stats.normaltest(resid_control)[1]
                            if pv> data.normaltest_alpha:
                                # shrink the zscores to 0s
                                edges[edge]= [0.0] * len(zscore)
                                continue


                        # zscores to p values
                        pvalues=stats.norm.sf(abs(zscore)) * sides

                        # correct for multi. testing
                        pvalues=sm.stats.multipletests(pvalues,method='bonferroni',alpha=data.bonferroni_alpha)[1]

                        pvalues= pvalues < data.bonferroni_alpha



                        # direction condition and a p_value 
                        valid= cond * pvalues



                        # shrink the z scores that are not signifcant or not in the condition
                        zscore[~valid]=0.0


                        edges[edge] = np.round(zscore, 1)

                        
                    
        results = pd.DataFrame.from_dict(edges)
        results = results.set_index('patient id')
        
        model_stats_cols = ["R2"] + ["coef_" + coef for coef in ["intercept", "TF"] + covariate_name] + ["pval_" + coef for coef in ["intercept", "TF"] + covariate_name]
        model_stats = pd.DataFrame([model_stats[edge] for edge in results.columns], index=results.columns, columns=model_stats_cols)

        
        return results, model_stats
