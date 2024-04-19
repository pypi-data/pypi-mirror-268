def adaboost():

    code= """
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import GridSearchCV
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define the base decision tree classifier
    base_tree = DecisionTreeClassifier()

    # Define the AdaBoost classifier with the base model
    adaboost = AdaBoostClassifier(base_estimator=base_tree)

    # Define the grid of hyperparameters to search
    param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 1.0]
    }

    # Perform grid search to find the best hyperparameters
    grid_search = GridSearchCV(adaboost, param_grid, cv=5,n_jobs=-1)
    grid_search.fit(X_train, y_train)

    # Get the best parameters found by grid search
    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    # Train the AdaBoost classifier with the best hyperparameters
    best_adaboost_clf = AdaBoostClassifier(base_estimator=base_tree, **best_params)
    best_adaboost_clf.fit(X_train, y_train)

    # Evaluate the classifier on the test set
    accuracy = best_adaboost_clf.score(X_test, y_test)
    print("Accuracy on test set:", accuracy)


    """
    
    print(code)
