import streamlit as st
from common.utils import regenerate_data, load_data, show_data_catalog_info, check_password


def run():
    load_data()
    if "data_catalog" not in st.session_state:
        st.error("**👈 Use the `Regenerate data catalogue** button to generate a new data catalogue.")
    else:
        df = st.session_state["data_catalog"]

        products = list(df['PRODUCT'].unique())

        products = st.multiselect(
            "Choose products", products, products
        )

        if not products:
            st.error("Please select at least one product.")
        else:
            data = df.loc[df['PRODUCT'].isin(products)]
            st.dataframe(data,use_container_width=True)


st.set_page_config(page_title="Multiselect example", page_icon="📈", layout="wide")
if not check_password():
    st.stop()

st.markdown("# Multiselect example️")
st.write("This example uses the standard multiselect widget to filter a dataframe.")

st.sidebar.header("Multiselect example️")


run()
show_data_catalog_info()
st.sidebar.button("Regenerate data catalogue", type='primary', on_click=regenerate_data, disabled=True,
                  help="EH! VOLEVI!")
