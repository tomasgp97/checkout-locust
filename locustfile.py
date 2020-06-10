from locust import HttpUser, between, task, TaskSet


class GetCartPriceUser(HttpUser):
    wait_time = between(0, 1)
    weight = 1

    @task
    def get_cart_price(self):
        checkout_information_for_address = {"products": [5],
                                            "address": 3}
        checkout_information_for_another_address = {"products": [5, 5, 5],
                                                    "address": 4}

        self.client.post("/cart", json=checkout_information_for_address)
        self.client.post("/cart", json=checkout_information_for_another_address)


class GetAllCartsUser(HttpUser):
    wait_time = between(0, 1)
    weight = 6

    @task
    def get_all_carts(self):
        self.client.get("/products/")


class InteractWithCartUser(HttpUser):
    wait_time = between(0, 1)
    weight = 3

    @task(6)
    def add_product_to_cart(self):
        self.client.put("/1/cart/add/5")

    @task(4)
    def add_product_to_cart(self):
        self.client.put("/2/cart/remove/5")


# class CheckoutTasks(TaskSet):
#     wait_time = between(0, 1)

# @task
# def create_transactions(self):
#     username_password = AUTH_MAP[random.randint(1, 4)]
#     self.client.post('/auth', json=username_password)
#     transaction_body = {
#         'userFrom': USER_MAP[random.randint(1, 4)],
#         'userTo': USER_MAP[random.randint(1, 4)],
#         'amount': random.randint(0, 20)
#     }
#     self.client.post("/transactions", json=transaction_body)
#
# def on_stop(self):
#     self.interrupt()

# @task
# def add_products_to_cart(self):
