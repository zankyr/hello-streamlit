import streamlit as st
from common.data_catalog_session_name import DataCatalogSessionName
from common.utils import load_data, show_data_catalog_info, check_password
from streamlit.logger import get_logger
from streamlit_extras.dataframe_explorer import dataframe_explorer

LOGGER = get_logger(__name__)


def run():
    data_catalog = st.session_state[DataCatalogSessionName.DATA_CATALOG]

    filtered_data = dataframe_explorer(data_catalog, False)
    st.dataframe(filtered_data, use_container_width=True)


st.set_page_config(page_title="Data Catalog - Option 2", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Data Catalog - Option 2 (DataFrame Explorer)")

load_data()
show_data_catalog_info()
run()
