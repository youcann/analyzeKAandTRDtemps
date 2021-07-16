# %%
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tikzplotlib
# %%
df=pd.read_csv("data/tempData.csv",index_col=0,parse_dates=[0])
df
# %%
plt.figure(figsize=(20,10))
plt.plot(df.Aussen)
# %%
df=df.resample('1h').mean()
dfTRD=df.loc["2020-01-01 00:00:00":"2020-07-01 00:00:00"]
dfKA=df.loc["2021-01-01 00:00:00":"2021-07-01 00:00:00"]
# %%
# Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')
plt.figure(figsize=(20,10))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.plot(dfTRD.Aussen.groupby(pd.Grouper(freq='7d')).min(),'C0',label="trdmin")
plt.plot(dfTRD.Aussen.groupby(pd.Grouper(freq='7d')).max(),'C0',label="trdmax")
plt.plot(dfTRD.Aussen,'C0',label="trd")
plt.plot(dfKA.Aussen.groupby(pd.Grouper(freq='7d')).min().shift(-365,freq="D"),'C1',label="kamin")
plt.plot(dfKA.Aussen.groupby(pd.Grouper(freq='7d')).max().shift(-365,freq="D"),'C1',label="kamax")
plt.plot(dfKA.Aussen.shift(-365,freq="D"),'C1',label="ka")
plt.legend()
X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
tikzplotlib.save("TrdVsKa.tikz")
# %%
