import hmac

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello, Data Catalogue!",
        page_icon="📊",
    )

    st.markdown("# Welcome to Data Catalogue 📊")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        **👈 Select a demo from the sidebar** to see some examples
        of what the data catalog can do!
        ### Site map
        - DataFrame explorer: Uses [streamlit-extras](https://arnaudmiribel.github.io/streamlit-extras/extras/dataframe_explorer/) to display the data.
        - Multiselect: Uses  standard [streamlit](https://streamlit.io/) widgets to display the data.
        - Raw Univar Features: Displays the univar features raw data from the database.
    """
    )


def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )

    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if __name__ == '__main__':
    if not check_password():
        st.stop()
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")
