from unittest import TestCase
from seCore.CustomLogging import logger


class seTestCase(TestCase):

    def setUp(self) -> None:
        self.msg = "Test Message"

    def test_logger(self):
        logger.info(self.msg)
