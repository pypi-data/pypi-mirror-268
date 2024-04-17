# tests/test_LocalVectaraClient.py
import pytest
from vectara_cli.core import LocalVectaraClient

@pytest.mark.parametrize("attribute", ["api_key", "customer_id"])
def test_LocalVectaraClient_attributes(attribute):
    client = LocalVectaraClient()
    assert getattr(client, attribute) is not None and getattr(client, attribute) != ""
