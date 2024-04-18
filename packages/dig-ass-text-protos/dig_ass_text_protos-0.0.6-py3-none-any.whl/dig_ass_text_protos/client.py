from dig_ass_text_protos.DigitalAssistantText_pb2_grpc import DigitalAssistantTextStub
from dig_ass_text_protos.DigitalAssistantText_pb2 import DigitalAssistantTextRequest, DigitalAssistantTextResponse, ChatItem, OuterContextItem, InnerContextItem, ReplicaItem

from .abstract_client import AbstractClient


class TextClient(AbstractClient):
    def __init__(self, address) -> None:
        super().__init__(address)
        self._stub = DigitalAssistantTextStub(self._channel)

    def __call__(self, text: str, chat: dict):
        outer_context = chat["OuterContext"]
        inner_context = chat["InnerContext"]
        request = DigitalAssistantTextRequest(
            Text=text,
            Chat=ChatItem(
                OuterContext=OuterContextItem(Sex=outer_context["Sex"], Age=outer_context["Age"], UserId=outer_context["UserId"], SessionId=outer_context["SessionId"]),
                InnerContext=InnerContextItem(Replicas=[self.__rep_to_obj(replica) for replica in inner_context["Replicas"]]),
            ),
        )
        response: DigitalAssistantTextResponse = self._stub.GetTextResponse(request)
        return response.Text

    def __rep_to_obj(self, replica_dict):
        return ReplicaItem(Body=replica_dict["Body"], Role=replica_dict["Role"], DateTime=replica_dict["DateTime"])
