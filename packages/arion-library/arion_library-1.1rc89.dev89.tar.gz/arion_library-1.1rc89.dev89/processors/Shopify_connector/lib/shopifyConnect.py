import requests
import logging
import shopify
from enum import Enum

logger = logging.getLogger(__name__)

class ShopifyConnector__(requests.Session):
    """
    A class used to interact with Shopify's REST API.

    This class provides methods to get and update products, as well as extract product IDs from SKUs.

    Attributes:
        store_url (str): The URL of the Shopify store.
        access_token (str): The access token for the Shopify API.
        headers (dict): The headers to be included in API requests.
        products (list): The list of all products in the store.
        collection_name (str): The name of the collection to interact with.

    Methods:
        __init__(store_url, access_token, collection_name): Initializes a new instance of the ShopifyConnector class.
        get_products(): Retrieves all products from the specified collection.
        get_product(product_id): Retrieves a specific product by its ID.
        extract_id_from_sku(target_sku): Extracts the product ID from a given SKU.
        update_product(product_id, data): Updates a specific product with the given data.
        create_webhook(webhook_url): Creates a webhook for the specified topic and URL.
    """

    class collection(Enum):
        PRODUCTS = "products"

    def __init__(self, store_url, access_token, collection_name):
        """
        Initialize a new instance of the ShopifyConnector class.

        Args:
            store_url (str): The URL of the Shopify store.
            access_token (str): The access token for the Shopify API.
            collection_name (str): The name of the collection to interact with.

        Raises:
            ValueError: If the provided collection name is unknown.
        """
        super().__init__()

        if collection_name not in [status.value for status in self.collection]:
            raise ValueError("Unknown collection: {}".format(collection_name))

        self.store_url = store_url
        self.access_token = access_token
        try:
            self.api_session = shopify.Session(
                self.store_url,
                "2023-01",
                self.access_token
            )
        except Exception as e:
            logger.error("An error occurred while creating the Shopify session:", e)

        self.headers.update(
            {
                'X-Shopify-Access-Token': access_token,
                'Content-Type': 'application/json'
            }
        )

        def rate_hook(r, *args, **kwargs):
            if "X-Shopify-Shop-Api-Call-Limit" in r.headers:
                logger.info("rate:", r.headers["X-Shopify-Shop-Api-Call-Limit"])
            if r.status_code == 429:
                time.sleep(int(float(r.headers["Retry-After"])))
                logger.info("rate limit reached, sleeping")

        self.hooks["response"].append(rate_hook)
        self.collection_name = collection_name

        if self.collection_name == self.collection.PRODUCTS.value:
            self.products = self.get_products()

    def get_products(self):
        """
        Retrieves all products from the specified collection.

        Returns:
            list or None: A list of all products in the store, or None if no products are found.
        """
        url = f"{self.store_url}/admin/api/2023-04/{self.collection_name}.json"
        products = []
        try:
            response = self.get(url, headers=self.headers)
            if response.status_code == 200:
                products = response.json()['products']
                if len(products) > 0:
                    return products
                else:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def get_product(self, product_id):
        """
        Retrieves a specific product by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            dict or None: The retrieved product, or None if the product is not found.
        """
        url = f"{self.store_url}/admin/api/2023-04/{self.collection_name}/{product_id}.json"
        product = {}
        try:
            response = self.get(url, headers=self.headers)
            if response.status_code == 200:
                product = response.json()['product']
                if len(product) > 0:
                    return product
                else:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def extract_id_from_sku(self, target_sku):
        """
        Extracts the product ID from a given SKU.

        Args:
            target_sku (str): The SKU from which to extract the product ID.

        Returns:
            int or None: The extracted product ID, or None if the SKU is not found.
        """
        url = f"{self.store_url}/admin/api/2023-04/products.json"
        target_sku = str(target_sku)
        try:
            products = self.products
            for product in products:
                for variant in product["variants"]:
                    if variant["sku"] == target_sku:
                        product_id = product["id"]
                        break
            if product_id:
                return product_id
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def update_product(self, product_id, data):
        """
        Updates a specific product with the given data.

        Args:
            product_id (str): The ID of the product to update.
            data (dict): The data to update the product with.

        Returns:
            None
        """
        url = f"{self.store_url}/admin/api/2023-04/products/{product_id}.json"
        try:
            response = requests.put(url, json=data, headers=self.headers)
            if response.status_code == 200:
                print("Product updated successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def create_webhook(self, webhook_url):
        """
        Creates a webhook for the specified topic and URL.

        Args:
            webhook_url (str): The URL to receive webhook notifications.

        Returns:
            None
        """
        url = f"{self.store_url}/admin/api/2023-04/webhooks.json"
        try:
            data = {
                "webhook": {
                    "topic": "orders/create",
                    "address": webhook_url,
                    "format": "json"
                }
            }
            response = requests.post(url, json=data, headers=self.headers)
            if response.status_code == 200:
                print("Webhook created successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
