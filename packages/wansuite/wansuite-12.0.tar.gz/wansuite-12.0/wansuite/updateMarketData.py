import numpy as np
import pandas as pd
import wansuite as ws
import yfinance as yf
import pandas as pd
from ib_insync import *
import numpy as np
import datetime as dt
import pytz
#%%
def updateBondIndexYahooDaily(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''
    pairlist = ["DX-Y.NYB","^IRX","^FVX","^TNX","^TYX","^GSPC","^IXIC","^VIX","^FTSE","^N225","^HSI","000001.SS","^AORD","^TWII","BTC-USD"]
    for n in pairlist:
        print(n)
        temp = yf.download(n, start=date, progress=False)
        temp["Symbol"] = n
        temp = temp.reset_index()
        ws.msql.df2table("market", temp,"yf_bondindex_1d", "append")
def updateFutureYahooDaily(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''
    pairlist = ws.msql.table2df("symbol", "future")["Symbol"].dropna()
    for n in pairlist:
        temp = yf.download(n, start=date, progress=False)
        temp["Symbol"] = n
        temp = temp.reset_index()
        ws.msql.df2table("market", temp,"yf_future_1d", "append")
def updateCurrencyYahooDaily(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''

    pairlist = ws.msql.table2df("symbol", "currencypair")["Ticker"].dropna()
    for n in pairlist:
        print("currency", n)
        temp = yf.download(n + "=X", start=date, progress=False)
        temp["Symbol"] = n

        temp = temp.reset_index()
        ws.msql.df2table("market", temp,"yf_currency_1d", "append")
def updateStockYahooDaily(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''
    sectorlist=["us_medical_sector","us_computer_sector","us_finance_sector","energy","service","products","discretionary","staples"]
    tablelist=["yf_health_1d","yf_computer_1d","yf_finance_1d","yf_energy_1d","yf_service_1d","yf_products_1d","yf_discretionary_1d","yf_staples_1d"]


    for h in range(len(sectorlist)):
        print("sector:",  sectorlist[h])
        sec= ws.msql.table2df("symbol", sectorlist[h])["Ticker"].dropna().to_list()

        for n in sec:
            temp = yf.download(n, start=date, progress=False)
            temp["Symbol"] = n
            temp = temp.reset_index()
            ws.msql.df2table("market", temp, tablelist[h], "append")


def updateBondIndexYahooMinute(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''

    pairlist = ["DX-Y.NYB","^IRX","^FVX","^TNX","^TYX","^GSPC","^IXIC","^VIX","^FTSE","^N225","^HSI","000001.SS","^AORD","^TWII","BTC-USD"]



    for n in pairlist:
        print("future",n)
        temp = yf.download(n, start=date,interval="1m", progress=False)
        temp["Symbol"] = n
        temp=temp.tz_convert("US/Eastern")
        temp = temp.reset_index()

        ws.msql.df2table("market", temp, "yf_bondinde_5m", "append")

def updateFutureYahooMinute(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''

    pairlist = ws.msql.table2df("symbol", "future")["Symbol"].dropna()


    for n in pairlist:
        print("future",n)
        temp = yf.download(n, start=date,interval="1m", progress=False)
        temp["Symbol"] = n
        temp=temp.tz_convert("US/Eastern")
        temp = temp.reset_index()

        ws.msql.df2table("market", temp, "yf_future_5m", "append")
def updateCurrencyYahooMinute(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''

    pairlist = ws.msql.table2df("symbol", "currencypair")["Ticker"].dropna()


    for n in pairlist:
        print("currency",n)
        temp = yf.download(n+"=X", start=date,interval="1m", progress=False)
        temp["Symbol"] = n
        temp=temp.tz_convert("US/Eastern")
        temp = temp.reset_index()

        ws.msql.df2table("market", temp, "yf_currency_5m", "append")




def updateStockYahooMinute(date):
    '''
    update daily us stock price from health and computer sectors
    :param date: starting date
    :param interval:"1d", "1m"
    :return:
    '''
    health = ws.msql.table2df("symbol", "us_medical_sector")["Ticker"].dropna().to_list()
    computer = ws.msql.table2df("symbol", "us_computer_sector")["Ticker"].dropna().to_list()
    sectorlist = ["us_medical_sector", "us_medical_sector", "us_finance_sector", "energy", "service", "products",
                  "discretionary", "staples"]
    tablelist = ["yf_health_5m", "yf_computer_5m", "yf_finance_5m", "yf_energy_5m", "yf_service_5m", "yf_products_5m",
                 "yf_discretionary_5m", "yf_staples_5m"]

    for n in range(len(sectorlist)):
        print("sector in 1 min", sectorlist[n])
        stocklist=ws.msql.table2df("symbol", sectorlist[n])["Ticker"].dropna().to_list()
        for m in stocklist:
            temp = yf.download(m, start=date, interval="1m", progress=False)
            temp["Symbol"] = m
            temp = temp.reset_index()
            ws.msql.df2table("market", temp, tablelist[n], "append")

def updateStockIB(enddate,duration,barsize,stocklist,database,table):
    '''

    :param enddate: "2024-01-01"
    :param duration: "30 D"
    :param barsize: "5 mins"
    :param stocklist:
    :param database: "market"
    :param table:sector_health_5m,sector_computer_5m
    :newtable: True
    :return:null
    '''
    #util.startLoop()
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=np.random.randint(10000))

    flist = [Stock(x, "SMART", "USD") for x in stocklist]
    stday = enddate
    misslist = []
    for ti in [0]:
        ib.sleep(5)
        for n in range(len(stocklist)):  # #for stock in
            try:
                stock = stocklist[n]
                bars = ib.reqHistoricalData(flist[n],
                                            endDateTime=stday + " 19:00:00" + " US/Eastern",
                                            durationStr=duration,
                                            barSizeSetting=barsize,  # 1 day
                                            whatToShow="TRADES",  # TRADES
                                            useRTH=1,
                                            keepUpToDate=False,
                                            formatDate=1)
                if len(bars) == 0:
                    misslist.append(stock)
                if n % 50 == 0:
                    print(flist[n])
                df = pd.DataFrame(bars)
                df["symbol"] = stock

                ws.msql.df2table(database, df, table, "append")
            except:
                print("cannot download", stock)
                misslist.append(stock)

    return misslist


def updateCurrencyIB(enddate,duration,barsize,pairlist,database, table,newtable):
    '''

    :param enddate: "2024-01-01"
    :param duration: "30 D"
    :param barsize: "5 mins"
    :param pairlist:
    :param database: "market"
    :param table:sector_health_5m,sector_computer_5m
    :newtable: True
    :return:null
    '''
    #util.startLoop()
    ib = IB()
    ib.connect('127.0.0.1', 7496, clientId=np.random.randint(10000))

    flist =[Forex(x) for x in pairlist]
    stday = enddate
    misslist = []
    for ti in [0]:
        ib.sleep(5)
        for n in range(len(pairlist)):  # #for stock in
            try:
                stock = pairlist[n]
                bars = ib.reqHistoricalData(flist[n],
                                            endDateTime=stday + " 19:00:00" + " US/Eastern",
                                            durationStr=duration,
                                            barSizeSetting=barsize,
                                            whatToShow="MIDPOINT",  # TRADES
                                            keepUpToDate=False,
                                            useRTH=0,
                                            formatDate=1)
                if len(bars) == 0:
                    misslist.append(stock)
                if n % 50 == 0:
                    print(flist[n])
                df = pd.DataFrame(bars)
                df["symbol"] = stock
                if newtable==True:
                    ws.msql.df2table(database, df, table, "replace")
                else:
                    ws.msql.df2table(database, df, table, "append")
            except:
                print("cannot download", stock)
                misslist.append(stock)

    return misslist

def updateForward(asset):
    if asset=="currency":
        stock2 = downloadfromsql("market", "currency_5m", "date")
        ustoday = dt.datetime.now(pytz.timezone('US/Eastern')).date()
        print("Last date for currency", stock2.index[-1])
        print("today", dt.datetime.now(pytz.timezone('US/Eastern')).date())
        diff = (ustoday - stock2.index[-1].date()).days
        print(diff, " days need to be updated")
        if diff > 0:
            startdate = str((stock4.index[-1] + dt.timedelta(days=1)).date())

            pairlist = ws.msql.table2df("symbol", "currencypair")["Ticker"].dropna()
            misslist = updateCurrencyIB(temp, str(diff) + " D", "1 min", pairlist,
                                        "market", "currency_5m", False)

        print("Currency 1 Minute is updated from IBKR")
    elif asset=="yahoo":
        stock1 = downloadfromsql("market", "yf_computer_1d", "Date")
        ustoday = dt.datetime.now(pytz.timezone('US/Eastern')).date()
        print("today", dt.datetime.now(pytz.timezone('US/Eastern')).date())
        print("Last date for yahoo daily stock price", stock1.index[-1])
        diff = (ustoday - stock1.index[-1].date()).days
        print(diff, " days need to be updated")
        if diff > 0:
            startdate = str((stock4.index[-1] + dt.timedelta(days=1)).date())

            pairlist = ws.msql.table2df("symbol", "currencypair")["Ticker"].dropna()
            misslist = updateCurrencyIB(temp, str(diff) + " D", "1 min", pairlist,
                                        "market", "currency_5m", False)

        print("Currency 1 Minute is updated from IBKR")
