import pandas as pd


def simple_preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # For this lab keep preprocessing minimal: fill NAs and return numeric columns
    df = df.copy()
    df = df.select_dtypes(include=['number'])
    df = df.fillna(df.mean())
    return df


if __name__ == '__main__':
    df = pd.read_csv('data/dataset.csv')
    df2 = simple_preprocess(df)
    print('Preprocessed shape:', df2.shape)
