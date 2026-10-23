"""Unit tests for ``src.utcnow`` (SANDBOX-001)."""

import re
from datetime import datetime, timezone

from src.utcnow import utcnow

ISO_UTC_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def test_utcnow_matches_iso_utc_format():
    """Acceptance 2: output matches ``^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z$``."""
    assert ISO_UTC_PATTERN.match(utcnow())


def test_utcnow_within_two_seconds_of_now():
    """Acceptance 3: value differs from ``datetime.now(timezone.utc)`` by <= 2s."""
    result = datetime.strptime(utcnow(), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    now = datetime.now(timezone.utc)
    assert abs((now - result).total_seconds()) <= 2


def test_utcnow_non_decreasing_between_calls():
    """Acceptance 4: two consecutive calls are non-decreasing."""
    first = utcnow()
    second = utcnow()
    assert first <= second
