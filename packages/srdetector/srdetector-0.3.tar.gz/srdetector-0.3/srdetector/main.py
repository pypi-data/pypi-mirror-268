import yfinance as yfi
import numpy as np
import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta

def srdetector(ticker, interval, sensitivity):
    list200=['1d','5d','1wk','1mo','3mo']
    list60=['1m','2m','5m','15m','30m','60m','90m','1h']
    if interval in list200:
        timedel=200
    elif interval in list60:
        timedel=60
    else:
        raise ValueError("Incorrect input for interval. use srdetector.help() for instructions")
    if sensitivity>=1 and sensitivity<=10:
        sensitivity=12-sensitivity
    else:
        raise ValueError('Incorrect input for sensitivity parameter. use srdetector.help() for instructions')
    def addcol(arr, count):
        if not isinstance(arr, np.ndarray):
            raise TypeError("Input 'arr' must be a NumPy array.")

        if arr.size == 0:
            raise ValueError("Input 'arr' is empty.")

        #print("Shape of arr:", arr.shape)  # Debugging print

        new_arr = np.empty((arr.shape[0], arr.shape[1] + count), dtype=arr.dtype)
        new_arr[:, :arr.shape[1]] = arr
        new_arr[:, arr.shape[1]:] = np.nan  # Fill the new columns with np.nan
        return new_arr

    def removenan(arr):
        templist=[]
        for index, i in enumerate(arr):
            for j in i:
                if np.isnan(j):
                    templist.append(index)
        arr=np.delete(arr, templist, axis=0)
        return arr

    enddate = datetime.now()
    startdate = enddate - timedelta(days=timedel)
    try:
        df = yfi.download(tickers=ticker, start=startdate, end=enddate, interval=interval)
    except:
        raise ValueError('Invalid Ticker')
    df['Average'] = (df['High'] + df['Low']) / 2
    df['SMA20'] = ta.sma(df['Average'], sensitivity)
    df['maxval']=''
    df['minval']=''
    df=df.round(2)
    df.dropna(inplace=True)
    for i in range(0, len(df)):
        templist=[df['High'].iloc[i],df['Low'].iloc[i],df['Close'].iloc[i],df['Open'].iloc[i], df['SMA20'].iloc[i]]
        maxval=max(templist)
        minval=min(templist)
        df.at[df.index[i], 'maxval']=maxval
        df.at[df.index[i], 'minval']=minval
    global currprice
    currprice=df['Close'].iloc[-1]
    df = df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'])
    data=df.values

    #Calculating support levels
    ds1=data 
    ds2=data
    templist=[]
    for index, value in enumerate(ds1):
        if value[2]>(currprice):
            templist.append(index)
    ds1=np.delete(ds1, templist, axis=0)
    global scond
    if len(ds1)<=10:
        scond=True
    else:
        scond=False
    ds1=addcol(ds1, 3)
    for i in range(1,len(ds1)):

        appensionf=0
        appensionb=0
        #-------------------------------------------------------------

        backpoints=0
        backchance=8
        for j in range(i,-1,-1):
            if backchance==0 or j==0 or i==len(ds1)-1:
                appensionb=ds1[j, 2]
                break
            elif ((ds1[j,2]>ds1[j+1,2])):
                backpoints=backpoints+1
            else:
                backpoints=backpoints+1
                backchance=backchance-1
        ds1[i,5]=backpoints

        #-------------------------------------------------------------

        frontpoints=0
        frontchance=8
        for j in range(i,len(ds1)):
            if frontchance==0 or j==(len(ds1))-1:
                appensionf=(ds1[j,2])
                break
            elif (ds1[j,2]<ds1[j+1,2]):
                frontpoints=frontpoints+1
            else:
                frontpoints=frontpoints+1
                frontchance=frontchance-1
        ds1[i,6]=frontpoints
        #-------------------------------------------------------------

        tempvar=abs(((appensionf+appensionb)/2)-(ds1[i,2]))
        ourvalue=ds1[i,2]
        if appensionb<ourvalue or appensionf<ourvalue:
            (ds1[i,7])=np.nan
        else:
            (ds1[i,7])=tempvar
    ds1=removenan(ds1)
    ds1=np.delete(ds1, 0, axis=0)
    sum_column = ds1[:, 6] + ds1[:, 5]
    ds1 = np.column_stack((ds1, sum_column))
    allval=ds1[:,7]
    maxval=np.nanmax(allval)
    sum_column = ds1[:, 7]/maxval*100
    ds1 = np.column_stack((ds1, sum_column))
    templist=np.array([x/len(ds1)*30 for x in range(len(ds1))])
    ds1 = np.column_stack((ds1, templist))
    sum_column = ds1[:, 10] + ds1[:, 9] + ds1[:, 8]
    ds1 = np.column_stack((ds1, sum_column))
    templist=[]
    for i in range(len(ds1)):
        totalpoints=0
        currval=ds1[i, 2]
        for j in range(0,len(ds1)):
            if i==j:
                continue
            else:
                subtraction=4
                addition=4

                if (j-4)<0:
                    subtraction=j
                if (j+4)>(len(ds1)-1):
                    addition=(len(ds1)-1)-j

                maxval=ds1[i,3]
                minval=ds1[i,4]
                if currval>=minval and currval<=maxval:
                    tempy=ds1[(i-subtraction):(i+addition), 11]
                    for k in tempy:
                        totalpoints=totalpoints+k
                else:
                    continue
        templist.append(totalpoints)

    maxov=np.max(templist)
    tempo=[]
    for i in templist:
        valtoap=i/maxov*100
        tempo.append(valtoap)
    ds1 = np.column_stack((ds1, tempo))
    sum_column = ds1[:, 11] + ds1[:, 12]
    ds1 = np.column_stack((ds1, sum_column))
    ds1 = ds1[:, [2,13]]

    #Calculating resistance levels
    templist=[]
    for index, value in enumerate(ds2):
        if value[2]<(currprice):
            templist.append(index)
    ds2=np.delete(ds2, templist, axis=0)
    global rcond
    if len(ds2)<=10:
        rcond=True
    else:
        rcond=False
    ds2=addcol(ds2, 3)
    for i in range(1,len(ds2)):

        appensionf=0
        appensionb=0
        #-------------------------------------------------------------

        backpoints=0
        backchance=8
        for j in range(i,-1,-1):
            if backchance==0 or j==0 or i==len(ds2)-1:
                appensionb=ds2[j, 2]
                break
            elif ((ds2[j,2]<ds2[j+1,2])):
                backpoints=backpoints+1
            else:
                backpoints=backpoints+1
                backchance=backchance-1
        ds2[i,5]=backpoints

        #-------------------------------------------------------------

        frontpoints=0
        frontchance=8
        for j in range(i,len(ds2)):
            if frontchance==0 or j==(len(ds2))-1:
                appensionf=(ds2[j,2])
                break
            elif (ds2[j,2]>ds2[j+1,2]):
                frontpoints=frontpoints+1
            else:
                frontpoints=frontpoints+1
                frontchance=frontchance-1
        ds2[i,6]=frontpoints
        #-------------------------------------------------------------

        tempvar=abs(((appensionf+appensionb)/2)-(ds2[i,2]))
        ourvalue=ds2[i,2]
        if appensionb>ourvalue or appensionf>ourvalue:
            (ds2[i,7])=np.nan
        else:
            (ds2[i,7])=tempvar
    ds2=removenan(ds2)
    ds2=np.delete(ds2, 0, axis=0)
    sum_column = ds2[:, 6] + ds2[:, 5]
    ds2 = np.column_stack((ds2, sum_column))
    allval=ds2[:,7]
    maxval=np.nanmax(allval)
    sum_column = ds2[:, 7]/maxval*100
    ds2 = np.column_stack((ds2, sum_column))
    templist=np.array([x/len(ds2)*30 for x in range(len(ds2))])
    ds2 = np.column_stack((ds2, templist))
    sum_column = ds2[:, 10] + ds2[:, 9] + ds2[:, 8]
    ds2 = np.column_stack((ds2, sum_column))
    templist=[]
    for i in range(len(ds2)):
        totalpoints=0
        currval=ds2[i, 2]
        for j in range(0,len(ds2)):
            if i==j:
                continue
            else:
                subtraction=4
                addition=4

                if (j-4)<0:
                    subtraction=j
                if (j+4)>(len(ds2)-1):
                    addition=(len(ds2)-1)-j

                maxval=ds2[i,3]
                minval=ds2[i,4]
                if currval>=minval and currval<=maxval:
                    tempy=ds2[(i-subtraction):(i+addition), 11]
                    for k in tempy:
                        totalpoints=totalpoints+k
                else:
                    continue
        templist.append(totalpoints)
    maxov=np.max(templist)
    tempo=[]
    for i in templist:
        valtoap=i/maxov*100
        tempo.append(valtoap)
    ds2 = np.column_stack((ds2, tempo))
    sum_column = ds2[:, 11] + ds2[:, 12]
    ds2 = np.column_stack((ds2, sum_column))
    ds2 = ds2[:, [2,13]]

    if scond==True:
        support=[currprice for x in range(10)]
        print('unreliable support levels due to all time low')
    if rcond==True:
        resistance=[currprice for x in range(10)]
        print('unreliable resistance levels due to all time high')

    column_names = ['Price', 'Points']
    ds1 = pd.DataFrame(ds1, columns=column_names)
    ds2 = pd.DataFrame(ds2, columns=column_names)
    ds1=ds1.sort_values(by='Points')
    ds2=ds2.sort_values(by='Points')
    support=[x for x in ds1['Price'].tolist() if x<currprice]
    resistance=[x for x in ds2['Price'].tolist() if x>currprice]
    support=sorted(support[:10], reverse=True)
    resistance=sorted(resistance[:10], reverse=False)
    finaldf=pd.DataFrame()
    finaldf['Support']=support
    finaldf['Resistance']=resistance
    
    return finaldf

def help():
    print('List of valid entries for parameters which are ticker, interval, and sensitivity')
    print('ticker: enter any valid yfinance ticker. This library runs on yfinance library')
    print('interval: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo')
    print('sensitivity: enter a number between 1 and 10 inclusive')
