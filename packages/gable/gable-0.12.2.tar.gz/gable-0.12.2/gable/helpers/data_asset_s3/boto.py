from botocore.exceptions import ClientError


def discover_patterns_from_s3_bucket(client, bucket_name: str) -> list[str]:
    """
    Discover patterns in an S3 bucket.

    Args:
        bucket (str): S3 bucket.

    Returns:
        list[str]: List of patterns.
    """
    files = [file["Key"] for file in _list_files(client, bucket_name)]
    return _discover_patterns_from_filepaths(files)


def discover_filepaths_from_patterns(
    client, bucket_name: str, patterns: list[str]
) -> list[str]:
    """
    Discover filepaths in an S3 bucket from patterns.

    Args:
        bucket_name (str): S3 bucket.
        patterns (list[str]): List of patterns.

    Returns:
        list[str]: List of filepaths.
    """
    files = [file["Key"] for file in _list_files(client, bucket_name)]
    return _discover_filepaths_from_patterns(patterns, files)


def _discover_filepaths_from_patterns(
    patterns: list[str], all_filepaths: list[str]
) -> list[str]:
    """
    Discover filepaths from DARN patterns.

    Args:
        patterns (list[str]): List of DARN patterns.
        all_filepaths (list[str]): List of all filepaths.

    Returns:
        list[str]: List of filepaths.
    """
    return []


def _discover_patterns_from_filepaths(
    filepaths: list[str],
) -> list[str]:
    """
    Discover patterns in a list of filepaths.

    Args:
        filespaths (list[str]): List of filepaths.

    Returns:
        list[str]: List of patterns.
    """
    return []


def _list_files(client, bucket_name: str, prefix: str = "") -> list[dict]:
    """
    List objects in an S3 bucket.

    Args:
        bucket_name (str): S3 bucket.
        prefix (str, optional): Prefix. Defaults to None.
    Returns:
        dict[str, object]: mapping of file names to contents.
    """
    _validate_bucket_exists(client, bucket_name)

    paginator = client.get_paginator("list_objects_v2")
    files = []
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        if "Contents" in page:
            for obj in page["Contents"]:
                files.append(obj)
    return files


def _validate_bucket_exists(client, bucket_name: str) -> None:
    try:
        client.head_bucket(Bucket=bucket_name)
    except Exception as e:
        if isinstance(e, ClientError):
            error_code = int(e.response["Error"]["Code"])
            if error_code == 404:
                print(f"Bucket {bucket_name} does not exist.")
            elif error_code == 403:
                print(f"Access to bucket {bucket_name} is forbidden.")
        raise ValueError(f"Bucket {bucket_name} does not exist or is not accessible.")
