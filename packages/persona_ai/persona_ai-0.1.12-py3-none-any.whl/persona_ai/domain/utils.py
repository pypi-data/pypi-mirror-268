from uuid import uuid4

import shortuuid


def create_id(prefix: str = "id") -> str:
    return "{}_{}".format(prefix, shortuuid.encode(uuid4()))
