class IndexEngine:
    def upsert(self, items):
        raise NotImplementedError()

    def search(self, vector, k=10):
        raise NotImplementedError()
