import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, vectors, metas):
        self.index.add(np.array(vectors))
        self.metadata.extend(metas)

    def search(self, query_vec, k=5):
        D, I = self.index.search(np.array(query_vec), k)
        return [self.metadata[i] for i in I[0]]