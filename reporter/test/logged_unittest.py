# -*- coding: utf-8 -*-
"""
    Provides a custom unit test base class which will log to sentry.

    :copyright: (c) 2010 by Tim Sutton
    :license: GPLv3, see LICENSE for more details.
"""
import unittest
import logging
from reporter import setup_logger

setup_logger()
LOGGER = logging.getLogger('osm-reporter')


class LoggedTestCase(unittest.TestCase):
    """A test class that logs to sentry on failure."""
    def failureException(self, msg):
        """Overloaded failure exception that will log to sentry.

        Args:
            msg: str - a string containing a message for the log entry.

        Returns:
            delegates to TestCase and returns the exception generated by it.

        Raises:
            see unittest.TestCase

        """
        LOGGER.exception(msg)
        return self.super(LoggedTestCase, self).failureException(msg)
