from gensim.models import KeyedVectors
import sys
import io
import numpy as np


def load_vec(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    dict = {}
    i = 0
    for line in fin:
        i += 1
        tokens = line.rstrip().split(' ')
        dict[tokens[0]] = np.array([float(val) for val in tokens[1:]])
        # data[tokens[0]] /= np.linalg.norm(data[tokens[0]])
        # data[tokens[0]] = map(float, tokens[1:])
    return dict


# load_vec('/home/code/NLP/Word_to_Vector/wiki/wiki.vi.vec')
# load_vec('/home/code/NLP/Word_to_Vector/fasttext-vi/cc.vi.300.vec')


def change_data_2_vec():
    fname = '/home/code/NLP/Word_to_Vector/wiki/wiki.vi.vec'
    data = open('/home/code/NLP/Summary-Text/data.txt', 'r')
    dict = load_vec(fname)
    i = 0
    for line in data:
        if line in dict:
            print(line)

change_data_2_vec()
