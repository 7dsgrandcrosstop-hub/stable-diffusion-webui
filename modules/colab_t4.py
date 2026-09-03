"""Small opt-in helpers for the Colab T4 runtime profile.

The profile is deliberately disabled by default so normal A1111 behavior does
not change. Set A1111_COLAB_T4=1 before importing modules.cmd_args to enable it.
"""

import gc
import os


_TRUE_VALUES = {"1", "true", "yes", "on"}


def enabled(environ=None):
    """Return whether the opt-in Colab T4 profile is enabled."""

    source = os.environ if environ is None else environ
    return source.get("A1111_COLAB_T4", "").strip().lower() in _TRUE_VALUES


def release_checkpoint_memory():
    """Collect temporary Python objects after checkpoint weights are applied."""

    if not enabled():
        return 0

    return gc.collect()


def debug_argument_limit(default=131072):
    """Keep Colab error cells compact without changing normal desktop logs."""

    return 4096 if enabled() else default
