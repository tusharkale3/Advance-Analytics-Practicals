import numpy as np

"""### Example 1: Calculating Total Revenue"""

prices = np.array([19.99, 29.99, 14.99, 9.99, 24.99])
print(prices)

quantities = np.array([10, 5, 8, 12, 3])
print(quantities)

revenue_per_product = prices * quantities
print(revenue_per_product)

total_revenue = np.sum(revenue_per_product)
print(total_revenue)

"""### Example 2: Analyzing Blog Post Stats"""

views = np.array([1000, 500, 800, 1200, 300, 600])
print(views)

max_views = np.max(views)
print(max_views)

min_views = np.min(views)
print(min_views)

average_views = np.round(np.mean(views), 2)
print(average_views)

total_views = np.sum(views)
print(total_views)

"""### Example 3: Splitting Order into Batches"""

order_ids = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008])
print(order_ids)

batches = np.split(order_ids, 4)
print(batches)

for batch in batches:
    print(batch)

"""### Example 4: Categorizing Product Rating"""

ratings = np.array([4.5, 3.2, 2.8, 5.0, 4.1, 3.9, 2.5, 4.7])
print(ratings)

positive_ratings = ratings[ratings >= 4.0]
print(positive_ratings)

negative_ratings = ratings[ratings < 4.0]
print(negative_ratings)

"""### Example 5: Calculate Total and Average quantites sold"""

# Each column is specific product in the order
# Each row represents specific order
order_quantities = np.array([[5, 3, 2, 7], [10, 6, 3, 9]])
print(order_quantities)

# Quantities of the sales of each product
total_quantities_sold = np.sum(order_quantities, axis=0)
print(total_quantities_sold)

# Quantities of the sales in each order
total_products_per_order = np.sum(order_quantities, axis=1)
print(total_products_per_order)

# Average quantities per product
average_quantities_sold = np.mean(order_quantities, axis=0)
print(average_quantities_sold)

"""### Example 6: Calculate Average product Rating and Maximum rating per Category"""

# Each row represents specific product
# Each product is rated in 4 different categories
product_reviews = np.array([[4.5, 3.2, 2.5, 5.0], [4.3, 3.8, 1.0, 4.8], [2.0, 3.6, 4.7, 0.5]])
print(product_reviews)

average_rating = np.mean(product_reviews, axis=1)
print(average_rating)

max_rating_per_category = np.max(product_reviews, axis=0)
print(max_rating_per_category)

"""### Example 7: Generation of the sample stock data"""

companies = ['Google', 'Microsoft', 'Apple']
days = ['Monday, 1 Apr', 'Tuesday, 2 Apr']
price_types = ['Open', 'Close', 'High', 'Low']

np.random.seed(1)
stock_prices = np.round(np.random.random((len(companies), len(days), len(price_types))), 3)
print(stock_prices)

print(stock_prices.shape)

for index_axis_0, company in enumerate(companies):
    print(f"Stock prices for the {company}:")
    for index_axis_1, day in enumerate(days):
        print(f"Day: {day}")
        for index_axis_2, price_type in enumerate(price_types):
            print(f"{price_type} Price: {stock_prices[index_axis_0, index_axis_1, index_axis_2]}")
        print('')
    print('')