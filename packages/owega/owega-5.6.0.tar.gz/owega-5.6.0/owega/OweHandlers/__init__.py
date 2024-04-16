"""Prompt session init."""
from .handlers import handlers, handle_help, handler_helps
from ..OwegaSession import set_ps, OwegaSession

set_ps(OwegaSession)
