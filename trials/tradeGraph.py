import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt

start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

data = web.DataReader('TSLA', 'stooq', start, end)

# plt.plot(data[])
# plt.show()

# print(data)

# print(mpf.available_styles())
# ['binance', 'binancedark', 'blueskies', 'brasil', 'charles', 'checkers', 'classic', 'default', 'ibd', 'kenan', 'mike', 'nightclouds', 'sas', 'starsandstripes', 'tradingview', 'yahoo']

colors = mpf.make_marketcolors(up="#03FF00", down="#00B1FF", wick="inherit", edge="inherit", volume="in")
mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)

mpf.plot(data, type="candle", style=mpf_style)
