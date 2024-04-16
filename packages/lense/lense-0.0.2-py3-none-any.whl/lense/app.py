from lense._chat.loader import load_document
from lense._chat.engine import embed_and_run
import os
import pandas as pd
import pickle

class lense:
    def __init__(self):
        self._var = []
    
    def load_document(self,filename):
        self._var=  (load_document(filename))
        pickle.dump(self._var,open("result","wb"))
    
    def chat(self):
        var = pickle.load(open("result","rb"))
        embed_and_run(var)


