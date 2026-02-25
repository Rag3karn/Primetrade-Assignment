# 🚀 Quick Start Guide

## 🌐 Live Dashboard

Use the hosted app directly:
https://primetradeassignment.streamlit.app/

## Run the Project

```bash
# 1. Open terminal in the project folder
cd Primetrade-Assignment

# 2. Create a virtual environment (first time only)
python -m venv .venv

# 3. Activate the virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download the CSV files from:
#    https://docs.google.com/document/d/16Cs2eat8qot90BYqq3_QZv_6FiuTrANtHJTRggaQ4EQ/edit?tab=t.0
#    Then place them in the same folder as dashboard.py (project root)
#    - fear_greed_index.csv
#    - historical_data.csv

# 6. Run the dashboard
streamlit run dashboard.py
```

## 📱 Accessing the Dashboard

- **Hosted URL (Recommended):** https://primetradeassignment.streamlit.app/
- **Local URL (when running locally):** http://localhost:8501
- **Network URL (local network):** http://192.168.x.x:8501

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
