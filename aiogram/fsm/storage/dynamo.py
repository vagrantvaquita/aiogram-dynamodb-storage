import aioboto3
from typing import Any, Dict, Optional, cast, AnyStr

from aiogram.fsm.state import State
from aiogram.fsm.storage.base import (
    BaseStorage,
    DefaultKeyBuilder,
    KeyBuilder,
    StateType,
    StorageKey,
)

class DynamoStorage(BaseStorage):
    ...
