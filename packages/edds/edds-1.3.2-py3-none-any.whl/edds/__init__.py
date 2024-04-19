from requests import Session
from json import loads
import pandas as pd

class edds:
    def __init__(self, key):
        self.key = key
        self.lang = "ENG"


    def make_request(self, url, params):
        param_text = "&".join([f"{key}={value}" for key, value in params.items()])
        headers = {"key": self.key} 
        response = Session().get(url + param_text, headers=headers)
        if response.status_code == 200:
          return response.content
        else:
          raise ConnectionError(
            f"Please check your API Key or the connection to the Web Service."
        )
    @property
    def categories(self):
        url = 'https://evds2.tcmb.gov.tr/service/evds/categories/'
        params = {'type': 'json'}
        response = self.make_request(url, params)
        data = loads(response)
        df = pd.DataFrame(data)[["CATEGORY_ID", f"TOPIC_TITLE_{self.lang}"]]
        df["CATEGORY_ID"] = df["CATEGORY_ID"].astype(int)
        categories = df.sort_values(by=['CATEGORY_ID'], ascending=True)
        return categories

    def data_groups(self, CATEGORY_ID):
        try:
          CATEGORY_ID = int(CATEGORY_ID)
        except ValueError:
          raise InputError(f"{CATEGORY_ID} is an invalid input. CATEGORY_ID must be a number. For checking CATEGORY_ID, use the 'categories' method")

        if CATEGORY_ID in self.categories["CATEGORY_ID"].tolist():
            params = {'mode': 2, 'code': CATEGORY_ID, 'type': 'json'}
        else:
            raise SerieNotFoundError("Category not found. For checking CATEGORY_ID, use the 'categories' method")

        data_groups = self.make_request('https://evds2.tcmb.gov.tr/service/evds/datagroups/',
                                           params=params)
        data_groups = loads(data_groups)
        df = pd.DataFrame(data_groups)
        return df[["CATEGORY_ID",
                       "DATAGROUP_CODE",
                       "DATAGROUP_NAME_" + (self.lang),
                       "METADATA_LINK_ENG"]]


    def series(self, datagroup_code ):
        series = self.make_request('https://evds2.tcmb.gov.tr/service/evds/serieList/',
                                     params={'type': 'json', 'code': datagroup_code})

        df = pd.DataFrame(loads(series))

        return df[["SERIE_CODE",
                    "SERIE_NAME_"+self.lang ,
                    "START_DATE",
                    "END_DATE",]]



    def get_data(self, serie, startdate, enddate):

        data = self.make_request('https://evds2.tcmb.gov.tr/service/evds/',
                                   params={
                                       'series': serie,
                                       'startDate': startdate,
                                       'endDate': enddate,
                                       'type': 'json',
                                       'key': self.key,
                                   })
        data = loads(data)["items"]
        df = pd.DataFrame(data)
        if "UNIXTIME" in df.columns:
            df.drop(columns=["UNIXTIME"], inplace=True)
        return df

class InputError(Exception):
    pass
class SerieNotFoundError(Exception):
    pass