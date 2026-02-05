import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Crypto Trading Sentiment Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-top: 0;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and prepare the data"""
    try:
        # Load datasets
        df_sentiment = pd.read_csv('fear_greed_index.csv')
        df_trades = pd.read_csv('historical_data.csv')
        
        # Convert dates
        df_sentiment['date'] = pd.to_datetime(df_sentiment['date'])
        df_trades['Timestamp IST'] = pd.to_datetime(df_trades['Timestamp IST'])
        df_trades['date'] = df_trades['Timestamp IST'].dt.date
        df_trades['date'] = pd.to_datetime(df_trades['date'])
        
        # Merge dataframes
        merged_df = pd.merge(df_trades, df_sentiment, on='date', how='inner')
        
        return df_sentiment, df_trades, merged_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Please ensure 'fear_greed_index.csv' and 'historical_data.csv' are in the same directory as this script.")
        return None, None, None

def calculate_metrics(merged_df):
    """Calculate key metrics for the dashboard"""
    if merged_df is None:
        return None
    
    metrics = {
        'total_pnl': merged_df['Closed PnL'].sum(),
        'avg_pnl': merged_df['Closed PnL'].mean(),
        'total_trades': len(merged_df),
        'win_rate': (merged_df['Closed PnL'] > 0).sum() / len(merged_df) * 100,
        'unique_accounts': merged_df['Account'].nunique(),
        'unique_coins': merged_df['Coin'].nunique(),
        'total_volume': merged_df['Size USD'].sum(),
        'avg_position_size': merged_df['Size USD'].mean()
    }
    
    return metrics

def main():
    # Header
    st.markdown('<p class="main-header">📈 Crypto Trading Sentiment Analysis Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Exploring the relationship between Fear & Greed Index and trading performance</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Load data
    with st.spinner("Loading data..."):
        df_sentiment, df_trades, merged_df = load_data()
    
    if merged_df is None:
        st.stop()
    
    # Sidebar filters
    st.sidebar.header("🎛️ Filters")
    
    # Sentiment filter
    sentiments = ['All'] + sorted(merged_df['classification'].unique().tolist())
    selected_sentiment = st.sidebar.selectbox("Market Sentiment", sentiments)
    
    # Date range filter
    min_date = merged_df['date'].min().date()
    max_date = merged_df['date'].max().date()
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Coin filter
    coins = ['All'] + sorted(merged_df['Coin'].unique().tolist())
    selected_coin = st.sidebar.selectbox("Cryptocurrency", coins)
    
    # Apply filters
    filtered_df = merged_df.copy()
    if selected_sentiment != 'All':
        filtered_df = filtered_df[filtered_df['classification'] == selected_sentiment]
    if len(date_range) == 2:
        filtered_df = filtered_df[(filtered_df['date'].dt.date >= date_range[0]) & 
                                  (filtered_df['date'].dt.date <= date_range[1])]
    if selected_coin != 'All':
        filtered_df = filtered_df[filtered_df['Coin'] == selected_coin]
    
    # Calculate metrics
    metrics = calculate_metrics(filtered_df)
    
    # Overview metrics
    st.header("📊 Key Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total PnL", f"${metrics['total_pnl']:,.2f}", 
                 help="Total profit/loss across all trades")
    with col2:
        st.metric("Win Rate", f"{metrics['win_rate']:.2f}%",
                 help="Percentage of profitable trades")
    with col3:
        st.metric("Total Trades", f"{metrics['total_trades']:,}",
                 help="Number of trades in selected period")
    with col4:
        st.metric("Avg Position", f"${metrics['avg_position_size']:,.2f}",
                 help="Average position size in USD")
    
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.metric("Unique Accounts", f"{metrics['unique_accounts']}")
    with col6:
        st.metric("Unique Coins", f"{metrics['unique_coins']}")
    with col7:
        st.metric("Total Volume", f"${metrics['total_volume']:,.0f}")
    with col8:
        st.metric("Avg PnL/Trade", f"${metrics['avg_pnl']:,.2f}")
    
    st.markdown("---")
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Sentiment Analysis", 
        "💰 Performance Metrics", 
        "🎯 Trading Behavior",
        "👥 Trader Segmentation",
        "📊 Advanced Analytics"
    ])
    
    with tab1:
        st.header("Sentiment Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # PnL by sentiment
            sentiment_pnl = filtered_df.groupby('classification')['Closed PnL'].sum().reset_index()
            sentiment_pnl = sentiment_pnl.sort_values('Closed PnL', ascending=False)
            
            fig = px.bar(sentiment_pnl, x='classification', y='Closed PnL',
                        title='Total PnL by Market Sentiment',
                        color='Closed PnL',
                        color_continuous_scale='RdYlGn')
            fig.update_layout(xaxis_title="Sentiment", yaxis_title="Total PnL ($)")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Win rate by sentiment
            sentiment_stats = filtered_df.groupby('classification').agg({
                'Closed PnL': [
                    ('Win Rate', lambda x: (x > 0).sum() / len(x) * 100),
                    ('Total Trades', 'count')
                ]
            }).reset_index()
            sentiment_stats.columns = ['classification', 'Win Rate', 'Total Trades']
            
            fig = px.bar(sentiment_stats, x='classification', y='Win Rate',
                        title='Win Rate by Market Sentiment',
                        color='Win Rate',
                        color_continuous_scale='Blues')
            fig.update_layout(xaxis_title="Sentiment", yaxis_title="Win Rate (%)")
            st.plotly_chart(fig, use_container_width=True)
        
        # Sentiment over time
        st.subheader("Market Sentiment Over Time")
        sentiment_timeline = filtered_df.groupby(['date', 'classification']).size().reset_index(name='trades')
        fig = px.scatter(sentiment_timeline, x='date', y='trades', 
                        color='classification',
                        title='Trade Activity by Sentiment Over Time',
                        size='trades')
        fig.update_layout(xaxis_title="Date", yaxis_title="Number of Trades")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Performance Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # PnL distribution
            st.subheader("PnL Distribution")
            fig = px.histogram(filtered_df, x='Closed PnL', nbins=50,
                             title='Distribution of Closed PnL')
            fig.add_vline(x=0, line_dash="dash", line_color="red", 
                         annotation_text="Break-even")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # PnL box plot by sentiment
            st.subheader("PnL Distribution by Sentiment")
            fig = px.box(filtered_df, x='classification', y='Closed PnL',
                        title='PnL Distribution by Sentiment',
                        color='classification')
            fig.add_hline(y=0, line_dash="dash", line_color="red")
            st.plotly_chart(fig, use_container_width=True)
        
        # Performance by sentiment table
        st.subheader("Detailed Performance Metrics by Sentiment")
        performance_table = filtered_df.groupby('classification').agg({
            'Closed PnL': [
                ('Total PnL', 'sum'),
                ('Avg PnL', 'mean'),
                ('Win Rate %', lambda x: (x > 0).sum() / len(x) * 100),
                ('Avg Loss', lambda x: x[x < 0].mean() if len(x[x < 0]) > 0 else 0)
            ],
            'Size USD': [('Avg Position Size', 'mean')],
            'Account': [('Total Trades', 'count')]
        }).round(2)
        performance_table.columns = ['Total PnL ($)', 'Avg PnL ($)', 'Win Rate (%)', 
                                     'Avg Loss ($)', 'Avg Position Size ($)', 'Total Trades']
        st.dataframe(performance_table, use_container_width=True)
    
    with tab3:
        st.header("Trading Behavior Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Trade frequency by sentiment
            st.subheader("Trade Frequency by Sentiment")
            trade_freq = filtered_df.groupby('classification').size().reset_index(name='count')
            fig = px.pie(trade_freq, values='count', names='classification',
                        title='Trade Distribution Across Sentiments')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Long/Short ratio by sentiment
            st.subheader("Long/Short Ratio by Sentiment")
            side_counts = filtered_df.groupby(['classification', 'Side']).size().unstack(fill_value=0)
            side_counts['Long/Short Ratio'] = side_counts['BUY'] / side_counts['SELL']
            
            fig = px.bar(side_counts.reset_index(), x='classification', y='Long/Short Ratio',
                        title='Long/Short Ratio by Sentiment',
                        color='Long/Short Ratio',
                        color_continuous_scale='RdBu')
            fig.add_hline(y=1, line_dash="dash", line_color="black", 
                         annotation_text="Neutral (1:1)")
            st.plotly_chart(fig, use_container_width=True)
        
        # Position sizing by sentiment
        st.subheader("Average Position Size by Sentiment")
        avg_size = filtered_df.groupby('classification')['Size USD'].mean().reset_index()
        fig = px.bar(avg_size, x='classification', y='Size USD',
                    title='Average Position Size by Sentiment',
                    color='Size USD',
                    color_continuous_scale='Viridis')
        fig.update_layout(xaxis_title="Sentiment", yaxis_title="Avg Position Size ($)")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.header("Trader Segmentation")
        
        # Calculate trader stats
        trader_stats = filtered_df.groupby('Account').agg({
            'Closed PnL': ['sum', lambda x: (x > 0).sum() / len(x) * 100],
            'Size USD': 'mean',
            'Account': 'count'
        })
        trader_stats.columns = ['Total PnL', 'Win Rate', 'Avg Position Size', 'Total Trades']
        trader_stats = trader_stats.reset_index()
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Top performers
            st.subheader("Top 10 Accounts by PnL")
            top_10 = trader_stats.nlargest(10, 'Total PnL')
            fig = px.bar(top_10, x='Account', y='Total PnL',
                        title='Top 10 Accounts by Total PnL',
                        color='Total PnL',
                        color_continuous_scale='Greens')
            fig.update_layout(xaxis_title="Account", yaxis_title="Total PnL ($)",
                            xaxis={'tickangle': -45})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Win rate distribution
            st.subheader("Win Rate Distribution")
            fig = px.histogram(trader_stats, x='Win Rate', nbins=30,
                             title='Distribution of Win Rates Across Accounts')
            median_wr = trader_stats['Win Rate'].median()
            fig.add_vline(x=median_wr, line_dash="dash", line_color="red",
                         annotation_text=f"Median: {median_wr:.1f}%")
            st.plotly_chart(fig, use_container_width=True)
        
        # Scatter: Win Rate vs Total PnL
        st.subheader("Win Rate vs Total PnL")
        fig = px.scatter(trader_stats, x='Win Rate', y='Total PnL',
                        size='Total Trades', 
                        hover_data=['Account', 'Avg Position Size'],
                        title='Account Performance: Win Rate vs Total PnL',
                        color='Total PnL',
                        color_continuous_scale='RdYlGn')
        fig.add_hline(y=0, line_dash="dash", line_color="gray")
        fig.add_vline(x=trader_stats['Win Rate'].median(), line_dash="dash", 
                     line_color="gray")
        st.plotly_chart(fig, use_container_width=True)
        
        # Segmentation
        median_wr = trader_stats['Win Rate'].median()
        consistent_winners = trader_stats[
            (trader_stats['Total PnL'] > 0) & 
            (trader_stats['Win Rate'] > median_wr)
        ]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Consistent Winners", len(consistent_winners))
        with col2:
            st.metric("Avg PnL (Winners)", f"${consistent_winners['Total PnL'].mean():,.2f}")
        with col3:
            st.metric("Avg Win Rate (Winners)", f"{consistent_winners['Win Rate'].mean():.2f}%")
    
    with tab5:
        st.header("Advanced Analytics")
        
        # Daily trading activity
        st.subheader("Daily Trading Activity")
        daily_stats = filtered_df.groupby('date').agg({
            'Closed PnL': 'sum',
            'Account': 'count'
        }).reset_index()
        daily_stats.columns = ['date', 'Daily PnL', 'Trade Count']
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(
            go.Scatter(x=daily_stats['date'], y=daily_stats['Daily PnL'], 
                      name="Daily PnL", line=dict(color='green')),
            secondary_y=False
        )
        fig.add_trace(
            go.Scatter(x=daily_stats['date'], y=daily_stats['Trade Count'], 
                      name="Trade Count", line=dict(color='blue')),
            secondary_y=True
        )
        fig.update_xaxes(title_text="Date")
        fig.update_yaxes(title_text="Daily PnL ($)", secondary_y=False)
        fig.update_yaxes(title_text="Trade Count", secondary_y=True)
        fig.update_layout(title_text="Daily PnL and Trade Count Over Time")
        st.plotly_chart(fig, use_container_width=True)
        
        # Top coins by volume
        st.subheader("Top Cryptocurrencies by Trading Volume")
        coin_volume = filtered_df.groupby('Coin')['Size USD'].sum().reset_index()
        coin_volume = coin_volume.nlargest(10, 'Size USD')
        
        fig = px.bar(coin_volume, x='Coin', y='Size USD',
                    title='Top 10 Coins by Trading Volume',
                    color='Size USD',
                    color_continuous_scale='Plasma')
        fig.update_layout(xaxis_title="Cryptocurrency", yaxis_title="Total Volume ($)")
        st.plotly_chart(fig, use_container_width=True)
        
        # Correlation heatmap
        st.subheader("Data Exploration")
        numeric_df = filtered_df[['Size USD', 'Closed PnL']].copy()
        numeric_df['Hour'] = filtered_df['Timestamp IST'].dt.hour
        numeric_df['Day of Week'] = filtered_df['Timestamp IST'].dt.dayofweek
        
        corr_matrix = numeric_df.corr()
        fig = px.imshow(corr_matrix, 
                       title='Correlation Matrix',
                       color_continuous_scale='RdBu',
                       aspect='auto')
        st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>📊 Crypto Trading Sentiment Analysis Dashboard | Data-driven insights for better trading decisions</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
