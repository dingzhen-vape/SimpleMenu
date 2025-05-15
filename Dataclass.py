from dataclasses import dataclass
@dataclass
class Option:
    Value:str|int
    func:any # type: ignore