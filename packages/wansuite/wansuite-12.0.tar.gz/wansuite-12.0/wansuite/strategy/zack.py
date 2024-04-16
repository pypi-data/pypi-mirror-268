import yfinance as yf
import wansuite as ws
import numpy as np
import pandas as pd
import wansuite as ws
pd.options.plotting.backend = "plotly"
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta
import scipy.stats as stats
from sklearn import datasets, ensemble
class ZackStrategy:
    def __init__(self,sector,startdate,lookback_window,seed):
        self.lookback_window = lookback_window
        self.sector=sector
        self.startdate=startdate
        self.zack=None
        self.dailymarket=None
        self.featurelist=[]
        self.hfmarket=None
        self.ind=None
        self.rank=None
        self.wealth=None
        self.trainsize=None
        self.traindates=None
        self.metric=None
        self.tempx=None
        self.tempy=None
        self.horizon=None
        self.randomseed=seed
        self.performance=None
        self.performancelist=[]
        self.time_1=None
        self.time_2=None
        self.ln=None
        self.sn=None
        self.look=None
        self.looks=None
        self.temp=None
        self.temp1=None
        self.temp2=None
        self.perlist=[]
        self.long=None
        self.short=None
        self.firmsize=None
        self.params = {
            "n_estimators": 300,
            "max_depth": 3,
            "min_samples_split": 5,
            "learning_rate": 0.2,
            "loss": "squared_error",
        }
        self.model = ensemble.GradientBoostingRegressor(**self.params, random_state=self.randomseed)
        self.modellist=[]

    def backtest_trend_hf(self, wealth, size, duration):
        self.wealth = wealth
        self.trainsize = size
        self.duration = duration
        self.perlist=[]
        for t in self.ind[self.trainsize:]:
            traindates = self.zack[self.zack.Today <= t].Today.value_counts().sort_index().iloc[-self.trainsize:].index

            data2 = self.zack.loc[(self.zack.Today.isin(traindates)) & (self.zack.MarketCap_mil > 3000)].dropna()

            # data2=data2[data2.Price>10]

            tempx = data2[self.featurelist]
            tempy = data2["Y"]
            self.tempx = tempx
            self.tempy = tempy

            # tempx=pd.concat([data2[featurelist],data2[featurelist]])
            # tempy=pd.concat([data2["Y"],data2["Y1"]])
            self.model.fit(tempx, tempy)

            performance = data2.copy()

            performance["Predict"] = self.model.predict(performance[self.featurelist])
            temp = performance[["Ticker", "MarketCap_mil", "Predict", "Price"]].groupby("Ticker").mean().sort_values(
                by="Predict")
            temp["ID"] = np.arange(len(temp))

            self.rank.loc[t, temp.index] = temp.loc[:, "ID"]

            time_1 = t + timedelta(days=1)
            time_2 = t - timedelta(days=4)
            self.time_1 = time_1
            self.time_2 = time_2

            # print(temp0[temp0.Ticker.isin(["NUVL","MORF","MRTX", "KYMR","OBIO", "KYMR"])][["Ticker"]])
            # temp=temp[temp.Price>10]

            if "ATHM" in temp.index:
                temp = temp.drop("ATHM")
            if "HZNP" in temp.index:
                temp = temp.drop("HZNP")
            if "PNT" in temp.index:
                temp = temp.drop("PNT")
            if "SMCI" in temp.index:
                temp = temp.drop("SMCI")

                # if "BHVN" in temp.index:
            #   temp=temp.drop("BHVN")
            temp1 = temp[temp.MarketCap_mil > 3000][temp.MarketCap_mil < 10000]
            temp2 = temp[temp.MarketCap_mil > 10000]

            # if len(temp1) > 0 and len(temp2) > 0 and temp1.iloc[-2]["Predict"] > 0 and temp2.iloc[1]["Predict"] < 0:
            if len(temp1) > 0 and len(temp2) > 0:
                try:

                    ln = temp1.index[-2]
                    sn = temp2.index[1]
                    # print(temp1.shape, temp2.shape, ln, sn)
                    look = self.hfmarket.loc[(self.hfmarket.index == ln) & (self.hfmarket.Date >= time_1.date())].iloc[
                           0:self.duration].set_index(
                        "Datetime")
                    # print(look)
                    looks = self.hfmarket.loc[(self.hfmarket.index == sn) & (self.hfmarket.Date >= time_1.date())].iloc[
                            0:self.duration].set_index(
                        "Datetime")
                    look["diff"]= look["Open"].shift(-1)-look["Open"]
                    look["fast"]= look["Open"].rolling(5).mean()
                    look["slow"] =  look["Open"].rolling(15).mean()
                    look["signal"]=[1 if look.loc[t,"fast"]>look.loc[t,"slow"] else np.nan for t in look.index]
                    longprofit=(wealth[0]/look["Open"].iloc[0])*(look["diff"]*look["signal"]).sum()
                    looks["diff"] = looks["Open"].shift(-1) - looks["Open"]
                    looks["fast"] = looks["Open"].rolling(2).mean()
                    looks["slow"] = looks["Open"].rolling(10).mean()
                    looks["signal"] = [-1 if looks.loc[t, "fast"] < looks.loc[t, "slow"] else np.nan for t in looks.index]
                    shortprofit = (wealth[1] / looks["Open"].iloc[0]) * (looks["diff"] * looks["signal"]).sum()
                    self.long=look
                    self.short=looks
                    self.perlist.append([time_1, ln, sn,longprofit,shortprofit])
                    print(ln,sn,perlist[-1][:-2:])
                except:
                    pass
            self.performance = pd.DataFrame(self.perlist,
                                            columns=["date", "longstock", "shortstock", "longreturn", "shortreturn"])

            self.performance.set_index("date", inplace=True)
            self.performance.sort_index(inplace=True)
            self.performance["total"] = self.performance["longreturn"] + self.performance["shortreturn"]
            print(time_1, temp1.shape, temp2.shape, ln, sn)

    def train(self,  size,firmsize):

        self.trainsize = size
        self.firmsize=firmsize
        for t in self.ind[self.trainsize:]:
            self.traindates = self.zack[self.zack.Today <= t].Today.value_counts().sort_index().iloc[
                              -self.trainsize:].index
            self.performance = self.zack.loc[
                (self.zack.Today.isin(self.traindates)) & (self.zack.MarketCap_mil > self.firmsize)]
            self.performance=self.performance.loc[:,self.performance.isnull().sum()<50].dropna()


            self.tempx = self.performance[self.featurelist]
            self.tempy = self.performance["Y"]
            self.model.fit(self.tempx, self.tempy)
            self.performance["Predict"] = self.model.predict(self.performance[self.featurelist])
            self.performancelist.append(self.performance)



    def backtest(self,wealth,duration,longsize,shortsize):
        self.wealth=wealth
        self.duration=duration
        self.perlist=[]

        for n in range(len(self.ind[self.trainsize:])):
            t=self.ind[self.trainsize:][n]
            self.traindates = self.zack[ self.zack.Today <= t].Today.value_counts().sort_index().iloc[-self.trainsize:].index

            self.performance = self.performancelist[n]

            self.temp = self.performance[["Ticker", "MarketCap_mil", 'FEG1','FEG2',"Predict", "Price"]].groupby("Ticker").mean().sort_values(
                by="Predict")

            self.time_1=t + timedelta(days=1)
            self.time_2=t - timedelta(days=4)

            self.temp1 = self.temp[self.temp.MarketCap_mil >longsize][self.temp.MarketCap_mil <shortsize]
            self.temp2 = self.temp[self.temp.MarketCap_mil >shortsize]


            #if len(temp1) > 0 and len(temp2) > 0 and temp1.iloc[-2]["Predict"] > 0 and temp2.iloc[1]["Predict"] < 0:
            if len(self.temp1) > 0 and len(self.temp2) > 0:
                try:
                    print("start")
                    self.ln =self.temp1.index[1]
                    self.sn =self.temp2.index[1]
                   # print(temp1.shape, temp2.shape, ln, sn)
                    self.look = self.dailymarket.loc[(self.dailymarket.index == self.ln) & (self.dailymarket.Date.dt.date >= self.time_1.date())].iloc[0:self.duration].set_index(
                        "Date")
                    #print(look)
                    self.looks = self.dailymarket.loc[(self.dailymarket.index == self.sn) & (self.dailymarket.Date.dt.date >= self.time_1.date())].iloc[0:self.duration].set_index(
                        "Date")
                    self.perlist.append([self.time_1,self.ln,self.sn, self.wealth[0] * (self.look.iloc[-1]["Close"] - self.look.iloc[0]["Open"]) / (self.look.iloc[0]["Open"]), self.wealth[1]* (
                                self.looks.iloc[-1]["Close"] - self.looks.iloc[0]["Open"]) / (self.looks.iloc[0]["Open"])])
                    print(self.ln,self.sn,self.perlist[-1])

                except:
                    pass
            self.metric=pd.DataFrame(self.perlist,columns=["date","longstock","shortstock","longreturn","shortreturn"])

            self.metric.set_index("date",inplace=True)
            self.metric.sort_index(inplace=True)
            self.metric["total"] = self.metric["longreturn"]+self.metric["shortreturn"]
            #print(time_1,temp1.shape, temp2.shape, ln, sn)
    def backtest_trend(self,wealth,duration,longsize,shortsize):
        self.wealth=wealth
        self.duration=duration
        self.perlist=[]
        for n in range(len(self.ind[self.trainsize:])):
            t=self.ind[self.trainsize:][n]
            self.traindates = self.zack[ self.zack.Today <= t].Today.value_counts().sort_index().iloc[-self.trainsize:].index

            self.performance = self.performancelist[n]

            self.temp = self.performance[["Ticker", "MarketCap_mil", "Predict", "Price"]].groupby("Ticker").mean().sort_values(
                by="Predict")

            self.time_1=t + timedelta(days=1)
            self.time_2=t - timedelta(days=4)

            self.temp1 = self.temp[self.temp.MarketCap_mil >longsize]
            self.temp2 = self.temp[self.temp.MarketCap_mil >shortsize]


            #if len(temp1) > 0 and len(temp2) > 0 and temp1.iloc[-2]["Predict"] > 0 and temp2.iloc[1]["Predict"] < 0:
            if len(self.temp1) > 0 and len(self.temp2) > 0:
                try:
                    print("start")
                    self.ln = self.temp1.index[-5]
                    self.sn =self.temp2.index[1]
                   # print(temp1.shape, temp2.shape, ln, sn)
                    self.look = self.dailymarket.loc[(self.dailymarket.index == self.ln) & (self.dailymarket.Date.dt.date >= self.time_1.date())].iloc[0:self.duration].set_index(
                        "Date")
                    #print(look)
                    self.looks = self.dailymarket.loc[(self.dailymarket.index == self.sn) & (self.dailymarket.Date.dt.date >= self.time_1.date())].iloc[0:self.duration].set_index(
                        "Date")

                    self.look["signal"] = [1 if self.look.loc[t, "fast"] > self.look.loc[t, "slow"] else np.nan for t in self.look.index]
                    longprofit = (self.wealth[0] / self.look["Open"].iloc[0]) * (self.look["future"] * selflook["signal"]).sum()

                    self.looks["signal"] = [-1 if self.looks.loc[t, "fast"] < self.looks.loc[t, "slow"] else np.nan for t in
                                       self.looks.index]
                    shortprofit = (self.wealth[1] / self.looks["Open"].iloc[0]) * (self.looks["future"] * self.looks["signal"]).sum()

                    self.perlist.append([self.time_1,self.ln,self.sn, longprofit,shortprofit ])
                    print(self.ln,self.sn,self.perlist[-1])

                except:
                    pass
            self.metric=pd.DataFrame(self.perlist,columns=["date","longstock","shortstock","longreturn","shortreturn"])

            self.metric.set_index("date",inplace=True)
            self.metric.sort_index(inplace=True)
            self.metric["total"] = self.metric["longreturn"]+self.metric["shortreturn"]
            #print(time_1,temp1.shape, temp2.shape, ln, sn)
    def PrepapreIndustry(self):
        data= self.zack.copy()
        data.Today = [x.date() for x in self.zack.Today]

        for l in ['Price', 'MarketCap_mil', 'SharesOutstanding_mil',
                  'AvgVolume', 'Price_Percentof52WkH-LRange', 'Percent_PriceChange_1Week',
                  'Percent_PriceChange_4Weeks', 'Percent_PriceChange_12Weeks',
                  'AverageTargetPrice', 'Percent_RatingDowngrades',
                  'Percent_RatingUpgrades', 'Percent_Rating_Hold',
                  'Percent_RatingStrongSellorSell', 'Percent_Rating_StrongBuyorBuy',
                  'Q0EPS', 'Q1EPS', 'Q2EPS', 'F0EPS', 'F1EPS', 'F2EPS', 'CurrentROE_TTM',
                  'CurrentROI_TTM', 'ROI_ 5YrAvg', 'CurrentROA_TTM', 'ROA_5YrAvg',
                  'MarketValue/Analysts', 'EBITDA_mil', 'EBIT_mil', 'NetIncome_mil',
                  'CashFlow_mil', 'NetIncomeGrowthF0/F-1', 'NetMargin_Percent',
                  'Turnover', 'InventoryTurnover', 'AssetUtilization',
                  'OperatingMargin_12Mo_Percent', 'Receivables_mil', 'Inventory_mil',
                  'Intangibles_mil', 'CurrentAssets_mil', 'CurrentLiabilities_mil',
                  'LongTermDebt_mil', 'PreferredEquity_mil', 'CommonEquity_mil',
                  'BookValue', 'Debt/TotalCapital', 'Debt/EquityRatio', 'CurrentRatio',
                  'QuickRatio', 'CashRatio']:
            self.zack[l] = [np.nan if x == "NULL" else float(x) for x in self.zack[l]]

        self.featurelist.append('Percent_PriceChange_12Weeks')
        self.featurelist.append('Percent_PriceChange_4Weeks')

        self.zack["PercentTarget"] = (self.zack["Price"] - self.zack['AverageTargetPrice']) / (self.zack['AverageTargetPrice'] + 0.0001)
        self.featurelist.append("PercentTarget")
        self.featurelist.append("QEG1")
        self.featurelist.append("QEG2")
        self.zack["QEG1"] = (self.zack["Q1EPS"] - self.zack["Q0EPS"]) / (self.zack["Q0EPS"] + 0.0001)
        self.zack["QEG2"] = (self.zack["Q2EPS"] - self.zack["Q1EPS"]) / (self.zack["Q1EPS"] + 0.0001)
        self.featurelist.append("FEG1")
        self.featurelist.append("FEG2")
        self.zack["FEG1"] = (self.zack["F1EPS"] - self.zack["F0EPS"]) / (self.zack["F0EPS"] + 0.0001)
        self.zack["FEG2"] = (self.zack["F2EPS"] -self.zack["F1EPS"]) / (self.zack["F1EPS"] + 0.0001)
        self.featurelist.append("FPE1")
        self.featurelist.append("FPE2")
        self.zack["FPE1"] = self.zack["Price"] / (self.zack["F1EPS"] + 0.0001)
        self.zack["FPE2"] = self.zack["Price"] / (self.zack["F2EPS"] + 0.0001)
        self.featurelist.append("FPEG1")
        self.featurelist.append("FPEG2")
        self.zack["FPEG1"] = self.zack["Price"] / (self.zack["FEG1"] + 0.0001)
        self.zack["FPEG2"] = self.zack["Price"] / (self.zack["FEG2"] + 0.0001)
        self.featurelist.append("QPE1")
        self.featurelist.append("QPE2")
        self.zack["QPE1"] =self.zack["Price"] / (self.zack["Q1EPS"] + 0.0001)
        self.zack["QPE2"] = self.zack["Price"] / (self.zack["Q2EPS"] + 0.0001)
        self.featurelist.append("QPEG1")
        self.featurelist.append("QPEG2")
        self.zack["QPEG1"] =self.zack["Price"] / (self.zack["QEG1"] + 0.0001)
        self.zack["QPEG2"] =self.zack["Price"] / (self.zack["QEG2"] + 0.0001)
        self.featurelist.append('CurrentROE_TTM')
        self.featurelist.append('CurrentROI_TTM')
        self.featurelist.append('CurrentROA_TTM')
        self.featurelist.append('EBITDA_mil')
        self.featurelist.append('EBIT_mil')
        self.featurelist.append('NetIncomeGrowthF0/F-1')
        self.cl=None
        for x in ['Debt/TotalCapital', 'Debt/EquityRatio', 'CurrentRatio']:
            self.featurelist.append(x)
            # data.columns


    def getZack(self):
        df = ws.msql.table2df("macro", "zack")
        df = df[df["Sector"] == self.sector]
        df = df.drop_duplicates(subset=["Today", "Ticker"], keep="last")
        df.Today.value_counts().sort_index()
        df["Price"] = [float(x) for x in df["Price"]]
        df = df[df["Sector"] ==self.sector]
        df["Today"] = pd.to_datetime(df["Today"])
        df = df.drop_duplicates(subset=["Today", "Ticker"])
        cl = df.Ticker.value_counts().index
        df = df.sort_values(by=["Today"])
        df = df.set_index("Ticker")
        df["Y"]=np.nan
        self.zack=df

    def getDailyStock(self,Trend=False):
        if self.sector=="Computer and Technology":
            market = ws.msql.table2df("market", "yf_computer_1d")
        elif self.sector=="Medical":
            market = ws.msql.table2df("market", "yf_health_1d")

        elif self.sector=="Finance":
            market = ws.msql.table2df("market", "yf_finance_1d")
        elif self.sector == "Oils-Energy":
            market = ws.msql.table2df("market", "yf_energy_1d")
        elif self.sector == "Business Services":
            market = ws.msql.table2df("market", "yf_service_1d")
        elif self.sector == "Industrial Products":
            market = ws.msql.table2df("market", "yf_products_1d")
        elif self.sector == "Consumer Discretionary":
            market = ws.msql.table2df("market", "yf_discretionary_1d")

        market["Date"] = pd.to_datetime(market["Date"])
        market = market.drop_duplicates(subset=["Date", "Symbol"])
        market = market.set_index("Symbol")
        market = market.sort_values(by=["Date"])
        if Trend==True:
            market["fast"]=np.nan
            market["slow"]=np.nan
            for c in market.index.value_counts().index:
                market.loc[market.index == c, "fast"]=market.loc[market.index == c, "Open"].rolling(5).mean()
                market.loc[market.index == c, "slow"]=market.loc[market.index == c, "Open"].rolling(20).mean()
                market.loc[market.index == c, "future"]=market.loc[market.index == c, "Open"].shift(-1)-market.loc[market.index == c, "Open"]
        self.dailymarket=market

    def prepareTrain(self):
        #self.zack=self.zack.set_index("Ticker")
        cl = set(self.zack.index.value_counts().index).intersection(self.dailymarket.index.value_counts().index)
        #print(self.zack.index.value_counts().index)
        #print(self.dailymarket.index.value_counts().index)
        #print(cl)
        self.cl=cl
        for c in cl:
            self.dailymarket.loc[c, "Y"] = self.dailymarket.loc[c, "Open"].pct_change(self.lookback_window)
            commondate = list(set(self.dailymarket.loc[c, "Date"]).intersection(set(self.zack.loc[c, "Today"])))
            self.zack.loc[(self.zack.index == c) & (self.zack.Today.isin(commondate)), "Y"] = self.dailymarket.loc[
                (self.dailymarket.index == c) & self.dailymarket.Date.isin(commondate), "Y"]

        self.PrepapreIndustry()
        self.zack =self.zack.reset_index()
        self.ind=self.zack.Today.value_counts().sort_index().index
        self.rank = pd.DataFrame(index=self.ind, columns=self.zack.Ticker.value_counts().index)



    def handleMissingValue(self):
        dl = self.zack[ self.zack["Today"] == pd.to_datetime( self.zack["Today"].iloc[-1]).date()].isnull().sum().sort_values().tail(
            3).index
        columns = list( self.zack.columns)
        for n in dl:
            if n in columns:
                columns.remove(n)
            if n in self.featurelist:
                self.featurelist.remove(n)
        self.zack = self.zack[columns]
        self.zack = self.zack.loc[self.zack[self.featurelist].dropna().index]
        self.zack = self.zack.dropna(subset=["Y"])


    def getMinuteData(self):
        if self.sector=="Computer and Technology":
            self.hfmarket = ws.msql.table2df("market", "yf_computer_5m")
        elif self.sector == "Medical":
            self.hfmarket = ws.msql.table2df("market", "yf_health_5m")
        elif self.sector == "Finance":
            self.hfmarket = ws.msql.table2df("market", "yf_finance_5m")
        elif self.sector == "Oils-Energy":
            self.hfmarket = ws.msql.table2df("market", "yf_energy_5m")

        elif self.sector == "Business Services":
            market = ws.msql.table2df("market", "yf_service_5m")
        elif self.sector == "Industrial Products":
            market = ws.msql.table2df("market", "yf_products_5m")
        self.hfmarket["Datetime"] = pd.to_datetime(self.hfmarket["Datetime"])
        self.hfmarket = self.hfmarket.sort_values(by="Datetime")
        self.hfmarket["Date"] = [x.date() for x in self.hfmarket.Datetime]
        self.hfmarket = self.hfmarket.loc[self.hfmarket.Date > self.zack.Today.iloc[0].date()]
        self.hfmarket = self.hfmarket.set_index("Symbol")
