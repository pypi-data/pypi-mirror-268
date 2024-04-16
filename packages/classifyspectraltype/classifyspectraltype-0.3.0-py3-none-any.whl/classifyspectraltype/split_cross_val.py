import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def split_cross_val(preprocessed_data, target, split=0.75, folds=5):
    """
    Purpose:
    Splitting the data and calculate the cross validation results for Random forests and logistic regression models.

    Parameters:
    - preprocessed_data: csv, cleaned and preprocessed data
    - target: string target column name
    - split: testing-training data set split (default: 75% training, 25% testing)
    - folds: number of folds for cross-validation (default: 5 folds)

    Returns:
    - dictionary, containing cross validation results of two models
    """

    data = pd.read_csv(preprocessed_data)
    results = {}
    # Setting y to our target variable
    y = data[target]

    # Our predictors will be the following 5 features
    X = data[["sy_umag", "sy_gmag", "sy_rmag", "sy_imag", "sy_zmag"]]

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=(1 - split), random_state=123
    )

    # Logistic Regression cross validation
    pipe = make_pipeline(StandardScaler(), LogisticRegression())
    lr_df = pd.DataFrame(
        cross_validate(pipe, X_train, y_train, cv=folds, return_train_score=True)
    ).mean()
    results["logistic"] = pd.Series(
        {col: f"{mean:.3f}" for col, mean in zip(lr_df.index, lr_df)}
    )

    # RandomForest Classifier cross validation
    rfc = RandomForestClassifier(n_estimators=275, random_state=123)
    pipe2 = make_pipeline(StandardScaler(), rfc)
    pipe2.fit(X_train, y_train)
    rfc_df = pd.DataFrame(
        cross_validate(pipe2, X_train, y_train, cv=folds, return_train_score=True)
    ).mean()
    results["random_forest"] = pd.Series(
        {col: f"{mean:.3f}" for col, mean in zip(rfc_df.index, rfc_df)}
    )

    return results
