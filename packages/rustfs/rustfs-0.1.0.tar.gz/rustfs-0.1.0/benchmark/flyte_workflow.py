import os
import flytekit
from flytekit import task, workflow, FlyteContextManager, Resources, WorkflowFailurePolicy
from flytekit.types.file import FlyteFile


resource = Resources(cpu="3", mem="4096Mi")
directory = "/tmp/test"
DEFAULT_REMOTE_PATH = "s3://union-cloud-oc-staging-dogfood/test/file.txt"
RUSTFS_IMAGE = "ghcr.io/unionai-oss/flytekit-rustfs:latest"


def upload_file(size_mb: int) -> FlyteFile:
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, "file.txt")
    with open(file_path, "w") as f:
        for i in range(size_mb):
            f.write(str(os.urandom(1024 * 1024)))
    if flytekit.current_context().execution_id.domain == "local":
        remote_path = DEFAULT_REMOTE_PATH
    else:
        ctx = FlyteContextManager.current_context()
        remote_path = ctx.file_access.get_random_remote_path()
    print(f"uploading {file_path} to {remote_path}.")
    return FlyteFile(file_path, remote_path=remote_path)


def download_file(f: FlyteFile):
    f._downloader()


@task(requests=resource)
def upload_file_with_fsspec(size_mb: int) -> FlyteFile:
    return upload_file(size_mb=size_mb)


@task(requests=resource)
def download_file_with_fsspec(f: FlyteFile):
    download_file(f=f)


@task(container_image=RUSTFS_IMAGE, requests=resource)
def upload_file_with_rustfs(size_mb: int) -> FlyteFile:
    return upload_file(size_mb=size_mb)


@task(container_image=RUSTFS_IMAGE, requests=resource)
def download_file_with_rustfs(f: FlyteFile):
    download_file(f=f)


@workflow(failure_policy=WorkflowFailurePolicy.FAIL_AFTER_EXECUTABLE_NODES_COMPLETE)
def wf(size_mb: int = 3000):
    f1 = upload_file_with_fsspec(size_mb=size_mb)
    download_file_with_fsspec(f=f1)

    f2 = upload_file_with_rustfs(size_mb=size_mb)
    download_file_with_rustfs(f=f2)


if __name__ == "__main__":
    print(wf())
