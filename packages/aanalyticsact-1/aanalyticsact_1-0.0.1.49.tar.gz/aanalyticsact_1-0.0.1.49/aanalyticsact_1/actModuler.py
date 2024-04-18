# Created by Sunkyeong Lee
# Inquiry : sunkyeong.lee@concentrix.com / sunkyong9768@gmail.com
# Updated by Youngkwang Cho 
# Inquiry : youngkwang.Cho@concentrix.com 

import aanalytics2 as api2
import aanalyticsactauth as auth
import json
from datetime import datetime, timedelta
from copy import deepcopy
from sqlalchemy import create_engine
import os
import re

from sqlalchemy import pool   ###YK
from sqlalchemy.pool import NullPool ###YK
import pandas as pd ###YK


# initator
def dataInitiator():
    api2.importConfigFile(os.path.join(auth.auth, 'aanalyticsact_auth.json'))
    logger = api2.Login()
    logger.connector.config

def dataReportSuites():
    cid = "samsun0"
    ags = api2.Analytics(cid)
    ags.header
    rsids = ags.getReportSuites()
    print(rsids)

# data retrieving function
def dataretriever_data(jsonFile):
    cid = "samsun0"
    ags = api2.Analytics(cid)
    ags.header
    myreport = ags.getReport(jsonFile, limit=1000000, n_results='inf')
    return myreport['data']


def dataretriever_data_breakdown(jsonFile):
    cid = "samsun0"
    ags = api2.Analytics(cid)
    ags.header
    myreport1 = ags.getReport(jsonFile, limit=1000000, n_results='inf',item_id=True)
    data_report = myreport1['data']

    return data_report


def exportToCSV(dataSet, fileName):
    dataSet.to_csv(fileName, sep=',', index=False)


def returnRsID(jsonFile):
    with open(jsonFile, 'r', encoding='UTF-8') as bla:
        json_data = json.loads(bla.read())
    json_data.pop("capacityMetadata")
    rsID = json_data['rsid']

    return rsID


def EndDateCalculation(startDate, endDate):
    startDate = str(startDate)
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    endDate += timedelta(days=1)
    endDate = str(endDate)

    return startDate, endDate


def timeChanger(time_obj, start):
    if start == True:
        return str('T' + time_obj + ':00.000/')
    else:
        time_obj = datetime.strptime(time_obj, "%H:%M")
        time_obj += timedelta(minutes=1)
        return str('T' + str(time_obj.strftime("%H:%M"))+ ':00.000')
    

def jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour):

    startDate = EndDateCalculation(startDate, endDate)[0]
    endDate = EndDateCalculation(startDate, endDate)[1]

    with open(jsonFile, 'r', encoding='UTF-8') as bla:
        json_data = json.load(bla)
    json_data.pop("capacityMetadata")

    globalFilterElement = json_data['globalFilters']
    if start_hour == "00:00" and end_hour == "00:00":
        tobeDate = str(startDate + "T00:00:00.000/" + endDate + "T00:00:00.000")
    else :
        tobeDate = str(startDate + timeChanger(start_hour, True) + endDate + timeChanger(end_hour, False))
        
    for i in range(len(globalFilterElement)):
        globalFilterElement[i]['dateRange'] = tobeDate

    json_data['globalFilters'] = globalFilterElement
    
    return json_data

def addStartEndDateColumn(startDate, endDate, rowNum):
    startDateList = []
    endDateList = []

    for i in range(rowNum):
        startDateList.append(startDate)
        endDateList.append(endDate)

    return startDateList, endDateList

def checkSiteCode(dimension):
    if (dimension == "variables/prop1" or dimension == "variables/evar1" or dimension == "variables/entryprop1"):
        return True

    else:
        return False

# 1st Level data Caller
def refinedFrame(startDate, endDate, period, jsonFile, epp, if_site_code, site_code_rs, start_hour, end_hour):
    dataInitiator()
    dateChange = jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour)
    dataFrame = dataretriever_data(dateChange)

    if dateChange['rsid'] != "sssamsung4mstglobal":
        columnList = []
        for i in range(dataFrame.shape[1]):
            columnList.append(i)

        dataFrame.columns = columnList

        if site_code_rs == True:
            dataFrame = dataFrame.drop(0,axis =1)

        if dateChange['rsid'] == "sssamsungnewus":
            dataFrame.insert(0, "site_code", "us", True)

        else:
            rsName = dateChange['rsid'].split('4')
            if "epp" in rsName[-1]:
                dataFrame.insert(0, "site_code", rsName[-1].replace('epp', ''), True)
                epp = "Y"
            else:
                dataFrame.insert(0, "site_code", rsName[-1], True)

    if (if_site_code == True or site_code_rs == True):
        dataFrame.insert(1, "period", period, True)
        if start_hour == "00:00" and end_hour == "00:00":
            dataFrame.insert(2, "start_date", startDate, True)
            dataFrame.insert(3, "end_date", endDate, True)
        else :
            dataFrame.insert(2, "start_date", "{0} {1}".format(startDate, start_hour), True)
            dataFrame.insert(3, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)     
        dataFrame.insert(4, "is_epp", epp, True)
    else:
        if dateChange['rsid'] == "sssamsung4mstglobal":
            dataFrame.insert(0, "site_code", "MST", True)
        dataFrame.insert(2, "period", period, True)
        if start_hour == "00:00" and end_hour == "00:00":
            dataFrame.insert(3, "start_date", startDate, True)
            dataFrame.insert(4, "end_date", endDate, True)        
        else :
            dataFrame.insert(3, "start_date", "{0} {1}".format(startDate, start_hour), True)
            dataFrame.insert(4, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)
        dataFrame.insert(5, "is_epp", epp, True)

    return dataFrame  
