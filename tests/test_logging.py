import os
import sys

# Ensure the package is importable without installation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_data_science_team.tools.logging import log_ai_function

def test_log_ai_function_returns_tuple_when_disabled(tmp_path):
    result = log_ai_function("response", "file.txt", log=False, log_path=str(tmp_path))
    assert result == (None, None)

