import importlib.metadata

try:
    __version__: str = importlib.metadata.version("toolforge_weld")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.0.0"
