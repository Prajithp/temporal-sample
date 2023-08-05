# @@@SNIPSTART python-project-template-run-workflow
import asyncio
import os
import uuid

from run_worker import SayHello
from temporalio.client import Client


async def main():
    address = os.environ['TEMPORAL_ADDR']
    client = await Client.connect(address)

    # Execute a workflow
    result = await asyncio.gather( 
        *[
            client.execute_workflow(
                SayHello.run, "Temporals", id="{0}".format(uuid.uuid1()), task_queue="hello-task-queue"
            ) for x in range(100)
        ]
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
# @@@SNIPEND
