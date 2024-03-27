import asyncio


async def delay(delay:float, error:bool) -> float:
    await asyncio.sleep(delay)
    if error:
        raise RuntimeError(f'Ups')
    return delay


async def main() -> None:
    
    pending = [
            asyncio.create_task(delay(1,False)),
            asyncio.create_task(delay(2,False)),
            asyncio.create_task(delay(3,True)),
            asyncio.create_task(delay(5,False)),
            asyncio.create_task(delay(6,False)),
            ]
    
    
    while pending:
        # done, pending = await asyncio.wait(pending, timeout=4, return_when=asyncio.FIRST_COMPLETED)
        done, pending = await asyncio.wait(pending, timeout=4)

        print(f'\nDone task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')
        
        # for task in done:
        #     try:
        #         result = await task
        #         print(f'Task_result: {result}')
        #     except:
        #         print(f'Exception:\n{task.exception()}')
        #         # for task in pending:
        #         #     task.cancel()

        for task in done:
            if task.exception() is not None:
                print(f'Exception:\n{task.exception()}')
                # Stop all other pending tasks
                # for task in pending:
                #     task.cancel()
                continue
            result = task.result()
            print(f'Task result:\n{result}')


    pass


asyncio.run(main())
