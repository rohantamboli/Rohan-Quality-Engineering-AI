"""Analyze e-commerce customer orders using Python collections."""

# List of customer names
customers = ["Rohan", "Abhishek", "Shubham", "Sarah", "Nancy", "Elena"]

# Tuples: (customer name, product, price, category)
orders = [
    ("Rohan", "Laptop", 899.99, "Electronics"),
    ("Rohan", "T-Shirt", 24.99, "Clothing"),
    ("Abhishek", "Coffee Maker", 64.99, "Home Essentials"),
    ("Abhishek", "Headphones", 79.99, "Electronics"),
    ("Shubham", "Notebook", 9.99, "Home Essentials"),
    ("Shubham", "Jeans", 54.99, "Clothing"),
    ("Sarah", "Smartphone", 599.99, "Electronics"),
    ("Sarah", "Blender", 49.99, "Home Essentials"),
    ("Elena", "Jacket", 89.99, "Clothing"),
    ("Elena", "Earbuds", 39.99, "Electronics"),
    ("Nancy", "Pillow", 29.99, "Home Essentials"),
    ("Nancy", "T-Shirt", 24.99, "Clothing"),
]

# Customer names map to their ordered products.
customer_orders = {customer: [] for customer in customers}
for customer, product, _price, _category in orders:
    customer_orders[customer].append(product)

# Product-to-category lookup and unique category set.
product_categories = {product: category for _customer, product, _price, category in orders}
unique_categories = set(product_categories.values())


def classify_customer(total_spending):
    """Return a purchase classification based on total spending."""
    if total_spending > 100:
        return "High-value buyer"
    if total_spending >= 50:
        return "Moderate buyer"
    return "Low-value buyer"


# Calculate totals and revenue by category in one pass through the order data.
customer_totals = {customer: 0.0 for customer in customers}
category_revenue = {category: 0.0 for category in unique_categories}
customer_category_sets = {customer: set() for customer in customers}

for customer, _product, price, category in orders:
    customer_totals[customer] += price
    category_revenue[category] += price
    customer_category_sets[customer].add(category)

customer_classifications = {
    customer: classify_customer(total)
    for customer, total in customer_totals.items()
}
unique_products = {product for _customer, product, _price, _category in orders}
electronics_customers = [
    customer
    for customer, _product, _price, category in orders
    if category == "Electronics"
]
electronics_customers = sorted(set(electronics_customers))
top_three_customers = sorted(
    customer_totals.items(), key=lambda customer_total: customer_total[1], reverse=True
)[:3]

customers_with_multiple_categories = {
    customer
    for customer, categories in customer_category_sets.items()
    if len(categories) > 1
}
electronics_buyers = {
    customer
    for customer, categories in customer_category_sets.items()
    if "Electronics" in categories
}
clothing_buyers = {
    customer
    for customer, categories in customer_category_sets.items()
    if "Clothing" in categories
}
common_electronics_clothing_buyers = electronics_buyers & clothing_buyers


def print_report():
    """Print the requested customer, category, and purchase-behavior analysis."""
    print("CUSTOMER ORDER ANALYSIS REPORT")
    print("=" * 32)

    print("\nAvailable product categories:")
    for category in sorted(unique_categories):
        print(f"- {category}")

    print("\nCustomer spending and classification:")
    for customer in customers:
        print(
            f"- {customer}: ${customer_totals[customer]:.2f} "
            f"({customer_classifications[customer]})"
        )

    print("\nTotal revenue by category:")
    for category, revenue in sorted(category_revenue.items()):
        print(f"- {category}: ${revenue:.2f}")

    print(f"\nUnique products ({len(unique_products)}): {', '.join(sorted(unique_products))}")
    print(f"Customers who purchased electronics: {', '.join(electronics_customers)}")
    print(
        "Customers who purchased from multiple categories: "
        f"{', '.join(sorted(customers_with_multiple_categories))}"
    )
    print(
        "Customers who bought both electronics and clothing: "
        f"{', '.join(sorted(common_electronics_clothing_buyers))}"
    )

    print("\nTop three highest-spending customers:")
    for position, (customer, total) in enumerate(top_three_customers, start=1):
        print(f"{position}. {customer}: ${total:.2f}")

    total_revenue = sum(category_revenue.values())
    highest_revenue_category = max(category_revenue, key=category_revenue.get)
    product_purchase_counts = {product: 0 for product in unique_products}
    for _customer, product, _price, _category in orders:
        product_purchase_counts[product] += 1
    highest_purchase_count = max(product_purchase_counts.values())
    most_frequent_products = sorted(
        product
        for product, purchase_count in product_purchase_counts.items()
        if purchase_count == highest_purchase_count
    )
    print("\nKey business insights:")
    print(f"- Total revenue: ${total_revenue:.2f}")
    print(
        f"- Highest-revenue category: {highest_revenue_category} "
        f"(${category_revenue[highest_revenue_category]:.2f})"
    )
    print(
        f"- Most frequently purchased product(s): {', '.join(most_frequent_products)} "
        f"({highest_purchase_count} orders)"
    )
    print(
        f"- High-value customers: {sum(value == 'High-value buyer' for value in customer_classifications.values())}"
    )


if __name__ == "__main__":
    print_report()
