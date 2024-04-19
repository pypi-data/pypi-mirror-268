from wkregister.producer import KafkaProducerWrapper, KafkaMessageSender
from wkregister.models import Records
from wkregister.util import kafkaParams
from typing import Callable, Any, Dict
from functools import wraps
import inspect
import asyncio
import json
import time


async def record2Kafka(org: str, key: str, value: Dict) -> None:
    producer_wrapper = KafkaProducerWrapper()
    # Crear el enviador de mensajes
    message_sender = KafkaMessageSender(producer_wrapper)
    # Enviar un mensaje
    topic = f"{org}_logs"
    key = f"{key}"
    value = json.dumps(value)
    await message_sender.send(topic, key, value)

    return None


# Decorator for logging
def record():
    def decorator_log(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            input = func(*args, **kwargs)

            if inspect.iscoroutine(input):
                result = await input
            else:
                result = input

            org, key, log = kafkaParams(result)

            start_time = time.time()  # Capture the start time

            # Log after function execution, you can adjust what you log as needed
            asyncio.create_task(record2Kafka(org, key, log.dict()))

            end_time = time.time()  # Capture the end time

            elapsed_time = end_time - start_time  # Calculate elapsed time
            # print(f"The function took {elapsed_time} seconds to complete.")

            output = {}
            for key, value in result.items():
                if not key == "record" or not key == "log":
                    output[key] = value
                if key == "record" or key == "log":
                    output[key] = log.dict()

            return output

        return wrapper

    return decorator_log
