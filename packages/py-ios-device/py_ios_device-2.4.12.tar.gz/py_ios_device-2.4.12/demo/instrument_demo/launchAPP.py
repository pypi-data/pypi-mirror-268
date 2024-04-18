"""
启动 app
"""
import os
import sys
from time import sleep

from ios_device.remote.remote_lockdown import RemoteLockdownClient
from ios_device.util.variables import InstrumentsService

sys.path.append(os.getcwd())

from ios_device.servers.Instrument import InstrumentServer


def _launch_app(rpc, bundleid):
    rpc._start()

    def on_channel_message(res):
        print(res.auxiliaries, res.selector)

    channel = "com.apple.instruments.server.services.processcontrol"
    rpc.register_channel_callback(channel, on_channel_message)
    pid = rpc.call(channel, "launchSuspendedProcessWithDevicePath:bundleIdentifier:environment:arguments:options:", "",
                   bundleid, {}, [], {"StartSuspendedKey": 0, "KillExisting": 1}).selector
    print("start", pid)


if __name__ == '__main__':
    host = 'fd43:dbaa:ecc1::1'  # randomized
    port = 50205  # randomized
    with RemoteLockdownClient((host, port)) as rsd:
        rpc = InstrumentServer(rsd).init()
        for i in range(1000):
            var = rpc.call(InstrumentsService.Screenshot, "takeScreenshot").selector
            print(f"start {len(var)}")

