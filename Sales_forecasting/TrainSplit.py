import pandas as pd
def set_train_valid(df,ini,fin,div):
    '''
        input: df: dataframe to split
                ini: inicial date
                fin: final date
                div: split date, considered in valid set
        output: train: dataframe for training
                valid: dataframe for validation
    
    '''
    df=df[['PostingDate','Quantity','PN10','Year','Month','Week','DayofWeek']]
    df=df.rename(columns={'PostingDate': 'ds', 'Quantity': 'y', 'PN10': 'unique_id'})#Nixtla require this names
    df=df.loc[df['ds'] >= ini]
    df=df.loc[df['ds'] <= fin]
    df=df.groupby(['ds','unique_id','Year','Month','Week','DayofWeek'])['y'].sum().reset_index()
    train = df.loc[df['ds'] < div]
    valid = df.loc[df['ds'] >= div]
    return train,valid