# updated 220527. smb site code added
# updated 221202. my bday! :D smb site code added (10.31 open)
def filterSiteCode(dataframe, site_code):
    if site_code != "":
        return dataframe.loc[dataframe['site_code'].isin(site_code)]
    else :
       return dataframe.loc[dataframe['site_code'].isin(["kw", "kw_ar", "bh", "bh_ar", "om", "om_ar", "eg_en", "jo", "jo_ar", "ma", "africa_en", "africa_fr", "africa_pt", "al", "ar", "au", "at", "az", "be", "be_fr", "br", "ba", "bd", "bg", "ca", "ca_fr", "cl", "cn", "co", "hr", "cz", "dk", "eg", "ee", "fi", "fr", "de", "gr", "hk", "hk_en", "hu", "in", "id", "iran", "ie", "il", "it", "jp", "kz_ru", "kz_kz", "sec", "lv", "levant", "levant_ar", "lt", "mk", "my", "mx", "mm", "nl", "nz", "n_africa", "no", "pk", "latin", "latin_en", "py", "pe", "ph", "pl", "pt", "ro", "ps", "ru", "sa", "sa_en", "rs", "sg", "sk", "si", "za", "es", "se", "ch", "ch_fr", "tw", "th", "tr", "ae", "ae_ar", "uk", "ua", "uy", "uz_ru", "uz_uz", "vn", "au-smb", "uk-smb", "fr-smb", "at-smb", "it-smb", "es-smb", "th-smb", "id-smb", "vn-smb", "my-smb", "se-smb", "dk-smb", "fi-smb", "no-smb", "ca-smb", "ca_fr-smb", "de-smb", "nl-smb", "be-smb", "be_fr-smb", "jo-smb", "jo_ar-smb", "ae-smb", "ae_ar-smb", "nz-smb", "ph-smb", "ru-smb", "iq_ar", "iq_ku", "lb", "qa", "qa_ar", "eg-smb", "pl-smb", "pt-smb", "sa_en-smb", "sa-smb", "sg-smb", "eg_en-smb", "mn", "ge"])] 


# updated 210907. added site_code_rs for us integration(us has no site code)
def jsonToDb(startDate, endDate, period, jsonLocation, tbColumn, dbTableName, epp, if_site_code, site_code_rs, limit, extra, start_hour, end_hour, site_code):
    df = refinedFrame(startDate, endDate, period, jsonLocation, epp, if_site_code, site_code_rs, start_hour, end_hour)
    df.columns = tbColumn
    if extra != "":
        df.insert(5, "extra", extra, True)

    if limit == 0:
        df = df
    else:
        df = df.head(limit)

    if if_site_code == True:
        if returnRsID(jsonLocation) == "sssamsung4mstglobal":
            df = filterSiteCode(df, site_code)
 
    stackTodb(df, dbTableName)

def create_connection_pool():   ###YK
    db_connection_str = 'mysql+pymysql://root:12345@127.0.0.1:3307/act'
    pool_size = 20  
    max_overflow = 10  
    return create_engine(db_connection_str, encoding='utf-8', poolclass=pool.QueuePool, pool_size=pool_size, max_overflow=max_overflow)

def stackTodb(dataFrame, dbTableName):  ###YK
    print(dataFrame)
    db_connection = create_connection_pool()
    with db_connection.connect() as conn:
    	dataFrame = unicodeCompile_df(dataFrame)
    	dataFrame.to_sql(name=dbTableName, con=conn, if_exists='append', index=False)
    db_connection.dispose()
    print("finished")
   
""" MST breakdown """

