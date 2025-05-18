from neuralforecast.models import GRU
from neuralforecast.losses.pytorch import DistributionLoss
def neural_model (**kwargs):
    #print('kwargs es: ',kwargs)
    models = [GRU(futr_exog_list = ['Month','Week','DayofWeek'],
                 **kwargs)]

    
    #print(model[0])
    return models

