from locust import HttpUser, between, task, TaskSet, SequentialTaskSet
import random

user_ids = [1, 2, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40]
address_ids = [3, 4, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41]
product_ids = [5, 7, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42]


def get_random_id_from_array(array):
    return array[random.randint(0, len(array) - 1)]


def get_random_elements_from_array(array):
    quantity = random.randint(2, 5)
    result = []
    for x in range(quantity):
        result.append(get_random_id_from_array(array))
    return result


class GetCartPriceUser(HttpUser):
    wait_time = between(0, 1)
    weight = 1

    @task
    def get_cart_price(self):
        checkout_information_for_address = {"products": get_random_elements_from_array(product_ids),
                                            "address": get_random_id_from_array(address_ids)}
        checkout_information_for_another_address = {"products": get_random_elements_from_array(product_ids),
                                                    "address": get_random_id_from_array(address_ids)}

        self.client.post("/cart", json=checkout_information_for_address)
        self.client.post("/cart", json=checkout_information_for_another_address)


class GetAllCartsUser(HttpUser):
    wait_time = between(0, 1)
    weight = 6

    @task
    def get_all_carts(self):
        self.client.get("/products/")


class SequentialTasks(SequentialTaskSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.random_product_id = get_random_id_from_array(product_ids)
        self.random_user_id = get_random_id_from_array(user_ids)

    @task
    def add_product_to_cart(self):
        url = "/users/{user_id}/cart/add/{prod_id}".format(prod_id=self.random_product_id,
                                                           user_id=self.random_user_id)
        self.client.put(url)

    @task
    def remove_product_from_cart(self):
        url = "/users/{user_id}/cart/remove/{prod_id}".format(prod_id=self.random_product_id,
                                                              user_id=self.random_user_id)
        self.client.put(url)


class InteractWithCartUser(HttpUser):
    wait_time = between(0, 3)
    weight = 3

    tasks = [SequentialTasks]
