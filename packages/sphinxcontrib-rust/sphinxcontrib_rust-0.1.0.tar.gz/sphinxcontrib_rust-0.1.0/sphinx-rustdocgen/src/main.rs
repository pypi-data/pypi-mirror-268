//! sphinx-rustdocgen is an executable to extract doc comments from Rust
//! crates. It is tightly coupled with the sphinxcontrib-rust extension and is
//! used by it during the Sphinx build process.
//!
//! Usage:
//!
//! .. code-block::
//!
//!    sphinx-rustdocgen <crate_name> <crate_src_dir> <output_dir> <format>
//!
//! .. toctree::
//!    :caption: Crate documentation
//!    :maxdepth: 3
//!
//!    /docs/crates/sphinx-rustdocgen/lib

use std::env;
use std::path::Path;
use std::str::FromStr;

use sphinx_rustdocgen::{traverse_crate, Format};

static USAGE: &str = "sphinx-rustdocgen <crate_name> <crate_src_dir> <output_dir> <format>";

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 5 {
        panic!("Invalid number of arguments: {}\n\n{}", args.len(), USAGE);
    }

    // Parse args
    let crate_name = args.get(1).unwrap();
    let crate_src_dir = Path::new(args.get(2).unwrap());
    let output_dir = Path::new(args.get(3).unwrap());
    let format = Format::from_str(args.get(4).unwrap()).unwrap_or_else(|_| {
        panic!(
            "Unknown format \"{}\". Must be one of rst or md.",
            args.get(4).unwrap(),
        )
    });

    traverse_crate(crate_name, crate_src_dir, output_dir, format)
}
