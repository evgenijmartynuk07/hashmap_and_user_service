from unittest.mock import MagicMock

import pytest
from pydantic import ValidationError
from tests.user.conftest import mock_get_async_session
from user_service.services import UserService
from user_service.schemas import UserDTO


@pytest.mark.asyncio
@pytest.mark.parametrize("user_data", [
        {"id": 1, "first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@example.com"},
        {"id": 2, "first_name": "Bob", "last_name": "Smith", "email": "bob.smith@example.com"},
        {"id": 3, "first_name": "Charlie", "last_name": "Brown", "email": "charlie.brown@example.com"},
        {"id": 4, "first_name": "David", "last_name": "Miller", "email": "david.miller@example.com"},
        {"id": 5, "first_name": "Eva", "last_name": "Davis", "email": "eva_davis@example.com"},
])
async def test_add_user_with_correct_data(user_data):
    user_dto = UserDTO(**user_data)

    with pytest.MonkeyPatch().context() as m:
        m.setattr("user_service.services.get_async_session", mock_get_async_session)
        service = UserService()
        result = await service.add(user_dto)
        assert result == user_dto


@pytest.mark.asyncio
@pytest.mark.parametrize("user_data", [
    {"id": 1, "first_name": "Aaaa", "last_name": "Johnson", "email": ""},
    {"id": 2, "first_name": "", "last_name": "Smith", "emil": "bob.smith@example.com"},
    {"id": 3, "first_name": "Charlie", "last_name": "B", "email": "charlie@example.com"},
    {"id": 4, "first_nae": "Miller", "emai": "@david.miller@example.com"},
])
async def test_add_user_with_invalid_data(user_data):
    with pytest.raises(ValidationError):
        service = UserService()
        await service.add(UserDTO(**user_data))


@pytest.mark.asyncio
async def test_get_user():
    user_id = 5
    user_data = {"id": 5, "first_name": "Eva", "last_name": "Davis", "email": "eva_davis@example.com"}
    user_dto = UserDTO(**user_data)

    with pytest.MonkeyPatch().context() as m:
        m.setattr("user_service.services.get_async_session", mock_get_async_session)
        service = UserService()
        service.get = MagicMock(return_value=user_dto)

        result = service.get(user_id)
        service.get.assert_called_with(user_data["id"])

        assert result == user_dto


@pytest.mark.asyncio
@pytest.mark.parametrize("user_id", [
    "a", {}, [2, 3], {"s"}
])
async def test_get_user_raise_type_error(user_id):

    with pytest.MonkeyPatch().context() as m:
        m.setattr("user_service.services.get_async_session", mock_get_async_session)
        service = UserService()
        with pytest.raises(TypeError):
            await service.get(user_id)


@pytest.mark.asyncio
@pytest.mark.parametrize("user_id", [
    -5, -0, -10, 0
])
async def test_get_user_raise_value_error(user_id):

    with pytest.MonkeyPatch().context() as m:
        m.setattr("user_service.services.get_async_session", mock_get_async_session)
        service = UserService()
        with pytest.raises(ValueError):
            await service.get(user_id)



