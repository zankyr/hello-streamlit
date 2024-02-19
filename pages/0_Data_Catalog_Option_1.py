import streamlit as st
from common.data_catalog_session_name import DataCatalogSessionName
from common.utils import load_data, show_data_catalog_info, check_password
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    data_catalog_univar_common = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_COMMON]
    data_catalog_univar_1m = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1M]
    data_catalog_univar_1h = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1H]
    data_catalog_univar_1d17 = st.session_state[DataCatalogSessionName.DATA_CATALOG_UNIVAR_1D17]

    st.write("## Data Catalog - Univar Common")
    st.dataframe(data_catalog_univar_common, use_container_width=True)

    st.write("## Data Catalog - Univar 1m")
    tickers_1m = list(data_catalog_univar_1m['ticker'].unique())

    tickers_1m = st.multiselect(
        key="tickers_1m",
        label="Choose ticker(s)",
        options=tickers_1m,
        default=tickers_1m
    )

    if not tickers_1m:
        st.error("Please select at least one product.")
    else:
        filtered_1m_df = data_catalog_univar_1m.loc[data_catalog_univar_1m['ticker'].isin(tickers_1m)]
        st.dataframe(filtered_1m_df, use_container_width=True)

    st.write("## Data Catalog - Univar 1h")
    tickers_1h = list(data_catalog_univar_1h['ticker'].unique())

    tickers_1h = st.multiselect(
        key="tickers_1h",
        label="Choose ticker(s)",
        options=tickers_1h,
        default=tickers_1h
    )

    if not tickers_1h:
        st.error("Please select at least one product.")
    else:
        filtered_1h_df = data_catalog_univar_1h.loc[data_catalog_univar_1h['ticker'].isin(tickers_1h)]
        st.dataframe(filtered_1h_df, use_container_width=True)

    st.write("## Data Catalog - Univar 1d17")

    tickers_1d17 = list(data_catalog_univar_1d17['ticker'].unique())

    tickers_1d17 = st.multiselect(
        key="tickers_1d17",
        label="Choose ticker(s)",
        options=tickers_1d17,
        default=tickers_1d17
    )

    if not tickers_1d17:
        st.error("Please select at least one product.")
    else:
        filtered_1d17_df = data_catalog_univar_1d17.loc[data_catalog_univar_1d17['ticker'].isin(tickers_1d17)]
        st.dataframe(filtered_1d17_df, use_container_width=True)


st.set_page_config(page_title="Data Catalog - Option 1", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Data Catalog - Option 1 (Multiselect)")

load_data()
show_data_catalog_info()
run()
