from ._bahc import BiasAwareHierarchicalClustering
from sklearn.cluster import KMeans


class BiasAwareHierarchicalKMeans(BiasAwareHierarchicalClustering):
    """Bias-Aware Hierarchical k-Means Clustering.

    Parameters
    ----------
    max_iter : int
        Maximum number of iterations.
    min_cluster_size : int
        Minimum size of a cluster.
    kmeans_params : dict
        k-means parameters
    
    Attributes
    ----------
    n_clusters_ : int
        The number of clusters found by the algorithm.
    labels_ : ndarray of shape (n_samples,)
        Cluster labels for each point.
    biases_ : ndarray of shape (n_clusters_,)
        Bias values for each cluster.
    
    References
    ----------
    .. [1] J. Misztal-Radecka, B. Indurkhya, "Bias-Aware Hierarchical Clustering for detecting the discriminated
           groups of users in recommendation systems", Information Processing & Management, vol. 58, no. 3, May. 2021.
    
    Examples
    --------
    >>> from bias_detection_tool.clustering import BiasAwareHierarchicalKMeans
    >>> import numpy as np
    >>> X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
    >>> y = np.array([0, 0, 0, 10, 10, 10])
    >>> bias_aware_kmeans = BiasAwareHierarchicalKMeans(max_iter=1, min_cluster_size=1, random_state=12).fit(X, y)
    >>> bias_aware_kmeans.labels_
    array([0, 0, 0, 1, 1, 1], dtype=uint32)
    >>> bias_aware_kmeans.biases_
    array([ 10., -10.])
    """

    def __init__(
        self,
        max_iter,
        min_cluster_size,
        **kmeans_params,
    ):
        super().__init__(max_iter, min_cluster_size)

        if "n_clusters" in kmeans_params and kmeans_params["n_clusters"] != 2:
            raise ValueError(
                f"The parameter `n_clusters` should be 2, got {kmeans_params['n_clusters']}."
            )
        else:
            kmeans_params["n_clusters"] = 2
        
        if "n_init" not in kmeans_params:
            kmeans_params["n_init"] = "auto"
        
        self.kmeans = KMeans(**kmeans_params)

    def _split(self, X):
        return self.kmeans.fit_predict(X)
