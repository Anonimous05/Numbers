from __future__ import print_function

import datetime
import os.path
import requests
from bs4 import BeautifulSoup
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from core.settings import BASE_DIR
from orders.models import Order


class GoogleSheetService:
    """
        GoogleSheetService - содержит в себе все необходимое для работы с google-sheets-api
    """

    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.sample_spreadsheet_id = '1IQQHwqaHmxIiKBRrGZ-EfsGo6LhLqAXREHtBX7eFJ-A'
        self.sample_range_name = 'A1:E'
        self.values = None
        self.get_sheet()

    def get_cb_url(self):

        """
            Возвращает готовый URL адресс ЦБ РФ по текущему дню
        """

        now_date = datetime.datetime.now().date()
        return f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={"/".join(now_date.__str__().split("-")[::-1])}'

    def get_sheet(self):
        """
        делает запрос на получение документа, после получения сохраняет данные в self.values
        """
        creds = None
        if os.path.exists(BASE_DIR / 'orders/google_sheets_configs/token.json'):
            creds = Credentials.from_authorized_user_file(BASE_DIR / 'orders/google_sheets_configs/token.json', self.scopes)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    BASE_DIR / 'orders/google_sheets_configs/creds.json', self.scopes)
                creds = flow.run_local_server(port=8000)
            with open(os.path.join(BASE_DIR, 'orders/google_sheets_configs/token.json'), 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('sheets', 'v4', credentials=creds)

            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.sample_spreadsheet_id,
                                        range=self.sample_range_name).execute()
            values = result.get('values', [])

            if values:
                self.values = values

        except HttpError as err:
            print(err)

    def set_values(self):
        """
            1: получает курс USD -> RUB по ЦБ РФ текущего дня
            2: проходится по данным (self.values) если найден существующий Order по order_number то обновляет данные
               или же создает новый Order
        """
        response = requests.get(self.get_cb_url())
        bs_data = BeautifulSoup(response.content, 'xml')
        usd = bs_data.find("Valute", {'ID': 'R01235'}).find('Value')

        for row in self.values[1:]:
            obj = {
                'order_number': row[1],
                'price_usd': row[2],
                'delivery_date': "-".join(row[3].split('.')[::-1]),
                'price_rub': int(row[2]) * float(usd.text.replace(',', '.'))
            }

            already_order: Order = Order.objects.filter(order_number=obj['order_number']).first()

            if already_order:
                already_order.price_usd = obj['price_usd']
                already_order.delivery_date = obj['delivery_date']
                already_order.price_rub = obj['price_rub']
                already_order.save()
            else:
                Order.objects.create(
                    order_number=obj['order_number'],
                    price_usd=obj['price_usd'],
                    delivery_date=obj['delivery_date'],
                    price_rub=obj['price_rub']
                )