# breakdown itemID
def ChangeItemID(itemID, breakdownJson):
    temp_breakdownJson = deepcopy(breakdownJson)
    before_temp = temp_breakdownJson['metricContainer']['metricFilters']

    # change date > call using itemID iteration
    after_temp = deepcopy(before_temp)
    for i in range(len(after_temp)):
        if "itemId" in after_temp[i]:
            after_temp[i]["itemId"] = itemID
        else:
            continue

    temp_breakdownJson['metricContainer']['metricFilters'] = after_temp

    return temp_breakdownJson


def readJson(jsonFile):
    with open(jsonFile, 'r', encoding='UTF-8') as bla:
        json_data = json.loads(bla.read())
    json_data.pop("capacityMetadata")
    return json_data
        

def returnItemID(startDate, endDate, jsonItemID, start_hour, end_hour, site_code):
    jsonFile = deepcopy(jsonItemID)
    itemIDjson = jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour)

    dataInitiator()

    itemIDdf = dataretriever_data_breakdown(itemIDjson)

    columnList = list(map(str, range(itemIDdf.shape[1])))   

    columnList[0] = 'site_code'
    columnList[-1] = 'item_id'

    itemIDdf.columns = columnList

    if (itemIDjson["dimension"] == "variables/prop1" or itemIDjson["dimension"] == "variables/evar1" or itemIDjson["dimension"] == "variables/entryprop1"):
        itemIDdfFiltered = filterSiteCode(itemIDdf, site_code)
        itemIDlist = itemIDdfFiltered[['site_code', 'item_id']].values.tolist()        

    else:
        itemIDlist = itemIDdf[['site_code', 'item_id']].values.tolist()

    return itemIDlist

def returnItemID_rs(jsonItemID):
    dataInitiator()

    itemIDdf = dataretriever_data_breakdown(jsonItemID)

    columnList = list(map(str, range(itemIDdf.shape[1])))   

    columnList[0] = 'site_code'
    columnList[-1] = 'item_id'

    itemIDdf.columns = columnList
    itemIDlist = itemIDdf[['site_code', 'item_id']].values.tolist()

    return itemIDlist

#emoji eliminator
def unicodeCompile_df(df):
    only_BMP_pattern = re.compile("["
                                  u"\U00010000-\U0010FFFF"  # out of BMP characters 
                                  "]+", flags=re.UNICODE)

    def remove_non_bmp(text):
        if isinstance(text, str):
            return only_BMP_pattern.sub(r'', text) # only BMP characters
        else:
            return text  # 문자열이 아닌 경우 그대로 반환

    return df.applymap(remove_non_bmp)

# Save as dictionary format return in tuple
def ReturnJsonchanged(startDate, endDate, jsonFile, jsonFilebreakdown, start_hour, end_hour, site_code):
    itemIDList = returnItemID(startDate, endDate, jsonFile, start_hour, end_hour, site_code)

    itemIDdict = {}
    for i in range(len(itemIDList)):
        jsonbreakdown = jsonDateChange(startDate, endDate, jsonFilebreakdown, start_hour, end_hour)
        itemIDdict[itemIDList[i][0]] = ChangeItemID(itemIDList[i][1], jsonbreakdown)
    
    itemIDdict = list(zip(itemIDdict.keys(), itemIDdict.values()))
    
    return itemIDdict

def StackbreakValue(startDate, endDate, period, jsonFile, jsonFilebreakdown, tbColumn, dbTableName, epp, limit, extra, start_hour, end_hour, site_code):
    if returnRsID(jsonFile) == "sssamsung4mstglobal":
        itemIDdict = ReturnJsonchanged(startDate, endDate, jsonFile, jsonFilebreakdown, start_hour, end_hour, site_code)

        # iterable = list(map(int, range(len(itemIDdict))))

        # pool = multiprocessing.Pool(4)
        # func = partial(mstbreakDown, itemIDdict, startDate, endDate, period, tbColumn, dbTableName, epp, limit)
        # pool.map(func, iterable)
        # pool.close()
        # pool.join()

        for i in range(len(itemIDdict)):
            dataFrame = dataretriever_data(itemIDdict[i][1])

            if limit == 0:
                dataFrame2 = dataFrame
            else:
                dataFrame2 = dataFrame.head(limit)

            dataFrame2.insert(0, "site_code", itemIDdict[i][0], True)
            dataFrame2.insert(2, "period", period, True)
            if start_hour == "00:00" and end_hour == "00:00":
                dataFrame2.insert(3, "start_date", startDate, True)
                dataFrame2.insert(4, "end_date", endDate, True)
            else :
                dataFrame2.insert(3, "start_date", "{0} {1}".format(startDate, start_hour), True)
                dataFrame2.insert(4, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)
            dataFrame2.insert(5, "is_us_epp", epp, True)

            dataFrame2.columns = tbColumn
            if extra != "":
                dataFrame2.insert(6, "extra", extra, True)

            stackTodb(dataFrame2, dbTableName)

    else:
        dataInitiator()
        dateChange = jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour)
        dataFrame = dataretriever_data(dateChange)

        dataFrame.columns = list(map(int, range(dataFrame.shape[1])))
        
        if limit == 0:
            dataFrame2 = dataFrame
        else:
            dataFrame2 = dataFrame.head(limit)

        if returnRsID(jsonFile) == "sssamsungnewus":
            dataFrame2.insert(0, "site_code", "us", True)
        else:
            rsName = dateChange['rsid'].split('4')
            dataFrame2.insert(0, "site_code", rsName[-1], True)   

        dataFrame2.insert(2, "period", period, True)
        if start_hour == "00:00" and end_hour == "00:00":
            dataFrame2.insert(3, "start_date", startDate, True)
            dataFrame2.insert(4, "end_date", endDate, True)
        else :
            dataFrame2.insert(3, "start_date", "{0} {1}".format(startDate, start_hour), True)
            dataFrame2.insert(4, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)
        dataFrame2.insert(5, "is_us_epp", epp, True)

        dataFrame2.columns = tbColumn
        if extra != "":
           dataFrame2.insert(6, "extra", extra, True)

        stackTodb(dataFrame2, dbTableName)

