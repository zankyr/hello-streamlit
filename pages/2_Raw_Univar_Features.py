import streamlit as st

from common.utils import read_parq


def load_univar_features():
    st.write("## Univariate Common")
    univar_common_placeholder = st.empty()

    st.write("## Univariate 1m")
    univar_1m_placeholder = st.empty()

    st.write("## Univariate 1h")
    univar_1h_placeholder = st.empty()

    st.write("## Univariate 1d17")
    univar_1d17_placeholder = st.empty()

    with st.sidebar.status("Loading features data...", expanded=True) as status:
        st.write("Connecting to the database...")
        # LOL, joking, we don't have a database yet

        st.write("Reading univariate common...")
        univar_common_df = read_parq("data-catalogue", "mock/univar_common.parquet");
        univar_common_placeholder.dataframe(univar_common_df)

        st.write("Reading univariate 1m...")
        univar_1m_df = read_parq("data-catalogue", "mock/univar_1m.parquet");
        univar_1m_placeholder.dataframe(univar_1m_df)

        st.write("Reading univariate 1h...")
        univar_1h_df = read_parq("data-catalogue", "mock/univar_1h.parquet");
        univar_1h_placeholder.dataframe(univar_1h_df)

        st.write("Reading univariate 1d17...")
        univar_1d17_df = read_parq("data-catalogue", "mock/univar_1d17.parquet");
        univar_1d17_placeholder.dataframe(univar_1d17_df)

        status.update(label="Download complete!", state="complete", expanded=False)

    st.sidebar.button("Re-run")


st.set_page_config(page_title="Raw Univar Features", page_icon="📈")
st.markdown("# Raw Univar Features")
st.sidebar.header("Raw Univar Features")
st.write(
    """Loads the raw univariate features from the database."""
)

load_univar_features()
