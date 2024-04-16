# Stub file for conditional import based on environment settings

from typing import Any

# The actual class type of OneServer depends on the PYONE_TEST_FIXTURE environment variable.
# It could be from the current package or from the pyone.tester module as OneServerTester.
# Here we abstractly import it as Any to accommodate both possibilities.

OneServer: Any
