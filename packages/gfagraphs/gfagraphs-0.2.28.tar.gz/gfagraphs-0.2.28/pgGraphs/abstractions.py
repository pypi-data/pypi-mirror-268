"Abstractions over GFA formats"
from enum import Enum


class Orientation(Enum):
    "Describes the way a node is read"
    FORWARD = '+'
    REVERSE = '-'
    ANY = '?'
    BOTH = '='


class GFAFormat(Enum):
    "Describes the different possible gfa-like formats"
    RGFA = 'rGFA'
    GFA1 = 'GFA1'
    GFA1_1 = 'GFA1.1'
    GFA1_2 = 'GFA1.2'
    GFA2 = 'GFA2'
    ANY = 'unknown'


class GFALine(Enum):
    "Describes the different GFA line formats"
    SEGMENT = 'S'
    LINE = 'L'
    WALK = 'W'
    PATH = 'P'
    HEADER = 'H'
    ANY = '?'
