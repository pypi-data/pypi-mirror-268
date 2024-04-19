import pytest
import py
import os

from depot.api import create_cluster, create_provider
from .utils import provider_test, cluster_test, config

def test_create_provider(config, provider_test):
    result = create_provider(config, provider_test)
    assert result == 0
    
def test_create_cluster(config, provider_test, cluster_test):
    result = create_cluster(config, cluster_test)
    assert result == 0