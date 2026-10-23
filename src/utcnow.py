"""Fictional UTC time utility used for sandbox workflow validation."""

from datetime import datetime, timezone


def utcnow() -> str:
    """Return the current UTC time as an ISO 8601 string.

    The format is ``YYYY-MM-DDTHH:MM:SSZ`` where the ``Z`` suffix
    explicitly denotes UTC. The local system timezone is never used.
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
