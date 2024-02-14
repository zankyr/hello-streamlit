import streamlit as st
from common.utils import regenerate_data, load_data, show_data_catalog_info, check_password
from streamlit_extras.dataframe_explorer import dataframe_explorer


def run():
    load_data()

    if "data_catalog" not in st.session_state:
        st.error("**👈 Use the `Regenerate data catalogue** button to generate a new data catalogue.")
    else:
        df = st.session_state["data_catalog"]

        filtered_df = dataframe_explorer(df, False)

        st.dataframe(filtered_df, use_container_width=True)


st.set_page_config(page_title="Dataframe explorer example", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Dataframe explorer example️")
st.write("This example uses the dataframe explorer from streamlit_extras to filter a dataframe.")

st.sidebar.header(" Dataframe explorer example️")


run()
show_data_catalog_info()
st.sidebar.button("Regenerate data catalogue", type='primary', on_click=regenerate_data, disabled=True,
                  help="EH! VOLEVI!")