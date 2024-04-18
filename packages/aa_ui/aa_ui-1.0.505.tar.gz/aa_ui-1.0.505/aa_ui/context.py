import asyncio
import uuid
from contextvars import ContextVar
from typing import TYPE_CHECKING, Dict, Optional, Union, List

from aa_ui.session import HTTPSession, WebsocketSession
from lazify import LazyProxy

if TYPE_CHECKING:
    from aa_ui.emitter import Baseaa_uiEmitter
    from aa_ui.user import PersistedUser, User
    from aa_ui.step import Step


class aa_uiContextException(Exception):
    def __init__(self, msg="aa_ui context not found", *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class aa_uiContext:
    loop: asyncio.AbstractEventLoop
    emitter: "Baseaa_uiEmitter"
    session: Union["HTTPSession", "WebsocketSession"]
    active_steps: List["Step"]

    @property
    def current_step(self):
        if self.active_steps:
            return self.active_steps[-1]

    def __init__(self, session: Union["HTTPSession", "WebsocketSession"]):
        from aa_ui.emitter import Baseaa_uiEmitter, aa_uiEmitter

        self.loop = asyncio.get_running_loop()
        self.session = session
        self.active_steps = []
        if isinstance(self.session, HTTPSession):
            self.emitter = Baseaa_uiEmitter(self.session)
        elif isinstance(self.session, WebsocketSession):
            self.emitter = aa_uiEmitter(self.session)


context_var: ContextVar[aa_uiContext] = ContextVar("aa_ui")
local_steps: ContextVar[Optional[List["Step"]]] = ContextVar("local_steps")
local_steps.set(None)


def init_ws_context(session_or_sid: Union[WebsocketSession, str]) -> aa_uiContext:
    if not isinstance(session_or_sid, WebsocketSession):
        session = WebsocketSession.require(session_or_sid)
    else:
        session = session_or_sid
    context = aa_uiContext(session)
    context_var.set(context)
    return context


def init_http_context(
    user: Optional[Union["User", "PersistedUser"]] = None,
    auth_token: Optional[str] = None,
    user_env: Optional[Dict[str, str]] = None,
) -> aa_uiContext:
    session = HTTPSession(
        id=str(uuid.uuid4()),
        token=auth_token,
        user=user,
        client_type="app",
        user_env=user_env,
    )
    context = aa_uiContext(session)
    context_var.set(context)
    return context


def get_context() -> aa_uiContext:
    try:
        return context_var.get()
    except LookupError:
        raise aa_uiContextException()


context: aa_uiContext = LazyProxy(get_context, enable_cache=False)
