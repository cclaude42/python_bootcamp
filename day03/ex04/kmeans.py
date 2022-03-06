#!/usr/bin/env python3
import numpy as np
import random
import math

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if not filename:
            raise ValueError("must specify a file to read")
        if not isinstance(skip_top, int) or skip_top < 0:
            raise ValueError("skip_top must be a positive integer")
        if not isinstance(skip_bottom, int) or skip_bottom < 0:
            raise ValueError("skip_bottom must be a positive integer")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = None
        self.fulldata = []

    def __enter__(self):
        self.file_obj = open(self.filename, mode="r", encoding="utf-8")
        for line in self.file_obj:
            self.fulldata.append(list(map(str.strip, line.split(self.sep))))
        if all(len(elem) == len(self.fulldata[0]) for elem in self.fulldata):
            return self
        else:
            return None

    def __exit__(self, type, value, traceback):
        self.fulldata = []
        self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
            Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        start = self.skip_top
        end = len(self.fulldata) - self.skip_bottom
        if self.header:
            return self.fulldata[ start + 1 : end ]
        else:
            return self.fulldata[ start : end ]

    def getheader(self):
        """ Retrieves the header from csv file.
            Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header:
            return self.fulldata[0]
        else:
            return None

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        if not isinstance(max_iter, int) or max_iter < 1:
            raise ValueError("Invalid value for max_iter")
        if not isinstance(ncentroid, int) or ncentroid < 1:
            raise ValueError("Invalid value for ncentroid")
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def get_dist(self, entries, point_1, point_2):
        total_dist = 0
        for stat in range(1, entries.shape[1]):
            total_dist += (entries[point_1][stat] - entries[point_2][stat]) ** 2
        return math.sqrt(total_dist)

    def get_mean(self, entries, belonging, centroid, data):
        total = 0
        count = 0
        for entry, ownership in zip(entries, belonging):
            if ownership == centroid:
                total += entry[data]
                count += 1
        return total / count
            

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        n_entries = X.shape[0]
        n_data = X.shape[1] - 1
        self.centroids = [X[i] for i in random.sample(range(n_entries), self.ncentroid)]
        belonging = [-1] * n_entries
        # for _i in range(self.max_iter):
        print(self.centroids)
        for entry in X:
            distances = [self.get_dist(X, centroid[0], entry[0]) for centroid in self.centroids]
            belonging[entry[0]] = distances.index(min(distances))
        print(belonging)
        for centroid in range(self.ncentroid):
            for data in range(1, n_data):
                self.centroids[centroid][data] = self.get_mean(X, belonging, centroid, data)
        print(self.centroids)
            




    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        print("hello")





if __name__ == "__main__":
    k = KmeansClustering()
    with CsvReader("solar_system_census.csv", header=True) as file:
        data = np.array(file.getdata())
        k.fit(data.astype(np.float))
