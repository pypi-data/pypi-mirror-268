from twisted.trial import unittest
from twisted.internet.defer import inlineCallbacks
import txboto3  # Adjust the import according to your package structure
from dotenv import load_dotenv
import os
from uuid import uuid4

load_dotenv()


class TestClient(unittest.TestCase):

    @inlineCallbacks
    def test_s3_client(self):
        test_bucket_name = str(uuid4())
        test_key = str(uuid4())
        test_content = str(uuid4()).encode()

        s3_client = txboto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
            region_name="us-east-1",
        )

        # Test Create Bucket
        yield s3_client.create_bucket(Bucket=test_bucket_name)

        # Test List Buckets
        result = yield s3_client.list_buckets()
        buckets = [x.get("Name") for x in result.get("Buckets", [])]
        self.assertIn(test_bucket_name, buckets)
