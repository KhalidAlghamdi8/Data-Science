import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # simple Stock Price App
    
    Shown are the stock closing price and volume of Google
    """
)

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on the ticker
tickerData = yf.Ticker(tickerSymbol)
# get historical data prices for the ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
#  Open   High  Low Close  Volume  Dividends  Stock Splits


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)