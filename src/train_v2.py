import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def load_data(path='data/dataset.csv'):
    df = pd.read_csv(path)
    return df


def main():
    df = load_data()
    # If experiment_version exists, remove it before training
    if 'experiment_version' in df.columns:
        df = df.drop(columns=['experiment_version'])

    if 'target' not in df.columns:
        raise ValueError("Dataset must contain a 'target' column")

    X = df.drop(columns=['target'])
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Dataset shape: {df.shape}")
    print(f"Training samples: {X_train.shape[0]}")
    print(f"Testing samples: {X_test.shape[0]}")

    clf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Accuracy: {acc:.4f}")
    print(f"Model parameters: n_estimators=200, max_depth=10, random_state=42")

    # Save model
    import os
    os.makedirs('models', exist_ok=True)
    out_path = 'models/random_forest_v2.pkl'
    joblib.dump(clf, out_path)
    print(f"Saved model to {out_path}")


if __name__ == '__main__':
    main()
