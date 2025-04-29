from astrapy.db import AstraDB

# initialize client
db = AstraDB(token="AstraCS:heLjPGrTBYDokfNjaGAqlygv:16bf8857f087526227c0f4cd112fb07a1e2d4b2a4c1698ed721e29c77da465c6",
             api_endpoint="https://3a3417ce-54d5-48b4-a46c-946bef8e06d7-us-east-1.apps.astra.datastax.com",
             namespace=None)
# {
#   "clientId": "mgDcgPridsqvWQqpIkPCKLmM",
#   "secret": "I3XPD,4eAW2QTk.kioi.uoJRMaE8eY+LcCRSOKonFcCW6aX1S17_iYzR,pe8GhK8KE9AsM1U.-hdwdpy4K4e_nHpkqNmWNHAijvBuc.69hsBZLo3tNWZcWNaxpK5EmrU",
#   "token": "AstraCS:mgDcgPridsqvWQqpIkPCKLmM:abac1027070a1e73976e8e607bbfd79971315c259e0e40723eb416ea638e6d30"
# }

# test connection
print(f"Connected to Astra DB: {db.get_collections()}")

# create collection
# collection = db.create_collection("test2", dimension=4, metric="cosine")
# print(collection)
collection = db.collection("test1")

# insert documents in collection
documents = [
    {
        "_id": "1",
        "text": "Hello World",
        "$vector": [0.1, 0.2, 0.34, 0.45],
    },
    {
        "_id": "2",
        "text": "astra db",
        "$vector": [0.05, 0.08, 0.3, 0.6],
    },
]
res = collection.insert_many(documents)
print(res)

update_result = collection.update_one({"_id": "1"}, {"$set": {"text": "New Text"}})

# perform similarity search
query = [0.15, 0.11, 0.12, 0.13]
results = collection.vector_find(query, limit=2, fields=["text", "$vector"])

for document in results:
    print(document)

res = db.delete_collection(collection_name="test2")
print(res)

# # Retrieve all collections and iterate over them
# collections_response = db.get_collections()
# for collection in collections_response["status"]["collections"]:
#     print(collection)

results = collection.find({
    "text": "astra db",
})
# Delete a single document by its ID from the collection
deleted_doc = collection.delete_one(id="1")

results = collection.find(
    {"product_price": 9.99},
    sort={"$vector": [1, 0, 1, 1]}
)

# If a document with the same ID exists, it is updated; otherwise, a new document is created.
upsert= collection.upsert(
    document={"_id": "id1", "product_name": "old product"}
)

# notes:
# Data Modeling:
# Can interact with data using two approaches. The first approach is to use REST API, GraphQL, and document apis using Stargate.io, an open source layer included in Astra DB. Second approach is directly in Cassandra Query Language in the CQL console.
#
# Clients (Data API-based) Namespace: Collection: Document: Field
# Drivers(CQL-based) Keyspace: Table: Row: Column

# Integrations?

# INSERT INTO electronic_vectors (product_id, product_name, product_vector)
# VALUES ('pi185','iPhone pro max charging cable',[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]);
# INSERT INTO electronic_vectors (product_id, product_name, product_vector)
# VALUES ('pi293','iPhone pro max charging case',[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]);
# INSERT INTO electronic_vectors (product_id, product_name, product_vector)
# VALUES ('pi012','Macbook pro case',[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]);
# INSERT INTO electronic_vectors (product_id, product_name, product_vector)
# VALUES ('pi011','Windows surface pro',[0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]);
# INSERT INTO electronic_vectors (product_id, product_name, product_vector)
# VALUES ('pi583','Windex Outdoor Windows cleaner',[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1]);