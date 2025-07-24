import sys
import os
from typing import Dict, Any, List
from mcp.server.fastmcp import FastMCP
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server

# Add parent directory to path to import alpha_vantage_client
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mcp_client.alpha_vantage_client import AlphaVantageClient

# Create the server
server = FastMCP("Stock Analytics Server")

# Initialize Alpha Vantage client
try:
    alpha_vantage_client = AlphaVantageClient()
except Exception as e:
    print(f"Warning: Could not initialize Alpha Vantage client: {e}")
    alpha_vantage_client = None

@server.tool(
    name="get_stock_intraday_data",
    description="Get intraday time series data for a stock symbol"
)
def get_stock_intraday_data(symbol: str, interval: str = "5min") -> Dict[str, Any]:
    """
    Get intraday time series data for a given stock symbol.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM', 'AAPL', 'MSFT')
        interval: Time interval between data points ('1min', '5min', '15min', '30min', '60min')
    
    Returns:
        dict: Stock intraday data from Alpha Vantage API
    """
    if not alpha_vantage_client:
        raise Exception("Alpha Vantage client not initialized. Check your API key.")
    
    try:
        data = alpha_vantage_client.get_intraday_data(symbol, interval)
        return {
            "symbol": symbol,
            "interval": interval,
            "data": data,
            "status": "success"
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "interval": interval,
            "error": str(e),
            "status": "error"
        }

@server.tool(
    name="get_stock_daily_data",
    description="Get daily time series data for a stock symbol"
)
def get_stock_daily_data(symbol: str) -> Dict[str, Any]:
    """
    Get daily time series data for a given stock symbol.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM', 'AAPL', 'MSFT')
    
    Returns:
        dict: Stock daily data from Alpha Vantage API
    """
    if not alpha_vantage_client:
        raise Exception("Alpha Vantage client not initialized. Check your API key.")
    
    try:
        data = alpha_vantage_client.get_daily_data(symbol)
        return {
            "symbol": symbol,
            "data": data,
            "status": "success"
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "error": str(e),
            "status": "error"
        }

@server.tool(
    name="get_company_overview",
    description="Get company overview information for a stock symbol"
)
def get_company_overview(symbol: str) -> Dict[str, Any]:
    """
    Get company overview information for a given stock symbol.
    
    Args:
        symbol: Stock symbol (e.g., 'IBM', 'AAPL', 'MSFT')
    
    Returns:
        dict: Company overview data from Alpha Vantage API
    """
    if not alpha_vantage_client:
        raise Exception("Alpha Vantage client not initialized. Check your API key.")
    
    try:
        data = alpha_vantage_client.get_company_overview(symbol)
        return {
            "symbol": symbol,
            "data": data,
            "status": "success"
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "error": str(e),
            "status": "error"
        }

@server.tool(
    name="calculate_stock_metrics",
    description="Calculate basic stock metrics from price data"
)
def calculate_stock_metrics(prices: List[float]) -> Dict[str, float]:
    """
    Calculate basic stock metrics from a list of prices.
    
    Args:
        prices: List of stock prices
    
    Returns:
        dict: Calculated metrics including mean, min, max, and volatility
    """
    if not prices:
        raise ValueError("Price list cannot be empty")
    
    try:
        mean_price = sum(prices) / len(prices)
        min_price = min(prices)
        max_price = max(prices)
        
        # Calculate volatility (standard deviation)
        variance = sum((price - mean_price) ** 2 for price in prices) / len(prices)
        volatility = variance ** 0.5
        
        return {
            "mean_price": mean_price,
            "min_price": min_price,
            "max_price": max_price,
            "volatility": volatility,
            "price_range": max_price - min_price
        }
    except Exception as e:
        raise ValueError(f"Error calculating metrics: {e}")

# Run the server over stdio
if __name__ == "__main__":
    server.run()