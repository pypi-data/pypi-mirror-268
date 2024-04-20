"""Init module for the extension with the ``setup`` function used by Sphinx"""

from importlib.metadata import version
import subprocess
from shutil import which
from typing import Any, Mapping

import sphinx.config
from sphinx.application import Sphinx
from sphinx.util import logging

from sphinxcontrib_rust.domain import RustDomain

__PKG_NAME = "sphinxcontrib_rust"
__VERSION__ = version(__PKG_NAME)
__REQUIRED_EXTENSIONS = ["sphinx.ext.autodoc"]
__LOGGER = logging.getLogger(__PKG_NAME)

"""The configuration options added by the extension.

Each entry is tuple consisting of
* The option name.
* The default value.
* The rebuild condition .
  * "html": Change needs a full rebuild of HTML.
  * "env": Change needs a full rebuild of the build environment.
  * "": No rebuild required.
* A list of types for the value.
"""
__CONFIG_OPTIONS = (
    ("rust_crates", None, "env", [dict]),
    ("rust_doc_dir", None, "env", [str]),
    ("rust_rustdoc_fmt", "rst", "env", [str]),
    ("rust_visibility", "pub", "html", [str]),  # TODO: Define a type for this
)

"""
See https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
"""
__METADATA = {
    "version": __VERSION__,
    "parallel_read_safe": True,
    "parallel_write_safe": True,
}
__RUSTDOCGEN = which("sphinx-rustdocgen")


def generate_docs(app: Sphinx, config: sphinx.config.Config):
    """Generate the Rust docs once the configuration has been read

    Args:
        :app: The Sphinx application.
        :config: The parsed configuration.
    """
    for crate, src_dir in config.rust_crates.items():
        __LOGGER.info(
            "[sphinxcontrib_rust] Processing contents of crate %s from directory %s",
            crate,
            src_dir,
        )
        __LOGGER.info(
            "[sphinxcontrib_rust] Generated files will be saved in %s/%s",
            config.rust_doc_dir,
            crate,
        )
        subprocess.run(
            [
                __RUSTDOCGEN,
                crate,
                src_dir,
                config.rust_doc_dir,
                config.rust_rustdoc_fmt,
            ],
            check=True,
        )


def setup(app: Sphinx) -> Mapping[str, Any]:
    """Set up the extension"""
    if __RUSTDOCGEN is None:
        raise ValueError(
            "Could not find the sphinx-rustdocgen executable. "
            "Make sure it is installed and available on the default PATH."
        )

    app.require_sphinx("7.0")

    for extension in __REQUIRED_EXTENSIONS:
        app.setup_extension(extension)

    for option in __CONFIG_OPTIONS:
        app.add_config_value(*option)

    app.add_domain(RustDomain)
    app.connect("config-inited", generate_docs)

    return __METADATA
