from score_model import score_mae_rmse_median_r2, get_cv_scores
from sklearn.model_selection import GridSearchCV
import mlflow
import numpy as np


def trainmodel(model,X_train, y_train, X_test, y_test):

    model = model()
    model.fit(X_train, y_train);

    print("Score du jeu TRAIN")
    score_mae_rmse_median_r2(model, X_train, y_train)
    print("\nScore du jeu TEST")
    score_mae_rmse_median_r2(model, X_test, y_test)

    return model


def trainmodelGSCV(model, X_train, y_train, param_grid):

    grid = GridSearchCV(model, cv=5, param_grid=param_grid)
    grid.fit(X_train, y_train)
    score = get_cv_scores(model, X_train, y_train)
    print(f"Le meilleur score est de: {grid.best_score_} avec {grid.best_params_}")

    with mlflow.start_run():
        mlflow.log_params(grid.best_params_)
        mlflow.log_metric("CV Mean", np.mean(score))
        mlflow.log_metric("STD", np.std(score))
        mlflow.log_metric("R2", grid.best_score_)

    return grid