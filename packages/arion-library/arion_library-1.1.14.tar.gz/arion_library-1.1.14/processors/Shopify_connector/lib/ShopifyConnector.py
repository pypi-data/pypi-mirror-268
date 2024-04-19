import requests
from datetime import datetime
import logging
import multiprocessing 
import time
import pandas as pd
import json
from enum import Enum
import time
import shopify

logger= logging.getLogger(__name__)

class ShopifyConnector(requests.Session):

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
    """

    class collection(Enum):
        PRODUCTS = "products"

    def __init__(self, store_url, access_token, collection_name)->None:

        super().__init__()
        
        if collection_name not in [status.value for status in self.collection]:
            raise ValueError("Unknown collection: {}".format(collection_name))
        
        self.store_url = store_url
        self.access_token = access_token
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

        ## Condition on the collection name
        if self.collection_name == self.collection.PRODUCTS.value:
            self.products = self.get_products()

    def get_products(self)->list | None:

        url = f"{self.store_url}/admin/api/2023-04/{self.collection_name}.json"
        products = []
        try :
            response = self.get(url, headers=self.headers)
            if response.status_code == 200:
                products = response.json()['products']
                if len(products) > 0 :
                    return products
                else:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    
    def get_product(
            self,
            product_id:str
            )-> dict | None:

        url = f"{self.store_url}/admin/api/2023-04/{self.collection_name}/{product_id}.json"
        product = {}
        try :
            response = self.get(url, headers=self.headers)
            if response.status_code == 200:
                product = response.json()['product']
                if len(product) > 0 :
                    return product
                else:
                    return None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def run_task_in_parallel(
            task_func:list,
            data_list:list
            )-> tuple | float:
        
        
        num_processes = multiprocessing.cpu_count()
        start_time = time.time()
        with multiprocessing.Pool(processes=num_processes) as pool:
            results = pool.map(task_func, data_list)
        execution_time = time.time() - start_time
        return results, execution_time
    
    def location_mapping(
            file1_path:str,
            file2_path:str,
            on_field:str
            ):
        """
        Maps the locations from two CSV files based on a specified field.
        Args:
            file1_path (str): The path to the first CSV file.
            file2_path (str): The path to the second CSV file.
            on_field (str): The field to perform the inner join on.
        Returns:
            pandas.DataFrame: The merged DataFrame containing the mapped locations.
        Raises:
            Exception: If an error occurs during the mapping process.
        """
        try:
            # Load CSV files into pandas DataFrames
            df1 = pd.read_csv(file1_path)
            df2 = pd.read_csv(file2_path)
            
            # Perform inner join
            merged_df = pd.merge(df1, df2, how='inner', on=on_field)
            
            return merged_df
        
        except Exception as e:
            print("An error occurred:", e)
            return None


    def extract_id_from_sku(
            self,
            target_sku:str
            )-> int | None:
        """
        Extracts the product ID from a given SKU.
        Args:
            target_sku (str): The SKU of the product.
        Returns:
            int | None: The product ID if found, None otherwise.
        Raises:
            requests.exceptions.RequestException: If there is an error making the API request.
        """
        url = f"{self.store_url}/admin/api/2023-04/products.json"
        target_sku = str(target_sku)
        try :

            # response = requests.get(url, headers=self.headers)
            # product_id = None
            # products = response.json()
            products = self.products
            for product in products:
                for variant in product["variants"]:
                    if variant["sku"] == target_sku:
                        product_id = product["id"]
                        break
            if product_id:
                return product_id
            else:
                return  None

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            
    def update_product(
            self,
            product_id:str,
            data:dict
            )-> None:

        url = f"{self.store_url}/admin/api/2023-04/products/{product_id}.json"
        try :
            response = requests.put(url, json=data, headers=self.headers)
            if response.status_code == 200:
                print("Product updated successfully")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def create_webhook_using_rest(self ,
                                  event_name:str,
                                  callback_url:str
                                  )-> None:
        """
        Creates a webhook using the REST API.
        Args:
            event_name (str): The name of the event to subscribe to.
            callback_url (str): The URL to send the event data to.
        Returns:
            None
        """
        try:
            url = f"{self.store_url}/admin/api/2024-01/webhooks.json"
            payload = json.dumps({
            "webhook": {
                "address": callback_url,
                "topic": event_name
            }
            })
            response = requests.request("POST", url, headers=self.headers, data=payload)

            if response.status_code == 200 or response.status_code == 201 or response.status_code == 202:
                logging.info("Webhook created successfully")
                return response
            else:
                logging.error(f"Error: {response.text}")
                return response

        except requests.exceptions.RequestException as e:
            logging.error(f"Error: {e}")
