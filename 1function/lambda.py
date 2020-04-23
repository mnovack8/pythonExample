items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

#can use lambda when a parameter is func: Callable or reference a function
#lambda object : expression, list
lambda_prices = list(map(lambda item: item[1], items))
print(lambda_prices)
#Another example
#list.sort(lambda object : expression)
#items.sort(key=lambda item:item[1])

#[expression for object in list]
comprehension_prices = [item[1] for item in items]
print(comprehension_prices)
