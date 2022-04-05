
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
import pickle



class Preprocessor:

    def __init__(self):

        self.sklearn_object = make_column_transformer(
        (
                MinMaxScaler(),
                make_column_selector(dtype_exclude=object)
        ),
       (
                OneHotEncoder(sparse=False,
                                categories='auto',
                                handle_unknown='ignore'),
                make_column_selector(dtype_include=object)
        )
        )
        

    def __getattr__(self, attr):
        return getattr(self.sklearn_object, attr)

    def save(self, filename):
        pickle.dump(self.sklearn_object, open(filename, "wb"))