from server import Server, check_server
import asyncio


async def main(server):
    try:
        while True:
            command = input("Enter 'exit' to stop the server. \n")
            if command == "exit":
                server.stop()
                break
    finally:
        server.join()

    print("server really stopped")


async def run():
    server = Server()
    server.start()
    check_server()
    await main(server)


if __name__ == "__main__":
    asyncio.run(run())
