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
    LOGGER.info('Reading data catalog...')

    data_catalog_df = read_parq("data-catalogue", "mock/data_catalog.parquet")

    st.session_state[DataCatalogSessionName.DATA_CATALOG] = data_catalog_df


def load_data_catalog_configs():
    LOGGER.info('Reading data catalog configs...')
    data_catalog_configs_df_ = read_parq("data-catalogue", "mock/data_catalog_configs.parquet")

    if data_catalog_configs_df_.empty:
        raise DataCatalogueException("Missing or empty data catalogue configs.")

    st.session_state[DataCatalogSessionName.DATA_CATALOG_CONFIGS] = data_catalog_configs_df_


def load_data():
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
