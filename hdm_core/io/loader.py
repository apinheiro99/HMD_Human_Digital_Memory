class ImageLoader:
    def scan(self, root_dir: str):
        raise NotImplementedError()

    def load_batch(self, paths, batch_size: int = 128):
        raise NotImplementedError()
