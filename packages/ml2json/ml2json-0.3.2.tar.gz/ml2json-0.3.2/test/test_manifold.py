# -*- coding: utf-8 -*-

import os
import unittest

import numpy as np
from sklearn.datasets import load_iris, load_digits, fetch_california_housing
from sklearn.manifold import (Isomap, LocallyLinearEmbedding,
                              MDS, SpectralEmbedding, TSNE)

# Allow testing of additional optional dependencies
__optionals__ = []
try:
    from umap import UMAP
    from umap.umap_ import nearest_neighbors
    __optionals__.append('UMAP')
except:
    pass

from src import ml2json


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.iris_data, _ = load_iris(return_X_y=True)
        self.digit_data, _ = load_digits(return_X_y=True)
        self.calhouse_data, _ = fetch_california_housing(return_X_y=True)
        self.calhouse_data = self.calhouse_data[:5000, :]

    def check_model(self, model, model_name, data):
        expected_ft = model.fit_transform(data)

        serialized_dict_model = ml2json.to_dict(model)
        deserialized_dict_model = ml2json.from_dict(serialized_dict_model)

        ml2json.to_json(model, model_name)
        deserialized_json_model = ml2json.from_json(model_name)
        os.remove(model_name)

        for deserialized_model in [deserialized_dict_model, deserialized_json_model]:
            actual_ft = deserialized_model.fit_transform(data)

            if not isinstance(actual_ft, tuple):
                np.testing.assert_array_almost_equal(expected_ft, actual_ft)
            else:
                for x, y in zip(expected_ft, actual_ft):
                    np.testing.assert_array_almost_equal(x, y)

    def test_tsne(self):
        self.check_model(TSNE(init='pca', learning_rate='auto'), 'tsne.json', self.iris_data)
        with self.assertRaises(AssertionError):
            self.check_model(TSNE(init='random', learning_rate='auto'), 'tsne.json', self.iris_data)

    def test_mds(self):
        self.check_model(MDS(random_state=1234), 'mds.json', self.iris_data)

    def test_isomap(self):
        self.check_model(Isomap(n_neighbors=50, n_components=10, neighbors_algorithm='kd_tree'), 'isomap.json', self.iris_data)
        self.check_model(Isomap(n_neighbors=50, n_components=10, neighbors_algorithm='brute'), 'isomap.json', self.iris_data)
        self.check_model(Isomap(n_neighbors=50, n_components=10, neighbors_algorithm='ball_tree'), 'isomap.json', self.iris_data)

    def test_locally_linear_embedding(self):
        self.check_model(LocallyLinearEmbedding(neighbors_algorithm='kd_tree'), 'locally-linear-embedding.json', self.iris_data)
        self.check_model(LocallyLinearEmbedding(neighbors_algorithm='brute'), 'locally-linear-embedding.json', self.iris_data)
        self.check_model(LocallyLinearEmbedding(neighbors_algorithm='ball_tree'), 'locally-linear-embedding.json', self.iris_data)

    def test_spectral_embedding(self):
        self.check_model(SpectralEmbedding(affinity='nearest_neighbors', random_state=1234, n_jobs=-1), 'spectral-embedding.json', self.digit_data)
        self.check_model(SpectralEmbedding(affinity='rbf', random_state=1234, n_jobs=-1), 'spectral-embedding.json', self.iris_data)

    def test_umap(self):
        if 'UMAP' in __optionals__:
            self.check_model(UMAP(random_state=1234, low_memory=False), 'umap.json', self.iris_data)
            self.check_model(UMAP(random_state=1234, output_dens=True, low_memory=False), 'umap.json', self.iris_data)
            precomputed_knn = nearest_neighbors(self.calhouse_data, 15, random_state=1234, metric='euclidean',
                                                metric_kwds={}, angular=False, verbose=False, low_memory=False)
            self.check_model(UMAP(n_neighbors=15, random_state=1234, metric='euclidean', output_dens=False,
                                  precomputed_knn=precomputed_knn, low_memory=False), 'umap.json',
                             self.calhouse_data)
            self.check_model(UMAP(n_neighbors=15, random_state=1234, metric='euclidean', output_dens=True,
                                  precomputed_knn=precomputed_knn, low_memory=False), 'umap.json',
                             self.calhouse_data)
