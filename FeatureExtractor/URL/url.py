from urllib.parse import urlparse, parse_qs

from URL.URLComposition.domainpart import DomainPart
from URL.URLComposition.fileextensionpart import FileExtensionPart
from URL.URLComposition.fragmentpart import FragmentPart
from URL.URLComposition.pathpart import PathPart
from URL.URLComposition.querypart import QueryPart
from URL.URLComposition.urlpart import URLpart


class URL:
    def __init__(self, url: str):
        parsed_url = urlparse(url.lower())
        self.url = URLpart(parsed_url)
        self.domain = DomainPart(parsed_url.netloc)
        self.path = PathPart(parsed_url.path)
        self.query = QueryPart(parse_qs(parsed_url.query))
        self.fragment = FragmentPart(parsed_url.fragment, len(url))
        self.file_extension = FileExtensionPart(parsed_url.path, len(url))

    def to_json(self):
        return {k:vars(v) for k, v in vars(self).items()}
    
