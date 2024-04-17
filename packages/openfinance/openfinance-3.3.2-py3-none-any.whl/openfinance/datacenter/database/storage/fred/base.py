import requests
import pandas
import json

# api
# https://api.stlouisfed.org/fred/category?category_id=125&api_key=578803ddc650f8e070b0e11f34bbe2b4&file_type=json

def fred_balance_sheet():
    url = "https://www.federalreserve.gov/datadownload/Output.aspx?rel=H41&series=7951a85bb48c5cc679a40e18f2d718bd&lastobs=300&from=&to=&filetype=csv&label=include&layout=seriescolumn"
    data = requests.get(url)
    data = str(data.content).split("\\r\\n")
    result = {
        "DATE": [],
        "ASSET": [],
        "CHANGE_WEEKLY": [],
        "CHANGE_YEAR": []
    }
    idx = 0
    for d in data:
        idx += 1
        if idx > 6:
            ds = d.split(",")
            result["DATE"].append(ds[0])
            result["ASSET"].append(str(ds[21]))
            result["CHANGE_WEEKLY"].append(str(ds[23]))
            result["CHANGE_YEAR"].append(str(ds[24]))            
    return pandas.DataFrame.from_dict(result)


# https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/summary-of-receipts-and-outlays-of-the-u-s-government
def us_government_fiscal():
    url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_3?sort=-record_date&format=json"
    #url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_3?filter=record_date:eq:2023-07-31&format=json"
    data = requests.get(url)
    data = json.loads(data.content)
    result = {}
    idx = 0
    for d in data['data']:
        if idx == 2:
            break
        if d['classification_desc'] == "Total Receipts":
            result["DATE"] = [d['record_date']]
            result["Total_Receipts"] = [d['current_fytd_rcpt_outly_amt']]
            result["Total_Receipts_Last_Year"] = [d['prior_fytd_rcpt_outly_amt']]
            idx += 1
        elif d['classification_desc'] == "Total Outlays":
            result["Total_Outlays"] = [d['current_fytd_rcpt_outly_amt']]
            result["Total_Outlays_Last_Year"] = [d['prior_fytd_rcpt_outly_amt']]
            idx += 1
    return pandas.DataFrame.from_dict(result)
