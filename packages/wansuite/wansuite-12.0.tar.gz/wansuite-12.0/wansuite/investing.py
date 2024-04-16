import sqlite3
import time 
from bs4 import BeautifulSoup
from helium import *
import pandas as pd
from . import msql
def idfromurl(url):
    id_url=None
    for n in range(10):
        if url[-n]!="-":
            id_url=url[-n:]
        else:
            break
    return id_url

    
def updateToday(newlink,sql,res):
    update=pd.DataFrame(columns=["index","time",	"country","indicator","value","forecast"])
    resource=msql.table2df(sql,res).drop_duplicates(subset="link").set_index("link")
    for l in newlink:
        cou=resource.loc[l,"country"]
        ind=resource.loc[l,"indicator"]
        url=l
        url_id=idfromurl(url)
        driver=start_chrome(url,headless=True)
        #driver.find_element("id", "showMoreHistory"+url_id).click()
        if url=="https://www.investing.com/economic-calendar/interest-rate-decision-168":
            for n in range(2):
                try:

                    driver.find_element("id", "showMoreHistory"+url_id).click()
                    time.sleep(1)
                    #driver.find_element_by_link_text("Show more").click()
                except:
                    break
      
        html_source=driver.page_source
        data=pd.read_html(html_source)[0].set_index("Release Date")[["Time","Actual","Forecast"]]
        #kill_browser()
        driver.quit()

       
        
        
        newind=[]
        for l in data.index:
            l=str(l)
            if l[-1]==")":
                newind.append(l[:-5])
            else:
                newind.append(l)
        data.index=newind
        data.index=pd.to_datetime(data.index).date
        data=data.sort_index()
        data=data.reset_index().drop_duplicates(subset=["index"]).set_index("index")
        if str(data.iloc[0]["Actual"])[-1]=="K":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("K","").replace("-","").replace(",",""))*1000)
                else:
                    val0.append(float(al0.replace("K","").replace(",",""))*1000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("K","").replace("-","").replace(",",""))*1000)
                else:
                    val0.append(float(al0.replace("K","").replace(",",""))*1000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0    
        elif str(data.iloc[0]["Actual"])[-1]=="M":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("M","").replace("-","").replace(",",""))*1000000)
                else:
                    val0.append(float(al0.replace("M","").replace(",",""))*1000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("M","").replace("-","").replace(",",""))*1000000)
                else:
                    val0.append(float(al0.replace("M","").replace(",",""))*1000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0    
        elif str(data.iloc[0]["Actual"])[-1]=="B":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("B","").replace("-","").replace(",",""))*1000000000)
                else:
                    val0.append(float(al0.replace("B","").replace(",",""))*1000000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("B","").replace("-","").replace(",",""))*1000000000)
                else:
                    val0.append(float(al0.replace("B","").replace(",",""))*1000000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0  
        elif str(data.iloc[0]["Actual"])[-1]=="T":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("T","").replace("-","").replace(",",""))*1000000000000)
                else:
                    val0.append(float(al0.replace("T","").replace(",",""))*1000000000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("T","").replace("-","").replace(",",""))*1000000000000)
                else:
                    val0.append(float(al0.replace("T","").replace(",",""))*1000000000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0  
        elif str(data.iloc[0]["Actual"])[-1]=="%":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("%","").replace("-","").replace(",",""))/100)
                else:
                    val0.append(float(al0.replace("%","").replace(",",""))/100)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("%","").replace("-","").replace(",",""))/100)
                else:
                    val0.append(float(al0.replace("%","").replace(",",""))/100)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0   
        newdate=data["Actual"].dropna().index[-1]
        update.loc[len(update)]=[str(newdate),data.loc[newdate,"Time"],cou,ind, data.loc[newdate,"Actual"],data.loc[newdate,"Forecast"]]
        print(newdate,cou,ind)
    return update
    
def addNewFeature(addlist,sql,table):
    '''
    addlist=[["us","Featurename",link],[]]
    save to sql.table
    '''
    newfeature=pd.DataFrame(columns=["country","indicator","link"])
    for l in addlist:
        newfeature.loc[len(newfeature)]=l
    msql.df2table(sql,newfeature,table,"append")

    
    
