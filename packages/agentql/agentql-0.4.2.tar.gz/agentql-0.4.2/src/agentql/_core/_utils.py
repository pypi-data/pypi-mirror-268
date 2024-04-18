def ensure_url_scheme(url: str) -> str:
    """
    Ensure that the URL has a scheme.
    """
    if not url.startswith(("http://", "https://", "file://")):
        return "https://" + url
    return url


def minify_query(query: str) -> str:
    """
    Minify the query by removing all newlines and extra spaces.
    """
    return query.replace("\n", "\\").replace(" ", "")
