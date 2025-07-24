import os
import requests
from dotenv import load_dotenv

# Load environment variables
try:
    load_dotenv()
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")

class AlphaVantageClient:
    def __init__(self):
        self.api_key = os.getenv('ALPHAVANTAGE_API_KEY')
        self.base_url = 'https://www.alphavantage.co/query'
        
        if not self.api_key:
            raise ValueError("ALPHAVANTAGE_API_KEY not found in environment variables")
    
    def get_intraday_data(self, symbol: str, interval: str = '5min') -> dict:
        """
        Get intraday time series data for a given symbol
        
        Args:
            symbol: Stock symbol (e.g., 'IBM', 'AAPL')
            interval: Time interval between data points ('1min', '5min', '15min', '30min', '60min')
        
        Returns:
            dict: JSON response from Alpha Vantage API
        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from Alpha Vantage: {e}")
    
    def get_daily_data(self, symbol: str) -> dict:
        """
        Get daily time series data for a given symbol
        
        Args:
            symbol: Stock symbol (e.g., 'IBM', 'AAPL')
        
        Returns:
            dict: JSON response from Alpha Vantage API
        """
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from Alpha Vantage: {e}")
    
    def get_company_overview(self, symbol: str) -> dict:
        """
        Get company overview information
        
        Args:
            symbol: Stock symbol (e.g., 'IBM', 'AAPL')
        
        Returns:
            dict: JSON response from Alpha Vantage API
        """
        params = {
            'function': 'OVERVIEW',
            'symbol': symbol,
            'apikey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from Alpha Vantage: {e}")

# Example usage
if __name__ == "__main__":
    try:
        client = AlphaVantageClient()
        
        # Test intraday data on IBM
        print("Fetching IBM intraday data...")
        data = client.get_intraday_data('IBM')
        print(data)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have ALPHAVANTAGE_API_KEY in your .env file")