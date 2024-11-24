import os

# import sys
from unittest import TestCase
from src.submission_001 import submission_getblockhash
from unittest.mock import mock_open, patch, MagicMock


class TestSubmissions(TestCase):

    def test_getblockhash(self):
        # The question block
        blockheight = 654321
        blockhash = submission_getblockhash(blockheight=blockheight)
        expected_blockhash = "000000000000000000058452bbe379ad4364fe8fda68c45e299979b492858095"
        self.assertEqual(blockhash, expected_blockhash)
        
