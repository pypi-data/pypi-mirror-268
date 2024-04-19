# Mentera/voting_regressor.py
def ensemble_regression():
    code = """

    from sklearn.datasets import load_boston
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import cross_val_score
    from sklearn.ensemble import VotingRegressor

    # Load Boston housing dataset
    X, y = load_boston(return_X_y=True)

    # Define estimators
    lr = LinearRegression()
    dt = DecisionTreeRegressor()
    rf = RandomForestRegressor()
    estimators = [('lr', lr), ('dt', dt), ('gb', svr)]

    # Evaluate individual estimators
    for estimator in estimators:
        scores = cross_val_score(estimator[1], X, y, scoring='r2', cv=10)
        print(estimator[0], np.round(np.mean(scores), 2))

    # Evaluate Voting Regressor
    vr = VotingRegressor(estimators)
    scores = cross_val_score(vr, X, y, scoring='r2', cv=10)
    print("Voting Regressor", np.round(np.mean(scores), 2))


    # Using different depths for Decision Trees
    dt1 = DecisionTreeRegressor(max_depth=1)
    dt2 = DecisionTreeRegressor(max_depth=3)
    dt3 = DecisionTreeRegressor(max_depth=5)
    dt4 = DecisionTreeRegressor(max_depth=7)
    dt5 = DecisionTreeRegressor(max_depth=None)
    estimators = [('dt1', dt1), ('dt2', dt2), ('dt3', dt3), ('dt4', dt4), ('dt5', dt5)]

    # Evaluate individual Decision Trees
    for estimator in estimators:
        scores = cross_val_score(estimator[1], X, y, scoring='r2', cv=10)
        print(estimator[0], np.round(np.mean(scores), 2))

    # Evaluate Voting Regressor with Decision Trees
    vr = VotingRegressor(estimators)
    scores = cross_val_score(vr, X, y, scoring='r2', cv=10)
    print("Voting Regressor", np.round(np.mean(scores), 2))
    """
    print(code)
