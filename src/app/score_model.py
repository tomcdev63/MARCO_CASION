import numpy as np 
from sklearn.metrics import *
from sklearn.model_selection import cross_val_score

def score_mae_rmse_median_r2(model, x_val, y_val):

    print("MAE: ", mean_absolute_error(model.predict(x_val), y_val))
    print("RMSE: ", np.sqrt(mean_squared_error(model.predict(x_val), y_val)))
    print("Median abs err: ", median_absolute_error(model.predict(x_val), y_val))
    print("R2: ", model.score(x_val,y_val))

    return model

    
# function to get cross validation scores
def get_cv_scores(model, X_train, y_train):
    
    scores = cross_val_score(model,
                             X_train,
                             y_train,
                             cv=5,
                             scoring='r2')
    print("\nScore après GridSearchCV")
    print('CV Mean: ', np.mean(scores))
    print('STD: ', np.std(scores))

    return scores