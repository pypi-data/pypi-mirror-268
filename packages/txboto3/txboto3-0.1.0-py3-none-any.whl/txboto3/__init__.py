from .client import TXBoto3Client


def client(
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
) -> TXBoto3Client:
    return TXBoto3Client(
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
    )
