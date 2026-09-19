import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_data(path):
    df = pd.read_csv(path)
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str, default='data/dataset.csv')
    parser.add_argument('--n_estimators', type=int, default=100)
    parser.add_argument('--max_depth', type=int, default=5)
    parser.add_argument('--test_size', type=float, default=0.2)
    parser.add_argument('--random_state', type=int, default=42)
    parser.add_argument('--output', type=str, default='models/random_forest_v1.pkl')
    args = parser.parse_args()

    df = load_data(args.data)
    print(f"Dataset shape: {df.shape}")

    if 'target' not in df.columns:
        raise ValueError("Dataset must contain a 'target' column")

    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=args.random_state, stratify=y if len(y.unique())>1 else None
    )

    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")

    clf = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, random_state=args.random_state)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Accuracy: {acc:.4f}")
    print(f"Model parameters: n_estimators={args.n_estimators}, max_depth={args.max_depth}, random_state={args.random_state}")

    joblib.dump(clf, args.output)
    print(f"Saved model to {args.output}")


if __name__ == '__main__':
    main()
