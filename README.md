# 📈 Crypto Trading Sentiment Analysis Dashboard

An interactive Streamlit dashboard for exploring the relationship between market sentiment (Fear & Greed Index) and cryptocurrency trading performance.

## 🎯 Features

- **Real-time Filtering**: Filter data by sentiment, date range, and cryptocurrency
- **Comprehensive Analytics**: 5 interactive tabs covering different aspects of the analysis
- **Visual Insights**: 15+ interactive charts using Plotly
- **Performance Metrics**: Track PnL, win rates, trade frequency, and more
- **Trader Segmentation**: Identify top performers and consistent winners
- **Sentiment Analysis**: Understand how market mood impacts trading behavior

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Data files: `fear_greed_index.csv` and `historical_data.csv`
- Run commands from the repository root folder (`Primetrade-Assignment/`)

## 📓 Notebook First (Important)

The Jupyter notebook (`Primetrade_assignement.ipynb`) is the primary artifact for review and should be examined before the Streamlit app. It contains the full analysis, methodology, and insights in a step-by-step format.

If you are reviewing the work, start with the notebook, then use the dashboard for interactive exploration.

## 📘 Other Docs

- **`QUICKSTART.md`** provides a short, command-only setup flow.
- **`PROJECT_STRUCTURE.md`** explains where files live.

## 🚀 Quick Start

### 1. Clone or Download the Repository

```bash
# If using git
git clone <repository-url>
cd Primetrade-Assignment

# Or simply download and extract the files
```

### 2. Activate the Existing Virtual Environment

If you already have a virtual environment, activate it. If not, create one first:

```bash
python -m venv .venv
```

**On Windows:**
```bash
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive visualizations
- `numpy` - Numerical computing

### 4. Prepare Your Data

Download the required CSV files from:
https://docs.google.com/document/d/16Cs2eat8qot90BYqq3_QZv_6FiuTrANtHJTRggaQ4EQ/edit?tab=t.0

Place the files in the same directory as `dashboard.py` (repo root):

- **`fear_greed_index.csv`** - Contains date and sentiment classification data
  - Required columns: `date`, `classification`, `value`
  - Accepted date formats: `YYYY-MM-DD` or `DD-MM-YYYY` (day-first supported)
  
- **`historical_data.csv`** - Contains trading transaction data
  - Required columns: `Timestamp IST`, `Account`, `Coin`, `Side`, `Size USD`, `Closed PnL`
  - Accepted timestamp formats: `YYYY-MM-DD HH:MM:SS` or `DD-MM-YYYY HH:MM`

**Example file structure:**
```
Primetrade-Assignment/
├── dashboard.py
├── requirements.txt
├── README.md
├── fear_greed_index.csv
└── historical_data.csv
```

### 5. Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

## 🎨 Dashboard Overview

### Tab 1: 📈 Sentiment Analysis
- Total PnL by market sentiment
- Win rate comparison across sentiments
- Trade activity timeline
- Identify which market moods are most profitable

### Tab 2: 💰 Performance Metrics
- PnL distribution histogram
- Box plots showing profit/loss spread by sentiment
- Detailed performance table with key statistics
- Average loss analysis

### Tab 3: 🎯 Trading Behavior
- Trade frequency distribution
- Long/Short ratio by sentiment (BUY vs SELL preference)
- Average position sizing across market conditions
- Behavioral pattern identification

### Tab 4: 👥 Trader Segmentation
- Top 10 accounts by total PnL
- Win rate distribution across all traders
- Scatter plot: Win Rate vs Total PnL
- "Consistent Winners" identification and statistics

### Tab 5: 📊 Advanced Analytics
- Daily PnL and trade count time series
- Top cryptocurrencies by trading volume
- Correlation matrix for numeric variables
- Temporal pattern analysis

## 🔧 Troubleshooting

### Issue: "Module not found" error
**Solution:** Make sure you've activated your virtual environment and installed all requirements:
```bash
source .venv/bin/activate  # On macOS/Linux
# OR
.venv\Scripts\activate  # On Windows

