# Rust Filesystem




```python
import pandas as pd
from rustfs import RustS3FileSystem

df = pd.DataFrame({"name": ["Tom", "Joseph"], "age": [20, 22]})
df.to_parquet("s3://my-s3-bucket/df.parquet", storage_options={"access_key_id": "minio", "secret_access_key":"miniostorage", "endpoint": "http://localhost:30002"})


rfs = RustS3FileSystem(access_key_id="minio", secret_access_key="miniostorage", endpoint="http://localhost:30002", allow_http=True)
```


Questions:
- Can I call super (basically make RustFS a subclass and then call the parent)
