import logging
import urllib.parse
from contextlib import asynccontextmanager
from typing import AsyncIterator, ClassVar, Optional

import websockets
import websockets.client

from hume._common.client_base import ClientBase
from hume._common.protocol import Protocol
from hume._voice.voice_socket import VoiceSocket
from hume.error.hume_client_exception import HumeClientException

logger = logging.getLogger(__name__)


class ChatMixin(ClientBase):
    """Client operations for EVI WebSocket connections."""

    DEFAULT_MAX_PAYLOAD_SIZE_BYTES: ClassVar[int] = 2**24

    @asynccontextmanager
    async def connect(self, config_id: Optional[str] = None) -> AsyncIterator[VoiceSocket]:
        """Connect to the EVI API.

        Args:
            config_id (Optional[str]): Config ID.
        """
        uri_base = self._build_endpoint("evi", "chat", Protocol.WS)

        params = {
            "cut_ms": VoiceSocket.DEFAULT_CUT_MS,
            "encoding": VoiceSocket.DEFAULT_ENCODING,
            "channels": VoiceSocket.DEFAULT_NUM_CHANNELS,
            "sample_rate": VoiceSocket.DEFAULT_SAMPLE_RATE,
        }

        encoded_params = urllib.parse.urlencode(params)
        uri = f"{uri_base}?{encoded_params}"

        if config_id is not None:
            uri += f"&config_id={config_id}"

        max_size = self.DEFAULT_MAX_PAYLOAD_SIZE_BYTES
        try:
            # pylint: disable=no-member
            async with websockets.connect(  # type: ignore[attr-defined]
                uri,
                extra_headers=self._get_client_headers(),
                close_timeout=self._close_timeout,
                open_timeout=self._open_timeout,
                max_size=max_size,
            ) as protocol:
                yield VoiceSocket(protocol)
        except websockets.exceptions.InvalidStatusCode as exc:
            status_code: int = exc.status_code
            if status_code == 401:  # Unauthorized
                message = "HumeVoiceClient initialized with invalid API key."
                raise HumeClientException(message) from exc
            raise HumeClientException("Unexpected error when creating EVI API connection") from exc
