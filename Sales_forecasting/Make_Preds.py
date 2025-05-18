import pandas as pd
from neuralforecast import NeuralForecast

def load_model(path):
    model = NeuralForecast.load(path=path)
    return model
def add_time_cols(df):
    df['Year']=df.ds.dt.year
    df['Month']=df.ds.dt.month
    df['Week']=df.ds.dt.isocalendar().week
    df['DayofWeek']=df.ds.dt.dayofweek
    return df

def make_pred(valid,folder='models'):
    pred = pd.DataFrame()
    for pn in valid['unique_id'].unique():
        
        df=valid[valid['unique_id']==pn]
        path=folder + '/' + pn
        model = load_model(path = path)
        

        p = model.predict(futr_df=df)
        p = p.merge(df[['ds', 'unique_id', 'y']], on=['ds', 'unique_id'], how='left')
        pred = pred.append(p)
    pred = pred[['ds','unique_id','GRU','y']]
    pred = add_time_cols(pred)
    
    return pred

