from datetime import datetime, timedelta
from fastapi import Request
import socket

from ..utils import format_user_agent
from ..exceptions import NotAuthenticatedException


class Permissions:
    def __init__(self, db, config: dict):
        self.db = db
        self.config = config

    async def get_user_session(self, request: Request):
        if not (user_session := await self.get_user(request)):
            raise NotAuthenticatedException()
        return user_session

    async def get_user(self, request: Request) -> object | None:
        """
        Retrieve the user based on the session token from the request.
        Also updates the last session time for the user's device.
        """
        session_token = request.session.get("session_token")
        if not session_token:
            return None

        user = await self.__get_user_by_session_token(session_token)
        if not user:
            return None

        if self.__is_session_expired(user.get('last_session')):
            return None

        client_ip = request.client.host
        proxy_ip = None
        if forwarded_for := request.headers.get("X-Forwarded-For"):
            proxy_ip = client_ip
            client_ip = forwarded_for.split(",")[0].strip()
        user_agent = format_user_agent(request.headers.get("User-Agent"))

        if proxy_ip and (proxy_ip != self.config.get('endpoint', dict()).get('proxy', '') and proxy_ip != socket.gethostbyname("parendum.com")):
            print(f"Not authorized proxy tried to connect ({proxy_ip} != {self.config.get('endpoint', dict()).get('proxy', '')})")
            return None

        if not self.__is_device_valid(user, client_ip, user_agent):
            return None

        await self.__update_user_last_session(user, client_ip, user_agent)
        return user

    async def __get_user_by_session_token(self, session_token):
        """Retrieve a user from the database using the session token."""
        users = await self.db.retrieve_all('users', dict(session_token=session_token))
        return users[0] if users else None

    def __is_device_valid(self, user, client_ip, user_agent):
        """Check if the device is valid for the user."""
        devices = user.get('devices', [])
        return any(self.__is_device_match(device, client_ip, user_agent) for device in devices)

    async def __update_user_last_session(self, user, client_ip, user_agent):
        """Update the last session time for the user's device."""
        devices = user.get('devices', [])
        for device in devices:
            if self.__is_device_match(device, client_ip, user_agent):
                device['last_session'] = datetime.utcnow()
        await self.db.update('users', user.get('_id'), dict(last_session=datetime.utcnow(), devices=devices))

    @staticmethod
    def __is_session_expired(last_session):
        """Check if the session has expired."""
        return last_session and datetime.utcnow() - last_session > timedelta(hours=24)

    @staticmethod
    def __is_device_match(device, client_ip, user_agent):
        return device.get('client_ip') == client_ip and device.get('user_agent') == user_agent and device.get('is_active')
