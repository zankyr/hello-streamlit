import streamlit as st
from common.data_catalog_session_name import DataCatalogSessionName
from common.utils import load_data, show_data_catalog_info, check_password
from streamlit.logger import get_logger
from streamlit_extras.dataframe_explorer import dataframe_explorer

LOGGER = get_logger(__name__)


def run():
    data_catalog_univar_common = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_COMMON]
    data_catalog_univar_1m = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1M]
    data_catalog_univar_1h = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1H]
    data_catalog_univar_1d17 = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1D17]

    st.write("## Data Catalog - Univar Common")
    filtered_univar_common_df = dataframe_explorer(data_catalog_univar_common, False)
    st.dataframe(filtered_univar_common_df, use_container_width=True)

    st.write("## Data Catalog - Univar 1m")
    filtered_1m_df = dataframe_explorer(data_catalog_univar_1m, False)
    st.dataframe(filtered_1m_df, use_container_width=True)

    st.write("## Data Catalog - Univar 1h")
    filtered_1h_df = dataframe_explorer(data_catalog_univar_1h, False)
    st.dataframe(filtered_1h_df, use_container_width=True)

    st.write("## Data Catalog - Univar 1d17")
    filtered_1d17_df = dataframe_explorer(data_catalog_univar_1d17, False)
    st.dataframe(filtered_1d17_df, use_container_width=True)


st.set_page_config(page_title="Data Catalog - Option 2", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Data Catalog - Option 2 (DataFrame Explorer)")

load_data()
show_data_catalog_info()
run()
