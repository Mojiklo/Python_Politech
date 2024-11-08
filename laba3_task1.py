# TODO Напишите функцию для поиска индекса товара
def function(product_list, find):
    for i, item in enumerate(product_list):  # если номер вхождения, то start=1
        if item == find:
            return i
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    # TODO Вызовите функцию, что получить индекс товара
    index_item = function(items_list, find_item)
    if index_item is not None:
        print(
            f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
