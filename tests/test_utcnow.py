"""Unit tests for ``src.utcnow`` (SANDBOX-001)."""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Deterministic import anchor: put the repository root on sys.path so that
# ``from src.utcnow import utcnow`` resolves identically under ``pytest -q``
# (console script, no cwd on sys.path) and ``python -m pytest``.
# Rationale: with a top-level ``src/`` directory present, setuptools automatic
# discovery always selects "src-layout" (see setuptools.discovery
# ``_analyse_src_layout``: it returns True unconditionally once ``src/``
# exists), so ``pip install -e .`` only exposes ``<repo>/src`` on sys.path
# (i.e. a top-level ``utcnow`` module), never the ``src`` package itself.
# Pinning the repo root here makes the import explicit and stable instead of
# depending on the caller's working directory ("碰巧成功").
_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

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
