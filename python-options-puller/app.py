import os
import datetime
import yfinance as yf
import pandas as pd
import time
import options_constants

def _next_friday(this_week=False):
    today = datetime.date.today()
    # weekday() returns 0 for Monday, 4 for Friday
    days_until_friday = (4 - today.weekday()) % 7
    next_friday = today + datetime.timedelta(days=days_until_friday)

    # Logic to skip to the following week if it's too close to current Friday
    if (next_friday - today).days < 3 and not this_week:
        next_friday = next_friday + datetime.timedelta(weeks=1)

    return str(next_friday)

def _get_options(stock_symbol):
    try:
        ticker_ob = yf.Ticker(stock_symbol)

        # Use history to get the most reliable 'last' close price
        hist = ticker_ob.history(period="1d")
        if hist.empty:
            return f"Error: No price data found for {stock_symbol}"

        current_price = hist['Close'].iloc[-1]
        ideal_strike = current_price * 0.9

        # Determine expiration date
        next_friday_date = _next_friday()

        try:
            chain = ticker_ob.option_chain(next_friday_date)
        except Exception:
            # Fallback to the immediate Friday if next week isn't listed yet
            next_friday_date = _next_friday(this_week=True)
            chain = ticker_ob.option_chain(next_friday_date)

        # Filter for Put options
        puts = chain.puts.sort_values('strike')
        # Find the 2 puts just under our 90% target
        filtered_puts = puts[puts['strike'] < ideal_strike].tail(2)

        report = f"Price: ${current_price:.2f} | Exp: {next_friday_date}"
        if filtered_puts.empty:
            report += " | No puts found below target strike."
        else:
            for _, row in filtered_puts.iterrows():
                report += f" | Strike: {row['strike']} Bid: {row['bid']}"

        return report

    except Exception as e:
        return f"Failed to process {stock_symbol}: {e}"

def main():
    print("="*60)
    print(f"OPTIONS SCANNER - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)

    for symbol in options_constants.STOCKS_LIST:
        print(f"Scanning {symbol}...")
        result = _get_options(symbol)
        print(f"   {result}")
        time.sleep(1) # Be polite to Yahoo Finance servers

    print("="*60)
    print("Scan finished.")

if __name__ == "__main__":
    main()
