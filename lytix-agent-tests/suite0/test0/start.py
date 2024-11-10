import asyncio
import json


async def start():
    """
    Start the test and print the results to the console
    """
    toReturn = {
        "output": "Output of your model",
        "messages": [
            {
                "id": 1,
                "content": "Some query here?",
                "role": "user",
            }
        ],
        "sources": ["/sources/used/here"],
    }
    # Make sure to ONLY print the json
    print(json.dumps(toReturn))


if __name__ == "__main__":
    asyncio.run(start())
