from collections import OrderedDict


def get_order_list(number_of_items):
    """ Takes in a list of items along with its price.
        Eg: apple 10
            banana 15
            orange 20
            apple 10
            banana 15

        The total price of the items are calculated by getting the total quantity and adding it.
        Eg: 2 apples: 10 + 10 = 20
            2 banana: 15 + 15 = 30
            1 orange: 20 = 20

        The similar items are grouped together using the ordered dict function,
        and it will return the total price.
        Eg: apple 20
            banana 30
            orange 20
    """
    item_list = OrderedDict()

    for i in range(number_of_items):
        item_name, x, item_price = map(str, input().rpartition(' '))
        net_price = item_list.get(item_name, 0) + int(item_price)
        item_list[item_name] = net_price
    for j, k in item_list.items():
        print(j, k)


num_of_items = int(input())
get_order_list(num_of_items)