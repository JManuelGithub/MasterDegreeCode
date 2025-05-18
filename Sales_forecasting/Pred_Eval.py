from sklearn.metrics import mean_absolute_error, r2_score
def valuate_prediction_loss(p):
    loss = mean_absolute_error(p['y'], p['GRU'])
    r2 = r2_score(p['y'], p['GRU'])
    year=p['GRU'].sum()/p['y'].sum()
    pearson=p['y'].corr(p['GRU'])
    return {'Year':year,'MAE':loss,'R2':r2,'Pearson':pearson}

