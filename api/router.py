from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import Response

from application.dto.create_student_dto import CreateStudentDto
from application.request_handlers.commands.create_student_command_handler import CreateStudentCommandHandler
from application.request_handlers.core.base_request_handler import BaseRequestHandler
from application.requests.commands.create_student_command import CreateStudentCommand
from application.requests.core.base_request import BaseRequest
from infrastructure.repositories.redis.student_repository import StudentRepository

_repositories = {
    StudentRepository: StudentRepository(),
}

_request_handlers: dict[type[BaseRequest], BaseRequestHandler] = {
    CreateStudentCommand: CreateStudentCommandHandler(_repositories[StudentRepository]),
}

router = APIRouter(prefix='/students')


@router.post('/create')
async def create(student_dto: CreateStudentDto) -> Response:
    request = CreateStudentCommand(student_dto)

    await _request_handlers[CreateStudentCommand].handle(request)

    return Response(status_code=HTTPStatus.CREATED)
