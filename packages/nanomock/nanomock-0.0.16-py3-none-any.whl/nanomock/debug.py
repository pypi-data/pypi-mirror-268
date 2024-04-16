from nanomock_manager import NanoLocalManager
from modules.nl_rpc import NanoRpc


# Setup code here
manager = NanoLocalManager("unit_tests/configs", "unittest")
nano_rpc = NanoRpc("http://127.0.0.1:45900")

manager.execute_command("down")
manager.execute_command("create")
manager.execute_command("start")
