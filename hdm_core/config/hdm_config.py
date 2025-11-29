import tomllib
from typing import Set
from hdm_core.constants.system_defaults import (
    DEFAULT_IMAGE_EXTENSIONS,
    DEFAULT_VIDEO_EXTENSIONS,
)

class HDMConfig:
    """
    HDM configuration manager.

    Loads and validates settings from hdm_config/hdm.toml.
    Ensures defaults and consistent structure for all modules.
    """

    def __init__(self, path: str = "hdm_config/hdm.toml"):
        self.path = path
        self.image_exts: Set[str] = set()
        self.video_exts: Set[str] = set()
        self.valid_exts: Set[str] = set()

        # Assign reusable system defaults
        self.DEFAULT_IMAGES = DEFAULT_IMAGE_EXTENSIONS
        self.DEFAULT_VIDEOS = DEFAULT_VIDEO_EXTENSIONS

        self.load()

    def load(self):
        """Load and validate the TOML config file."""

        # Attempt to open the config file defined in self.path
        try:
            with open(self.path, "rb") as f:
                config = tomllib.load(f)  # Parse the .toml file into a Python dictionary
        except FileNotFoundError:
            # Raise a more descriptive error if the file is missing
            raise FileNotFoundError(f"HDM config not found: {self.path}")

        # Check if the required [extensions] section exists
        if "extensions" not in config:
            raise ValueError("Missing [extensions] section in hdm.toml")

        # Extract the extensions section (image and video formats)
        ext_section = config["extensions"]

        # Load image extensions from config or fallback to system defaults
        self.image_exts = set(ext_section.get("image", []))
        if not self.image_exts:
            print("[HDMConfig] Missing image extensions. Using defaults.")
            self.image_exts = self.DEFAULT_IMAGES

        # Load video extensions from config or fallback to system defaults
        self.video_exts = set(ext_section.get("video", []))
        if not self.video_exts:
            print("[HDMConfig] Missing video extensions. Using defaults.")
            self.video_exts = self.DEFAULT_VIDEOS

    def reload(self):
        """Reload config (useful when modified by the Web UI)."""
        self.load()

    def as_dict(self):
        """Return the config as a plain dictionary (without derived values)."""
        return {
            "image_exts": sorted(self.image_exts),
            "video_exts": sorted(self.video_exts),
        }
