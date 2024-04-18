from __future__ import annotations

from typing import ClassVar

from schwifty import checksum
from schwifty.domain import Component


@checksum.register("NL")
class DefaultAlgorithm(checksum.Algorithm):
    name = "default"
    accepts: ClassVar[list[Component]] = [Component.ACCOUNT_CODE]

    def compute(self, components: list[str]) -> str:
        # There is no actual check digit as part of the BBAN.
        return ""

    def validate(self, components: list[str], expected: str) -> bool:
        [account_code] = components
        return sum(int(digit) * (10 - i) for i, digit in enumerate(account_code)) % 11 == 0
