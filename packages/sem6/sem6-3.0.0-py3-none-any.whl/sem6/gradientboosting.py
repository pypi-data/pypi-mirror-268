def gradientboosting():
    code = """
        # 1. Loading
    import pandas as pd
    import numpy as np

    # Load your dataset
    df = pd.read_csv('your_dataset.csv')

    # a. Fill all the Null values with appropriate filler values (mean, median, or a specific value)
    df.fillna(df.mean(), inplace=True)

    # 2. Basic EDA
    import matplotlib.pyplot as plt
    import seaborn as sns

    # a. Insights - Document initial insights about the dataset after looking at the data
    # For example, checking df.describe() and df.info() to get an overview of the data

    # b. Plot KDEs for numerical features to understand the distribution
    for column in df.select_dtypes(include=np.number).columns:
        sns.kdeplot(data=df, x=column)
        plt.title(f'Distribution of {column}')
        plt.show()

    # c. SNS Heatmap - Visualizing the correlation between features
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()

    # 3. Preprocessing
    from sklearn.preprocessing import LabelEncoder, StandardScaler

    # a. Label Encoding for categorical variables if any
    encoder = LabelEncoder()
    for column in df.select_dtypes(include=['object', 'category']).columns:
        df[column] = encoder.fit_transform(df[column])

    # b. Feature engineering - Create or transform features
    # Example: Adding a square of a feature (adjust 'feature_name' accordingly)
    df['feature_squared'] = df['feature_name'] ** 2

    # c. Standard scaler - Standardize features by removing the mean and scaling to unit variance
    scaler = StandardScaler()
    features = df.columns.drop('target')  # Replace 'target' with the name of your target column
    df[features] = scaler.fit_transform(df[features])

    # 4. Gradient Boosting for Classification
    from sklearn.ensemble import GradientBoostingClassifier

    # a. Import and declare the model
    # Gradient Boosting is part of the ensemble family, boosting category

    # b. Instantiate the model
    gb_model = GradientBoostingClassifier(random_state=42)

    # 5. Train/Test Split and model training
    from sklearn.model_selection import train_test_split

    # Split the data into training and testing sets
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # c. Fit the model on the training data and predict on the test data
    gb_model.fit(X_train, y_train)
    predictions = gb_model.predict(X_test)

    # 6. Use appropriate accuracy metrics
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    # Calculate metrics
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("Classification Report:\n", classification_report(y_test, predictions))

    #8 Adding Gridsearch:
    param_grid = {
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [50, 100, 150],
    'max_depth': [1,3, 5, 7],
    }

    
    grid_search = GridSearchCV(gb_model, param_grid, cv=5, n_jobs=-1)

    grid_search.fit(x_train, y_train)

    # Print the best parameters found
    print("Best parameters:", grid_search.best_params_)

    # Evaluate the model with the best parameters on the test set
    best_lgb = grid_search.best_estimator_
    y_pred = best_lgb.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)


    """
    print(code)
