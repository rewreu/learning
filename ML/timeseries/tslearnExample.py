#%%
from tslearn.clustering import TimeSeriesKMeans
from tslearn.generators import random_walks
from tslearn.utils import to_time_series_dataset
#%%
X = random_walks(n_ts=50, sz=32, d=1)
km = TimeSeriesKMeans(n_clusters=3, metric="euclidean", max_iter=5,
                       random_state=0).fit(X)
km.cluster_centers_.shape

#%%
km_dba = TimeSeriesKMeans(n_clusters=3, metric="dtw", max_iter=5,
                           max_iter_barycenter=5,
                           random_state=0).fit(X)
km_dba.cluster_centers_.shape

#%%
km_sdtw = TimeSeriesKMeans(n_clusters=3, metric="softdtw", max_iter=5,
                            max_iter_barycenter=5,
                            metric_params={"gamma": .5},
                            random_state=0).fit(X)
km_sdtw.cluster_centers_.shape
#%%
X_bis = to_time_series_dataset([[1, 2, 3, 4],
                                 [1, 2, 3],
                                 [2, 5, 6, 7, 8, 9]])
km = TimeSeriesKMeans(n_clusters=2, max_iter=5,
                       metric="dtw", random_state=0).fit(X_bis)
km.cluster_centers_.shape