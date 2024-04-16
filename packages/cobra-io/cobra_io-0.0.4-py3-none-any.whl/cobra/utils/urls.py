from cobra.utils import configurations

BASE_URL = configurations.COBRA_CONFIG['API']['base_url']
ASSET_URL = BASE_URL + 'scenariocrok/assets/'
MODULE_DB_URL = BASE_URL + 'robots'
TASK_URL = BASE_URL + 'scenariocrok/'
SOLUTION_URL = BASE_URL + 'solutioncrok/'
RANKING_URL = SOLUTION_URL + 'ranking/'
SCHEMA_URL = BASE_URL + 'schemas/'
