from typing import overload
import abc
import typing

import QuantConnect.Notifications
import System
import System.Collections.Concurrent
import System.Collections.Generic

JsonConverter = typing.Any


class Notification(System.Object, metaclass=abc.ABCMeta):
    """Local/desktop implementation of messaging system for Lean Engine."""

    def send(self) -> None:
        """Method for sending implementations of notification object types."""
        ...


class NotificationWeb(QuantConnect.Notifications.Notification):
    """Web Notification Class"""

    @property
    def headers(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Optional email headers"""
        ...

    @property
    def address(self) -> str:
        """Send a notification message to this web address"""
        ...

    @property
    def data(self) -> System.Object:
        """Object data to send."""
        ...

    def __init__(self, address: str, data: typing.Any = None, headers: System.Collections.Generic.Dictionary[str, str] = None) -> None:
        """
        Constructor for sending a notification SMS to a specified phone number
        
        :param address: Address to send to
        :param data: Data to send
        :param headers: Optional headers to use
        """
        ...


class NotificationSms(QuantConnect.Notifications.Notification):
    """Sms Notification Class"""

    @property
    def phone_number(self) -> str:
        """Send a notification message to this phone number"""
        ...

    @property
    def message(self) -> str:
        """Message to send. Limited to 160 characters"""
        ...

    def __init__(self, number: str, message: str) -> None:
        """Constructor for sending a notification SMS to a specified phone number"""
        ...


class NotificationEmail(QuantConnect.Notifications.Notification):
    """Email notification data."""

    @property
    def headers(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Optional email headers"""
        ...

    @property
    def address(self) -> str:
        """Send to address:"""
        ...

    @property
    def subject(self) -> str:
        """Email subject"""
        ...

    @property
    def message(self) -> str:
        """Message to send."""
        ...

    @property
    def data(self) -> str:
        """Email Data"""
        ...

    def __init__(self, address: str, subject: str = ..., message: str = ..., data: str = ..., headers: System.Collections.Generic.Dictionary[str, str] = None) -> None:
        """
        Default constructor for sending an email notification
        
        :param address: Address to send to. Will throw ArgumentException if invalid Validate.EmailAddress
        :param subject: Subject of the email. Will set to string.Empty if null
        :param message: Message body of the email. Will set to string.Empty if null
        :param data: Data to attach to the email. Will set to string.Empty if null
        :param headers: Optional email headers to use
        """
        ...


class NotificationTelegram(QuantConnect.Notifications.Notification):
    """Telegram notification data"""

    @property
    def id(self) -> str:
        """
        Send a notification message to this user on Telegram
        Can be either a personal ID or Group ID.
        """
        ...

    @property
    def message(self) -> str:
        """Message to send. Limited to 4096 characters"""
        ...

    @property
    def token(self) -> str:
        """Token to use"""
        ...

    def __init__(self, id: str, message: str, token: str = None) -> None:
        """
        Constructor for sending a telegram notification to a specific User ID
        or group ID. Note: The bot must have an open chat with the user or be
        added to the group for messages to deliver.
        
        :param id: User Id or Group Id to send the message too
        :param message: Message to send
        :param token: Bot token to use, if null defaults to "telegram-token" in config on send
        """
        ...


class NotificationJsonConverter(JsonConverter):
    """Defines a JsonConverter to be used when deserializing to the Notification class."""

    @property
    def can_write(self) -> bool:
        """Use default implementation to write the json"""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class NotificationManager(System.Object):
    """Local/desktop implementation of messaging system for Lean Engine."""

    @property
    def messages(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Notifications.Notification]:
        """Public access to the messages"""
        ...

    def __init__(self, liveMode: bool) -> None:
        """Initialize the messaging system"""
        ...

    @overload
    def email(self, address: str, subject: str, message: str, data: str, headers: typing.Any) -> bool:
        """
        Send an email to the address specified for live trading notifications.
        
        :param address: Email address to send to
        :param subject: Subject of the email
        :param message: Message body, up to 10kb
        :param data: Data attachment (optional)
        :param headers: Optional email headers to use
        """
        ...

    @overload
    def email(self, address: str, subject: str, message: str, data: str = ..., headers: System.Collections.Generic.Dictionary[str, str] = None) -> bool:
        """
        Send an email to the address specified for live trading notifications.
        
        :param address: Email address to send to
        :param subject: Subject of the email
        :param message: Message body, up to 10kb
        :param data: Data attachment (optional)
        :param headers: Optional email headers to use
        """
        ...

    def sms(self, phone_number: str, message: str) -> bool:
        """
        Send an SMS to the phone number specified
        
        :param phone_number: Phone number to send to
        :param message: Message to send
        """
        ...

    def telegram(self, id: str, message: str, token: str = None) -> bool:
        """
        Send a telegram message to the chat ID specified, supply token for custom bot.
        Note: Requires bot to have chat with user or be in the group specified by ID.
        
        :param message: Message to send
        :param token: Bot token to use for this message
        """
        ...

    @overload
    def web(self, address: str, data: typing.Any, headers: typing.Any) -> bool:
        """
        Place REST POST call to the specified address with the specified DATA.
        Python overload for Headers parameter.
        
        :param address: Endpoint address
        :param data: Data to send in body JSON encoded
        :param headers: Optional headers to use
        """
        ...

    @overload
    def web(self, address: str, data: typing.Any = None, headers: System.Collections.Generic.Dictionary[str, str] = None) -> bool:
        """
        Place REST POST call to the specified address with the specified DATA.
        
        :param address: Endpoint address
        :param data: Data to send in body JSON encoded (optional)
        :param headers: Optional headers to use
        """
        ...


