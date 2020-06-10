from locust import HttpUser, between, task, TaskSet, SequentialTaskSet


class GetCartPriceUser(HttpUser):
    wait_time = between(0, 1)
    weight = 1

    @task
    def get_cart_price(self):
        checkout_information_for_address = {"products": [5], "address": 3}
        checkout_information_for_another_address = {"products": [5], "address": 4}

        self.client.post("/cart", json=checkout_information_for_address)
        self.client.post("/cart", json=checkout_information_for_another_address)


class GetAllCartsUser(HttpUser):
    wait_time = between(0, 1)
    weight = 6

    @task
    def get_all_carts(self):
        self.client.get("/products/")


class SequentialTasks(SequentialTaskSet):
    @task
    def add_product_to_cart(self):
        self.client.put("/users/1/cart/add/5")

    @task
    def remove_product_from_cart(self):
        self.client.put("/users/1/cart/remove/5")


class InteractWithCartUser(HttpUser):
    wait_time = between(0, 3)
    weight = 3

    tasks = [SequentialTasks]
    # @task
    # def add_then_remove_product(self):
    #     self.client.put("http://127.0.0.1:8080/users/1/cart/add/5")
    #     self.client.put("http://127.0.0.1:8080/users/1/cart/remove/5")
