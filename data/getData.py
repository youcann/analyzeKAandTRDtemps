# %%
from influxdb import DataFrameClient
import pandas as pd
cli = DataFrameClient(host='172.16.0.240', port=8086,username='admin',password='72404452')
print(cli.get_list_database())
cli.switch_database('TempData')
cli.query('SELECT "temperature2" AS "Außen" FROM "Temperature" LIMIT 10')
# %%
raw=cli.query('SELECT * FROM "Temperature"')['Temperature']
raw.head()
# %%
data=raw.drop(columns=['location'])
data=data.rename(columns={  "temperature1":'Innen1',
                            "temperature2":'Aussen',
                            "temperature3":'Innen2',
                            "temperature4":'Innen3',})
data.index.name="Time"
data.index=pd.to_datetime(data.index).tz_convert('Europe/Berlin').tz_localize(None)
data=data[['Aussen', 'Innen1', 'Innen2', 'Innen3']]
data.info()
# %%
data.to_csv("tempData.csv")
# %%
