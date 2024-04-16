#   Copyright (c) 2021 DeepEvolution Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import _io
import numpy
import gym
from numpy import random

class RandomRNN(object):
    def __init__(self, n_emb=16, n_hidden=64, n_vocab=256):
        self.n_emb = n_emb
        self.n_hidden = n_hidden
        self.n_vocab = n_vocab
        self.emb = numpy.random.normal(0, 1.0, shape=(self.V, self.n))
        self.W_i = numpy.random.normal(0, 1.0, shape=(self.n, self.N))
        self.W_h = numpy.random.normal(0, 1.0, shape=(self.N, self.N))
        self.b_h = numpy.random.normal(0, 1.0, shape=(self.N))
        self.W_o = numpy.random.normal(0, 1.0, shape=(self.N, self.V))
        self.b_o = numpy.random.normal(0, 1.0, shape=(self.V))

    def forward(self, l, batch):
        ind = 0
        s_tok = numpy.random.randint(0, n_vocab, size=(batch,))
        h = numpy.zeros((batch, self.n_hidden))
        seqs = []
        while ind < l:
            ind += 1
            i = self.emb[s_tok]
            h = numpy.tanh(numpy.matmul(i, self.W_i) + numpy.matmul(h, self.W_h) + self.b_h)
            o = numpy.softmax(numpy.matmul(h, self.W_o) + self.b_o)
            cum_prob = np.cumsum(o, axis=-1) # shape (batch,)
            r = np.random.uniform(size=(batch, 1))

            # argmax finds the index of the first True value in the last axis.
            s_tok = np.argmax(cum_prob > r, axis=-1)
            seqs.append(s_tok)
        return numpy.asarray(seqs, dtype="int32")

class MetaLM2(gym.Env):
    """
    Pseudo Langauge Generated from RNN models
    V: vocabulary size
    n: embedding size (input size)
    N: hidden size
    L: maximum length
    """
    def __init__(self, 
            V=64, 
            n=4,
            N=4
            L=4096):
        self.L = int(L)
        self.V = int(V)
        self.n = n
        self.N = N
        assert n > 1 and V > 1 and N > 1 and L > 1 

    def data_generator(self):
        nn = RandomRNN(n_emb = self.n, n_hidden = self.N, n_vocab = self.V)
        return nn.forward(self.L, 1)[0]

    def batch_generator(self, batch_size):
        nn = RandomRNN(n_emb = self.n, n_hidden = self.N, n_vocab = self.V)
        return nn.forward(self.L, batch_size)

    def generate_to_file(self, size, output_stream):
        sequences = self.batch_generator(size)
        if(isinstance(output_stream, _io.TextIOWrapper)):
            need_close = False
        elif(isinstance(output_stream, str)):
            output_stream = open(output_stream, "w")
            need_close = True
        for i in range(sequences.shape[0]):
            output_stream.write("\t".join(map(lambda x: str(x), sequences[i].tolist()))
            output_stream.write("\n")
        if(need_close):
            output_stream.close()
