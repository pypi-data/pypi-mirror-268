import pandas as pd
import numpy as np
import wansuite as ws
import yfinance as yf
downloadcol=['Company Name', 'Ticker','today','Last Close', 'Market Cap (mil)', 'Exchange',
       'Month of Fiscal Yr End', 'Sector', 'Industry',
       'Shares Outstanding (mil)', 'Avg Volume',
       'Price as a % of 52 Wk H-L Range', '% Price Change (1 Week)',
       '% Price Change (4 Weeks)', '% Price Change (12 Weeks)',
       'Average Target Price', '% Rating Downgrades ', '% Rating Upgrades ',
       '% Rating Hold', '% Rating Strong Sell or Sell',
       '% Rating Strong Buy or Buy',
       'Q0 Consensus Est. (last completed fiscal Qtr)', 'Q1 Consensus Est. ',
       'Q2 Consensus Est. (next fiscal Qtr)', 'F0 Consensus Est.',
       'F1 Consensus Est.', 'F2 Consensus Est.', 'Current ROE (TTM)',
       'Current ROI (TTM)', 'ROI (5 Yr Avg)', 'Current ROA (TTM)',
       'ROA (5 Yr Avg)', 'Market Value/# Analysts', 'EBITDA ($mil)',
       'EBIT ($mil)', 'Net Income  ($mil)', 'Cash Flow ($mil)',
       'Net Income Growth F(0)/F(-1)', 'Net Margin %', 'Turnover',
       'Inventory Turnover', 'Asset Utilization', 'Operating Margin 12 Mo %',
       'Receivables ($mil)', 'Inventory ($mil)', 'Intangibles ($mil)',
       'Current Assets  ($mil)', 'Current Liabilities ($mil)',
       'Long Term Debt ($mil)', 'Preferred Equity ($mil)',
       'Common Equity ($mil)', 'Book Value', 'Debt/Total Capital',
       'Debt/Equity Ratio', 'Current Ratio', 'Quick Ratio', 'Cash Ratio',
       ]
changecol=['CompanyName', 'Ticker','Today','Price', 'MarketCap_mil', 'Exchange',
       'MonthofFiscalYrEnd', 'Sector', 'Industry',
       'SharesOutstanding_mil', 'AvgVolume',
       'Price_Percentof52WkH-LRange', 'Percent_PriceChange_1Week',
       'Percent_PriceChange_4Weeks', 'Percent_PriceChange_12Weeks',
       'AverageTargetPrice', 'Percent_RatingDowngrades', 'Percent_RatingUpgrades',
       'Percent_Rating_Hold', 'Percent_RatingStrongSellorSell',
       'Percent_Rating_StrongBuyorBuy',
       'Q0EPS', 'Q1EPS',
       'Q2EPS', 'F0EPS',
       'F1EPS', 'F2EPS', 'CurrentROE_TTM',
       'CurrentROI_TTM', 'ROI_ 5YrAvg', 'CurrentROA_TTM',
       'ROA_5YrAvg', 'MarketValue/Analysts', 'EBITDA_mil',
       'EBIT_mil', 'NetIncome_mil', 'CashFlow_mil',
       'NetIncomeGrowthF0/F-1', 'NetMargin_Percent', 'Turnover',
       'InventoryTurnover', 'AssetUtilization', 'OperatingMargin_12Mo_Percent',
       'Receivables_mil', 'Inventory_mil', 'Intangibles_mil',
       'CurrentAssets_mil', 'CurrentLiabilities_mil',
       'LongTermDebt_mil', 'PreferredEquity_mil',
       'CommonEquity_mil', 'BookValue', 'Debt/TotalCapital',
       'Debt/EquityRatio', 'CurrentRatio', 'QuickRatio', 'CashRatio',
       ]



dellist=["underlyingSymbol", "shortName","longName",'country',"currency" ,'sectorKey',
       'sectorDisp', 'longBusinessSummary','industryKey', 'industryDisp', 'website',"companyOfficers","address1","city","state","zip","financialCurrency","phone"]
def updateFundmental_Yahoo(today):
    sl=list(ws.msql.table2df("symbol","allstocks")["Ticker"].dropna())
    for symbol in sl:
           temp=yf.Ticker(symbol)
           data=pd.DataFrame(temp.info).drop(columns=dellist)
           data["date"]=today
           A=data.iloc[-1].to_frame().T
           ml=[]
           for c in A.columns[:]:
               if type(A.loc[A.index[0],c])==str:
                   ml.append(A.loc[A.index[0],c])
               else:
                   ml.append(float(A.loc[A.index[0],c]))
           A.loc[A.index[0]]=ml
           ws.msql.df2table("macro",A,"yf_fund","append")
