import os
import unittest
from pathlib import Path

from hmd_tf_pdf_generation.hmd_tf_pdf_generation import do_transform


class TestTransform:
    def test_exit_code(self):
        exit_code = do_transform(
            "./test/input",
            "./test/output",
            "test-nid-1234",
            {"title": "Test Report", "filename": "report"},
        )

        assert exit_code == 0
        assert os.path.exists("./test/output/report.pdf")
