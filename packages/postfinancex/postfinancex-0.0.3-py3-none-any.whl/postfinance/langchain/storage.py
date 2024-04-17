from typing import Iterator, List, Optional, Sequence, Tuple

from langchain_core.documents import Document
from langchain_core.stores import BaseStore


class MongoDBAtlasStore(BaseStore[str, Document]):
    """MongoDB Atlasas store.

    Examples:
        Create a MongoDBAtlasStore instance and perform operations on it:

        .. code-block:: python

            # Instantiate the MongoDBAtlasStore with a MongoDB Atlas connection
            from postfinance.storage import MongoDBAtlasStore

            uri = "mongodb+srv://yizhang:<password>@cluster0.uivjbbk.mongodb.net/?retryWrites=true&w=majority&appName=<appName>"
            store = MongoDBAtlasStore(
                uri,
                database_name="postfinance",
                collection_name="transcripts",
            )

            # Set values for keys
            doc1 = Document(...)
            doc2 = Document(...)
            store.mset([("key1", doc1), ("key2", doc2)])

            # Get values for keys
            values = store.mget(["key1", "key2"])
            # [doc1, doc2]

            # Iterate over keys
            for key in store.yield_keys():
                print(key)

            # Delete keys
            store.mdelete(["key1", "key2"])

    References:
        [1] https://api.python.langchain.com/en/latest/storage/langchain_community.storage.mongodb.MongoDBStore.html
        [2] https://github.com/mongodb-university/atlas_starter_python
    """


def __init__(
    self,
    uri: str,
    database_name: str,
    collection_name: str,
    *,
    client_kwargs: Optional[dict] = None,
) -> None:
    """Initialize the MongoDBAtlasStore with a MongoDB Atlas connection string.

    Args:
        uri (str): MongoDB Atlas connection string
        database_name (str): database name to use
        collection_name (str): collection name to use
        client_kwargs (dict): Keyword arguments to pass to the MongoDB client
    """
    try:
        from pymongo import MongoClient
        from pymongo.server_api import ServerApi
    except ImportError as e:
        raise ImportError(
            "The MongoDBAtlasStore requires the MongoDB Python Driver to be installed."
            "pip install pymongo[srv]"
        ) from e

    if not uri:
        raise ValueError("uri must be provided.")
    if not database_name:
        raise ValueError("database_name must be provided.")
    if not collection_name:
        raise ValueError("collection_name must be provided.")

    # Create a new client and connect to the server
    self.client = MongoClient(
        uri,
        server_api=ServerApi("1"),
        **(client_kwargs or {}),
    )

    # Send a ping to confirm a successful connection
    try:
        self.client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        raise e

    self.collection = self.client[database_name][collection_name]


def mget(self, keys: Sequence[str]) -> List[Optional[Document]]:
    """Get the list of documents associated with the given keys.

    Args:
        keys (list[str]): A list of keys representing Document IDs.

    Returns:
        list[Document]: A list of Documents corresponding to the provided
            keys, where each Document is either retrieved successfully or
            represented as None if not found.
    """
    result = self.collection.find({"_id": {"$in": keys}})
    result_dict = {doc["_id"]: Document(**doc["value"]) for doc in result}
    return [result_dict.get(key) for key in keys]


def mset(self, key_value_pairs: Sequence[Tuple[str, Document]]) -> None:
    """Set the given key-value pairs.

    Args:
        key_value_pairs (list[tuple[str, Document]]): A list of id-document pairs.
    Returns:
        None
    """
    from pymongo import UpdateOne

    updates = [{"_id": k, "value": v.__dict__} for k, v in key_value_pairs]
    self.collection.bulk_write(
        [
            UpdateOne({"_id": u["_id"]}, {"$set": u}, upsert=True)
            for u in updates
        ]
    )


def mdelete(self, keys: Sequence[str]) -> None:
    """Delete the given ids.

    Args:
        keys (list[str]): A list of keys representing Document IDs.
    """
    self.collection.delete_many({"_id": {"$in": keys}})


def yield_keys(self, prefix: Optional[str] = None) -> Iterator[str]:
    """Yield keys in the store.

    Args:
        prefix (str): prefix of keys to retrieve.
    """
    if prefix is None:
        for doc in self.collection.find(projection=["_id"]):
            yield doc["_id"]
    else:
        for doc in self.collection.find(
            {"_id": {"$regex": f"^{prefix}"}}, projection=["_id"]
        ):
            yield doc["_id"]
