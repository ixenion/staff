import asyncio
import aiofiles
import toml

async def foo() -> str:
    try:
        async with aiofiles.open("file.toml", "r") as file:
            config = await file.read()
            config = toml.loads(config)
        # get parameter(s)
        result = config["parameter"]
        return str(result)
    except:
        return "???"
