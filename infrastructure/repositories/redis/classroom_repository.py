from domain.models.redis.classroom import Classroom
from infrastructure.repositories.core.redis_repository import RedisRepository


class ClassroomRepository(RedisRepository):
    _model_type = Classroom
