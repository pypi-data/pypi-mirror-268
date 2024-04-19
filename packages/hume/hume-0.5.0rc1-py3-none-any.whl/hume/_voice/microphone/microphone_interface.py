"""Interface for connecting a device microphone to an EVI connection."""

import asyncio
import base64
import datetime
import json
import logging
from dataclasses import dataclass
from typing import ClassVar, Optional, Protocol

from hume._voice.microphone.asyncio_utilities import Stream
from hume._voice.microphone.audio_utilities import play_audio
from hume._voice.microphone.microphone import Microphone
from hume._voice.voice_socket import VoiceSocket
from hume.error.hume_client_exception import HumeClientException

logger = logging.getLogger(__name__)


class Sender(Protocol):
    """Protocol for sending streaming audio to an EVI connection."""

    async def on_audio_begin(self) -> None:
        """Handle the start of an audio stream."""
        raise NotImplementedError()

    async def on_audio_end(self) -> None:
        """Handle the end of an audio stream."""
        raise NotImplementedError()

    async def send(self, *, socket: VoiceSocket) -> None:
        """Send audio data over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
        """
        raise NotImplementedError()


@dataclass
class MicrophoneSender(Sender):
    """Sender for streaming audio from a microphone."""

    microphone: Microphone
    send_audio: bool
    allow_interrupt: bool

    @classmethod
    def new(cls, *, microphone: Microphone, allow_interrupt: bool) -> "MicrophoneSender":
        """Create a new microphone sender.

        Args:
            microphone (Microphone): Microphone instance.
            allow_interrupt (bool): Whether to allow interrupting the audio stream.
        """
        return cls(microphone=microphone, send_audio=True, allow_interrupt=allow_interrupt)

    async def on_audio_begin(self) -> None:
        """Handle the start of an audio stream."""
        self.send_audio = self.allow_interrupt

    async def on_audio_end(self) -> None:
        """Handle the end of an audio stream."""
        self.send_audio = True

    async def send(self, *, socket: VoiceSocket) -> None:
        """Send audio data over an EVI socket.

        Args:
            socket (VoiceSocket): EVI socket.
        """
        async for byte_str in self.microphone:
            if self.send_audio:
                await socket.send(byte_str)


@dataclass
class ChatClient:
    """Async client for handling messages to and from an EVI connection."""

    DEFAULT_USER_ROLE_NAME: ClassVar[str] = "You"
    DEFAULT_ASSISTANT_ROLE_NAME: ClassVar[str] = "EVI"

    sender: Sender
    byte_strs: Stream[bytes]

    @classmethod
    def new(cls, *, sender: Sender) -> "ChatClient":
        """Create a new chat client.

        Args:
            sender (Sender): Sender for audio data.
        """
        return cls(sender=sender, byte_strs=Stream.new())

    @classmethod
    def _map_role(cls, role: str) -> str:
        if role == "user":
            return cls.DEFAULT_USER_ROLE_NAME
        if role == "assistant":
            return cls.DEFAULT_ASSISTANT_ROLE_NAME
        return role

    async def _recv(self, *, socket: VoiceSocket) -> None:
        async for socket_message in socket:
            message = json.loads(socket_message)
            if message["type"] in ["user_message", "assistant_message"]:
                role = self._map_role(message["message"]["role"])
                message_text = message["message"]["content"]
                text = f"{role}: {message_text}"
            elif message["type"] == "audio_output":
                message_str: str = message["data"]
                message_bytes = base64.b64decode(message_str.encode("utf-8"))
                await self.byte_strs.put(message_bytes)
                continue
            elif message["type"] == "error":
                error_message: str = message["message"]
                raise HumeClientException(f"ERROR: {error_message}")
            else:
                message_type = message["type"].upper()
                text = f"<{message_type}>"

            now = datetime.datetime.now(tz=datetime.timezone.utc)
            now_str = now.strftime("%H:%M:%S")

            print(f"[{now_str}] {text}")

    async def _play(self) -> None:
        async for byte_str in self.byte_strs:
            await self.sender.on_audio_begin()
            await play_audio(byte_str)
            await self.sender.on_audio_end()

    async def run(self, *, socket: VoiceSocket) -> None:
        """Run the chat client.

        Args:
            socket (VoiceSocket): EVI socket.
        """
        recv = self._recv(socket=socket)
        send = self.sender.send(socket=socket)

        await asyncio.gather(recv, self._play(), send)


@dataclass
class MicrophoneInterface:
    """Interface for connecting a device microphone to an EVI connection."""

    DEFAULT_ALLOW_USER_INTERRUPT: ClassVar[bool] = False

    @classmethod
    async def start(
        cls,
        socket: VoiceSocket,
        device: Optional[int] = Microphone.DEFAULT_DEVICE,
        allow_user_interrupt: bool = DEFAULT_ALLOW_USER_INTERRUPT,
    ) -> None:
        """Start the microphone interface.

        Args:
            socket (VoiceSocket): EVI socket.
            device (Optional[int]): Device index for the microphone.
            allow_user_interrupt (bool): Whether to allow the user to interrupt EVI.
        """
        with Microphone.context(device=device) as microphone:
            sender = MicrophoneSender.new(microphone=microphone, allow_interrupt=allow_user_interrupt)
            chat_client = ChatClient.new(sender=sender)
            print("Configuring socket with microphone settings...")
            await socket.update_session_settings(
                encoding=VoiceSocket.DEFAULT_ENCODING,
                sample_rate=microphone.sample_rate,
                num_channels=microphone.num_channels,
            )
            print("Microphone connected. Say something!")
            await chat_client.run(socket=socket)
