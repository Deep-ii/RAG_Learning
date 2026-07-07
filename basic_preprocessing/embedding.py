from sentence_transformers import SentenceTransformer
import requests
import os
import numpy as np
from chunking_processes import chunking_overlapping

url = "https://raw.githubusercontent.com/progit/progit2/main/book/01-introduction/sections/what-is-git.asc"
source_text = requests.get(url).text
print(len(source_text))



model = SentenceTransformer('all-MiniLM-L6-v2')


dataset = chunking_overlapping(source_text,250,0.2)

embedding = model.encode(dataset)


np.save('embedding.npy', embedding)

