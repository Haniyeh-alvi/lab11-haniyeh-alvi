# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    # making one async task for number! Each task will return the multiplied number by 2, 
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
 async def double(n):
    return n* 2

 results = await asyncio.gather(*(double(n) for n in numbers))
 return results



async def fastest(jobs):
    # Outline:
    # create a async task for each job, then wait for assigned delay!
    # Use asyncio.as_completed to get results as they finish.
    # Return the first job's label.
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.

    async def job(label, delay):
        await asyncio.sleep(delay)
        return label

    coroutines = [job(label, delay) for label, delay in jobs]

    for completed in asyncio.as_completed(coroutines):
        result = await completed
        return result

    

def echo_once(host, port, message):
    # Outline:
    # create a tcp socket, connect to host and port!
    # send the message as byters and then receive the reply, decode and return it as string
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message.encode())
        data = s.recv(1024)
    return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
