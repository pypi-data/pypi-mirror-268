# vectara_cli/utils/config_manager.py

import os

ENV_FILE_PATH = '.env'

class ConfigManager:
    @staticmethod
    def set_api_keys(customer_id, api_key):
        """
        Sets the customer ID and API key in the .env file.
        """
        # Write directly to the .env file
        with open(ENV_FILE_PATH, 'w') as env_file:
            env_file.write(f"VECTARA_CUSTOMER_ID={customer_id}\n")
            env_file.write(f"VECTARA_API_KEY={api_key}\n")

        # Optionally, directly set them in the current environment as well
        os.environ['VECTARA_CUSTOMER_ID'] = customer_id
        os.environ['VECTARA_API_KEY'] = api_key

    @staticmethod
    def get_api_keys():
        """
        Retrieves the customer ID and API key from the .env file.
        """
        # Ensure that the .env file is loaded into the environment variables
        if os.path.exists(ENV_FILE_PATH):
            with open(ENV_FILE_PATH, 'r') as env_file:
                for line in env_file:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

        # Retrieve the values from environment variables
        customer_id = os.getenv('VECTARA_CUSTOMER_ID')
        api_key = os.getenv('VECTARA_API_KEY')

        if customer_id is None or api_key is None:
            raise ValueError(
                "API keys are not set in the environment. Please set them using the appropriate method."
            )
        return customer_id, api_key

    @staticmethod
    def are_api_keys_set():
        """
        Checks if the API keys are set in the environment variables.
        Returns True if both keys are set, False otherwise.
        """
        customer_id = os.getenv('VECTARA_CUSTOMER_ID')
        api_key = os.getenv('VECTARA_API_KEY')
        return customer_id is not None and api_key is not None
