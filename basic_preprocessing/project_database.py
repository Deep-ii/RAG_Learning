#in this we are using weaviate vectorDatabase
import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Configure
import os
import numpy as np
from chunking_processes import overlaping_chunking

embeddings = np.load('embedding.npy')

# It's best to set these as environment variables rather than hardcoding
weaviate_url = ""  # your endpoint
weaviate_api_key = ""

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=weaviate_url,
    auth_credentials=Auth.api_key(weaviate_api_key),
)

print(client.is_ready())  # should print True

'''
client.collections.create(
    name = 'git_Tutorial',
    properties=[
        Property(name='chunk_id',data_type = DataType.INT),
        Property(name='Contect',data_type = DataType.TEXT),
        Property(name='word_count',data_type = DataType.INT),
        Property(name='source',data_type = DataType.TEXT),
    ],
    vectorizer_config=Configure.Vectorizer.none()
)'''

collection = client.collections.get('git_Tutorial')

with collection.batch.dynamic() as batch:
    for idx , text in enumerate(overlaping_chunking,start=1):
        vector = embeddings[idx - 1]
        batch.add_object(
            properties={
                "chunk_id":idx,
                "Content":text,
                "word_count":len(text.split()),
                "source":"git_Tutorial",
            },
            vector=vector.tolist(),
        )

if len(collection.batch.failed_objects) > 0:
    print(collection.batch.failed_objects[0])
else:
    print("Inserted Successfully")


print(client.close())





