"""
Sample Data Generator for Crypto Trading Dashboard
Use this if you want to test the dashboard without actual data files.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_fear_greed_index(days=365):
    """Generate sample Fear & Greed Index data"""
    
    sentiments = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    sentiment_values = {
        'Extreme Fear': (0, 25),
        'Fear': (25, 45),
        'Neutral': (45, 55),
        'Greed': (55, 75),
        'Extreme Greed': (75, 100)
    }
    
    start_date = datetime.now() - timedelta(days=days)
    dates = [start_date + timedelta(days=i) for i in range(days)]
    
    data = []
    for date in dates:
        sentiment = np.random.choice(sentiments, p=[0.15, 0.30, 0.20, 0.25, 0.10])
        value_range = sentiment_values[sentiment]
        value = np.random.randint(value_range[0], value_range[1])
        
        data.append({
            'date': date.strftime('%Y-%m-%d'),
            'value': value,
            'classification': sentiment
        })
    
    df = pd.DataFrame(data)
    return df

def generate_historical_data(num_trades=50000, num_accounts=20, num_coins=15):
    """Generate sample trading data"""
    
    # Sample data
    accounts = [f"0x{''.join(np.random.choice(list('0123456789abcdef'), 40))}" 
                for _ in range(num_accounts)]
    coins = ['BTC', 'ETH', 'SOL', 'AVAX', 'MATIC', 'LINK', 'UNI', 'AAVE', 
             'DOT', 'ADA', 'XRP', 'DOGE', 'SHIB', 'APT', 'ARB'][:num_coins]
    sides = ['BUY', 'SELL']
    
    start_date = datetime.now() - timedelta(days=365)
    
    data = []
    for _ in range(num_trades):
        # Generate random timestamp
        random_days = np.random.randint(0, 365)
        random_hours = np.random.randint(0, 24)
        random_minutes = np.random.randint(0, 60)
        timestamp = start_date + timedelta(days=random_days, hours=random_hours, 
                                          minutes=random_minutes)
        
        # Generate trade details
        account = np.random.choice(accounts)
        coin = np.random.choice(coins)
        side = np.random.choice(sides)
        
        # Position size with some variation
        base_size = np.random.lognormal(mean=8, sigma=1.2)
        size_usd = max(100, min(50000, base_size))
        
        # PnL - slightly more winners than losers
        win_chance = 0.42  # 42% win rate
        if np.random.random() < win_chance:
            # Winning trade
            pnl = np.random.exponential(scale=150) + 10
        else:
            # Losing trade
            pnl = -(np.random.exponential(scale=120) + 10)
        
        data.append({
            'Timestamp IST': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Account': account,
            'Coin': coin,
            'Side': side,
            'Size USD': round(size_usd, 2),
            'Closed PnL': round(pnl, 2)
        })
    
    df = pd.DataFrame(data)
    return df

def main():
    """Generate and save sample data files"""
    
    print("Generating sample data...")
    
    # Generate Fear & Greed Index data
    print("Creating fear_greed_index.csv...")
    df_sentiment = generate_fear_greed_index(days=365)
    df_sentiment.to_csv('fear_greed_index.csv', index=False)
    print(f"✓ Generated {len(df_sentiment)} days of sentiment data")
    
    # Generate historical trading data
    print("\nCreating historical_data.csv...")
    df_trades = generate_historical_data(num_trades=50000, num_accounts=20, num_coins=15)
    df_trades.to_csv('historical_data.csv', index=False)
    print(f"✓ Generated {len(df_trades):,} trades")
    
    # Print summary
    print("\n" + "="*50)
    print("Sample Data Generation Complete!")
    print("="*50)
    print(f"\nFiles created:")
    print("  - fear_greed_index.csv")
    print("  - historical_data.csv")
    print(f"\nData Summary:")
    print(f"  - Date range: {df_sentiment['date'].min()} to {df_sentiment['date'].max()}")
    print(f"  - Unique accounts: {df_trades['Account'].nunique()}")
    print(f"  - Unique coins: {df_trades['Coin'].nunique()}")
    print(f"  - Total trades: {len(df_trades):,}")
    print(f"  - Total volume: ${df_trades['Size USD'].sum():,.2f}")
    print(f"  - Total PnL: ${df_trades['Closed PnL'].sum():,.2f}")
    print("\nYou can now run the dashboard with:")
    print("  streamlit run dashboard.py")

if __name__ == "__main__":
    main()