def buildNewFeature(addlist):
    
    '''
    new
    addlist=[["us","Featurename",link],[]]
    output: new data point
    '''
   
    new=pd.DataFrame(columns=["index","time","country","indicator","value","forecast"])
    for l in addlist:
        url=l[2]
        cou=l[0]
        indi=l[1]
        url_id=idfromurl(url)
        driver=start_chrome(url,headless=True)
        for n in range(200):
            try:

                driver.find_element("id", "showMoreHistory"+url_id).click()
                time.sleep(1)
                #driver.find_element_by_link_text("Show more").click()
            except:
                break
        print(indi,n)
        html_source=driver.page_source
        kill_browser()
        #driver.quit()
        data=pd.read_html(html_source)[0].set_index("Release Date")[["Time","Actual","Forecast"]]


        newind=[]
        for l in data.index:
            l=str(l)
            if l[-1]==")":
                newind.append(l[:-5])
            else:
                newind.append(l)
        data.index=newind
        data.index=pd.to_datetime(data.index)
        data=data.sort_index().drop_duplicates().rename_axis("date").reset_index().drop_duplicates(subset="date").set_index("date")
        if str(data.iloc[0]["Actual"])[-1]=="K":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("K","").replace("-","").replace(",",""))*1000)
                else:
                    val0.append(float(al0.replace("K","").replace(",",""))*1000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("K","").replace("-","").replace(",",""))*1000)
                else:
                    val0.append(float(al0.replace("K","").replace(",",""))*1000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0    
        elif str(data.iloc[0]["Actual"])[-1]=="M":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("M","").replace("-","").replace(",",""))*1000000)
                else:
                    val0.append(float(al0.replace("M","").replace(",",""))*1000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("M","").replace("-","").replace(",",""))*1000000)
                else:
                    val0.append(float(al0.replace("M","").replace(",",""))*1000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0    
        elif str(data.iloc[0]["Actual"])[-1]=="B":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("B","").replace("-","").replace(",",""))*1000000000)
                else:
                    val0.append(float(al0.replace("B","").replace(",",""))*1000000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("B","").replace("-","").replace(",",""))*1000000000)
                else:
                    val0.append(float(al0.replace("B","").replace(",",""))*1000000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0  
        elif str(data.iloc[0]["Actual"])[-1]=="T":
            val0=[]
            for al0 in data["Actual"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("T","").replace("-","").replace(",",""))*1000000000000)
                else:
                    val0.append(float(al0.replace("T","").replace(",",""))*1000000000000)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("T","").replace("-","").replace(",",""))*1000000000000)
                else:
                    val0.append(float(al0.replace("T","").replace(",",""))*1000000000000)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0   
        elif "%" in str(data["Actual"].dropna().iloc[-1]):
            val0=[]
            for al0 in data["Actual"].dropna():
                if "-" in al0:
                    val0.append(-float(al0.replace("%","").replace("-","").replace(",",""))/100)
                else:
                    val0.append(float(al0.replace("%","").replace(",",""))/100)
            data.loc[data["Actual"].dropna().index,"Actual"]=val0   
            val0=[]
            for al0 in data["Forecast"].dropna():
                if al0[0]=="-":
                    val0.append(-float(al0.replace("%","").replace("-","").replace(",",""))/100)
                else:
                    val0.append(float(al0.replace("%","").replace(",",""))/100)
            data.loc[data["Forecast"].dropna().index,"Forecast"]=val0   

        for d in data.index:
            da=str(d)
            t=str(data.loc[d,"Time"])
            v=float(data.loc[d,"Actual"])
            p=float(data.loc[d,"Forecast"])

            new.loc[len(new)]=[da,t,cou,indi,v,p]
    return new    
def updateTableDaily(table,linklist):
    '''
    table: name of table to save data "investing"
    linklist: link we need to update to table
    '''
    
    for n in linklist:
        try:
            update=updateToday([n],"macro","resource")
            msql.df2table("macro",update,table,"append")
        except:
            print("The following link does not work")
            print(n)
            pass
        
        
        
def getLink(lockkey):
    url="https://www.investing.com/economic-calendar/"
    
    elem = start_chrome(url,headless=True).find_elements_by_xpath("//*[@href]")
    kill_browser()
    
    newlink=[]
    for el in elem:
        a=el.get_attribute("href")
        if a[:43]=='https://www.investing.com/economic-calendar' and a!='https://www.investing.com/economic-calendar/' and a!= 'https://www.investing.com/economic-calendar/#':
            block=False
            for k in lockkey:
                if k in a:
                    block=True
                    break
            if block==False:
                newlink.append(a)
    addlist=[]
    resource=msql.table2df("macro","resource").drop_duplicates().set_index("link")
    for l in newlink:
        if l not in resource.index:
            addlist.append(["","",l])
    return newlink,addlist