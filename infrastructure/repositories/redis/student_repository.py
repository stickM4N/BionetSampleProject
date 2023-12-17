from domain.models.redis.student import Student
from infrastructure.repositories.core.redis_repository import RedisRepository


class StudentRepository(RedisRepository):
    _model_type = Student