"""Return after RS Name changed"""

def rsIDchange(jsonFile, rsID):
    temp_simple = deepcopy(jsonFile)
    temp_simple['rsid'] = rsID

    return temp_simple

def refineRsIDChange(startDate, endDate, jsonFile, rsList, period, tbColumn, epp, extra, start_hour, end_hour):
    datechanged = jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour)
    rschanged = rsIDchange(datechanged, rsList[1])

    dataInitiator()
    dataFrame = dataretriever_data(rschanged)

    columnList = []
    for i in range(dataFrame.shape[1]):
        columnList.append(i)

    dataFrame.columns = columnList

    dataFrame.insert(0, "site_code", rsList[0], True)
    dataFrame.insert(2, "period", period, True)
    if start_hour == "00:00" and end_hour == "00:00":
        dataFrame.insert(3, "start_date", startDate, True)
        dataFrame.insert(4, "end_date", endDate, True)
    else :
        dataFrame.insert(3, "start_date", "{0} {1}".format(startDate, start_hour), True)
        dataFrame.insert(4, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)

    if epp == True:
        dataFrame.insert(5, "is_epp", "Y", True)
    else:
        dataFrame.insert(5, "is_epp", "N", True)

    if (rsList[1] == "sssamsungnewus" or rsList[1] == "sssamsung4sec"):
        dataFrame.insert(6, "is_epp_integ", "Y", True)
    else:
        dataFrame.insert(6, "is_epp_integ", "N", True)
            
    dataFrame.columns = tbColumn
    if extra != "":
        dataFrame.insert(7, "extra", extra, True)

    return dataFrame

def secondCaller(startDate, endDate, jsonFile, jsonFilebreakdown, rsList, limit, period, tbColumn, dbTableName, epp, extra="", start_hour="00:00", end_hour="00:00"):
    dateChanged_json = jsonDateChange(startDate, endDate, jsonFile, start_hour, end_hour)
    dateChanged_bd_json = jsonDateChange(startDate, endDate, jsonFilebreakdown, start_hour, end_hour)
    
    rsChanged_json = rsIDchange(dateChanged_json, rsList[1])
    rsChanged_json_bd = rsIDchange(dateChanged_bd_json, rsList[1])

    itemIDList = returnItemID_rs(rsChanged_json)

    itemIDdict = {}
    for i in range(len(itemIDList)):
        itemIDdict[itemIDList[i][0]] = ChangeItemID(itemIDList[i][1], rsChanged_json_bd)
    
    itemIDdict = list(zip(itemIDdict.keys(), itemIDdict.values()))

    for i in range(len(itemIDdict)):
        dataFrame = dataretriever_data(itemIDdict[i][1])
        
        if limit == 0:
            dataFrame2 = dataFrame
        else:
            dataFrame2 = dataFrame.head(limit)

        dataFrame2.insert(0, "site_code", rsList[0], True)
        dataFrame2.insert(1, "dimension", itemIDdict[i][0], True)
        dataFrame2.insert(3, "period", period, True)
        if start_hour == "00:00" and end_hour == "00:00":
            dataFrame2.insert(4, "start_date", startDate, True)
            dataFrame2.insert(5, "end_date", endDate, True)
        else :
            dataFrame2.insert(4, "start_date", "{0} {1}".format(startDate, start_hour), True)
            dataFrame2.insert(5, "end_date", "{0} {1}".format(EndDateCalculation("0", endDate)[1], end_hour), True)
        dataFrame2.insert(6, "epp", epp, True)
        
        if extra != "":
            dataFrame2.insert(7, "extra", extra, True)
        dataFrame2.columns = tbColumn
        stackTodb(dataFrame2, dbTableName)