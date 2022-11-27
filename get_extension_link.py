import os.path
from urllib.parse import urlparse, unquote




def get_extension_link(link):
    link_unquote = unquote(link)
    parsed_link = urlparse(link_unquote)
    link_path = parsed_link.path
    path, fullname = os.path.split(link_path)
    filename, expansion = os.path.splitext(fullname)
    return filename, expansion


"""
def main():
    get_extension_link(link)





if __name__ == "__main__":
    main()
"""

