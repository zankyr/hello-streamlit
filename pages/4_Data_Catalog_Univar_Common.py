import statsmodels.stats.descriptivestats as smd
import streamlit as st

from common.utils import read_parq


def im_just_a_test_not_yet_a_function(show_intermediate_dataframes=False):
    # Testing statistics on univar_common
    univar_common_df = read_parq("data-catalogue", "mock/univar_common.parquet")

    statsmodels_describe_df = smd.describe(univar_common_df)

    df_reset = statsmodels_describe_df.reset_index()
    df_transposed = df_reset.transpose()
    df_transposed.columns = df_transposed.iloc[0]
    df_transposed = df_transposed.drop(df_transposed.index[0])

    univar_common_data_catalog_config_df = read_parq("data-catalogue",
                                                     "mock/univar_common_data_catalog_configs.parquet")
    # univar_common_data_catalog_config_df.drop(columns=['PRODUCT'], inplace=True)
    # univar_common_data_catalog_config_df.to_parquet("mock/univar_common_data_catalog_configs.parquet")

    # univar_common_data_catalog_config_df.drop(
    #     columns=['AVERAGE', 'STD._DEVIATION', 'SKEW', 'KURTOSIS', 'MIN', 'MAX', 'START_DATE', 'END_DATE', 'BOUNDED'],
    #     inplace=True)
    # columns_to_keep = univar_common_data_catalog_config_df.columns
    univar_common_data_catalog_df = univar_common_data_catalog_config_df.merge(df_transposed, left_on='ID',
                                                                               right_index=True, how='inner')
    # univar_common_data_catalog_config_df = univar_common_data_catalog_config_df[columns_to_keep]
    #
    # univar_common_data_catalog_config_df.to_parquet("mock/univar_common_data_catalog_configs.parquet")

    if show_intermediate_dataframes:
        st.write("## Statsmodels describe dataframe")
        st.dataframe(statsmodels_describe_df, use_container_width=True)
        st.write("## Statsmodels transposed dataframe")
        st.dataframe(df_transposed)
        st.write("## Univar common data catalog config dataframe")
        st.dataframe(univar_common_data_catalog_config_df)

    st.write("## Data Catalog - Univar Common")
    st.dataframe(univar_common_data_catalog_df, use_container_width=True)


st.set_page_config(page_title="Data Catalog - Univar Common", page_icon="📈", layout="wide")

show_intermediate_dataframes = st.sidebar.checkbox("Show intermediate dataframes", value=False)

st.write("# Data Catalog - Univar Common️")

im_just_a_test_not_yet_a_function(show_intermediate_dataframes)
