from __future__ import annotations


class FTMError(Exception):
    """Base exception for Family Time Manager."""


class ConfigurationError(FTMError):
    """Configuration loading failed."""


class RepositoryError(FTMError):
    """Repository operation failed."""
