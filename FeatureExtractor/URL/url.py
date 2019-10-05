from urllib.parse import urlparse, parse_qs

from FeatureExtractor.URL.URLComposition.domainpart import DomainPart
from FeatureExtractor.URL.URLComposition.fileextensionpart import FileExtensionPart
from FeatureExtractor.URL.URLComposition.fragmentpart import FragmentPart
from FeatureExtractor.URL.URLComposition.pathpart import PathPart
from FeatureExtractor.URL.URLComposition.querypart import QueryPart
from FeatureExtractor.URL.URLComposition.urlpart import URLpart


class URL:
    def __init__(self, url):
        parsed_url = urlparse(url)
        self.url = URLpart(parsed_url)
        self.domain = DomainPart(parsed_url.netloc)
        self.path = PathPart(parsed_url.path)
        self.query = QueryPart(parse_qs(parsed_url))
        self.fragment = FragmentPart(parsed_url.fragment)
        self.file_extension = FileExtensionPart()