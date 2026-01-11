import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


df = pd.read_csv("C:\VSCodeCProjects\hello\Data\sales_data_sample.csv",encoding="latin1")

df.columns = df.columns.str.lower().str.strip()

print(df.isnull().sum())
df.fillna(0,inplace=True)

string_columns = df.select_dtypes(include=['object']).columns

for col in string_columns:
    df[col] = df[col].astype(str).str.strip()

df['contactfullname'] = df['contactfirstname'] + ' ' + df['contactlastname']

df = df.drop(['phone','addressline1','addressline2','contactfirstname','contactlastname'],axis=1)

df['orderdate'] = pd.to_datetime(df['orderdate'])
df['order_year'] = df['orderdate'].dt.year
df['order_month'] = df['orderdate'].dt.month
df['order_day'] = df['orderdate'].dt.day
df['order_dow'] = df['orderdate'].dt.day_name()


df.to_excel('clean_sale.xlsx',index=False)

sns.set(style='whitegrid')

plt.figure(figsize=(6,4))
sns.barplot(x='order_year',y='sales',data=df,palette=['green','yellow','skyblue'],estimator=sum)
plt.ticklabel_format(style='plain',axis='y')
plt.title('Sales Over Year',color='black',fontsize=15)
plt.xlabel('Year',color='black',fontsize=15)
plt.ylabel('Total Sale',color='black',fontsize=15)

plt.tight_layout()
plt.savefig('Sales_by_year.png',dpi=400,bbox_inches='tight')
plt.show()



Country_sale = df.groupby('country')['sales'].sum().sort_values(ascending=False).head().reset_index()

plt.figure(figsize=(6,4))
plt.bar(Country_sale['country'],Country_sale['sales'],color=['#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51'])
plt.ticklabel_format(style='plain',axis='y')
plt.title('Total Sale By Country',color='black',fontsize=15)
plt.xlabel('Countries',color='black',fontsize=15)
plt.ylabel('Total Sale',color='black',fontsize=15)

plt.tight_layout()
plt.savefig('Country_Sales.png',dpi=400,bbox_inches='tight')
plt.show()


plt.figure(figsize=(6,4))
sns.lineplot(x='order_month',y='sales',data=df,hue='order_year',estimator=sum,marker='o',linewidth=3,errorbar=None)
plt.xticks(range(1,13),['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
plt.title('Monthly Sale Comparison: 2003,2004,2005',color='black',fontsize=15)
plt.xlabel('Month',color='black',fontsize=15)
plt.ylabel('Sale',color='black',fontsize=15)

plt.tight_layout()
plt.savefig('Sales_by_Month',dpi=400,bbox_inches='tight')
plt.show()


Status_counts = df['status'].value_counts()

plt.figure(figsize=(6,4))
plt.pie(Status_counts,labels=Status_counts.index,startangle=160,autopct='%1.1f%%')
plt.title('Distribution of Order Status',color='black',fontsize=15)

plt.tight_layout()
plt.savefig('Order_Status.png',dpi=400,bbox_inches='tight')
plt.show()


plt.figure(figsize=(12,6))
sns.countplot(x='productline',data=df,palette='viridis',hue='dealsize')
plt.title('Distribution of Product Line & Dealsize (No of Orders)',color='black',fontsize=15)
plt.xlabel('Product Line & Dealsize',color='black',fontsize=15)
plt.ylabel('Count',color='black',fontsize=15)

plt.tight_layout()
plt.savefig('Productline_&_Dealsize.png',dpi=400,bbox_inches='tight')
plt.show()