pip install -r requirements.txt
```

### Issue: "File not found" error
**Solution:** Ensure your CSV files are in the same directory as `dashboard.py` (repo root):
```bash
ls -la  # On macOS/Linux
# OR
dir  # On Windows

# You should see:
# - dashboard.py
# - fear_greed_index.csv
# - historical_data.csv
```

### Issue: Dashboard won't load/blank screen
**Solution:** 
1. Check terminal for error messages
2. Verify CSV files have correct column names
3. Try refreshing browser or restarting the Streamlit server (Ctrl+C then rerun)

### Issue: Port already in use
**Solution:** Either stop the existing Streamlit process or run on a different port:
```bash
streamlit run dashboard.py --server.port 8502
```

## 📊 Using the Dashboard

### Filters (Left Sidebar)
1. **Market Sentiment**: Filter by specific sentiment (Fear, Greed, etc.) or view all
2. **Date Range**: Select custom date range for analysis
3. **Cryptocurrency**: Focus on specific coin or view entire portfolio

### Key Metrics (Top of Page)
- Monitor 8 key performance indicators in real-time
- Metrics update automatically based on your filter selections

### Interactive Charts
- **Hover** over data points for detailed information
- **Click** legend items to show/hide series
- **Zoom** by clicking and dragging on chart area
- **Download** charts using the camera icon

## 🎯 Best Practices

1. **Start Broad**: Begin with "All" filters to get the full picture
2. **Compare Sentiments**: Use the Sentiment Analysis tab to identify patterns
3. **Identify Winners**: Check Trader Segmentation to find top-performing accounts
4. **Drill Down**: Use filters to investigate specific periods or coins
5. **Export Insights**: Screenshot charts or take notes on key findings

## 💡 Tips for Analysis

- **Extreme Fear vs Fear**: Compare performance to identify risk/reward tradeoffs
- **Position Sizing**: Look at Tab 3 to see how traders adjust sizes by sentiment
- **Consistency**: Tab 4 helps identify accounts with sustainable strategies
- **Temporal Patterns**: Tab 5 shows if performance varies by time of day/week

## 🔄 Updating Data

To analyze new data:
1. Replace `fear_greed_index.csv` and/or `historical_data.csv` with updated files
2. Keep the same column structure
3. Refresh the dashboard (it auto-reloads on file changes)

## 📁 Project Structure

```
project-folder/
├── dashboard.py              # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── fear_greed_index.csv     # Sentiment data (you provide)
└── historical_data.csv      # Trading data (you provide)
```

## 🛠️ Customization

### Changing Color Schemes
Edit the color scales in `dashboard.py`:
```python
# Find lines like:
color_continuous_scale='RdYlGn'

# Replace with: 'Viridis', 'Plasma', 'Blues', 'Greens', etc.
```

### Adding New Metrics
Add custom calculations in the `calculate_metrics()` function:
```python
def calculate_metrics(merged_df):
    metrics = {
        # ... existing metrics ...
        'your_metric': merged_df['column'].your_calculation()
    }
    return metrics
```

### Modifying Filters
Add new filters in the sidebar section:
```python
st.sidebar.selectbox("Your Filter", options)
```

## 🐛 Known Limitations

- Large datasets (>1M rows) may load slowly - consider filtering at data source
- Date ranges must be selected properly (start date before end date)
- Missing data in CSV files will cause errors - ensure data quality

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Verify your data files match the required format
3. Ensure all dependencies are installed correctly

## 📄 License

This dashboard is provided as-is for analysis purposes.

## 🎓 Learning More

To understand the analysis methodology and insights:
- Review the Jupyter notebook: `Primetrade_assignement.ipynb`
- Read the executive summary: `Trading_Analysis_Summary.md`

---

**Happy Analyzing! 📊**

