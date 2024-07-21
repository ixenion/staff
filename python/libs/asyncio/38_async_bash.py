import asyncio

async def foo() -> tuple[bool, str]:
    cmd = f"ls | grep '123'"
    proc = await asyncio.create_subprocess_shell(
            cmd,
            stderr=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            )
    stdout, stderr = [ val.decode("utf-8") for val in await proc.communicate() ]
    
    if not stderr:
        return True, stdout
    else:
        return False, stderr
