from __future__ import annotations

from momotor.rpc.proto.resource_pb2 import Resource as ResourceMessage
from momotor.shared.resources import Resources


def resources_to_message(resources: Resources) -> list[ResourceMessage] | None:
    """ Convert a :py:class:`~momotor.shared.resources.Resources` object into
    a list of :py:class:`~momotor.rpc.proto.resource_pb2.Resource` messages

    :param resources: The resources
    :return: The message
    """
    return [
        ResourceMessage(name=name, value=value) for name, value in resources.as_str_tuples()
    ] if resources else None


def message_to_resources(resources: list[ResourceMessage] | None) -> Resources:
    """ Convert a list of :py:class:`~momotor.rpc.proto.resource_pb2.Resource` messages into
    a :py:class:`~momotor.shared.resources.Resources`

    :param resources: The resource messages
    :return: Resources object for the messages
    """
    return Resources.union(*(
        Resources.from_key_value(resource.name, resource.value) for resource in resources
    )) if resources else Resources()
