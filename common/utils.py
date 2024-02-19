import hmac

import pandas as pd
import streamlit as st
from exception.data_catalogue_exception import DataCatalogueException
from streamlit.logger import get_logger

from .data_catalog_session_name import DataCatalogSessionName

LOGGER = get_logger(__name__)


def read_parq(_: str, s3_file_path: str) -> pd.DataFrame:
    try:
        return pd.read_parquet(s3_file_path)
    except FileNotFoundError:
        LOGGER.error(f"File not found: {s3_file_path}")
        return pd.DataFrame()


def _save_data(df_: pd.DataFrame, path) -> None:
    pass


def _regenerate_configs() -> pd.DataFrame:
    pass


def _regenerate_features_data() -> pd.DataFrame:
    pass


def regenerate_data():
    pass



def load_data_catalogs():
    LOGGER.info('Reading data catalogs...')

    data_catalog_univar_common = read_parq("data-catalogue-univar-common", "mock/data_catalog_univar_common.parquet")
    if data_catalog_univar_common.empty:
        raise DataCatalogueException("Missing or empty data catalogue univar common.")

    data_catalog_univar_1m = read_parq("data-catalogue-univar-1m", "mock/data_catalog_univar_1m.parquet")
    if data_catalog_univar_1m.empty:
        raise DataCatalogueException("Missing or empty data catalogue univar 1m.")

    data_catalog_univar_1h = read_parq("data-catalogue-univar-1h", "mock/data_catalog_univar_1h.parquet")
    if data_catalog_univar_1h.empty:
        raise DataCatalogueException("Missing or empty data catalogue univar 1h.")

    data_catalog_univar_1d17 = read_parq("data-catalogue-univar-1d17", "mock/data_catalog_univar_1d17.parquet")
    if data_catalog_univar_1d17.empty:
        raise DataCatalogueException("Missing or empty data catalogue univar 1d17.")

    st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_COMMON] = data_catalog_univar_common
    st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1M] = data_catalog_univar_1m
    st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1H] = data_catalog_univar_1h
    st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1D17] = data_catalog_univar_1d17


def load_data_catalog_configs():
    LOGGER.info('Reading data catalog configs...')
    data_catalog_configs_df_ = read_parq("data-catalogue", "mock/data_catalog_configs.parquet")

    if data_catalog_configs_df_.empty:
        raise DataCatalogueException("Missing or empty data catalogue configs.")

    st.session_state[DataCatalogSessionName.DATA_CATALOG_CONFIGS] = data_catalog_configs_df_


def load_data():
    LOGGER.warning(st.session_state)
    if DataCatalogSessionName.SESSION_LOADED not in st.session_state:
        load_data_catalogs()
        load_data_catalog_configs()
        st.session_state[DataCatalogSessionName.SESSION_LOADED] = True


def show_data_catalog_info():
    if DataCatalogSessionName.DATA_CATALOG_CONFIGS not in st.session_state:
        st.sidebar.error("**🖕 Use the `Regenerate data catalogue** button to generate a new data catalogue.")
    else:
        data_catalog_df_configs = st.session_state[DataCatalogSessionName.DATA_CATALOG_CONFIGS]

        with st.sidebar.container(border=True):
            st.write("Last process date: ", data_catalog_df_configs['generation_date'].iloc[0])
            st.write("Start date: ", data_catalog_df_configs['start_date'].iloc[0])
            st.write("end date: ", data_catalog_df_configs['end_date'].iloc[0])


def check_password():
    return True

    def password_entered():
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )

    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False
