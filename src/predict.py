import argparse
import pandas as pd
import joblib


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='Path to model file')
    parser.add_argument('--data', type=str, default='data/dataset.csv')
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)

    if 'experiment_version' in df.columns:
        df = df.drop(columns=['experiment_version'])

    X = df.drop(columns=['target'])
    preds = model.predict(X)
    print(f"Total predictions: {len(preds)}")
    print(f"First 10 predictions: {list(preds[:10])}")


if __name__ == '__main__':
    main()
