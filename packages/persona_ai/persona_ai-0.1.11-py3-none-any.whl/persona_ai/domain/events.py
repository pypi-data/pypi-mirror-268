from pydantic import BaseModel


JOIN = "join"
"""Event to send to party when a new participant wants to joins."""

LEAVE = "leave"
"""Event to send to party when a participant leaves."""

ACCEPT = "accept"
"""Event to send to participant when a party accepts a join request."""

REJECT = "reject"
"""Event to send to participant when a party rejects a join request."""

PING = "ping"
"""Event to send to participant to check if it is alive."""

PONG = "pong"
"""Event to send to participant to reply to a ping."""

ITERATION = "iteration"
"""Event to send when a iteration occur."""

AGENT_STEP = "agent_step"
"""Event to send when agent step occur."""


class Event(BaseModel):
    sender_id: str
    type: str
    body: dict
    conversation_id: str | None = None
