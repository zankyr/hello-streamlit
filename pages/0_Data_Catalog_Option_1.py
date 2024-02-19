import streamlit as st
from common.data_catalog_session_name import DataCatalogSessionName
from common.utils import load_data, show_data_catalog_info, check_password
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    data_catalog = st.session_state[DataCatalogSessionName.DATA_CATALOG]

    tickers = list(data_catalog['ticker'].unique())

    tickers = st.multiselect(
        key="tickers",
        label="Choose ticker(s)",
        options=tickers,
        default=tickers
    )

    sources = list(data_catalog['source_config'].unique())
    sources = st.multiselect(
        key="sources",
        label="Choose source(es)",
        options=sources,
        default=sources
    )

    if not tickers and not sources:
        st.error("Please select at least one ticker or source.")
    else:
        if tickers and sources:
            filtered_data = data_catalog.loc[data_catalog['ticker'].isin(tickers)
                                             & data_catalog['source_config'].isin(sources)]
        elif tickers:
            filtered_data = data_catalog.loc[data_catalog['ticker'].isin(tickers)]
        else:
            filtered_data = data_catalog.loc[data_catalog['source_config'].isin(sources)]
        st.dataframe(filtered_data, use_container_width=True)


st.set_page_config(page_title="Data Catalog - Option 1", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Data Catalog - Option 1 (Multiselect)")

load_data()
show_data_catalog_info()
run()
