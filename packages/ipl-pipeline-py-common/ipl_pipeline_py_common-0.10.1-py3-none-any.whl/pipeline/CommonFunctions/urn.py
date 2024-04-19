"""
Handles parsing of IPL URNs

example:
    urn:iplsplatoon:production:commentators:id:{id}
"""
from typing import List, Optional


class URN:
    urn: str
    ns: Optional[str]
    ns_specific: Optional[str]
    sub_component: Optional[str]
    id_provider: Optional[str]
    id_type: Optional[str]
    identifier: Optional[str]

    @staticmethod
    def get_from_index(input_list: List[str], i: int, default=None) -> Optional[str]:
        if len(input_list) < i:
            if default:
                return default
            raise IndexError
        if input_list[i]:
            return input_list[i]

    def __init__(self, urn: str):
        try:
            string_split = urn.split(':')
            if string_split[0] != "urn":
                raise ValueError('Invalid URN')
            self.ns = self.get_from_index(string_split, 1)
            self.ns_specific = self.get_from_index(string_split, 2)
            self.sub_component = self.get_from_index(string_split, 3)
            self.id_provider = self.get_from_index(string_split, 4)
            self.id_type = self.get_from_index(string_split, 5)
            self.identifier = self.get_from_index(string_split, 6)
            self.urn = urn
        except IndexError:
            raise ValueError('Invalid URN')
