stock_prices = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}
print("enter print to see the stock prices and its average")
print("enter add to add a new stock and its prices")
options = input("Enter your option: ")
if options == "print":
    for stock, prices in stock_prices.items():
        average_price = sum(prices) / len(prices)
        print(f"{stock}: Prices: {prices}, Average Price: {average_price:.2f}")
elif options == "add":
    stock = input("Enter the stock name: ")
    prices = []
    for i in range(3):
        price = float(input(f"Enter price {i + 1} for {stock}: "))
        prices.append(price)
    stock_prices[stock] = prices
    print(f"{stock} with prices {prices} added.")
    print(stock_prices)