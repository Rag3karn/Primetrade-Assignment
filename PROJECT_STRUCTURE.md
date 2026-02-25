# 📁 Project Structure Overview

## Complete File List

```
Primetrade-Assignment/
├── 📊 ANALYSIS FILES
│   ├── Primetrade_assignement.ipynb          # Jupyter notebook with full analysis
│   └── Trading_Analysis_Summary.md           # Executive summary (1-page)
│
├── 🖥️ DASHBOARD FILES
│   ├── dashboard.py                          # Main Streamlit application
│   ├── requirements.txt                      # Python dependencies
│   ├── README.md                             # Complete documentation
│   └── QUICKSTART.md                         # Quick start guide
│
└── 📄 DATA FILES (You provide these)
    ├── fear_greed_index.csv                  # Market sentiment data
    └── historical_data.csv                   # Trading transaction data
```

## File Descriptions

### Analysis Files

**Primetrade_assignement.ipynb**
- Full data analysis in Jupyter notebook format
- Contains all code, visualizations, and insights
- Great for understanding the methodology step-by-step

**Trading_Analysis_Summary.md**
- Concise 1-page executive summary
- Methodology, key insights, and strategy recommendations
- Perfect for stakeholders and quick reference

The analysis summary is captured in **Trading_Analysis_Summary.md**.

### Dashboard Files

**dashboard.py**
- Interactive Streamlit web application
- 5 tabs covering different aspects of analysis
- 15+ interactive Plotly visualizations
- Real-time filtering and exploration

**requirements.txt**
- List of required Python packages
- Ensures consistent environment setup
- Use with: `pip install -r requirements.txt`

**README.md**
- Complete documentation (7,500+ words)
- Installation instructions
- Feature overview
- Troubleshooting guide
- Customization tips

**QUICKSTART.md**
- Condensed setup guide
- Two-minute quick start
- Essential commands only

## Data File Requirements

Download the required data files from:
https://docs.google.com/document/d/16Cs2eat8qot90BYqq3_QZv_6FiuTrANtHJTRggaQ4EQ/edit?tab=t.0

### fear_greed_index.csv
Required columns:
- `date` (YYYY-MM-DD or DD-MM-YYYY format)
- `value` (0-100)
- `classification` (Extreme Fear, Fear, Neutral, Greed, Extreme Greed)

### historical_data.csv
Required columns:
- `Timestamp IST` (YYYY-MM-DD HH:MM:SS or DD-MM-YYYY HH:MM format)
- `Account` (account identifier)
- `Coin` (cryptocurrency symbol)
- `Side` (BUY or SELL)
- `Size USD` (position size in USD)
- `Closed PnL` (profit/loss for the trade)

## Usage Workflows

### Workflow 1: Analyze with Notebook
1. Open `Primetrade_assignement.ipynb` in Jupyter
2. Run cells to see analysis step-by-step
3. Review `Trading_Analysis_Summary.md` for insights

### Workflow 2: Explore with Dashboard
1. Install dependencies: `pip install -r requirements.txt`
2. Place CSV files in project folder
3. Run: `streamlit run dashboard.py`
4. Interact with visualizations in browser

## Size Information

- **Total Project Size**: ~750 KB
- **Largest Files**: 
  - Notebook: ~700 KB
  - Dashboard: ~17 KB
  - README: ~8 KB
- **Data Files**: Size varies (your actual data)

## Technology Stack

- **Python 3.8+**: Programming language
- **Streamlit**: Web dashboard framework
- **Pandas**: Data manipulation
- **Plotly**: Interactive visualizations
- **NumPy**: Numerical computing
- **Jupyter**: Notebook environment (for .ipynb)

## Next Steps

1. **Read**: Start with `QUICKSTART.md`
2. **Setup**: Follow instructions in `README.md`
3. **Run**: Launch the dashboard
4. **Explore**: Use filters and tabs to discover insights
5. **Customize**: Modify dashboard.py for your needs

## Support Resources

- Full documentation in `README.md`
- Troubleshooting section included
- Code comments in all Python files

---

**Everything you need to analyze crypto trading sentiment is included! 🚀**
