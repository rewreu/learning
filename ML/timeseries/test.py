from tslearn.clustering import TimeSeriesKMeans
from tslearn.generators import random_walks
from tslearn.utils import to_time_series_dataset
X_bis = to_time_series_dataset([[1, 2, 3, 4],
                                 [1, 2, 3],
                                 [2, 5, 6, 7, 8, 9]])
km = TimeSeriesKMeans(n_clusters=2, max_iter=5,
                       metric="dtw", random_state=0).fit(X_bis)