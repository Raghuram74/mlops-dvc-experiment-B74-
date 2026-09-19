from sklearn.datasets import load_breast_cancer
import pandas as pd
import os


def main():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target

    os.makedirs('data', exist_ok=True)
    out_path = os.path.join('data', 'dataset.csv')
    df.to_csv(out_path, index=False)
    print(f"Saved dataset to {out_path}")
    print(f"Dataset shape: {df.shape}")
    print("First 5 rows:\n", df.head())


if __name__ == '__main__':
    main()
