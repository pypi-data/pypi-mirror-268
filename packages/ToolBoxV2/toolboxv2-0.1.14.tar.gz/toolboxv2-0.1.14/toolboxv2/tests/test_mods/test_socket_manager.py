import queue
import time

try:
    from toolboxv2.mods.SocketManager import export, Name, App, get_app, Tools, SocketType, Result, asyncio
except ImportError:
    export, Name, App, get_app, Tools, SocketType, Result, asyncio = None, None, None, None, None, None, None, None


async def client_server_sync(app: App = None):
    if app is None:
        app = get_app("test_client_server_sync", "debug-test")

    sm: Tools = app.get_mod(Name)

    # crate a sever

    server = await sm.create_socket("localhost-testS",
                                    "",
                                    1234,
                                    SocketType.server,
                                    test_override=True,
                                    return_full_object=True)

    assert not server.is_error(), server.print(show=False)
    server = server.get()

    await asyncio.sleep(0.1)

    client = await sm.create_socket("localhost-testC",
                                    "127.0.0.1",
                                    1234,
                                    SocketType.client,
                                    test_override=True,
                                    return_full_object=True)

    assert not client.is_error(), client.print(show=False)

    client = client.get()

    server_client_, addr = server['receiver_queue'].get(timeout=2).get("data")
    # await asyncio.sleep(1)
    await server["client_to_receiver_thread"](server_client_, "main1")
    # await asyncio.sleep(1)

    await server["sender"]({'test': 'server2client'}, "main1")
    await client["sender"]({'test': 'client2server'}, "main")

    await server["sender"](b'server2client', "main1")
    await client["sender"](b'client2server', "main")

    await client['close']()
    await asyncio.sleep(1)
    # return client, server
    # queue.Queue().qsize()
    print(client['receiver_queue'].qsize())
    print(server['receiver_queue'].qsize())
    print(client['receiver_queue'].get(timeout=2))
    print(server['receiver_queue'].get(timeout=2))
    print(client['receiver_queue'].get(timeout=2))
    print(server['receiver_queue'].get(timeout=2))
    # time.sleep(2)
    print(server)
    print(client)

    await asyncio.sleep(1)
    time.sleep(2)
    await server['close']()

    print(server)
    print(client)


async def client_server_async(app: App = None):
    if app is None:
        app = get_app("test_client_server_sync", "debug-test")

    sm: Tools = app.get_mod(Name)

    # crate a sever

    server = await sm.create_socket("localhost-testS",
                                    "127.0.0.1",
                                    1234,
                                    SocketType.server,
                                    test_override=True,
                                    return_full_object=True)

    assert not server.is_error(), server.print(show=False)
    server = await server.aget()

    client = await sm.create_socket("localhost-testC",
                                    "127.0.0.1",
                                    1234,
                                    SocketType.client,
                                    test_override=True,
                                    return_full_object=True,do_async=True)

    await asyncio.sleep(1)
    time.sleep(2)

    assert not client.is_error(), client.print(show=False)

    client = client.get()

    server_client_, addr = server['receiver_queue'].get(timeout=2).get("data")
    # await asyncio.sleep(1)
    await server["client_to_receiver_thread"](server_client_, "main1")
    # await asyncio.sleep(1)

    await server["sender"]({'test': 'server2client'}, "main1")
    await client["sender"]({'test': 'client2server'}, "main")

    await server["sender"](b'server2client', "main1")
    await client["sender"](b'client2server', "main")

    await client['close']()
    await asyncio.sleep(1)
    time.sleep(2)
    # return client, server
    # queue.Queue().qsize()
    x = client['a_receiver_queue'].qsize()
    print(x)
    print(server['receiver_queue'].qsize())
    x = await client['a_receiver_queue'].get()
    print(x)
    print(server['receiver_queue'].get(timeout=2))
    print(client['a_receiver_queue'].get(timeout=2))
    print(server['receiver_queue'].get(timeout=2))
    # time.sleep(2)
    print(server)
    print(client)

    await asyncio.sleep(1)
    time.sleep(2)
    await server['close']()

    print(server)
    print(client)


def test_helper():
    asyncio.run(client_server_sync())


if __name__ == "__main__":
    test_helper()
