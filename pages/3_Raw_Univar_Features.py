import streamlit as st
from common.utils import read_parq, check_password


def load_univar_features():
    with st.sidebar.status("Loading features data...", expanded=True) as status:
        st.write("Connecting to the database...")
        # LOL, joking, we don't have a database yet

        st.write("Reading univariate common...")
        univar_common_df = read_parq("data-catalogue", "mock/univar_common.parquet")
        st.session_state["univar_common_df"] = univar_common_df

        st.write("Reading univariate 1m...")
        univar_1m_df = read_parq("data-catalogue", "mock/univar_1m.parquet")
        st.session_state["univar_1m_df"] = univar_1m_df

        st.write("Reading univariate 1h...")
        univar_1h_df = read_parq("data-catalogue", "mock/univar_1h.parquet")
        st.session_state["univar_1h_df"] = univar_1h_df

        st.write("Reading univariate 1d17...")
        univar_1d17_df = read_parq("data-catalogue", "mock/univar_1d17.parquet")
        st.session_state["univar_1d17_df"] = univar_1d17_df

        status.update(label="Download complete!", state="complete", expanded=False)

        st.session_state["raw_univar_features"] = True


st.set_page_config(page_title="Raw Univar Features", page_icon="📈", layout="wide")

if not check_password():
    st.stop()

st.markdown("# Raw Univar Features")
st.sidebar.header("Raw Univar Features")

if 'raw_univar_features' not in st.session_state:
    load_univar_features()

st.write(
    """Loads the raw univariate features from the database."""
)

st.write("## Univariate Common")
if 'univar_common_df' in st.session_state:
    st.dataframe(st.session_state["univar_common_df"], use_container_width=True)

st.write("## Univariate 1m")
if 'univar_1m_df' in st.session_state:
    st.dataframe(st.session_state["univar_1m_df"], use_container_width=True)

st.write("## Univariate 1h")
if 'univar_1h_df' in st.session_state:
    st.dataframe(st.session_state["univar_1h_df"], use_container_width=True)

st.write("## Univariate 1d17")
if 'univar_1d17_df' in st.session_state:
    st.dataframe(st.session_state["univar_1d17_df"], use_container_width=True)

st.sidebar.button("Reload data", on_click=load_univar_features)
