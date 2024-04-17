from contextvars import ContextVar

ctx: ContextVar[int] = ContextVar("TheCtx")
