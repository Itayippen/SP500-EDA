import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

SP500_comp = pd.read_csv('sp500_companies.csv')
print(SP500_comp.info())
#counting how many companies per sector + graph
sector_count = SP500_comp['Sector'].value_counts()
plt.figure(figsize = (12,8))
sns.barplot(x =sector_count.values, y = sector_count.index, palette ='viridis', hue=sector_count.index,
            legend = False)
plt.title('Number of companies in Sector', fontsize= 14 , fontweight = 'bold')
plt.xlabel('number of companies', fontsize = 10)
plt.ylabel('Sector', fontsize= 10)
plt.tight_layout()
plt.show()

#missing revenue growth data
missing_growth_tickers = SP500_comp[SP500_comp['Revenuegrowth'].isnull()]['Symbol'].tolist()
print(missing_growth_tickers)
def replace_null(df, ticker, col, missing_key):
    print(f"🔄 Fetching '{missing_key}' for {ticker} from Yahoo Finance...")
    sym = yf.Ticker(ticker)
    new_value = sym.info.get(missing_key, None)
    df.loc[df['Symbol'] == ticker, col] = new_value
    print(f"✅ Successfully updated {sym} {col} to: {new_value}")
for ticker in missing_growth_tickers:
    replace_null(SP500_comp, ticker, 'Revenuegrowth', 'revenueGrowth')

#missing employees data
missing_employees = SP500_comp['Fulltimeemployees'].isnull()
print(SP500_comp[missing_employees][['Symbol']])
mode_employees = SP500_comp['Fulltimeemployees'].mode()[0]
print(f"\n the mode is : {mode_employees}")
SP500_comp.loc[missing_employees, 'Fulltimeemployees'] = mode_employees
print(" Filled missing full-time employees with the mode.")
print("\n --- Missing Values in Fulltimeemployees ---")
print(SP500_comp['Fulltimeemployees'].isnull().sum())

#finding correlation
SP_corr = SP500_comp.corr(numeric_only=True)
mask = np.zeros_like(SP_corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style('white'):
    f, ax = plt.subplots(figsize=(12,10))
    ax = sns.heatmap(SP_corr , mask=mask, vmax=1, vmin=-1,linewidths=.5,
                     square=True,cmap='coolwarm', annot=True)
plt.title('Correlation Heatmap of S&P 500 Companies dataset', fontsize = 15)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

sns.set(style='darkgrid')
#plt.figure(figsize=(15,12), height = 3)
sns.pairplot(SP500_comp, corner=True, hue='Exchange', height=3)
plt.tight_layout()
plt.show()

f = {'Revenuegrowth':['mean'], 'Marketcap':['sum'], 'Longname':['count']}
sector_breakdown = SP500_comp.groupby('Sector').agg(f)
sector_breakdown.columns = sector_breakdown.columns.get_level_values(0)
sector_breakdown = sector_breakdown.reset_index()
sector_breakdown = sector_breakdown.sort_values('Longname', ascending=False)
fig = plt.figure(num=None, figsize=(14, 6), dpi=100, facecolor='w', edgecolor='k')

plt.subplot(1, 3, 1)
ax1 = sns.barplot(x="Longname", y="Sector", data=sector_breakdown, palette=('coolwarm'))
ax1.set_xlabel('Number of companies', weight='bold')
ax1.set_ylabel('Sector', weight = 'bold')
ax1.set_title('SECTOR BREAKDOWN\n', weight='bold').set_fontsize('18')

plt.subplot(1, 3, 2)
ax2 = sns.barplot(x="Marketcap", y="Sector", data=sector_breakdown, palette=('Wistia'))
ax2.set_xlabel('Total Market Cap', weight='bold')
ax2.set_ylabel('')
ax2.set_yticks([])

plt.subplot(1, 3, 3)
ax2 = sns.barplot(x="Revenuegrowth", y="Sector", data=sector_breakdown, palette=('OrRd_r'))
ax2.set_xlabel('Revenue Growth', weight='bold')
ax2.set_ylabel('')
ax2.set_yticks([])
sns.despine()
plt.tight_layout()
plt.show()

# pi chart
exchange_df = (SP500_comp.groupby(["Exchange"]).size().reset_index(name="Counts").sort_values(by=["Exchange"]))
labels = exchange_df['Exchange'].unique()
values = exchange_df['Counts']
plt.figure(figsize=(10,12))
fig1 = plt.pie(x=values, labels=labels,explode=[0,0,0.05,0.01], autopct='%.2f')
plt.legend()
plt.title('Exchange % in S&P 500 Index')
plt.show()

#top 12 stocks dashboard
N = 12
fig2 = plt.figure(num=None, figsize=(17, 6), dpi=100, facecolor='w', edgecolor='k')
#market cap
plt.subplot(1, 4, 1)
ax1 = sns.barplot(x=SP500_comp.iloc[:N,7], y=SP500_comp.iloc[:N,2], data=SP500_comp, palette=('coolwarm'))
ax1.set_xlabel('Market Cap', weight='bold')
ax1.set_ylabel(f'Top {N} Companies', weight = 'bold')
ax1.set_title(f'TOP {N} STOCK ANALYSIS', weight='bold').set_fontsize('18')
#ebitda
plt.subplot(1, 4, 2)
ax2 = sns.barplot(x=SP500_comp.iloc[:N,8], y=SP500_comp.iloc[:N,2], data=SP500_comp, palette=('turbo'))
ax2.set_xlabel('EBITDA', weight='bold')
ax2.set_ylabel('')
ax2.set_yticks([])
#current price
plt.subplot(1, 4, 3)
ax2 = sns.barplot(x= SP500_comp.iloc[:N , 6], y= SP500_comp.iloc[:N, 2], data = SP500_comp,
                  palette=('rainbow'))
ax2.set_xlabel('Current Price', weight='bold')
ax2.set_ylabel('')
ax2.set_yticks([])
#Full Time Employees
# Full Time Employees
plt.subplot(1, 4, 4)
ax2 = sns.barplot(x=SP500_comp['Fulltimeemployees'].iloc[:N], y=SP500_comp.iloc[:N, 2], data=SP500_comp,
    palette='Spectral', hue=SP500_comp.iloc[:N, 2], legend=False)
ax2.set_xlabel('Employees', weight='bold')
ax2.set_ylabel('')
ax2.set_yticks([])
plt.tight_layout()
plt.show()

