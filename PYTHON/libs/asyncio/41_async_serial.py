import asyncio
import aioserial


PORT = "/dev/ttyUSB0"

socket = aioserial.AioSerial(port=PORT)

# READ_ASYNC
bytes_read: bytes = \
    await aioserial_instance.read_async(size: int = 1)

# READ_UNTIL_ASYNC
at_most_certain_size_of_bytes_read: bytes = \
    await aioserial_instance.read_until_async(
        expected: bytes = aioserial.LF, size: Optional[int] = None)

# READINTO_ASYNC
number_of_byte_read: int = \
    await aioserial_instance.readinto_async(b: Union[array.array, bytearray])

# READLINE_ASYNC
a_line_of_at_most_certain_size_of_bytes_read: bytes = \
    await aioserial_instance.readline_async(size: int = -1)

# READLINES_ASYNC
lines_of_at_most_certain_size_of_bytes_read: bytes = \
    await aioserial_instance.readlines_async(hint: int = -1)

# WRITE_ASYNC
number_of_byte_like_data_written: int = \
    await aioserial_instance.write_async(bytes_like_data)

# WRITELINES_ASYNC
number_of_byte_like_data_in_the_given_list_written: int = \
    await aioserial_instance.writelines_async(list_of_bytes_like_data)


# All the other APIs in the mother package pySerial are supported in aioserial as-is.
