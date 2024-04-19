import trio
import asyncio

from ._base import BaseTrioEventLoop, TrioAsyncioExit


class TrioEventLoop(BaseTrioEventLoop):
    """An asyncio event loop that runs on top of Trio, opened from
    within Trio code using :func:`open_loop`.
    """

    def _queue_handle(self, handle):
        self._check_closed()
        self._q_send.send_nowait(handle)
        return handle

    def default_exception_handler(self, context):
        """Default exception handler.

        This default handler simply re-raises an exception if there is one.

        Rationale:

        In traditional asyncio, there frequently is no context which the
        exception is supposed to affect.

        trio-asyncio, however, collects the loop and all its tasks in
        a Trio nursery. This means the context in which the error should
        be raised is known and can easily be controlled by the programmer.

        For maximum compatibility, this default handler is only used in
        asynchronous loops.

        """

        # Call the original default handler so we get the full info in the log
        super().default_exception_handler(context)

        if self._nursery is None:
            # Event loop is already closed; don't do anything further.
            # Some asyncio libraries call the asyncio exception handler
            # from their __del__ methods, e.g., aiohttp for "Unclosed
            # client session".
            return

        # Also raise an exception so it can't go unnoticed
        exception = context.get("exception")
        if exception is None:
            message = context.get("message")
            if not message:
                message = "Unhandled error in event loop"
            exception = RuntimeError(message)

        async def propagate_asyncio_error():
            raise exception

        self._nursery.start_soon(propagate_asyncio_error)

    def stop(self, waiter=None):
        """Halt the main loop.

        (Or rather, tell it to halt itself soon(ish).)

        :param waiter: an Event that is set when the loop is stopped.
        :type waiter: :class:`trio.Event`
        :return: Either the Event instance that was passed in,
                 or a newly-allocated one.

        """
        if waiter is None:
            if self._stop_wait is not None:
                return self._stop_wait
            waiter = self._stop_wait = trio.Event()
        else:
            if waiter.is_set():
                waiter.clear()

        def stop_me():
            waiter.set()
            raise TrioAsyncioExit("stopping trio-asyncio loop")

        if self._stopped.is_set():
            waiter.set()
        else:
            self._queue_handle(asyncio.Handle(stop_me, (), self))
        return waiter

    def _close(self):
        """Hook for actually closing down things."""
        if not self._stopped.is_set():
            raise RuntimeError("You need to stop the loop before closing it")
        super()._close()
