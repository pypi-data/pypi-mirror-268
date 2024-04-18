"""HomeLINK utilities."""
from dateutil import parser

from .exceptions import ApiException, AuthException


def check_status(resp):
    """Check status of the call."""
    if resp.status == 401:
        raise AuthException(f"Authorization failed: {resp.status}")
    if resp.status != 200:
        raise ApiException(f"Error request failed: {resp.status}, url: {resp.url}")


def parse_date(in_date):
    """Parse the date."""
    return parser.parse(in_date) if in_date else None
