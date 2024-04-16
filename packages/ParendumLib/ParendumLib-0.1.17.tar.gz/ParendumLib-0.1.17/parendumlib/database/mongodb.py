import motor.motor_asyncio
from bson.objectid import ObjectId


class Mongo:

    def __init__(self, db_name: str, user: str = None, password: str = None, host: str = "127.0.0.1", port: int = 27017):
        if not user and not password:
            mongo_uri = f'mongodb://{host}:{port}/{db_name}?authSource=admin'
        else:
            mongo_uri = f'mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin'
        self.db_name = db_name
        self.client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)

    def collection(self, collection_name: str):
        return getattr(self.client, self.db_name).astra.get_collection(collection_name)

    @staticmethod
    def parse_helper(result) -> dict:
        result['_id'] = str(result['_id'])
        return dict(result)

    async def retrieve_all(self,
                           collection_name: str,
                           query: dict = None,
                           filter_fields: dict = None) -> list:
        results = []
        async for result in self.collection(collection_name).find(
                query, filter_fields):
            results.append(self.parse_helper(result))
        return results

    async def retrieve_last(self, collection_name: str, order_field: str) -> dict:
        result = await self.collection(collection_name).find_one(
            {}, sort=[(order_field, -1)]
        )
        if result:
            return self.parse_helper(result)

    async def retrieve_one(self, collection_name: str, id_obj: str) -> dict:
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            return self.parse_helper(result)

    async def add(self, collection_name: str, data: dict) -> dict:
        result = await self.collection(collection_name).insert_one(data)
        new_result = await self.collection(collection_name).find_one(
            {"_id": result.inserted_id})
        return self.parse_helper(new_result)

    async def update(self, collection_name: str, id_obj: str,
                     data: dict) -> bool:
        if len(data) < 1:
            return False
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            updated_result = await self.collection(collection_name).update_one(
                {"_id": ObjectId(id_obj)}, {"$set": data})
            if updated_result:
                return True
            return False

    async def delete(self, collection_name: str, id_obj: str) -> bool:
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            await self.collection(collection_name).delete_one(
                {"_id": ObjectId(id_obj)})
            return True

    async def create_index(self, collection_name: str, field_name: str, seconds: int = 60):
        await self.collection(collection_name).create_index(
            [(field_name, 1)],
            expireAfterSeconds=seconds
        )

    async def find_limit(self, collection_name: str, start: int = 1, limit: int = 10, query: dict = None):
        _logs = (await self.retrieve_all(collection_name, query))[::-1]
        _start_index = (start - 1) * limit
        _end_index = _start_index + limit
        return _logs[_start_index:_end_index]
