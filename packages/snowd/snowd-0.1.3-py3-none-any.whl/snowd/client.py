import logging
from datetime import datetime, timedelta, timezone

import pysnow
import pytz

from .envvars import (
    SNOW_CLIENT_ID,
    SNOW_CLIENT_SECRET,
    SNOW_INSTANCE,
    SNOW_PASSWORD,
    SNOW_USER,
)
from .polling import poll as _poll

log = logging.getLogger(__name__)

# TO DO: use it
# https://stackoverflow.com/questions/5537876/get-utc-offset-from-time-zone-name-in-python
# datetime.now(pytz.timezone('Asia/Jerusalem')).strftime('%z')


def now_with_offset(tz_offset=0):
    tzinfo = timezone(timedelta(hours=tz_offset))

    def now():
        return datetime.now(tzinfo)

    return now


def get_query(last, until=None):
    builder = pysnow.QueryBuilder()
    if until:
        return (
            builder.field("sys_created_on")
            .greater_than_or_equal(last)
            .OR()
            .field("sys_updated_on")
            .greater_than_or_equal(last)
        )
    return (
        builder.field("sys_created_on")
        .between(last, until)
        .OR()
        .field("sys_updated_on")
        .between(last, until)
    )


def poll(resource, step=60, since=None, current_datetime_getter=None):
    if not current_datetime_getter:
        current_datetime_getter = datetime.now
    last = since or current_datetime_getter()

    def target():
        nonlocal last
        until = current_datetime_getter()
        query = get_query(last, until)
        log.debug(f"Query: {query._query}")  # noqa
        last = until
        return resource.get(query=query).all()

    for result in _poll(target, step=step):
        yield from result


def current_user(client, username=None):
    if not username:
        username = client._user  # noqa
    return (
        client.resource("/table/sys_user")
        .get(pysnow.QueryBuilder().field("user_name").equals(username))
        .one()
    )


# from dateutil import ...

# REST API explorer
# https://{instance}.service-now.com/nav_to.do?uri=%2F$restapi.do

# GraphQL API: We can create api based on predefined graphql queries ?
# https://{instance}.service-now.com/sys_graphql_schema_list.do?sysparm_userpref_module=884050143b133300d69c229c93efc4c8&sysparm_clear_stack=true


# We can by-pass the QueryBuilder if needed
# https://pysnow.readthedocs.io/en/latest/usage/query.html#sn-pass-through

# Nb: having the url "https://myinstance.service-now.com/", the instance value is "myinstance"


# Code taken here:
# https://pysnow.readthedocs.io/en/latest/full_examples/oauth_client.html
def _get_oauth_client(instance, user, password, client_id, client_secret):
    store = {"token": None}

    # Takes care of refreshing the token storage if needed
    def updater(new_token):
        store["token"] = new_token

    # Create the OAuthClient with the ServiceNow provided `client_id` and `client_secret`, and a `token_updater`
    # function which takes care of refreshing local token storage.
    client = pysnow.OAuthClient(
        client_id=client_id,
        client_secret=client_secret,
        token_updater=updater,
        instance=instance,
    )
    if not store["token"]:
        # No previous token exists. Generate new.
        store["token"] = client.generate_token(user, password)
    # Set the access / refresh tokens
    client.set_token(store["token"])
    return client


def get_client(
    instance=None,
    user=None,
    password=None,
    /,
    client_id=None,
    client_secret=None,
):
    instance = instance or SNOW_INSTANCE
    user = user or SNOW_USER
    password = password or SNOW_PASSWORD
    client_id = client_id or SNOW_CLIENT_ID
    client_secret = client_secret or SNOW_CLIENT_SECRET
    if client_id and client_secret:
        return _get_oauth_client(instance, user, password, client_id, client_secret)
    return pysnow.Client(instance=instance, user=user, password=password)


class Client:
    def __init__(
        self,
        instance=None,
        user=None,
        password=None,
        client_id=None,
        client_secret=None,
    ):
        self._client = get_client(
            instance,
            user,
            password,
            client_id=client_id,
            client_secret=client_secret,
        )
        self._user = None
        self._tz_name = None
        self._tz = None
        self._utcoffset = None

    @property
    def user(self):
        if not self._user:
            self._user = current_user(self._client)
        return self._user

    @property
    def tz_name(self):
        if not self._tz_name:
            self._tz_name = self.user.get("time_zone") or "UTC"
        return self._tz_name

    @property
    def tz(self):
        if not self._tz:
            self._tz = pytz.timezone(self.tz_name)
        return self._tz

    @property
    def utcoffset(self):
        if not self.utcoffset:
            self.utcoffset = int(self.now().utcoffset().total_seconds())
        return self._tz

    def astimezone(self, dt):
        """
        Make sure that the date timezone is the one defined on the user.
        Nb: if datetime doesn't have a specified timezone, it default to the system timezone
        Also, be sure that your environment time is synchronized
        sudo hwclock -s
        """
        if isinstance(dt, float):
            dt = datetime.fromtimestamp(dt)
        return dt.astimezone(self.tz)

    def now(self):
        return datetime.now(self.tz)

    def resource(self, resource):
        if isinstance(resource, str):
            return self._client.resource(resource)
        return resource

    def get_all_since(self, resource, since, until=None):
        r = self.resource(resource)
        since = self.astimezone(since)
        until = self.astimezone(until) if until else self.now()
        query = get_query(since, until)
        return r.get(query=query).all()

    def poll(self, resource, step=60, since=None):
        if isinstance(resource, str):
            resource = self.resource(resource)

        def current_datetime_getter():
            return self.now()

        return poll(
            resource,
            step=step,
            since=since,
            current_datetime_getter=current_datetime_getter,
        )


# me = current_user(client)
# time_zone = me["time_zone"]
