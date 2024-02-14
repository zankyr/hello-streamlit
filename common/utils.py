import pandas as pd
import streamlit as st
from common.constants import DATA_CATALOG_PATH, DATA_CATALOG_CONFIGS_PATH
from exception.data_catalogue_exception import DataCatalogueException
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def read_parq(_: str, s3_file_path: str) -> pd.DataFrame:
    try:
        return pd.read_parquet(s3_file_path)
    except FileNotFoundError:
        LOGGER.error(f"File not found: {s3_file_path}")
        return pd.DataFrame()


def _save_data(df_: pd.DataFrame, path) -> None:
    pass


@st.cache_data
def load_data_catalog():
    LOGGER.info('Reading data catalog...')
    data_catalog_df_ = read_parq("data-catalogue", DATA_CATALOG_PATH)

    if data_catalog_df_.empty:
        raise DataCatalogueException("Missing or empty data catalogue.")

    return data_catalog_df_


@st.cache_data
def load_data_catalog_configs():
    LOGGER.info('Reading data catalog configs...')
    data_catalog_configs_df_ = read_parq("data-catalogue", DATA_CATALOG_CONFIGS_PATH)

    if data_catalog_configs_df_.empty:
        raise DataCatalogueException("Missing or empty data catalogue configs.")

    return data_catalog_configs_df_


def load_data():
    data_catalog_df = load_data_catalog()
    st.session_state["data_catalog"] = data_catalog_df
    data_catalog_df_configs = load_data_catalog_configs()
    st.session_state["data_catalog_configs"] = data_catalog_df_configs
    st.balloons()


def show_data_catalog_info():
    if "data_catalog" not in st.session_state:
        st.sidebar.error("**👈 Use the `Regenerate data catalogue** button to generate a new data catalogue.")
    else:
        data_catalog_df_configs = st.session_state["data_catalog_configs"]

        with st.sidebar.container(border=True):
            st.write("Last process date: ", data_catalog_df_configs['generation_date'].iloc[0])
            st.write("Start date: ", data_catalog_df_configs['start_date'].iloc[0])
            st.write("end date: ", data_catalog_df_configs['end_date'].iloc[0])