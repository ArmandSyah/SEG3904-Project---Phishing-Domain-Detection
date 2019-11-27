import json
import os
from urllib.parse import urlparse, parse_qs

from src.features.domainpart import DomainPart
from src.features.fileextensionpart import FileExtensionPart
from src.features.fragmentpart import FragmentPart
from src.features.pathpart import PathPart
from src.features.querypart import QueryPart
from src.features.urlpart import URLpart

base = os.path.abspath(os.path.join(__file__, "../../.."))


class URL:
    # is_legit set {-1: undetermined, 0: not legit (phish), 1: legit}
    def __init__(self, url: str, is_legit: int = -1):
        file_extension = os.path.join(
            base, 'Datasets\\processed\\file_probabilities.json')
        with open(file_extension, 'r', encoding="utf8") as probability_file:
            file_extension_probabilites = json.load(probability_file)
        parsed_url = urlparse(url.lower())
        self.url = URLpart(parsed_url)
        self.domain = DomainPart(parsed_url.netloc)
        self.path = PathPart(parsed_url.path)
        self.query = QueryPart(parse_qs(parsed_url.query), parsed_url.query)
        self.fragment = FragmentPart(parsed_url.fragment, len(url))
        self.file_extension = FileExtensionPart(
            parsed_url.path, len(url), file_extension_probabilites)
        self.is_legit = is_legit

    def to_json(self):
        url_features = {}
        for k, v in vars(self).items():
            if isinstance(v, int):
                url_features[k] = v
            else:
                for key, value in vars(v).items():
                    url_features[key] = value
        return url_features
