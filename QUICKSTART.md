# 🚀 Quick Start Guide

## Option 1: Using Your Own Data (Recommended)

```bash
# 1. Activate the existing virtual environment
venv\Scripts\activate

# 2. Install dependencies
pip install -r venv/requirements.txt

# 3. Download the CSV files from:
#    https://docs.google.com/document/d/16Cs2eat8qot90BYqq3_QZv_6FiuTrANtHJTRggaQ4EQ/edit?tab=t.0
#    Then place them in the same folder as dashboard.py (inside venv/)
#    - fear_greed_index.csv
#    - historical_data.csv

# 4. Run the dashboard
cd venv
streamlit run dashboard.py
```

## Option 2: Using Sample Data (For Testing)

```bash
# 1. Activate the existing virtual environment
venv\Scripts\activate

# 2. Install dependencies
pip install -r venv/requirements.txt

# 3. Generate sample data
python venv/generate_sample_data.py

# 4. Run the dashboard
cd venv
streamlit run dashboard.py
```

## 📱 Accessing the Dashboard

Once running, the dashboard will open automatically at:
- **Local URL:** http://localhost:8501
- **Network URL:** http://192.168.x.x:8501 (for other devices on your network)

## 🎯 First Steps in the Dashboard

1. **Check the metrics** at the top of the page
2. **Use filters** in the left sidebar to explore different segments
3. **Navigate tabs** to see different analyses:
   - Tab 1: Sentiment Analysis
   - Tab 2: Performance Metrics
   - Tab 3: Trading Behavior
   - Tab 4: Trader Segmentation
   - Tab 5: Advanced Analytics

## 💡 Pro Tips

- Start with "All" filters to see the complete picture
- Hover over charts for detailed information
- Click legend items to show/hide data series
- Use date range filter to zoom into specific periods
- Download charts using the camera icon in the top-right of each chart

## 🛑 Stopping the Dashboard

Press `Ctrl+C` in the terminal to stop the Streamlit server.

## ❓ Need Help?

Check the full README.md for detailed instructions and troubleshooting.
