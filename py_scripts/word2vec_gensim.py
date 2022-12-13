from gensim.models import Word2Vec
import gensim.downloader as api
from gensim.test.utils import common_texts
import pandas as pd

a = Word2Vec(sentences=common_texts, vector_size=100, window=5, min_count=1, workers=4)
a.save('w2v.model')
#
b = Word2Vec.load('w2v.model')
# b.train([['hello', 'world']], total_examples=1, epochs=1)
# vec = b.wv['computer']
# sims = b.wv.most_similar('computer', topn=10)
vec_list = b.wv
vec = vec_list.load('/home/code/NLP/Word2Vector/Vec/w2v_vectors.vector')


# wv = Word2Vec.load('/home/code/NLP/Word2Vector/Vec/w2v_vectors.vector')
#
# for i, word in enumerate(wv.index_to_key):
#     if i == 10:
#         break
#     print(f"word #{i}/{len(wv.index_to_key)} is {word}")
