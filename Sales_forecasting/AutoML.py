import pandas as pd
import numpy as np
import os

import Testing
import Pred_Eval
import importlib
import CreateDir

importlib.reload(Testing)
importlib.reload(Pred_Eval)
importlib.reload(CreateDir)

def product(*args):
    '''Makes the combination for GridSearch'''
    pools = [pool for pool in args[0]]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield list(prod)
def tunning_params(train,
                      valid,
                      hyperparam,
                      type = 'gru',
                      folder='models',
                      metric='MAE'):
    '''
    Search best hyperparameters by grid search
    input: train: dataframe trainset
            valid: dataframe validset
            hyperparam: dict for gridsearch
            folder: folder to save models
    '''
    
    assert train['unique_id'].nunique() == valid['unique_id'].nunique(), 'unique_id numbers must match between train and valid sets'
    
    for pn in train['unique_id'].unique():
        t = train[train['unique_id']==pn]
        v = valid[valid['unique_id']==pn]
           
        mae = float('inf')
        path=folder + '/' + pn

        
        for r in product(list(hyperparam.values())):

            saved=[0]
            hiperparam=dict(zip(hyperparam.keys(),r))
            print(f'PN: {pn} and Evaluating: {hiperparam}')
            model_trained,p=Testing.test(train=t,
                                valid=v,
                                hiper=hiperparam,
                                type='gru'
                                )
            d = Pred_Eval.valuate_prediction_loss(p)            
        
            if d['MAE']<mae:
                mae = d['MAE']
                saved = [1]
                print('*****Saving model*****')
                print(f'*PN: {pn} \n*Hyperparams: {hiperparam} \n*Stats:{d}\n')
                CreateDir.save_model(folder=folder,
                                     pn=pn)
                model_trained.save(path=path,
                           model_index=None,
                           overwrite=True,
                           save_dataset=True)
                cond = os.path.isfile(path+'/doe.csv')
                if cond:
                    df = pd.read_csv(path+'/doe.csv', header = None)
                    #print(df.iloc[:,1])
                    df = df[ df.iloc[:,1]!='h']
                    df = df[ df.iloc[:,1]!=np.nan]
                    df.iloc[:,-1:] = 0
                    #print(df)
                    df.to_csv(path+'/doe.csv', header = False, index = False)
            df = pd.DataFrame([pn] + r + list(d.values()) + saved).transpose()
            #print(df)
            df.to_csv(path+'/doe.csv', header = False, index = False, mode='a')

        cols=['PN'] + list(hyperparam.keys()) + list(d.keys()) + ['Best Model']
        #print('Columnas: ', cols)
        df = pd.read_csv(path+'/doe.csv', header = None)
        df.columns = cols
        df.to_csv(path+'/doe.csv', index = False)
        print('\n\n************************************')
        

    
