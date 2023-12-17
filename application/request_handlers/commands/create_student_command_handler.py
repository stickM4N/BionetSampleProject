from application.request_handlers.core.base_request_handler import BaseRequestHandler
from application.requests.commands.create_student_command import CreateStudentCommand
from infrastructure.repositories.redis.student_repository import StudentRepository


class CreateStudentCommandHandler(BaseRequestHandler):
    _request_type = CreateStudentCommand

    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

        super().__init__()

    @BaseRequestHandler.validate_handle
    async def handle(self, request: CreateStudentCommand) -> None:
        student = request.student

        await self.student_repository.create(student)
