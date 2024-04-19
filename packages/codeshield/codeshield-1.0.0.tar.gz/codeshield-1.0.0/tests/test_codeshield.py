# (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

# pyre-strict

from __future__ import annotations

import unittest

from ..codeshield import CodeShield


class CodeShieldTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        super().setUp()

    test_cases = [
        ("eval(input)", True),
        ("hello world", False),
        ("temp_filename = tmpnam(NULL);", False),
    ]

    async def test_scanner(self) -> None:
        for test_case in self.test_cases:
            test_input, expected_result = test_case
            scan_results = await CodeShield.scan_code(test_input)
            self.assertEqual(scan_results.is_insecure, expected_result)
