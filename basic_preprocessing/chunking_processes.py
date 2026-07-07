import requests


url = "https://raw.githubusercontent.com/progit/progit2/main/book/01-introduction/sections/what-is-git.asc"
source_text = requests.get(url).text


print(len(source_text))

#rint(source_text[0:500])  # Print the first 500 characters of the source text
'''

def get_chunks_fixed_size(text: str, chunk_size: int):
    text_words = text.split()

    chunk = []

    for i in range(0,len(text_words),chunk_size):

        chunk_words = text_words[i:i+chunk_size]

        chunks = " ".join(chunk_words)

        chunk.append(chunks)

    return chunk


fixed_size_chunk = get_chunks_fixed_size(source_text,200)

#print(fixed_size_chunk[0])
#print(f'\n{fixed_size_chunk[1]}')'''


# chunking process with overlapping 

def chunking_overlapping(text: str,chunk_size: int,over__lapping: float):

    word_text = text.split()
    
    over_lapping = int(chunk_size * over__lapping)

    chunk = []

    for i in range(0,len(word_text),chunk_size):

        chunk_wordss = word_text[max(i-over_lapping,0):i + chunk_size]

        chunks = ' '.join(chunk_wordss)

        chunk.append(chunks)

    return chunk


overlaping_chunking = chunking_overlapping(source_text,250,0.2)

for idx, c in enumerate(overlaping_chunking):
    print(f"Chunk {idx+1}: {len(c.split())} words")


