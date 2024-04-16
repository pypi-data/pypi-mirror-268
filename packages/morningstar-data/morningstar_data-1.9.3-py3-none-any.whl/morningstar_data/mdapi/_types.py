from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class TaskStatus(str, Enum):
    SUCCESS = "success"
    PENDING = "pending"
    FAILURE = "failure"


@dataclass
class TaskResult:
    dataframe_file_url: str
    columns_with_list_values: List[str] = field(default_factory=list)


@dataclass
class MdapiTask:
    id: str
    # TODO: Add request_id
    poll_url: str
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[TaskResult] = None
    error_class: Optional[str] = None
    error_message: Optional[str] = None
    next_poll_delay_milliseconds: int = 1000

    def is_complete(self) -> bool:
        return self.status != TaskStatus.PENDING

    def is_successful(self) -> bool:
        return self.status == TaskStatus.SUCCESS

    def failed(self) -> bool:
        return self.status == TaskStatus.FAILURE

    def __post_init__(self) -> None:
        if isinstance(self.result, dict):
            # This is initted from a API response json object with MdapiTask(**response.json()), so the initial
            # init will be called with a dict, even though we are specifying a TaskResult. Tell mypy to not warn about this.
            self.result = TaskResult(**self.result)  # type: ignore


@dataclass
class RequestObject:
    pass
