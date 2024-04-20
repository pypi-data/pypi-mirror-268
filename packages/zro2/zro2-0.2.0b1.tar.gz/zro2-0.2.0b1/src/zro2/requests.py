from typing import overload


def resolve_github_link():
    ...

@overload
def download_github_raw(url : str):
    ...

@overload
def download_github_raw(userOrOrg : str, repo : str, branch : str, filepath : str):
    ...

def download_github_raw(*args, **kwargs):
    ...


