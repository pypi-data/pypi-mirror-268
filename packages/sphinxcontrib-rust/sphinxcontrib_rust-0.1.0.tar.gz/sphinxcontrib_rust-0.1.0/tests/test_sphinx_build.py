""" Tests for the various directives """

import unittest
from pathlib import Path

import sphinx.cmd.build


class TestSphinxBuild(unittest.TestCase):
    """Integration tests for the Rust domain which test the complete Sphinx build"""

    def exec_sphinx(self, test_docs_dir: str):
        """Execute the Sphinx build and test that it completes successfully.

        Args:
            :files: The files to include for the build. Only these files are processed
                    along with the ``index.rst`` file.
        """
        self.assertEqual(
            sphinx.cmd.build.main(
                [
                    "-b",
                    "html",
                    "-W",  # fail on warnings
                    "-E",  # new env each time
                    "-T",  # show full traceback
                    "--keep-going",  # parse everything
                    test_docs_dir,
                    f"{test_docs_dir}/_build/",
                ]
            ),
            0,
        )

    def test_build(self):
        """Test building the docs"""
        project_dir = Path(__file__).absolute().parent.parent
        self.exec_sphinx(str(project_dir))


if __name__ == "__main__":
    unittest.main()
