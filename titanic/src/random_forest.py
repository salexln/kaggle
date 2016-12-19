import clean_data as cd
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def run_random_forest():
    print '*'*27
    print '   Running Random Forest   '
    print '*'*27

    df = pd.DataFrame.from_csv('../data/train.csv')

    df = cd.clean_data(df)

    forest = RandomForestClassifier(n_estimators=100)

    X = df.ix[:, 1:]
    y = df.ix[:, 0]
    forest = forest.fit(X, y)

    output = forest.predict(X)
    print output


if __name__ == "__main__":

    run_random_forest()
