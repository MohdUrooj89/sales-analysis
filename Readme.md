# Sales Data Analysis and Visualization 📊

--A Python-based data analysis project that cleanses raw sales records and generates visual insights into yearly performance, 
  geographical distribution, and product trends.

# 🚀Project Overview : 

* This project takes a raw sales dataset (CSV), performs rigorous data cleaning using 'Pandas', and 'utilizes Matplotlib' and 'Seaborn' to create high-quality visualizations. The goal is to transform messy transactional data into actionable business intelligence.

# ⚙️Tech Stack :

* Language : Python 3.x

* Libraries :  Pandas : Data manipulation and cleaning

  NumPy: Numerical operations

  Matplotlib & Seaborn : Data visualization

# 🧹Data Cleaning Process :

--The script performs several preprocessing steps to ensure data integrity :

  * Normalization: Converts all column names to lowercase and removes whitespace.

  * Missing Value Handling: Fills null values with 0 to prevent calculation errors.

  * String Sanitization: Strips leading/trailing spaces from all object-type columns.

  * Feature Engineering:

   Combines contactfirstname and contactlastname into a single contactfullname.

   Extracts year, month, day, and day_name from the orderdate.

 * Dimensionality Reduction: Drops unnecessary columns like phone numbers and specific address lines to focus on analytical features.

 * Export: Saves the refined dataset to clean_sale.xlsx.

# 📈Visualizations : 

--The script generates five key analytical plots :

 * Sales Over Year : A bar chart showing total revenue growth across different years.

 * Total Sale By Country : A breakdown of the top 5 performing countries.

 * Monthly Sale Comparison : A multi-line chart comparing seasonal trends for 2003, 2004, and 2005.

 * Order Status Distribution : A pie chart showing the percentage of orders (Shipped, Cancelled, On Hold, etc.).

 * Product Line & Deal Size : A grouped count plot analyzing which product categories drive small, medium, or large deals.


