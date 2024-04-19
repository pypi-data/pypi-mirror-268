from pydantic import BaseModel, Field, model_validator
from typing import Optional, Generic, TypeVar, Union

T = TypeVar("T", bound=Union[BaseModel, object])


class ServiceResponse(BaseModel, Generic[T]):
    response_node_id: Optional[str] = Field("unknown")
    response_node_version: Optional[str] = Field("unknown")
    request_error: bool = Field(False, description="Error in request")
    server_error: bool = Field(False, description="Error in server")
    request_error_message: Optional[str] = Field(None, description="Error Message")
    response_data: Optional[T] = Field(None, description="Response Data")

    def set_error(self, **kwargs):
        """
        Set error in response
        :param kwargs: server_error, request_error, message
        :return:
        """
        if kwargs.get('server_error', False) and kwargs.get('request_error', False):
            raise ValueError("Both server_error and request_error cannot be True")
        self.server_error = kwargs.get('server_error', False)
        self.request_error = kwargs.get('request_error', False)
        self.request_error_message = kwargs.get('message', None)

    @model_validator(mode='after')
    def check_state(self):
        """
        Check if response data is None if request error is True
        :return:
        """
        if self.request_error and self.response_data:
            raise ValueError("Response data should be None if request error is True")
        return self
