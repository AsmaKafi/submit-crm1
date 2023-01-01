from dotenv import load_dotenv
import pandas as pd
import requests
import os

load_dotenv()

# reading the excel file
def load_data() -> pd.DataFrame:
  file_path = 'Faux-Export-Abonnés-Newsletter-Décembre-2017.xlsx'
  df = pd.read_excel(file_path, 0, header=None)
  return df[1:]

def save_crm(data: pd.DataFrame) -> None:
  apiUrl = 'https://interview.yiu.ngo/api/create-newsletter-subscriber'
  for row in data.values:
    subscriber_data = {
      'lastname': row[0],
      'firstname': row[1],
      'email': row[2],
      'candidate': os.environ('API_KEY')
    }

    response = requests.post(apiUrl, subscriber_data, timeout=10)
    if (response.status_code == '200'):
      print(f'{row} saved successfully')

def show_data() -> None:
  api_key = os.environ('API_KEY')
  apiUrl = f'https://interview.yiu.ngo/api/list-newslettersubscribers/{api_key}'
  response = requests.get(apiUrl, timeout=10)
  if (response.status_code == 200):
    print(response)