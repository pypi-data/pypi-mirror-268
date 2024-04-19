def dbscan():
    code = """

    from sklearn.cluster import DBSCAN
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_circles
    # Sample data for linear 
    X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])

    # Visualize sample data
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

    # DBSCAN clustering
    db = DBSCAN(eps=10, min_samples=2)
    db.fit(X)
    db.labels_

    # Sample data for non linear
    X, _ = make_circles(n_samples=500, factor=.5, noise=.03, random_state=4)

    # Apply DBSCAN to the dataset
    dbscan = DBSCAN(eps=0.1, min_samples=5)
    clusters = dbscan.fit_predict(X)

    # Plotting
    plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis', marker='o')
    plt.title("DBSCAN Clustering of Concentric Circles")
    plt.xlabel("Feature 0")
    plt.ylabel("Feature 1")
    plt.show()
    """
    print(code)




def hierarchical():
    code = """

    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import scipy.cluster.hierarchy as shc
    from sklearn.cluster import AgglomerativeClustering

    # Load data
    data = pd.read_csv('.csv')

    # Extract relevant columns
    data = data[[""]]

    # Visualize dendrogram
    plt.figure(figsize=(10, 7))
    plt.title("Customer Dendograms")
    dend = shc.dendrogram(shc.linkage(data, method='ward'))

    # Perform Agglomerative Clustering
    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    labels_ = cluster.fit_predict(data)

    # Visualize clustered data
    plt.figure(figsize=(10, 7))
    plt.scatter(data[:, 0], data[:, 1], c=cluster.labels_, cmap='rainbow')
    plt.show()
    """
    print(code)


def kmeans():
    code="""
    from sklearn.cluster import KMeans

    
    # Finding optimal number of clusters using : ELBOW METHOD
    data = df[]
    inertias = []

    for i in range(1,10):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1,11), inertias, marker='o')
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()

    # Calculate silhouette score for different number of clusters
    silhouette_scores = []
    for i in range(2, 11):  # Assuming you want to check clusters from 2 to 10
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        score = silhouette_score(data, kmeans.labels_)
        silhouette_scores.append(score)

    # Plot silhouette scores
    plt.plot(range(2, 11), silhouette_scores, marker='o')
    plt.title('Silhouette Score')
    plt.xlabel('Number of clusters')
    plt.ylabel('Silhouette Score')
    plt.show()

    #Performing kmeans

    kmeans = KMeans(n_clusters=optimal clusters from doing elbow)
    kmeans.fit(data)


    plt.scatter(x, y, c=kmeans.labels_)
    plt.show()

    """
    print(code)

