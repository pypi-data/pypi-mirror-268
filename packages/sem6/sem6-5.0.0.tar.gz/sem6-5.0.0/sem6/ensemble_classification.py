
def ensemble_classification():
    code = """

    import numpy as np
    import pandas as pd
    import os
    from sklearn.preprocessing import LabelEncoder
    import seaborn as sns
    from sklearn.model_selection import cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import GradientBoostingClassification
    from sklearn.ensemble import RandomForestClassifier, VotingClassifier
    from sklearn.svm import SVC
    from sklearn.datasets import make_classification

    # Load  dataset
    df = pd.read_csv('.csv')
    

    # Label encode categorical variable
    encoder = LabelEncoder()
    df[''] = encoder.fit_transform(df[''])

    # standardise numerical variable
    scaler = StandardScaler()
    df[''] = scaler.fit_transform(df[''])

    # Prepare data for classification
    X = df.drop(['target'],axis=1)
    y = df['target']

    # Define classifiers
    clf1 = LogisticRegression()
    clf2 = RandomForestClassifier()
    clf3 = GradientBoostingClassifier()

    # Perform cross-validation for individual classifiers
    estimators = [('lr', clf1), ('rf', clf2), ('gb', clf3)]
    for estimator in estimators:
        scores = cross_val_score(estimator[1], X, y, cv=10, scoring='accuracy')
        print(estimator[0], np.round(np.mean(scores), 2))

    # Perform cross-validation for Voting Classifier
    vc_hard = VotingClassifier(estimators=estimators, voting='hard')
    vc_soft = VotingClassifier(estimators=estimators, voting='soft')
    print("Hard Voting:", np.round(np.mean(cross_val_score(vc_hard, X, y, cv=10, scoring='accuracy')), 2))
    print("Soft Voting:", np.round(np.mean(cross_val_score(vc_soft, X, y, cv=10, scoring='accuracy')), 2))



    # Classifiers of the same algorithm (SVC)
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=2)
    svm1 = SVC(probability=True, kernel='poly', degree=1)
    svm2 = SVC(probability=True, kernel='poly', degree=2)
    svm3 = SVC(probability=True, kernel='poly', degree=3)
    svm4 = SVC(probability=True, kernel='poly', degree=4)
    svm5 = SVC(probability=True, kernel='poly', degree=5)

    estimators_svm = [('svm1', svm1), ('svm2', svm2), ('svm3', svm3), ('svm4', svm4), ('svm5', svm5)]

    for estimator in estimators_svm:
        scores = cross_val_score(estimator[1], X, y, cv=10, scoring='accuracy')
        print(estimator[0], np.round(np.mean(scores), 2))

    vc_svm = VotingClassifier(estimators=estimators_svm, voting='soft')
    print("Soft Voting with SVMs:", np.round(np.mean(cross_val_score(vc_svm, X, y, cv=10, scoring='accuracy')), 2))
    """
    print(code)
