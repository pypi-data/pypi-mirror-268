# TXBOTO3

A boto3 compatible Twisted Library. Run your AWS calls in a Deffered that runs the boto3 call in a separate thread, not blocking
Twisted.

Currently all clients are supported.

# Usage

We aim to be as close as possible to the boto3 interface.

```
import txboto3
from twisted.internet.defer import inlineCallbacks
from io import BytesIO

class MyResource:
    def __init__(self):
        self.s3_client = txboto3.client("s3")

    @inlineCallbacks
    def get_file(self):
        temp_buffer = BytesIO()
        yield self.s3_client.download_fileobj("my_bucket", "my_file", temp_buffer)
        return temp_buffer

    @inlineCallbacks
    def put_object(self, file_obj):
        yield self.s3_client.put_object(Bucket="my_bucket", Key="my_file", Body=file_obj.read())
```

# Stability

Unstable. Needs more testing and not reccomended for production use without proper testing. If you find
any bug please fill an issue in this repository.
