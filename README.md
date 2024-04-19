## Installation

Python3 must be already installed

```shell

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

create .env based on .env.sample

alembic upgrade head

```
*You don't need to make changes to alembic.ini; the changes have been made in env.py. PostgreSQL database is being used.

# №1 HashMap
## Description
### The HashMap class provides a basic implementation of a hash map data structure with the following functionality:

* Initialization: Creates a hash map with an initial size of 8.
* Length: Returns the number of key-value pairs in the hash map.
* Get: Retrieves the value associated with a given key.
* Put: Associates a value with a given key.

## Implementation Details
* __init__(): Initializes the hash map with a load factor of 0 and an initial capacity of 8.
* __len__(): Returns the current number of key-value pairs in the hash map.
* get(key: Hashable) -> Optional[Any]: Retrieves the value associated with the specified key.
* put(key: Hashable, value: Any) -> None: Associates the specified value with the specified key in the hash map.

## Key Features
* Efficient hash table resizing: The hash map automatically resizes itself to maintain a load factor of less than 75%.
* Handling collisions: Implements open addressing with linear probing to handle collisions between hash values.
* Error handling: Raises a KeyError if an attempt is made to retrieve a value for a non-existent key.

## Advantages
* Offers a simple and efficient implementation of a hash map data structure.
* Supports dynamic resizing to accommodate varying numbers of key-value pairs, optimizing memory usage and performance.
* Provides error handling to ensure robustness when accessing or modifying key-value pairs.

# №2 User Service
## Functionality
### The UserService class provides methods for user operations:

* get: Retrieves a user by their ID.
* add: Adds a new user to the database.

## Description
* _with_session(func): Decorator function to handle database session management for asynchronous methods.

* get(user_id: int, session: AsyncSession) -> Optional[UserDTO]: Retrieves a user by their ID. Returns a UserDTO object representing the retrieved user, or None if not found. Raises an exception if an unexpected error occurs during database interaction.

* add(user_data: UserDTO, session: AsyncSession) -> Optional[UserDTO]: Adds a new user to the database. Accepts a UserDTO object containing the data for the new user. Returns a UserDTO object representing the newly created user, or None if an error occurs. Raises an exception if an unexpected error occurs during database interaction or data validation.

## Advantages
* Simplifies database session management for asynchronous methods using the _with_session decorator.
* Provides clear methods for user retrieval and addition, enhancing code readability and maintainability.