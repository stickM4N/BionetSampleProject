from types import NoneType

from application.dto.create_student_dto import CreateStudentDto
from application.requests.commands.core.base_command import BaseCommand
from domain.models.redis.student import Student


class CreateStudentCommand(BaseCommand):
    _result_type = NoneType

    def __init__(self, dto: CreateStudentDto):
        super().__init__()

        self.student = Student(
            dni=dto.dni,
            first_name=dto.first_name,
            middle_name=dto.middle_name,
            last_name=dto.last_name,
            age=dto.age
        )
