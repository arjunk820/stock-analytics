# Testing Guide for Stock Analytics

This guide will help you test the Alpha Vantage API client and MCP server functionality.

## Prerequisites

Note: These steps also exist in README and are critical in setting up this project in general.

1. **Get an Alpha Vantage API Key**
   - Go to https://www.alphavantage.co/support/#api-key
   - Sign up for a free API key
   - Add it to your `.env` file:
   ```
   ALPHAVANTAGE_API_KEY=your_api_key_here
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Testing Options

### Option 1: Test Alpha Vantage Client Directly

Run the basic Alpha Vantage client test:
```bash
py -m tests.test_alpha_vantage
```

This will test:
- ✅ Client initialization
- ✅ IBM intraday data (5-minute intervals)
- ✅ IBM daily data
- ✅ IBM company overview

### Option 2: Test MCP Server Functions (Simulated)

Run the MCP server function simulation:
```bash
py -m tests.test_mcp_server
```

This will test all the MCP server functions:
- ✅ `get_stock_intraday_data` - Get intraday stock data
- ✅ `get_stock_daily_data` - Get daily stock data
- ✅ `get_company_overview` - Get company information
- ✅ `calculate_stock_metrics` - Calculate price statistics
- ✅ `evaluate_expression` - Mathematical expression evaluator

### Option 3: Test Individual Components

#### Test Alpha Vantage Client
```bash
py alpha_vantage_client.py
```

#### Test with Different Symbols
You can modify the test scripts to use different stock symbols:
- `AAPL` (Apple)
- `MSFT` (Microsoft)
- `GOOGL` (Google)
- `TSLA` (Tesla)
- `IBM` (IBM)

## Expected Output

### Successful Test Output
```
🧪 Testing Alpha Vantage Client
==================================================
1. Initializing Alpha Vantage client...
✅ Client initialized successfully

2. Testing intraday data for IBM...
✅ Intraday data retrieved successfully
   Data points: 100
   Latest data: 2024-01-15 16:00:00 - Open: 150.25, Close: 151.30

3. Testing daily data for IBM...
✅ Daily data retrieved successfully
   Data points: 100

4. Testing company overview for IBM...
✅ Company overview retrieved successfully
   Company: International Business Machines Corporation
   Sector: Technology
   Market Cap: 150000000000

🎉 All tests completed!
```

### Error Output
If you see errors, check:
1. ✅ API key is in `.env` file
2. ✅ API key is valid
3. ✅ Internet connection
4. ✅ Dependencies installed

## API Rate Limits

Alpha Vantage has rate limits:
- **Free tier**: 5 API calls per minute, 500 per day
- **Premium tier**: Higher limits available

## Troubleshooting

### Common Issues

1. **"ALPHAVANTAGE_API_KEY not found"**
   - Create a `.env` file in your project root
   - Add: `ALPHAVANTAGE_API_KEY=your_key_here`

2. **"Error fetching data from Alpha Vantage"**
   - Check your API key is valid
   - Check internet connection
   - Check if you've hit rate limits

3. **Import errors**
   - Run: `pip install -r requirements.txt`
   - Activate your virtual environment if using one

### Getting Help

- Alpha Vantage API docs: https://www.alphavantage.co/documentation/
- Check the API response for error messages
- Test with the demo key first: `demo`

## Next Steps

Once testing is successful, you can:
1. Integrate with a real MCP server
2. Build a web interface
3. Create data visualization tools
4. Add more sophisticated analytics 