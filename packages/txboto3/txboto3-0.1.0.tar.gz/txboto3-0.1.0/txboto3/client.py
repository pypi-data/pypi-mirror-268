import boto3
from twisted.internet.threads import deferToThread


def boto3_client_call(client_kwargs: dict, method: str, *args, **kwargs):
    client = boto3.client(**client_kwargs)
    result = getattr(client, method)(*args, **kwargs)
    return result


class MethodInterceptor:
    def __init__(self, method_name: str, client_kwargs: dict):
        self.method_name = method_name
        self.client_kwargs = client_kwargs

    def __call__(self, *args, **kwargs):
        return deferToThread(
            boto3_client_call, self.client_kwargs, self.method_name, *args, **kwargs
        )


class TXBoto3Client:
    def __init__(
        self,
        service_name,
        region_name=None,
        api_version=None,
        use_ssl=True,
        verify=None,
        endpoint_url=None,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        aws_session_token=None,
        config=None,
    ) -> None:
        self.client_kwargs = {
            "service_name": service_name,
            "region_name": region_name,
            "api_version": api_version,
            "use_ssl": use_ssl,
            "verify": verify,
            "endpoint_url": endpoint_url,
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "aws_session_token": aws_session_token,
            "config": config,
        }

    def __getattr__(self, name: str):
        return MethodInterceptor(name, self.client_kwargs)
