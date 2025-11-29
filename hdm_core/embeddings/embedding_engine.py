class EmbeddingEngine:
    def load_models(self):
        raise NotImplementedError()

    def embed(self, batch):
        raise NotImplementedError()
