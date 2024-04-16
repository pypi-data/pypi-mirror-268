import sys

import pytest
import validators
from minio import Minio
from minio.error import S3Error


@pytest.mark.UNIT
@pytest.mark.API
def test_make_bucket(minio_mock):
    bucket_name = "test-bucket"
    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    assert client.bucket_exists(bucket_name), "Bucket should exist after creation"


@pytest.mark.UNIT
@pytest.mark.API
def test_adding_and_removing_objects(minio_mock):
    bucket_name = "test-bucket"
    object_name = "test-object"
    file_path = "tests/fixtures/maya.jpeg"

    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    client.make_bucket(bucket_name)
    client.fput_object(bucket_name, object_name, file_path)

    assert (
        object_name in client.buckets[bucket_name]
    ), "Object should be in the bucket after upload"
    client.remove_object(bucket_name, object_name)

    assert object_name not in client.buckets[bucket_name]


@pytest.mark.UNIT
@pytest.mark.API
def test_file_download(minio_mock):
    bucket_name = "test-bucket"
    object_name = "test-object"
    file_content = b"Test file content"
    length = sys.getsizeof(file_content)
    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    client.put_object(bucket_name, object_name, file_content, length)

    response = client.get_object(bucket_name, object_name)
    downloaded_content = response.data

    assert (
        downloaded_content == file_content
    ), "Downloaded content should match the original"


@pytest.mark.UNIT
@pytest.mark.API
def test_bucket_exists(minio_mock):
    bucket_name = "existing-bucket"
    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    assert client.bucket_exists(bucket_name), "Bucket should exist"


@pytest.mark.UNIT
@pytest.mark.API
def test_get_presigned_url(minio_mock):
    bucket_name = "test-bucket"
    object_name = "test-object"
    file_path = "tests/fixtures/maya.jpeg"

    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    client.make_bucket(bucket_name)
    client.fput_object(bucket_name, object_name, file_path)
    url = client.get_presigned_url("GET", bucket_name, object_name)
    assert validators.url(url)


@pytest.mark.UNIT
@pytest.mark.API
def test_presigned_put_url(minio_mock):
    bucket_name = "test-bucket"
    object_name = "test-object"
    file_path = "tests/fixtures/maya.jpeg"

    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    client.fput_object(bucket_name, object_name, file_path)
    url = client.presigned_put_object(bucket_name, object_name)
    assert validators.url(url)


@pytest.mark.UNIT
@pytest.mark.API
def test_presigned_get_url(minio_mock):
    bucket_name = "test-bucket"
    object_name = "test-object"
    file_path = "tests/fixtures/maya.jpeg"

    client = Minio("http://local.host:9000")
    client.make_bucket(bucket_name)
    client.fput_object(bucket_name, object_name, file_path)
    url = client.presigned_get_object(bucket_name, object_name)
    assert validators.url(url)


@pytest.mark.UNIT
@pytest.mark.API
def test_list_buckets(minio_mock):
    client = Minio("http://local.host:9000")
    buckets = client.list_buckets()
    n = len(buckets)
    bucket_name = "new-bucket"
    client.make_bucket(bucket_name)
    buckets = client.list_buckets()
    assert len(buckets) == n + 1


@pytest.mark.REGRESSION
@pytest.mark.UNIT
@pytest.mark.API
def test_list_objects(minio_mock):
    client = Minio("http://local.host:9000")

    with pytest.raises(S3Error):
        objects = client.list_objects("no-such-bucket")

    bucket_name = "new-bucket"
    client.make_bucket(bucket_name)
    objects = client.list_objects(bucket_name)
    assert len(list(objects)) == 0

    client.put_object(bucket_name, "a/b/c/object1", data=b"object1 data", length=12)
    client.put_object(bucket_name, "a/b/object2", data=b"object2 data", length=12)
    client.put_object(bucket_name, "a/object3", data=b"object3 data", length=11)
    client.put_object(bucket_name, "object4", data=b"object4 data", length=11)

    # Test recursive listing
    objects_recursive = client.list_objects(bucket_name, prefix="a/", recursive=True)
    # assert len(objects_recursive) == 3, "Expected 3 objects under 'a/' with recursion"
    # Check that all expected paths are returned
    assert set(obj.object_name for obj in objects_recursive) == {
        "a/b/c/object1",
        "a/b/object2",
        "a/object3",
    }

    # Test non-recursive listing
    objects_non_recursive = client.list_objects(
        bucket_name, prefix="a/", recursive=False
    )

    # Check that the correct path is returned
    assert set(obj.object_name for obj in objects_non_recursive) == {
        "a/object3",
        "a/b/",
    }

    # Test listing at the bucket root
    objects_root = client.list_objects(bucket_name, recursive=False)
    # Check that the correct paths are returned
    assert set(obj.object_name for obj in objects_root) == {"a/", "object4"}


@pytest.mark.REGRESSION
def test_connecting_to_the_same_endpoint(minio_mock):
    client_1 = Minio("http://local.host:9000")
    client_1_buckets = ["bucket-1", "bucket-2", "bucket-3"]
    for bucket in client_1_buckets:
        client_1.make_bucket(bucket)

    client_2 = Minio("http://local.host:9000")
    client_2_buckets = client_2.list_buckets()
    assert client_2_buckets == client_1_buckets
