import aio_pika

from src.app.core.config import settings


class MessageBroker:
    def __init__(self, connection_url: str):
        """Message broker class."""
        self.connection_url = connection_url
        self.connection = None

    async def connect(self):
        self.connection = await aio_pika.connect_robust(self.connection_url)

    async def close(self):
        await self.connection.close()

    def get_channel(self):
        return self.connection.channel()


async def get_message_broker():
    broker = MessageBroker(connection_url=settings.con_rabbit)
    await broker.connect()
    try:
        yield broker
    finally:
        await broker.close()
