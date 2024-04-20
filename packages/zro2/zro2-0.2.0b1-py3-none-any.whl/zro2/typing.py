from typing import TypedDict, get_overloads
import inspect
import typing

def get_overload_signatures(func):
    overloads = get_overloads(func)
    for overloadFunc in overloads:
        yield inspect.signature(overloadFunc)

def bind_overload(overloadFunc, *args, **kwargs):
    for sig in get_overload_signatures(overloadFunc):
        try:
            return sig.bind(*args, **kwargs).arguments
        except TypeError:
            pass

# Github release typeddict
class GithubAsset(TypedDict):
    url: str
    id: int
    node_id: str
    name: str
    label: str
    content_type: str
    state: str
    size: int
    download_count: int
    browser_download_url: str

class GithubRelease(TypedDict):
    url: str
    assets_url: str
    upload_url: str
    html_url: str
    id: int
    node_id: str
    tag_name: str
    target_commitish: str
    name: str
    draft: bool
    prerelease: bool
    assets: typing.List[GithubAsset]
    tarball_url: str
    zipball_url: str
    body: str