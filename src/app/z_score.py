from scipy import stats

def zscore(data, serie):

    """Permet de calculer le z_score d'une serie et de ne garder que les index compris dans ce z_score au sein des données

    Args:
        data (DataFrame): Notre DataFrame
        serie (Series): Notre feature
    """
    
    data[f"Z_score_{serie}"] = stats.zscore(data[serie])
    data = data[data[f"Z_score_{serie}"].between(left = -3, right = 3 )]
    data.reset_index(inplace=True, drop=True)
    del data[f"Z_score_{serie}"]

    return data