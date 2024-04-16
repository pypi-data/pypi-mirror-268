from minio import Minio
from minio.error import S3Error
import io

def main():
    # Create a client with the MinIO server running in Docker
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    bucket_name = "new-bucket"
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
    except S3Error:
        pass

    objects = client.list_objects(bucket_name, recursive=True)
    for obj in objects:
        # Remove each object
        client.remove_object(bucket_name, obj.object_name)
        print(f"Removed {obj.object_name}")

    objects = client.list_objects(bucket_name)
    assert len(list(objects)) == 0

    client.put_object(bucket_name, "a/b/c/object1", data=io.BytesIO(b"object1 data"), length=12)
    client.put_object(bucket_name, "a/b/object2", data=io.BytesIO(b"object2 data"), length=12)
    client.put_object(bucket_name, "a/object3", data=io.BytesIO(b"object3 data"), length=12)
    client.put_object(bucket_name, "object4", data=io.BytesIO(b"object4 data"), length=12)

    # Test recursive listing
    objects_recursive = client.list_objects(bucket_name, prefix="a/", recursive=True)
    
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

    print(objects_non_recursive)

    # Test listing at the bucket root
    objects_root = client.list_objects(bucket_name, recursive=False)
    print(objects_root)
    assert len(objects_root) == 2, "Expected 2 objects at the root"
    # Check that the correct paths are returned
    assert set(obj.object_name for obj in objects_root) == {"a/", "object4"}
    

if __name__ == "__main__":
    main()