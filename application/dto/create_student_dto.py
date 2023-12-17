from pydantic import BaseModel

from domain.models.redis.student import Student


class CreateStudentDto(BaseModel, Student):
    middle_name: str | None = None
