# Created by Sunkyeong Lee
# Inquiry : sunkyeong.lee@concentrix.com / sunkyong9768@gmail.com

from copy import Error
# from actModuler import *
# from actRunner import *
from .actModuler import *
from .actRunner import *
import time


def retrieve_FirstLevel(start_date, end_date, period, jsonLocation, tbColumn, dbTableName, epp, site_code_rs, limit, extra = "", start_hour="00:00", end_hour="00:00", site_code = ""):
    if limit > 1000:
        raise Error("limit은 0 ~ 1000 사이 값으로 넣어주세요")

    dateCaller = dateGenerator(start_date, end_date, period)
    if_site_code = checkSiteCode(readJson(jsonLocation)["dimension"])
    
    tbColumn = tbColumnGenerator(tbColumn, if_site_code, False, False, site_code_rs)
    
    startDate = dateCaller[0]
    endDate = dateCaller[1]

    for i in range(len(startDate)):
        while True:
            try:
                start = time.time()
                jsonToDb(startDate[i], endDate[i], period, jsonLocation, tbColumn, dbTableName, epp, if_site_code, site_code_rs, limit, extra, start_hour, end_hour, site_code)
                timeSec = round(time.time() - start, 2)
                print("Time took: ", timeSec, "sec")
  
            except KeyError:
                print("Server Error occurred, please wait for the next response")
                continue

            except IndexError:
                print("Index Error occurred, please wait for the next response")
                continue

            except AttributeError:
                print("Attribute Error occurred, please wait for the next response")
                continue

            except ConnectionError:
                print("Connection Error occurred, please wait for the next response")
                continue

            except ConnectionResetError:
                print("Connection Error occurred, please wait for the next response")
                continue 
            
            break

def retrieve_SecondLevel(start_date, end_date, period, jsonLocation, jsonLocation_breakdown,tbColumn, dbTableName, epp, limit, extra = "", start_hour="00:00", end_hour="00:00", site_code=""):
    dateCaller = dateGenerator(start_date, end_date, period)
    if_site_code = checkSiteCode(readJson(jsonLocation)["dimension"])

    if returnRsID(jsonLocation) == "sssamsungnewus":
        if_site_code = True

    site_code_rs = False
    tbColumn = tbColumnGenerator(tbColumn, if_site_code, True, False, site_code_rs)
    
    startDate = dateCaller[0]
    endDate = dateCaller[1]

    for i in range(len(startDate)):
        while True:
            try:
                start = time.time()
                StackbreakValue(startDate[i], endDate[i], period, jsonLocation, jsonLocation_breakdown, tbColumn, dbTableName, epp, limit, extra, start_hour, end_hour, site_code)
                timeSec = round(time.time() - start, 2)
                print("Time took: ", timeSec, "sec")

            except KeyError:
                print("Server Error occurred, please wait for the next response")
                continue

            except IndexError:
                print("Index Error occurred, please wait for the next response")
                continue

            except AttributeError:
                print("Attribute Error occurred, please wait for the next response")
                continue

            except ConnectionError:
                print("Connection Error occurred, please wait for the next response")
                continue

            except ConnectionResetError:
                print("Connection Error occurred, please wait for the next response")
                continue

            break

def retrieve_by_RS(start_date, end_date, period, jsonLocation, rsInput, tbColumn, dbTableName, epp, extra = "", start_hour="00:00", end_hour="00:00"):
    dateCaller = dateGenerator(start_date, end_date, period)
    site_code_rs = False
    tbColumn = tbColumnGenerator(tbColumn, False, False, True, site_code_rs)
    
    startDate = dateCaller[0]
    endDate = dateCaller[1]

    rsList = returnRsList(epp, rsInput)

    for i in range(len(startDate)):
        for j in range(len(rsList)):
            try:
                start = time.time()
                sample = refineRsIDChange(startDate[i], endDate[i], jsonLocation, rsList[j], period, tbColumn, epp, extra, start_hour, end_hour)

            except KeyError:
                print("Server Error occurred, please wait for the next response")
                continue

            except IndexError:
                print("Index Error occurred, please wait for the next response")
                continue

            except AttributeError:
                print("Attribute Error occurred, please wait for the next response")
                continue

            except ConnectionError:
                print("Connection Error occurred, please wait for the next response")
                continue

            except ConnectionResetError:
                print("Connection Error occurred, please wait for the next response")
                continue

            stackTodb(sample, dbTableName)
            timeSec = round(time.time() - start, 2)
            print("Time took: ", timeSec, "sec")

def retrieve_by_RS_breakdown(startDate, endDate, period, jsonFile, jsonFilebreakdown, rsInput, tbColumn, dbTableName, limit, epp, extra = "", start_hour = "00:00", end_hour = "00:00"):
    dateCaller = dateGenerator(startDate, endDate, period)
    defaultColumn = ["site_code", "dimension", "breakdown", "period", "start_date", "end_date", "is_epp"]
    
    if extra != "":
        defaultColumn.append("extra")

    newColumn = defaultColumn + tbColumn

    startDate = dateCaller[0]
    endDate = dateCaller[1]

    rsList = returnRsList(epp, rsInput)

    for i in range(len(startDate)):
        for j in range(len(rsList)):
            try:
                start = time.time()
                secondCaller(startDate[i], endDate[i], jsonFile, jsonFilebreakdown, rsList[j], limit, period, newColumn, dbTableName, epp, extra, start_hour, end_hour)
                timeSec = round(time.time() - start, 2)
                print("Time took: ", timeSec, "sec")
                
            except KeyError:
                print("Server Error occurred, please wait for the next response")
                continue

            except IndexError:
                print("Index Error occurred, please wait for the next response")
                continue

            except AttributeError:
                print("Attribute Error occurred, please wait for the next response")
                continue

            except ConnectionError:
                print("Connection Error occurred, please wait for the next response")
                continue

            except ConnectionResetError:
                print("Connection Error occurred, please wait for the next response")
                continue
        