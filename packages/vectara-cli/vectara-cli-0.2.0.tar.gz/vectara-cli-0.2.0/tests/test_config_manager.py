# tests/test_config_manager.py

from vectara_cli.utils.config_manager import ConfigManager
import os
from unittest.mock import patch
import pytest


@pytest.fixture(autouse=True)
def fresh_env():
    old_env = dict(os.environ)
    os.environ.clear()
    yield
    os.environ.update(old_env) 

class TestConfigManagerEffect:
    @patch.dict(os.environ, {}, clear=True)
    def test_set_and_get_api_keys_effect(self, fresh_env):
        """Test setting and then getting API keys reflects the expected changes in environment variables."""
        customer_id = "test_customer_id"
        api_key = "test_api_key"
        ConfigManager.set_api_keys(customer_id, api_key)

        assert os.environ.get('VECTARA_CUSTOMER_ID') == customer_id
        assert os.environ.get('VECTARA_API_KEY') == api_key

        retrieved_customer_id, retrieved_api_key = ConfigManager.get_api_keys()
        assert retrieved_customer_id == customer_id
        assert retrieved_api_key == api_key