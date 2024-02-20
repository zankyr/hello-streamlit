import streamlit as st
from common.data_catalog_session_name import DataCatalogSessionName
from common.utils import load_data, show_data_catalog_info, check_password
from streamlit.logger import get_logger
from streamlit_extras.dataframe_explorer import dataframe_explorer

LOGGER = get_logger(__name__)


def run():
    data_catalog = st.session_state[DataCatalogSessionName.DATA_CATALOG]

    filtered_data = dataframe_explorer(data_catalog, False)

    # Magic formula to define the height of the dataframe_explorer:
    # Show `rows_to_show` rows and the header, 35 is the height of each row, 3 is the height of the borders
    rows_to_show = len(filtered_data)
    height = (rows_to_show + 1) * 35 + 3

    st.dataframe(filtered_data, use_container_width=True, height=height)


st.set_page_config(page_title="Data Catalog", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Data Catalog")

load_data()
show_data_catalog_info()
run()
