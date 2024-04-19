"""Voice socket connection."""

import json
import logging
from pathlib import Path
from typing import Any, AsyncIterator, ClassVar

from pydub import AudioSegment
from websockets.client import WebSocketClientProtocol as WebSocket

logger = logging.getLogger(__name__)


class VoiceSocket:
    """Voice socket connection."""

    DEFAULT_CUT_MS: ClassVar[int] = 250
    DEFAULT_ENCODING: ClassVar[str] = "linear16"
    DEFAULT_NUM_CHANNELS: ClassVar[int] = 1
    DEFAULT_SAMPLE_RATE: ClassVar[int] = 44_100

    def __init__(self, protocol: WebSocket):
        """Construct a `VoiceSocket`.

        Args:
            protocol (WebSocketClientProtocol): Protocol instance from websockets library.

        Raises:
            HumeClientException: If there is an error processing media over the socket connection.
        """
        self._protocol = protocol

    async def __aiter__(self) -> AsyncIterator[Any]:
        """Async iterator for the voice socket."""
        async for message in self._protocol:
            yield message

    async def send(self, byte_str: bytes) -> None:
        """Send a byte string over the voice socket.

        Args:
            byte_str (bytes): Byte string to send.
        """
        await self._protocol.send(byte_str)

    async def recv(self) -> Any:
        """Receive a message on the voice socket."""
        await self._protocol.recv()

    async def update_session_settings(
        self,
        *,
        encoding: str,
        sample_rate: int,
        num_channels: int,
    ) -> None:
        """Update the EVI session settings."""
        session_settings = {
            "type": "session_settings",
            "audio": {
                "encoding": encoding,
                "channels": num_channels,
                "sample_rate": sample_rate,
            },
        }

        logger.info(f"Updating session settings to: {session_settings}")
        message = json.dumps(session_settings).encode("utf-8")
        await self._protocol.send(message)

    async def send_file(self, filepath: Path) -> None:
        """Send a file over the voice socket.

        Args:
            filepath (Path): Filepath to the file to send over the socket.
        """
        with filepath.open("rb") as f:
            segment: AudioSegment = AudioSegment.from_wav(f)
            audio_bytes = segment.raw_data
            await self._protocol.send(audio_bytes)
