async def __init__(hub):
    hub.log.LOGGER = {}
    hub.log.HANDLER = []
    hub.log.INT_LEVEL = hub.lib.logging.INFO
    hub.log.QUEUE = hub.lib.asyncio.Queue()

    # Set up aliases for each log function
    hub.log.trace = hub.log.init.trace
    hub.log.info = hub.log.init.info
    hub.log.debug = hub.log.init.debug
    hub.log.error = hub.log.init.error
    hub.log.warning = hub.log.init.warning
    hub.log.warn = hub.log.warning
    hub.log.critical = hub.log.init.critical
    hub.log.fatal = hub.log.critical



async def get_caller(hub) -> tuple[str, int]:
    """
    Inspect the stack and get the function that called get_caller
    """
    if not __debug__:
        return "hub", 0

    try:
        # Grab the third ref back, fall back to closer refs
        ref, stack_summary = (hub._call_stack.get()[-3:] or [None])[0]
        filename, lineno, *_ = stack_summary
        return ref, lineno
    except Exception:
        return "hub", 0


async def get_logger(hub, name: str):
    """
    Create a logger for the given ref with all the configured handlers
    """
    if name not in hub.log.LOGGER:
        if hub.log.HANDLER:
            logger = hub.lib.aiologger.Logger(name=name, level=hub.log.INT_LEVEL)
            for handler in hub.log.HANDLER:
                handler.level = hub.log.INT_LEVEL
                logger.add_handler(handler)
        else:
            logger = hub.lib.aiologger.Logger.with_default_handlers(name=name, level=hub.log.INT_LEVEL)

        hub.log.LOGGER[name] = logger

    return hub.log.LOGGER[name]


async def setup(hub, log_plugin: str = "init", *, log_level: str, log_file: str, **kwargs):
    """
    Initialize the logger with the named plugin
    """
    if not __debug__:
        return

    if hub.log.HANDLER:
        # We already set up the logger
        return

    # Set up trace logger
    hub.lib.aiologger.levels.LEVEL_TO_NAME[5] = "TRACE"
    levels = hub.lib.logging.getLevelNamesMapping()
    levels["TRACE"] = 5
    hub.lib.logging.addLevelName(5, "TRACE")

    # Convert log level to integer
    if str(log_level).isdigit():
        hub.log.INT_LEVEL = int(log_level)
    else:
        hub.log.INT_LEVEL = levels[log_level.upper()]

    if log_plugin != "init":
        # Create the log file
        if log_file:
            path = await hub.lib.aiopath.Path(log_file).expanduser()
            if not await path.parent.exists():
                await path.parent.mkdir(parents=True, exist_ok=True)
            await path.touch(exist_ok=True)
            log_file = str(path)
        await hub.log[log_plugin].setup(log_file=log_file, **kwargs)

    if not __debug__:
        return
    

    # Create a handler that puts the main python log messages through aiologger via an asynchronous Queue
    class _AsyncHandler(hub.lib.logging.Handler):
        def emit(self, record):
            if hub.lib.asyncio._get_running_loop() is None:
                return
            hub._auto(
                hub.log.init.emit(record)
            )

    async_handler = _AsyncHandler()

    # Replace all existing synchronous loggers with the aiologger
    for logger in hub.lib.logging.root.manager.loggerDict.values():
        if isinstance(logger, hub.lib.logging.Logger):
            for handler in logger.handlers[:]:
                logger.removeHandler(handler)
                handler.close()
            logger.addHandler(async_handler)
            logger.setLevel(hub.log.INT_LEVEL)


async def emit(hub, record):
    if not __debug__:
        return
    logger_name = f"lib.{record.name}"
    logger = await hub.log.init.get_logger(logger_name)
    message = record.getMessage()
    # Pass the log record to the appropriate aiologger instance
    await logger._log(record.levelno, message, tuple(), extra={"lineno": record.lineno, "filepath": record.pathname})


async def trace(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger._log(5, msg, args, **kwargs, extra={"lineno": lineno})


async def debug(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger.debug(msg, *args, **kwargs, extra={"lineno": lineno})


async def info(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger.info(msg, *args, **kwargs, extra={"lineno": lineno})


async def warning(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger.warning(msg, *args, **kwargs, extra={"lineno": lineno})


async def error(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger.error(msg, *args, **kwargs, extra={"lineno": lineno})


async def critical(hub, msg: str, *args, **kwargs):
    if not __debug__:
        return
    ref, lineno = await hub.log.init.get_caller()
    logger = await hub.log.init.get_logger(ref)
    await logger.critical(msg, *args, **kwargs, extra={"lineno": lineno})
