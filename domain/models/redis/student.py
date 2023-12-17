from dataclasses import dataclass


@dataclass
class Student:
    dni: int
    first_name: str
    middle_name: str | None
    last_name: str
    age: int
