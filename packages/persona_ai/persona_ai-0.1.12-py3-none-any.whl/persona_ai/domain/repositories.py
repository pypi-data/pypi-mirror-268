from persona_ai.domain.conversations import Conversation, Message
from persona_ai.domain.tasks import Task
from persona_ai.infrastructure.repositories.in_memory import InMemoryRepository
from persona_ai.infrastructure.repositories.mongo import MongoRepository


class MongoConversationsRepository(MongoRepository[Conversation]):
    def __init__(self):
        super().__init__("conversations", Conversation)


class InMemoryConversationsRepository(InMemoryRepository[Conversation]):
    def __init__(self):
        super().__init__(Conversation)


class MongoMessagesRepository(MongoRepository[Message]):
    def __init__(self):
        super().__init__("messages", Message)

        self.collection.create_index("conversation_id", unique=False)


class InMemoryMessagesRepository(InMemoryRepository[Message]):
    def __init__(self):
        super().__init__(Message)


class MongoTasksRepository(MongoRepository[Task]):
    def __init__(self):
        super().__init__("tasks", Task)

        self.collection.create_index("conversation_id", unique=False)


class InMemoryTasksRepository(InMemoryRepository[Task]):
    def __init__(self):
        super().__init__(Task)
