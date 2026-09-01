CUSTOMER ORDER ANALYSIS USING PYTHON

Project Overview 

This project analyses e-commerce customer orders using Python built-in data structures and control statements. It identifies customer spending patterns, classifies customers by value, calculates category revenue, and produces useful business insights for inventory and marketing decisions. 

The problem asks us to act as an e-commerce data analyst. Given customer orders, we must use Python collections to answer business questions: 
• Who spends the most? 
• Which customers are high-, moderate-, or low-value buyers? 
• Which category earns the most revenue? 
• Who buys Electronics, Clothing, or multiple categories? 
• What product is ordered most frequently? 

Files : 
customer_order_analysis.py - Main Python program that performs 
the analysis. 
index.html  - Optional browser dashboard showing the results. 

Data Structures Used 
1. List - Stores the customer names. - Stores all order records. 
2. Tuple - Each order is stored as: 
(customer name, product, price, category) 
3. Dictionary - Maps each customer to their purchased products. - Maps products to categories. - Stores total spending for every customer. - Stores total revenue for every product category. - Stores each customer's purchase classification. 
4. Set - Extracts unique categories and unique products. - Tracks categories purchased by each customer. - Finds customers who bought from multiple categories. - Finds customers who bought both Electronics and Clothing. 
Analysis Performed - Calculates each customer's total spending. - Classifies spending as: 
High-value buyer: above $100 
Moderate buyer:   $50 to $100 
Low-value buyer:  below $50

- Calculates total revenue for Electronics, Clothing, and Home 
Essentials. - Finds unique products and available categories. - Identifies customers who purchased Electronics. - Finds customers who purchased from more than one category. - Finds customers who purchased both Electronics and Clothing. - Sorts customers to show the top three highest spenders. - Counts product purchases to identify the most frequently bought product. 
Business Results 
Total revenue: $1,969.88 
Highest-revenue category: Electronics ($1,619.96) 
Most frequently purchased product: T-Shirt (2 orders) 
High-value buyers: Rohan, Abhishek, Sarah, and Elena

Top three customers by spending: 
1. Rohan - $924.98 
2. Sarah - $649.98 
3. Abhishek - $144.98
4. 
Customers who bought Electronics: 
Rohan, Abhishek, Sarah, Elena 
Customers who bought both Electronics and Clothing 
Rohan, Elena

Conclusion 
This solution meets the course project requirements by using lists, tuples, dictionaries, sets, loops, conditionals, comprehensions, sorting, and set operations to analyse real-world-style customer order data. 
