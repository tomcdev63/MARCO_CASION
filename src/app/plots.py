import seaborn as sns
import matplotlib.pyplot as plt
import math

from seaborn.palettes import color_palette


def plot_validation(model, X_train, y_train, X_test, y_test, target, model_name, COLOR1, COLOR2):
        
    y_train_pred_ll = model.predict(X_train)
    y_test_pred_ll = model.predict(X_test)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 6))

    ### Validation Plot
    sns.scatterplot(x=y_train, y=y_train_pred_ll, ax=ax1, alpha=0.8, label='train', color=COLOR1)
    sns.scatterplot(x=y_test, y=y_test_pred_ll, ax=ax1, alpha=0.8, label='test', color=COLOR2)
    sns.lineplot(y_train, y_train, ax=ax1, color='gray', alpha=0.5)
    ax1.set_xlabel('True values', fontsize=12); ax1.set_ylabel('Predicted values', fontsize=12)

    ### Residuals Plot
    sns.scatterplot(x=range(len(y_train)), y=y_train-y_train_pred_ll, ax=ax2, alpha=0.8, label='train', color=COLOR1)
    sns.scatterplot(x=range(len(y_train), len(target)), y=y_test-y_test_pred_ll, ax=ax2, alpha=0.8, label='test', color=COLOR2)
    ax2.set_ylabel('Residual errors', fontsize=12)

    ### Residuals Distribution
    sns.distplot(y_train-y_train_pred_ll, ax=ax3, label='train', color=COLOR1)
    sns.distplot(y_test-y_test_pred_ll, ax=ax3, label='test', color=COLOR2)
    ax3.legend()
    ax1.set_title(f'Validation Plot {model_name}'); ax2.set_title(f'Residuals Plot {model_name}'); ax3.set_title(f'Residuals Distribution {model_name}')
    plt.show()


def plot_validation_bis(model, X_train, y_train, X_test, y_test, target, model_name, COLOR1, COLOR2):
        
    y_train_pred_ll = model.predict(X_train)
    y_test_pred_ll = model.predict(X_test)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(30, 6))

    ### Validation Plot
    sns.scatterplot(x=y_train, y=y_train_pred_ll, ax=ax1, alpha=0.8, label='train', color=COLOR1)
    sns.scatterplot(x=y_test, y=y_test_pred_ll, ax=ax1, alpha=0.8, label='test', color=COLOR2)
    sns.lineplot(y_train, y_train, ax=ax1, color='gray', alpha=0.5)
    ax1.set_xlabel('True values', fontsize=12); ax1.set_ylabel('Predicted values', fontsize=12)

    ### Residuals Distribution
    sns.distplot(y_train-y_train_pred_ll, ax=ax2, label='train', color=COLOR1)
    sns.distplot(y_test-y_test_pred_ll, ax=ax2, label='test', color=COLOR2)
    ax2.legend()
    ax1.set_title(f'Validation Plot {model_name}'); ax2.set_title(f'Residuals Distribution {model_name}')
    plt.show()


def plot_residu(data, model_str,ax, target, COLOR):

    sns.distplot(data[target]-data[model_str], ax=ax, label='train', color=COLOR)
    ax.legend()
    ax.set_title(f'Validation Plot {model_str}'); ax.set_title(f'Residuals Plot {model_str}'); ax.set_title(f'Residuals Distribution {model_str}')



def plot_r2(data, model_str,ax, target, y_train, COLOR):

    ### Validation Plot
    sns.scatterplot(data=data, x=target, y=model_str, ax=ax, alpha=0.8, label=model_str, color=COLOR)
    sns.lineplot(y_train, y_train, ax=ax, color='gray', alpha=0.5)
    ax.set_xlabel('True values', fontsize=12); ax.set_ylabel('Predicted values', fontsize=12)


