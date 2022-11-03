import requests


def get_extension_link(link):
    link_unquote = unquote(link)
    parsed_link = urlparse(link_unquote)
    link_path = parsed_link.path
    path, fullname = os.path.split(link_path)
    filename, expansion = os.path.splitext(fullname)
    return filename, expansion


