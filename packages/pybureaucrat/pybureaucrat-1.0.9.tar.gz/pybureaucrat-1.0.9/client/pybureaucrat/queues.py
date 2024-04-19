from typing import TypeVar
from .base import BaseHttpService, ServiceError
from .deserializers import raw_deserializer, default_deserializer\

T = TypeVar("T")

class QueueService(BaseHttpService):
    def __init__(self, baseUrl: str) -> None:
        super().__init__(baseUrl)

    async def queues(self) -> list[str]:
        return await self.get("queues/")
    
    async def dequeue(self, queue_name) -> str|None:
        data:str = await self.get(f"queues/{queue_name}", caster=raw_deserializer)
        return data if len(data) > 0 else None
    
    async def enqueue(self, queue_name, data:T):
        return await self.post(f"queues/{queue_name}", data, is_raw=True)
    
    async def delete_queue(self, queue_name) -> bool:
        try:
            await self.delete(f"queues/{queue_name}")
        except ServiceError as e:
            return False