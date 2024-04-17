from .client.client import Client
from .client.events import DiscordEvents
from .util.enums import ReadyStates
from .util.packets import GateWayOpen, HeartBeat, GuildRequest, TokenCheck

user_interface = {
    "Client": Client,
    "DiscordEvents": DiscordEvents,
    "ReadyStates": ReadyStates,
    "GateWayOpen": GateWayOpen,
    "HeartBeat": HeartBeat,
    "GuildRequest": GuildRequest,
    "TokenCheck": TokenCheck,
    "version": 1.0,
}
