import streamlit as st
from streamlit.logger import get_logger

from common.utils import check_password

LOGGER = get_logger(__name__)


def run():
    st.markdown("# Welcome to Data Catalogue 📊")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        **👈 Select a demo from the sidebar** to see some examples
        of what the data catalog can do!
        ### Site map
        - Data Catalog: Uses [streamlit-extras](https://arnaudmiribel.github.io/streamlit-extras/extras/dataframe_explorer/) to display the data.
        - Raw Univar Features: Displays the univar features raw data from the database.
    """
    )


if __name__ == '__main__':
    st.set_page_config(
        page_title="Hello, Data Catalogue!",
        page_icon="📊",
    )

    if not check_password():
        st.stop()
    run()