def convertForexData(filename):
    data = pd.read_csv(filename, index_col=0)
    data = data.reset_index()
    date = data.columns[0]
    data = data.rename(columns={data.columns[0]: "time"})
    data = data[data.time != "All Day"]
    data = data[data["Unnamed: 2"] != "Holiday"]
    data = data[data["time"] != "Tentative"]
    data["date"] = np.nan
    data.isnull().sum(axis=1).sort_values(ascending=False)


    for n in data.index:
        if data.loc[n].isnull().sum() == 7:
            date = data.loc[n, "time"]
            # print("OK",data.loc[n,"time"])
        else:

            data.loc[n, "date"] = pd.to_datetime(date + " " + data.loc[n, "time"])

    data = data.drop(columns=["Unnamed: 2", "time"])
    data = data.dropna(subset=["date"])
    data = data.rename(
        columns={"Unnamed: 1": "Currency", "Unnamed: 3": "Indicator", "Unnamed: 4": "Actual", "Unnamed: 5": "Forecast",
                 "Unnamed: 6": "Previous"})
    droplist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    indicator = []
    for i in data.Indicator:
        if i[-4:-1] in droplist:
            indicator.append(i[:-5])
        else:
            indicator.append(i)
    data["Indicator"] = indicator

    droplist = ["Q1", "Q2", "Q3", "Q4"]
    indicator = []
    for i in data.Indicator:
        if i[-3:-1] in droplist:
            indicator.append(i[:-4])
        else:
            indicator.append(i)
    data["Indicator"] = indicator

    return  data[data.isnull().sum(axis=1) < 3]

def updateCompanyData(filename,date):
    zack = pd.read_csv(filename)
    zack["today"] = date

    zack = zack[zack["Exchange"] != "OTCBB"]
    zack = zack[downloadcol]
    zack.columns = changecol


    return zack

def updateEarning(filename):
    data = pd.read_csv(filename)
    date = data.columns[0]
    data = data.rename(columns={data.columns[0]: "date"})
    for n in data.index:
        if data.loc[n].isnull().sum() == 6:
            date = data.loc[n, "date"]
            # print("OK",data.loc[n,"time"])
        else:
            data.loc[n, "date"] = pd.to_datetime(date)
    data = data.dropna(subset=["Unnamed: 1"])
    data = data.rename(columns={"Unnamed: 1": "Company", "Unnamed: 2": "Actual EPS", "Unnamed: 3": "Forcast EPS",
                                "Unnamed: 4": "Actual Revenue", "Unnamed: 5": "Forcast Revenue",
                                "Unnamed: 6": "Market Cap"})
    temp = []
    for t in data.index:
        i = data.loc[t, "Actual EPS"]
        if i == "--":
            temp.append(np.nan)
        else:
            if i[-1] == "K":
                temp.append(float(i[:-1].replace(",", "")) * 1000)
            else:
                temp.append(float(i.replace(",", "")))
    data["Actual EPS"] = temp
    temp = []
    for t in data["Forcast EPS"].index:
        i = data.loc[t, "Forcast EPS"]
        if i == "/--" or i == "/ --":
            temp.append(np.nan)
        else:
            # print(i)
            temp.append(float(i[1:].replace(",", "")))
    data[("Forcast EPS")] = temp
    temp = []
    for i in data["Actual Revenue"]:
        if i == "--":
            temp.append(np.nan)
        else:
            temp.append(i)
    data["Actual Revenue"] = temp
    temp = []
    for t in data["Forcast Revenue"].index:
        i = data.loc[t, "Forcast Revenue"]
        if i == "/--" or i == "/ --":
            temp.append(np.nan)
        else:
            # print(i)
            temp.append(i[1:])
    data[("Forcast Revenue")] = temp
    data["date"] = pd.to_datetime(data["date"])
    data["Symbol"] = np.nan
    temp = []
    for i in data.Company:
        if i[-3] == "(":
            temp.append(i[-2:-1])
        elif i[-4] == "(":
            temp.append(i[-3:-1])
        elif i[-5] == "(":
            temp.append(i[-4:-1])
        elif i[-6] == "(":
            temp.append(i[-5:-1])
        elif i[-7] == "(":
            temp.append(i[-6:-1])
        elif i[-8] == "(":
            temp.append(i[-7:-1])
        elif i[-9] == "(":
            temp.append(i[-8:-1])
        else:
            print(i)
    data["Symbol"] = temp
    data["date"] =[x.date() for x in  pd.to_datetime(data["date"])]
    return data

