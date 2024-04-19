from typing import Optional
from functools import wraps

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from user_service.db.database import get_async_session
from user_service.db.models import User
from user_service.schemas import UserDTO


class UserService:
    @staticmethod
    def _with_session(func):
        """
        Decorator function to handle database session management for asynchronous methods.
        """
        @wraps(func)
        async def wrapper(*args, **kwargs):
            async with await get_async_session() as session:
                return await func(*args, session=session, **kwargs)
        return wrapper

    @_with_session
    async def get(
            self,
            user_id: int,
            session: AsyncSession
    ) -> Optional[UserDTO]:
        """
        Retrieves a user by their ID.

        Args:
            user_id (int): The unique identifier of the user to retrieve.
            session (AsyncSession):
        Returns:
            Optional[UserDTO]: A UserDTO object representing the retrieved user, or None if not found.

        Raises:
            Exception: If an unexpected error occurs during database interaction.
        """
        if not isinstance(user_id, int):
            raise TypeError("user_id must be an integer")

        if user_id <= 0:
            raise ValueError(f"user_id {user_id} must be biggest then 0")

        stmt = select(User).filter_by(id=user_id)
        user = await session.scalar(stmt)

        return UserDTO(**user.__dict__) if user else None

    @_with_session
    async def add(
            self,
            user_data: UserDTO,
            session: AsyncSession
    ) -> Optional[UserDTO]:
        """
        Adds a new user to the database.

        Args:
            user_data (UserDTO): A UserDTO object containing the data for the new user.
            session (AsyncSession)
        Returns:
            Optional[UserDTO]: A UserDTO object representing the newly created user, or None if an error occurs.

        Raises:
            Exception: If an unexpected error occurs during database interaction or data validation.
        """
        if not isinstance(user_data, UserDTO):
            raise TypeError(f"{user_data} is not UserDTO. Provide valid data.")

        try:
            new_user = User(**user_data.dict())
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return UserDTO(**new_user.__dict__)

        except Exception as error:
            await session.rollback()
            raise error
