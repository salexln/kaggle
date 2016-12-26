import clean_data as cd
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def run_random_forest():
    print '*'*27
    print '   Running Random Forest   '
    print '*'*27

    train_df = pd.DataFrame.from_csv('../data/train.csv')

    train_df = cd.clean_data(train_df)

    # Initialize the model
    rf_model = RandomForestClassifier(n_estimators=1000, max_features=2, oob_score=True)
    features = ["Gender","Pclass","SibSp","Age*Class","Fare"]

    # Train the model
    rf_model.fit(X=train_df[features], y=train_df["Survived"])
    print("OOB accuracy: ")
    print(rf_model.oob_score_)

    # for feature, imp in zip(features, rf_model.feature_importances_):
    #     print(feature, imp)


    # Read and prepare test data
    titanic_test = pd.read_csv('../data/test.csv')
    titanic_test = cd.clean_data(titanic_test)


    test_preds = rf_model.predict(X= titanic_test[features])


    # Create a submission for Kaggle
    submission = pd.DataFrame({"PassengerId":titanic_test["PassengerId"], "Survived":test_preds})

    # Save submission to CSV
    submission.to_csv("../results/random_forest_submission.csv", index=False)


if __name__ == "__main__":

    run_random_forest()
