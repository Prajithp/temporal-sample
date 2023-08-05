# @@@SNIPSTART python-project-template-run-worker
import asyncio
import os

from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

from activities import say_hello
from workflows import SayHello

async def main():
    address = os.environ['TEMPORAL_ADDR']
    namespace = os.environ['TEMPORAL_NAMESPACE']
    client = await Client.connect(address, namespace=namespace)

    # Run the worker
    worker = Worker(
        client, task_queue="hello-task-queue", workflows=[SayHello], activities=[say_hello]
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
