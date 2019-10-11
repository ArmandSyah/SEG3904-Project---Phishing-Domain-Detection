from urllib.parse import urlparse, parse_qs

from .URLComposition.domainpart import DomainPart
from .URLComposition.fileextensionpart import FileExtensionPart
from .URLComposition.fragmentpart import FragmentPart
from .URLComposition.pathpart import PathPart
from .URLComposition.querypart import QueryPart
from .URLComposition.urlpart import URLpart

import inspect


class URL:
    # is_legit set {-1: undetermined, 0: not legit (phish), 1: legit}
    def __init__(self, url: str, is_legit: int):
        parsed_url = urlparse(url.lower())
        self.url = URLpart(parsed_url)
        self.domain = DomainPart(parsed_url.netloc)
        self.path = PathPart(parsed_url.path)
        self.query = QueryPart(parse_qs(parsed_url.query), parsed_url.query)
        self.fragment = FragmentPart(parsed_url.fragment, len(url))
        self.file_extension = FileExtensionPart(parsed_url.path, len(url))
        self.is_legit = is_legit if is_legit else -1

    def to_json(self):
        url_features = {}
        for k, v in vars(self).items():
            if isinstance(v, int):
                url_features[k] = v
            else:
                for key, value in vars(v).items():
                    url_features[key] = value
        return url_features
    
