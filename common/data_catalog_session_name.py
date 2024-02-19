from enum import Enum


class DataCatalogSessionName(Enum):
    SESSION_LOADED = "session_loaded",
    DATA_CATALOG = "data_catalog",
    DATA_CATALOG_CONFIGS = 'data_catalog_configs',
    DATA_CATALOG_UNIVAR_COMMON = "data_catalog_univar_common",
    DATA_CATALOG_UNIVAR_1M = "data_catalog_univar_1m",
    DATA_CATALOG_UNIVAR_1H = "data_catalog_univar_1h",
    DATA_CATALOG_UNIVAR_1D17 = "data_catalog_univar_1d17",
