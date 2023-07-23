def join_url(base_url: str, relative_url: str) -> str:
    return "/".join([base_url.rstrip("/"), relative_url.lstrip("/")])


def get_url_resource_name(url: str) -> str:
    return url.split("/")[-1]
