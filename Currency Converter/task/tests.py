from typing import List

from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestStage1(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase()
        ]

    def check(self, reply: str, attach) -> CheckResult:
        if "meet a conicoin!" not in reply.lower():
            return CheckResult.wrong("Check your output")
        return CheckResult.correct()


if __name__ == '__main__':
    TestStage1("cconverter.cconverter").run_tests()
