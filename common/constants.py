CLEAN_DATA_BUCKET_NAME = 'etna-clean-data-dev'
DATA_CATALOG_PATH = 's3://etna-clean-data-dev/FX/spot/features/data-catalog/latest.parq'
DATA_CATALOG_CONFIGS_PATH = 's3://etna-clean-data-dev/FX/spot/features/data-catalog/configs.parq'
MAPPING_FEATURES_GROUPS_PATH = 's3://etna-clean-data-dev/FX/spot/features/mapping_features_groups/latest.parq'

G10 = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'NZDUSD', 'USDSEK', 'USDNOK', 'USDCAD', 'USDCHF']
G10_INVERSE = ['USDEUR', 'USDGBP', 'CADUSD', 'CHFUSD', 'JPYUSD', 'NOKUSD', 'SEKUSD', 'USDAUD', 'USDNZD']
G10_CROSS = [
    'AUDCAD', 'AUDCHF', 'AUDEUR', 'AUDGBP', 'AUDJPY', 'AUDNOK', 'AUDNZD', 'AUDSEK',
    'CADAUD', 'CADCHF', 'CADEUR', 'CADGBP', 'CADJPY', 'CADNOK', 'CADNZD', 'CADSEK',
    'CHFAUD', 'CHFCAD', 'CHFEUR', 'CHFGBP', 'CHFJPY', 'CHFNOK', 'CHFNZD', 'CHFSEK',
    'EURAUD', 'EURCAD', 'EURCHF', 'EURGBP', 'EURJPY', 'EURNOK', 'EURNZD', 'EURSEK',
    'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPEUR', 'GBPJPY', 'GBPNOK', 'GBPNZD', 'GBPSEK',
    'JPYAUD', 'JPYCAD', 'JPYCHF', 'JPYEUR', 'JPYGBP', 'JPYNOK', 'JPYNZD', 'JPYSEK',
    'NOKAUD', 'NOKCAD', 'NOKCHF', 'NOKEUR', 'NOKGBP', 'NOKJPY', 'NOKNZD', 'NOKSEK',
    'NZDAUD', 'NZDCAD', 'NZDCHF', 'NZDEUR', 'NZDGBP', 'NZDJPY', 'NZDNOK', 'NZDSEK',
    'SEKAUD', 'SEKCAD', 'SEKCHF', 'SEKEUR', 'SEKGBP', 'SEKJPY', 'SEKNOK', 'SEKNZD'
]
INDEXES = [
    'EW_USD_G10_INDEX', 'EW_EUR_G10_INDEX', 'EW_GBP_G10_INDEX', 'EW_JPY_G10_INDEX', 'EW_AUD_G10_INDEX',
    'EW_NZD_G10_INDEX', 'EW_CAD_G10_INDEX', 'EW_NOK_G10_INDEX', 'EW_SEK_G10_INDEX', 'EW_CHF_G10_INDEX',
    'EW_USD_G4_INDEX', 'EW_USD_G10CMDTY_INDEX', 'EW_USD_SCANDI_INDEX'

]
ALL_TICKERS = [*G10, *G10_INVERSE, *G10_CROSS, *INDEXES]

TYPES = ['continuos', 'discrete', 'dummy']

COLUMNS = {
    'ID': 'int',
    'NAME/ID FEATURE': 'string',
    'PRODUCT': 'string',
    'DESCRIPTION': 'string',
    'GH CODE': 'string',
    'TYPE': 'string',
    'CATEGORY': 'string',
    'START ID FEAT': 'string',
    'PARAMETRIZATION': 'string',
    'SOURCE FREQ': 'string',
    'START DATE': 'date',
    'END DATE': 'date',
    'AVERAGE': 'float',
    'STD. DEVIATION': 'float',
    'SKEW': 'float',
    'KURTOSIS': 'float',
    'MIN': 'float',
    'MAX': 'float',
    'BOUNDED': 'boolean'
}
