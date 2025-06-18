def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


t1 = (1, 2, "example")
s1 = {b"item1", b"item2"}
print(process_items(t1, s1))
# 元组和集合类型提示
