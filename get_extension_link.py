import os.path
from urllib.parse import urlparse, unquote




def get_file_format_link(link):
    link_unquote = unquote(link)
    parsed_link = urlparse(link_unquote)
    link_path = parsed_link.path
    path, fullname = os.path.split(link_path)
    filename, file_format = os.path.splitext(fullname)
    return filename, file_format
    
