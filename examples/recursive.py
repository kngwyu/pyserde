from dataclasses import dataclass
from typing import Optional

from serde import from_dict, serde, to_dict


@dataclass
class Recur:
    f: Optional['Recur']


serde(Recur)


def main() -> None:
    f = Recur(Recur(Recur(None)))
    print(to_dict(f))
    print(from_dict(Recur, {'f': {'f': {'f': None}}}))


if __name__ == "__main__":
    main()
