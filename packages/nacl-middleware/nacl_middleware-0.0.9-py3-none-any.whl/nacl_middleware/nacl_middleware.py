from inspect import signature
from logging import getLogger
from operator import itemgetter
from sys import exc_info
from traceback import format_exception
from typing import Tuple

from aiohttp import WSCloseCode
from aiohttp.typedefs import Handler, Middleware
from aiohttp.web import (
    HTTPUnauthorized,
    Request,
    Response,
    StreamResponse,
    WebSocketResponse,
    middleware,
)
from nacl.public import PrivateKey

from nacl_middleware.nacl_utils import MailBox
from nacl_middleware.utils import is_exclude

mailBoxes = {}


def nacl_middleware(
    private_key: PrivateKey,
    exclude_routes: Tuple = tuple(),
    exclude_methods: Tuple = tuple(),
    log=getLogger(),
) -> Middleware:
    """
    Middleware function that handles NaCl encryption and decryption.

    Args:
        private_key (PrivateKey): The private key used for decryption.
        exclude_routes (Tuple, optional): Tuple of routes to exclude from encryption/decryption. Defaults to an empty tuple.
        exclude_methods (Tuple, optional): Tuple of HTTP methods to exclude from encryption/decryption. Defaults to an empty tuple.
        log (Logger, optional): Logger object for logging debug messages. Defaults to getLogger().

    Returns:
        Middleware: The middleware function.

    """

    def nacl_decryptor(public_key, encrypted_message) -> Tuple[any, MailBox]:
        """
        Decrypts the encrypted message using the public key.

        Args:
            public_key: The public key used for encryption.
            encrypted_message: The encrypted message to decrypt.

        Returns:
            Tuple[any, MailBox]: A tuple containing the decrypted message and the MailBox object.

        """
        if public_key in mailBoxes:
            my_mail_box = mailBoxes[public_key]
        else:
            my_mail_box = MailBox(private_key, public_key)
            mailBoxes[public_key] = my_mail_box

        log.debug("Decrypting message...")
        message = my_mail_box.unbox(encrypted_message)
        log.debug(f"Message {message} decrypted!")
        return message, my_mail_box

    @middleware
    async def returned_middleware(request: Request, handler: Handler) -> StreamResponse:
        """
        Middleware function that processes the incoming request and handles exceptions.

        Args:
            request (Request): The incoming request object.
            handler (Handler): The handler function to be called.

        Returns:
            StreamResponse: The response object.

        Raises:
            HTTPUnauthorized: If a valid message cannot be retrieved.

        """
        if not (
            is_exclude(request, exclude_routes) or request.method in exclude_methods
        ):

            try:
                log.debug("Retrieving publicKey and encryptedMessage from message...")
                publicKey, encryptedMessage = itemgetter(
                    "publicKey", "encryptedMessage"
                )(request.query)
                log.debug(
                    f"PublicKey {publicKey} and EncryptedMessage {encryptedMessage} retrieved!"
                )

                decrypted_message, my_mail_box = nacl_decryptor(
                    publicKey, encryptedMessage
                )

                request["mail_box"] = my_mail_box
                request["decrypted_message"] = decrypted_message
            except Exception:
                the_exc_info = exc_info()
                exception_str = "".join(format_exception(*the_exc_info))
                log.debug(f"Exception body: {exception_str}")
                exception = HTTPUnauthorized(
                    reason="Failed to retrieve a valid message!", body=exception_str
                )

                # Inspect the handler's signature
                return_annotation = signature(handler).return_annotation
                if return_annotation == WebSocketResponse:
                    log.debug("WebSocketResponse hook.")
                    log.debug(f"Exception is {exception_str}")
                    socket = WebSocketResponse()
                    await socket.prepare(request)
                    await socket.close(
                        code=WSCloseCode.PROTOCOL_ERROR,
                        message="".join(format_exception(exception)),
                    )
                    return socket
                elif return_annotation == Response:
                    log.debug("Response hook.")
                    log.debug(f"headers: {exception.headers}")
                    log.debug(f"status: {exception.status}")
                    log.debug(f"reason: {exception.reason}")
                    log.debug(f"body: {exception.body}")
                    return Response(
                        headers=exception.headers,
                        status=exception.status,
                        reason=exception.reason,
                        body=exception.body,
                    )

        return await handler(request)

    return returned_middleware
