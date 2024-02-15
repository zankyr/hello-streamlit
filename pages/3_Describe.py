import statsmodels.stats.descriptivestats as smd
import streamlit as st

from common.utils import read_parq


def im_just_a_test_not_yet_a_function():
    # Testing statistics on univar_common
    univar_common_df = read_parq("data-catalogue", "mock/univar_common.parquet")
    pandas_describe_df = univar_common_df.describe()
    statsmodels_describe_df = smd.describe(univar_common_df)

    pandas_describe.dataframe(pandas_describe_df, use_container_width=True)
    statsmodels_describe.dataframe(statsmodels_describe_df, use_container_width=True)


st.set_page_config(page_title="Describe", page_icon="📈", layout="wide")

st.write("# Describe")
st.write(
    """This page compares the output of `pandas.describe` and `statsmodels.stats.descriptivestats.describe` using the `univar_common` dataframe as example."""
)

st.write("## Pandas describe")
pandas_describe = st.empty()

st.write("## Statsmodels describe")
statsmodels_describe = st.empty()

# im_just_a_test_not_yet_a_function()