def catplot(feature1, feature2, data, PALETTE, TITRE):

    plt.figure(figsize=(30,6))

    sns.catplot(x=feature1, y=feature2, palette=PALETTE, data=data, kind="bar", aspect=3)
    sns.despine()
    plt.title(TITRE)
    plt.show()


def catplot2(feature1, feature2, data, PALETTE, TITRE):
    

    plt.figure(figsize=(30,6))

    sns.catplot(x=feature2, y=feature1, palette=PALETTE, data=data, kind="bar", aspect=3)
    sns.despine()
    plt.title(TITRE)
    plt.show()




def featurerepartition(series, title, COLOR):
    
    """Fonction qui permet de ploter la ditribution d'une serie et de lui ajouter un titre

    Args:
        series (serie): Colonne souhaitée
        title (str): Titre
    """

    fig = plt.subplots(figsize=(14,8))
    sns.histplot(series, kde=True, stat='density',discrete=True,palette="ch:start=.2,rot=-.3", color=COLOR)
    sns.despine()
    plt.title(title)
    plt.show()



def quali_quanti(df):

    """Fonction qui permet d'afficher le nombre de variables quantitatives et qualitatives

    Returns:
        variables quantitatives: Retourne les variables quantitatives
    """
    num_vars = df.dtypes[df.dtypes != "object"].index
    cat_vars = df.dtypes[df.dtypes == "object"].index

    print("Nombres des variables quantitatives: ", len(num_vars))
    print("Nombres des variables qualitatives: ", len(cat_vars))
    return num_vars



def featuresrepartition(df, COLOR):
    
    num_vars = quali_quanti(df)
    n = len(num_vars)

    if 1 <= n <= 3: 
        nb_col = 3
        nb_ind = 1
    elif n == 4: 
        nb_col = 2
        nb_ind = 2
    elif n >= 5:
        nb_col = 3
        nb_ind = int(math.ceil(n / 3))

    _, axes = plt.subplots(nb_ind, nb_col, figsize=(7 * nb_col, 5 * nb_ind))

    axes = axes.flatten()

    for ax, c in zip(axes, df[num_vars]):
        sns.distplot(df[c].dropna().values, ax=ax, label=c, color=COLOR)
        plt.setp(ax.get_xticklabels(), rotation=55, fontsize=8)
        ax.set_yticks([])
        ax.legend()

    nb_axes_trop = len(axes) - n
    if nb_axes_trop != 0:
        for i in range(nb_axes_trop):
            axes[-i - 1].axis('off')


def countplot(data, serie, PAL, title):

    plt.figure(figsize = (30,10))
    sns.countplot(data[serie], palette=PAL, order=data[serie].value_counts().index)
    plt.title(title)
    plt.xticks(rotation= 45)
    plt.show()



def barplot(data, serie, TARGET, PAL, COLOR, COLOR2, title):

    plt.figure(figsize=(30,10))
    sns.barplot(x=data[serie], y=data[TARGET], palette=PAL)
    plt.xlabel('', fontsize=15, color=COLOR)
    plt.ylabel(f"{TARGET}\n", fontsize=15, color=COLOR2)
    plt.title(f"{title}\n", fontsize=18, color=COLOR2)
    plt.xticks(rotation= 45)
    plt.tight_layout()



def scatter(data, serie1, serie2, titre):

    plt.figure(figsize=(30,10))
    sns.scatterplot(y = serie1,x = serie2, palette="ch:start=.2,rot=-.3", data=data, hue=serie1)
    plt.title(titre)
    plt.show()


def pairplots(data, list_x_var, list_y_var, titre):
    plt.figure(figsize=(30,10))
    sns.pairplot(data,x_vars=list_x_var, y_vars=list_y_var,kind="reg")
    plt.title(titre)
    plt.show()


def joinplot(data, serie1, serie2, serie3, hue, titre):
    plt.figure(figsize=(30,10))
    g = sns.jointplot(
        data = data[data[serie1]], x=serie2, y=serie3, hue=hue, kind="kde"
    )
    plt.title(titre)
    plt.show()