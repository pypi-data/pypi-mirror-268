from typing import TypeVar, Any
from .base import BaseHttpService, ServiceError

class TreeService(BaseHttpService):
    def __init__(self, baseUrl: str) -> None:
        super().__init__(baseUrl)

    async def get_forests(self) -> list[str]:
        return await self.get("trees/")

    async def get_trees(self, forest:str) -> list[str]:
        return await self.get(f"trees/{forest}")

    async def index(self, forest:str, tree:str, path:str = "$"):
        return await self.get(f"trees/{forest}/{tree}/index:{path}")

    async def get_value(self, forest:str, tree:str, path:str = "$"):
        return await self.get(f"trees/{forest}/{tree}/{path}")

    async def set_value(self, forest:str, tree:str, path:str, value):
        return await self.post(f"trees/{forest}/{tree}/{path}", value)

    async def remove_value(self, forest:str, tree:str, path:str):
        return await self.delete(f"trees/{forest}/{tree}/{path}")