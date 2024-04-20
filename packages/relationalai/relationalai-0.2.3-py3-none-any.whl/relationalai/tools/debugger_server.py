import asyncio
import logging
import os
import threading
import websockets

from relationalai import debugging
import __main__ # to get the users root file path

connected_clients = set()
has_connected_client = threading.Event()
buffered_broadcasts = []

async def broadcast(message):
    buffered_broadcasts.append(message)
    if connected_clients:
        tasks = [asyncio.create_task(client.send(message)) for client in connected_clients]
        await asyncio.wait(tasks)

async def handle_connection(websocket, path):
    connected_clients.add(websocket)
    if not has_connected_client.is_set():
        has_connected_client.set()

    try:
        for message in buffered_broadcasts:
            await websocket.send(message)
        async for message in websocket:
            print("GOT", message)
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Client disconnected with reason: {e}")
    finally:
        connected_clients.remove(websocket)

def _start_server(host: str, port: int, program_span: dict):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start_server_coro = websockets.serve(handle_connection, host, port)
    server = loop.run_until_complete(start_server_coro)

    try:
        while True:
            if not threading.main_thread().is_alive():
                break
            loop.run_until_complete(asyncio.sleep(1))
    finally:
        debugging.span_end(program_span)
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()


class WebSocketLoggingHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from relationalai.analysis.mechanistic import Mechanism
        self.Mechanism = Mechanism

    def emit(self, record):
        d = record.msg
        if isinstance(d, dict) and d["event"] == "span_start" and "task" in d and "mech" not in d:
            d["mech"] = self.Mechanism(d["task"])
        log_entry = self.format(record)
        asyncio.run(broadcast(log_entry))

already_debugging = False
def start_debugger_session(wait_for_connection = False, host = "0.0.0.0", port = 5678):
    global already_debugging
    if already_debugging:
        return

    already_debugging = True
    ws_handler = WebSocketLoggingHandler()
    ws_handler.setFormatter(debugging.JsonFormatter())
    debugging.logger.addHandler(ws_handler)

    program_span = debugging.span_start("program",  main=os.path.relpath(__main__.__file__))

    # daemon so the make program exiting will kill the thread
    server_thread = threading.Thread(target=_start_server, args=(host, port, program_span)) # , daemon=True
    server_thread.start()

    if wait_for_connection:
        print(f"Waiting for debugger client to connect at ws://{host}:{port} ...")
        has_connected_client.wait()
        print("Connected.")
