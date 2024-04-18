from bson.objectid import ObjectId
from pydantic import BaseModel
from pymongo.results import InsertOneResult
import pytest
from tokka import Client
from tokka import Collection


@pytest.mark.asyncio(scope="session")
async def test_insert_one(
    collection: Collection, client: Client, user_1: BaseModel
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            result = await collection.insert_one(user_1, session=session)
            assert isinstance(result, InsertOneResult) == True
            assert ObjectId().is_valid(result.inserted_id) == True
            await session.abort_transaction()


@pytest.mark.asyncio(scope="session")
async def test_find_one(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            found = await collection.find_one(user_1, hide={"_id"}, session=session)
            assert user_1.model_dump() == found
            await session.abort_transaction()


@pytest.mark.asyncio(scope="session")
async def test_find_one_and_replace(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
    user_2: BaseModel
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            found = await collection.find_one_and_replace(
                user_1, user_2, session=session, hide={"_id"}
            )
            assert user_2.model_dump() == found
            await session.abort_transaction()

@pytest.mark.asyncio(scope="session")
async def test_find_one_and_delete(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            found = await collection.find_one_and_delete(
                user_1, hide={"_id"}, session=session
            )
            assert user_1.model_dump() == found
            await session.abort_transaction()

@pytest.mark.asyncio(scope="session")
async def test_find_one_and_update(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
    user_1_update: BaseModel
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            found = await collection.find_one_and_update(
                user_1, {"$set": {"name": "John Doe"}}, session=session, hide={"_id"}
            )
            assert user_1_update.model_dump() == found
            await session.abort_transaction()

@pytest.mark.asyncio(scope="session")
async def test_find_one_and_set(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
    user_1_update: BaseModel
) -> None: 
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            found = await collection.find_one_and_set(
                user_1, {"name": "John Doe"}, session=session, hide={"_id"}
            )
            assert user_1_update.model_dump() == found
            await session.abort_transaction()

@pytest.mark.asyncio(scope="session")
async def test_replace_one(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
    user_2: BaseModel
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            result = await collection.replace_one(
                user_1, user_2, session=session
            )
            assert result.modified_count == 1
            await session.abort_transaction()

@pytest.mark.asyncio(scope="session")
async def test_set(
    client: Client,
    collection: Collection,
    user_1: BaseModel,
) -> None:
    async with await client.motor.start_session() as session:
        async with session.start_transaction():
            await collection.insert_one(user_1, session=session)
            result = await collection.set(
                user_1, {"name": "John Doe"}, session=session
            )
            assert result.modified_count == 1
            await session.abort_transaction()
