__version__ = (1, 0, 0)


from .. import loader, utils

from telethon.tl.types import Message
from ..inline.types import InlineCall

from miio.device import Device
plug = Device(DEVICE_IP, DEVICE_TOKEN)
def __init__(self):
self.config = loader.ModuleConfig(
loader.ConfigValue(
'DEVICE_IP',
None,
doc=lambda: "Ip of device"
)
)
def __init__(self):
self.config = loader.ModuleConfig(
loader.ConfigValue(
'DEVICE_TOKEN',
None,
doc=lambda: "Token of device"
)
)

async def relayon(self, call: InlineCall):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                print(plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':True}]))

async def relayoff(self, call: InlineCall):
                DEVICE_IP = self.config['DEVICE_IP']
                DEVICE_TOKEN = self.config['DEVICE_TOKEN']
                print(plug.send("set_properties", [{'did': 'MYDID', 'siid': 2, 'piid': 1, 'value':False}]))


