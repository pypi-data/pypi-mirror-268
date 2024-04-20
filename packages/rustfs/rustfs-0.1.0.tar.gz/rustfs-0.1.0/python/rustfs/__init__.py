import fsspec
from .rustfs import RustS3FileSystem


print("init rustfs")

fsspec.register_implementation(name="s3", cls=RustS3FileSystem, clobber=True)
