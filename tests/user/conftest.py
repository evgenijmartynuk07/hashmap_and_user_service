from unittest.mock import AsyncMock, MagicMock


async def mock_get_async_session():
    session = MagicMock()
    execute_result = AsyncMock()
    session.execute.return_value = execute_result
    return session
