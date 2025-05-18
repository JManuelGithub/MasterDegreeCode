import pandas as pd

from neuralforecast.losses.pytorch import DistributionLoss, MSE, RMSE, MAE

def read_best_model(folder,lead_types,h):
    df = pd.DataFrame()
    hiper = {}
    losses = {'DistributionLoss()' : DistributionLoss(distribution='Poisson', level=[90]),
              'MAE()' : MAE(),
              'MSE()' : MSE(),
              'RMSE()' : RMSE()}
    for _ in lead_types:
        #print(_)
        path = folder + '/' + _ + '/doe.csv'
        data = pd.read_csv(path)
        data = data[data.iloc[:,-1]==1]
        #print(data)
        df = data.iloc[:,1:-5]
        df['h'] = h
        print(df['loss'].iloc[0])
        df['loss'] = losses[df['loss'].iloc[0]]
        #print(df)
        best_hiper = df.to_dict('list')
        #print(best_hiper)
        hiper[_] = best_hiper
        #max_steps = data[data['PN']==_]['max_steps'].iloc[0]
        #print(max_steps)
        #df = df.append(data,ignore_index=True)
    return hiper

