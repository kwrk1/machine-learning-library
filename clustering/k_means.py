import numpy as np

class KMeans:
    def __init__(self, k = 3):
        self.k = k
        self.centroids = None

    @staticmethod
    def euclidean_distance(x: np.array, centroids: np.ndarray) -> np.array:
        """
        Calculates distance of a data point x 
        to all k centroids.
        Returns an array with each distance.

        x (numpy.array): Data point (vector)
        centroids (numpy.ndarray): Centroids in a matrix (each row is one centroid) 
        """
        # change axis to 1 because every centroid is stored in one row
        return np.sqrt(np.sum((x - centroids)**2, axis = 1))      

    def fit(self, X: np.ndarray, max_iterations = 500, threshold = 0.001) -> np.array:
        """
        Assigns each data point the best cluster by calculating the distances.

        X (numpy.ndarray): Matrix of data points (each row is one data point) 
        max_iterations (int, optional): Number of iterations to update the centroids, default: 500
        threshold (float, optional): Stopping criterion to interrupt the update iterations, default: 0.001
        """
        # axis 0: rows, axis 1: columns
        # Centroids as k x len(X) matrix with one centroid each row
        self.centroids = np.random.uniform(np.amin(X), np.amax(X), size = (self.k, X.shape[1]))     
    
        for _ in range(max_iterations):
            data_point_to_cluster = []      # stores cluster number each data point belongs to

            for data_point in X:
                distances = KMeans.euclidean_distance(data_point, self.centroids)
                cluster_num = np.argmin(distances)          
                data_point_to_cluster.append(cluster_num)
            
            data_point_to_cluster = np.array(data_point_to_cluster)

            cluster_indices = []            # array of arrays 

            for i in range(self.k):
                # argwhere returns array of indices where condition true
                # each cluster has an array of indices of its associated data points
                cluster_indices.append(np.argwhere(data_point_to_cluster == i))     

            cluster_centers = []            # to recalculate the new cluster centers

            for i, indices in enumerate(cluster_indices):
                if len(indices) == 0:   # if a centroid has no data point
                    cluster_centers.append(self.centroids[i])
                else:
                    # each row of the X matrix is a data point
                    # calculate mean for each coordinate (axis 0) for each selected data point (indices)
                    # returned array only has one element, but is an array of array, therefore [0]
                    cluster_centers.append(np.mean(X[indices], axis = 0)[0])

            if np.max(self.centroids - np.array(cluster_centers)) < threshold:      # stopping criterion to prevent stagnation
                break
            else:
                self.centroids = np.array(cluster_centers)                          # update centroids
                
        return data_point_to_cluster