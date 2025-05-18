from pathlib import Path
def save_model(folder='models',pn='default'):

    # 1. Create general models directory 
    MODEL_PATH = Path(folder)
    MODEL_PATH.mkdir(parents=True, exist_ok=True)

    # 1. Create specific model directory 
    MODEL_NAME = pn
    MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME
    
    MODEL_PATH = Path(MODEL_SAVE_PATH)
    MODEL_PATH.mkdir(parents=True, exist_ok=True)