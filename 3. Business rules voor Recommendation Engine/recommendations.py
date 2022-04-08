import PostgreSQL.connect_postgresql_database as sql_c
from load_data_sql import product_gender
import random


#from one product this algorithm will pick a random int which is used as an index to select a new product with the same gender tag
def simular_gender(product_id):
    con, cur = sql_c.connect()
    product_query = product_gender()
    cur.execute(product_query, (product_id, product_id))
    similar_products = [product_id[0] for product_id in cur.fetchall()]

    index = random.randint(0, len(similar_products))
    new_product_gender = similar_products[index]

    return new_product_gender


if __name__ == '__main__':
    print(simular_gender('16121'))


def event_product_query():
    """"""
    return """SELECT ep.product__id FROM event_products ep, sessions s, products p 
    WHERE ep.session__id = s.session__id 
    AND ep.product__id = p.product__id
    AND s.session__id in (SELECT session__id FROM event_products WHERE product__id = %s)
    AND ep.event_type = %s
    AND ep.product__id != %s;"""


def get_all_ordered_together(product):
    """"""
    sql_connection, sql_cursor = sql_c.connect()
    products_query = event_product_query()
    sql_cursor.execute(products_query, (product, 'ordered', product))
    return [ordered_product[0] for ordered_product in sql_cursor.fetchall()]


def get_frequency(a_list):
    """
    Takes a list as input. Counts how many times each element occurs and returns each unique element in a dict together
    with the count. (dict) {:int}
    """
    result = dict()
    for item in a_list:
        try:
            result[item] += 1
        except KeyError:
            result[item] = 1
    return result


def highest_counts(frequency_dict, amount):
    """"""
    product_amount = len(frequency_dict)
    recommended_products = list()

    product_counts_list = list(frequency_dict.items())
    counts = [item[1] for item in product_counts_list]

    if amount > product_amount:
        amount = product_amount

    while amount:
        highest_count = max(counts)
        index = counts.index(highest_count)
        recommended_products.append(product_counts_list[index][0])
        del counts[index]
        del product_counts_list[index]
        amount -= 1

    return recommended_products


def recommend(product_id, amount):
    """"""
    products_ordered_together = get_all_ordered_together(product_id)
    frequency_products = get_frequency(products_ordered_together)
    recommended_products = highest_counts(frequency_products, amount)
    return recommended_products


if __name__ == '__main__':
    print(recommend('8533', 4))