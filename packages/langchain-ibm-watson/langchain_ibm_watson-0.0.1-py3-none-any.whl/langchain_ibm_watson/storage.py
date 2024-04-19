from langchain_core.documents import Document
from langchain_core.stores import BaseStore


class WatsonDiscoveryStore(BaseStore[str, Document]):
    """IBM Watson Discovery store.

    References:
        [1] https://www.ibm.com/products/watson-discovery
        [2] https://cloud.ibm.com/apidocs/discovery-data?code=python
    """

    pass
