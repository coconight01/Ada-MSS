from __future__ import annotations

from dataclasses import dataclass

from .data import RepairTask


@dataclass
class ValidationResult:
    passed: bool
    error_type: str
    output: str


class ValidationSandbox:
    """Executes candidate code + tests in isolated namespace (lightweight local simulation)."""

    def run(self, task: RepairTask, candidate_code: str) -> ValidationResult:
        ns: dict = {}
        try:
            exec(candidate_code, ns, ns)
            exec(task.tests, ns, ns)

            test_functions = [v for k, v in ns.items() if k.startswith("test_") and callable(v)]
            if not test_functions:
                return ValidationResult(False, "NoTestsDiscovered", "No test_* function found")

            for fn in test_functions:
                fn()
            return ValidationResult(True, "", "all tests passed")
        except AssertionError as e:
            return ValidationResult(False, "AssertionError", str(e) or "assertion failed")
        except Exception as e:
            return ValidationResult(False, type(e).__name__, str(e))
