from typing import TypeVar, Any
from .base import BaseHttpService, ServiceError

class TablesService(BaseHttpService):
    def __init__(self, baseUrl: str) -> None:
        super().__init__(baseUrl)

    async def get_databases(self) -> list[str]:
        return await self.get('tables/')
    
    async def get_tables(self, database:str) -> list[str]:
        return await self.get(f'tables/{database}')
    
    async def create_table(self, database:str, table:str, **fields) -> bool:
        fields = ', '.join([f'{field} {fields[field]}' for field in fields])
        query = f'create table {table} ({fields});'
        data = await self.post(f'tables/{database}', query, is_raw=True)
        if data is None:
            return False
        return True
    
    async def insert(self, database:str, table:str, **item):
        fields = ', '.join([i for i in item])
        values = ', '.join([(f"'{item[i]}'" if isinstance(item[i], str) else str(item[i])) for i in item])
        query = f'insert into {table} ({fields}) values ({values});'
        if await self.post(f'tables/{database}', query, is_raw=True) is None:
            return False
        return True
    
    async def insert_many(self, database:str, table:str, items:list[dict[str, Any]]):
        return [await self.insert(database, table, **item) for item in items]
    
    async def drop_table(self, database:str, table:str) -> bool:
        if await self.post(f'tables/{database}', f'drop table {table};', is_raw=True) is None:
            return False
        return True

    async def execute_query(self, database:str, query:str):
        return await self.post(f'tables/{database}', query, is_raw=True)
    
    async def get_rows(self, database:str, table:str, page_number:int = 0, page_size:int = 10):
        return await self.get(f'tables/{database}/{table}?page_number={page_number}&page_size={page_size}')