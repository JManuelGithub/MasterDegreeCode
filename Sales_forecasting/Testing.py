import importlib
from neuralforecast import NeuralForecast

import Models
importlib.reload(Models)

def test(train, valid, hiper,type='gru'):
    model = NeuralForecast(models = Models.neural_model(**hiper),freq='D')
    #print(train)
    model.fit(train)

    p = model.predict(futr_df=valid)
    #print(p)
    p = p.merge(valid[['ds', 'unique_id', 'y']], on=['ds', 'unique_id'], how='left')
    
    return model, p
