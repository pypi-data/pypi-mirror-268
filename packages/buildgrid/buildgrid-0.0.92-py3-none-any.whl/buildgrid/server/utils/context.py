from threading import Event
from typing import Callable, List

from grpc import ServicerContext


class CancellationContext:
    def __init__(self, context: ServicerContext) -> None:
        """
        Creates a wrapper for a grpc.ServicerContext which allows determining if a gRPC request has been
        cancelled by the client. Callbacks may be added to this context which will be invoked if the
        underlying grpc.ServicerContext is triggered.
        """

        self._event = Event()
        self._context = context
        self._callbacks: List[Callable[[], None]] = []
        context.add_callback(self._on_callback)

    def is_cancelled(self) -> bool:
        return self._event.is_set()

    def _on_callback(self) -> None:
        self._event.set()
        for callback in self._callbacks:
            callback()

    def on_cancel(self, callback: Callable[[], None]) -> None:
        self._callbacks.append(callback)
        if self.is_cancelled():
            callback()
