class ImageLoader:
    """
    HDM Core Module: ImageLoader

    Responsibilities:
    - Directory scanning and file validation
    - Batch preparation
    - Corruption detection
    - Lightweight metadata extraction (EXIF, path, size, etc.)
    """

    def scan(self, root_dir: str) -> List[str]:
        """
        Scan the directory recursively and collect all valid media file paths.
        To be implemented.
        """
        raise NotImplementedError()

    def load_batch(self, paths: List[str], batch_size: int = 128):
        """
        Yield batches of media files for processing.
        To be implemented.
        """
        raise NotImplementedError()
