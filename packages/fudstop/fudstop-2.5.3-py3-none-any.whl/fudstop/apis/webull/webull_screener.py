import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pandas as pd
import requests
import httpx
from .webull_options import WebullOptionsData
from typing import List
from .screener_models import ScreenerRule, TickerInfo
load_dotenv()




class WebulScreener:
    def __init__(self):
        self.pool = None
        self.as_dataframe = None
        self.session = requests.session()
        self.account_id=os.environ.get('WEBULL_ACCOUNT_ID')
        self.api_key = os.environ.get('YOUR_POLYGON_KEY')
        self.today = datetime.now().strftime('%Y-%m-%d')
        self.yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        self.tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        self.thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        self.thirty_days_from_now = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
        self.fifteen_days_ago = (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d')
        self.fifteen_days_from_now = (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d')
        self.eight_days_from_now = (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d')
        self.eight_days_ago = (datetime.now() - timedelta(days=8)).strftime('%Y-%m-%d')
        self.headers = {
        "Access_token": os.environ.get('ACCESS_TOKEN'),
        "Accept": "*/*",
        "App": "global",
        "App-Group": "broker",
        "Appid": "wb_web_app",
        "Content-Type": "application/json",
        "Device-Type": "Web",
        "Did": os.environ.get('DID'),
        "Hl": "en",
        "Locale": "eng",
        "Os": "web",
        "Osv": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Ph": "Windows Chrome",
        "Platform": "web",
        "Referer": "https://app.webull.com/",
        "Reqid": os.environ.get('REQ_ID'),
        "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "T_time": "1698276695206",
        "Tz": "America/Los_Angeles",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    def get_option_data_for_id(self, id, symbol):
        print(f"Starting processing for ticker: {id}")
        dataframes = []  # Initialize a list to collect DataFrames
  

        print(f"Processing batch ID: {id} for ticker: {id}")
        url = f"https://quotes-gw.webullfintech.com/api/quote/option/quotes/queryBatch?derivativeIds={id}"

        data = self.session.get(url, headers=self.headers).json()
        if not data:  # If data is empty or None, break the loop
            print(f"No more data for ticker: {id}. Moving to next.")
          
        wb_data = WebullOptionsData(data)
        if self.as_dataframe is not None:
            df = wb_data.as_dataframe
            df['ticker'] = id
            df['symbol'] = symbol
            df = df.rename(columns={'open_interest_change': 'oi_change'})
            return df
    async def query(self, **kwargs):
        url = "https://quotes-gw.webullfintech.com/api/wlas/option/screener/query"

        # Initialize the filter dictionary
        filter_dict = {}

        # Dynamically build the filter dictionary from kwargs
        for key, value in kwargs.items():
            if isinstance(value, tuple) and len(value) == 2:
                filter_key = f"options.screener.rule.{key}"
                filter_dict[filter_key] = f"gte={value[0]}&lte={value[1]}"
            elif key == 'direction':  # Special handling for non-range criteria
                filter_dict[f"options.screener.rule.{key}"] = value

        payload = {"filter": filter_dict, "page": {"fetchSize": 25}}

        try:
            async with httpx.AsyncClient() as client:
                data = await client.post(url, headers=self.headers, json=payload)
                response = data
                response.raise_for_status()  # Raises an HTTPError if the response status code is 4xx or 5xx
                data = response.json()
                print(data)
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return []

        # Process and return the data
        datas = data.get('datas', [])
        if not datas:
            return []

        # Extract and return the relevant information
        return [{
            'symbol': d.get('derivative', {}).get('unSymbol'),
            'strike': d.get('derivative', {}).get('strikePrice'),
            'call_put': d.get('derivative', {}).get('direction'),
            'expiry': d.get('derivative', {}).get('expireDate'),
            'id': d.get('derivativeId')
        } for d in datas]


import disnake
class ScreenerSelect(disnake.ui.Select):
    def __init__(self, data_dict):
        self.data_dict = data_dict

        options = []
        # Ensure all lists are of the same length
        num_items = len(data_dict['id'])
        if all(len(data_dict[key]) == num_items for key in ['symbol', 'strike', 'expiry', 'call_put']):
            for i in range(num_items):
                # Construct the label and value for each option
                label = f"{data_dict['symbol'][i]} | Strike: {data_dict['strike'][i]} | Expiry: {data_dict['expiry'][i]} | {data_dict['call_put'][i]}"
                value = str(data_dict['id'][i])

                options.append(disnake.SelectOption(label=label, value=value))
        else:
            print("Data lists are not of equal length")

        super().__init__(
            placeholder="> Results >",
            min_values=1,
            max_values=len(options),
            custom_id='optionscreener',
            options=options
        )
        super().__init__(
            placeholder="> Results >",
            min_values=1,
            max_values=len(data_dict),
            custom_id='optionscreener',
            options=options
        )




    async def callback(self, inter:disnake.AppCmdInter):
        await inter.response.defer()
        if self.values[0]:

            url = requests.get(f"https://quotes-gw.webullfintech.com/api/quote/option/quotes/queryBatch?derivativeIds={','.join(self._selected_values)}").json()
            print(url)

            data = WebullOptionsData(url).data_dict

            description = self.format_data_for_embed(data)
            embed = disnake.Embed(title=f"Results for Option:", description=f"> ***{description}***")
            view = disnake.ui.View()
            await inter.edit_original_message(embed=embed)

    def format_data_for_embed(self, data):
        # Format each key-value pair in data
        formatted_data = []
        for key, values in data.items():
            formatted_values = ', '.join(str(value) for value in values)
            formatted_data.append(f"**{key}:** {formatted_values}")

        # Join all formatted data into a single string
        return '\n'.join(formatted_data)