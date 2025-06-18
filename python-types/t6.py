def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


d1 = {'foo': 1.0, 'bar': 2.0}
print(process_items(d1))
# 字典类型提示
