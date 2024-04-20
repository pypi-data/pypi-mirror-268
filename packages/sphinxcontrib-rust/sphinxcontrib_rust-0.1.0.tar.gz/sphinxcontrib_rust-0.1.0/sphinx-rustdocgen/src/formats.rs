//! Module for handling the output formats supported.

use std::str::FromStr;

use quote::ToTokens;
use syn::Visibility;

use crate::directives::Directive;

/// Generate title decoration string for RST or fence for MD.
///
/// Args:
///     :ch: The character to use.
///     :len: The length of the decoration required.
///
/// Returns:
///     A string of length ``len`` composed entirely of ``ch``.
fn generate_decoration(ch: char, len: usize) -> String {
    let mut decoration = String::with_capacity(len);
    for _ in 0..len {
        decoration.push(ch);
    }
    decoration
}

/// Supported formats for the docstrings
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq)]
pub enum Format {
    /// Markdown format
    Md,
    /// reStructuredText format
    Rst,
}

impl Format {
    const MD_VALUES: [&'static str; 3] = ["md", ".md", "markdown"];
    const RST_VALUES: [&'static str; 3] = ["rst", ".rst", "restructuredtext"];

    /// Returns the extension for the format
    pub fn extension(&self) -> &'static str {
        match self {
            Format::Md => Self::MD_VALUES[1],
            Format::Rst => Self::RST_VALUES[1],
        }
    }

    /// Make a format specific document title using the provided title string.
    pub(crate) fn make_title(&self, title: &str) -> Vec<String> {
        match self {
            Format::Md => {
                vec![format!("# {title}"), String::new()]
            }
            Format::Rst => {
                let decoration = generate_decoration('=', title.len());
                vec![
                    decoration.clone(),
                    title.to_string(),
                    decoration,
                    String::new(),
                ]
            }
        }
    }

    /// Get format specific content for the directive's output file.
    ///
    /// The function assumes that the directive is the top level directive of
    /// the output file and generates the content accordingly.
    ///
    /// Args:
    ///     :directive: The directive to get the content for, typically a
    ///         ``Crate`` or ``Module`` directive.
    ///
    /// Returns:
    ///     A vec of strings which are the lines of the document.
    pub(crate) fn get_content(&self, directive: Directive) -> Vec<String> {
        match self {
            Format::Md => {
                let fence_size = directive.fence_size();
                directive.get_md_text(fence_size, None)
            }
            Format::Rst => directive.get_rst_text(0, None),
        }
    }
}

impl FromStr for Format {
    type Err = ();

    /// Parses the string into an enum value, or panics.
    ///
    /// If the string is ``md``, ``.md`` or ``markdown``, the function
    /// returns ``Md``. If the string is ``rst``, ``.rst`` or
    /// ``restructuredtext``, the function returns ``Rst``. Comparison is
    /// case-insensitive. This is meant to be used for input parsing, hence
    /// the function panics.
    ///
    /// Args:
    ///     :value: The value to parse.
    ///
    /// Returns:
    ///     The parsed enum value, or panics.
    ///
    /// Panics:
    ///     If the input value is not one of the values associated with a
    ///     format.
    fn from_str(value: &str) -> Result<Self, Self::Err> {
        let value_lower = value.to_lowercase();
        if Self::RST_VALUES.contains(&&*value_lower) {
            Ok(Format::Rst)
        }
        else if Self::MD_VALUES.contains(&&*value_lower) {
            Ok(Format::Md)
        }
        else {
            Err(())
        }
    }
}

/// Trait for directives that can be written as RST content
pub(crate) trait RstDirective {
    const INDENT: &'static str = "   ";

    /// Generate RST text with the given level of indentation and inherited
    /// visibility.
    ///
    /// Implementations must provide a vec of the lines of the content of the
    /// item and all its members.
    ///
    /// Args:
    ///     :level: The level of indentation for the content. Use the
    ///         ``make_indent`` and ``make_content_indent`` functions to get
    ///         the actual indentation string.
    ///     :inherited_visibility: The ``Visibility`` value to use when the
    ///         directive inherits the parent's visibility. If ``None``, the
    ///         directive is for a private item.
    ///
    /// Returns:
    ///     The RST text for the documentation of the item and its members.
    fn get_rst_text(self, level: usize, inherited_visibility: Option<&Visibility>) -> Vec<String>;

    /// Make a string for indenting the directive.
    ///
    /// Args:
    ///     :level: The level of the indentation.
    ///
    /// Returns:
    ///     A string that is ``Self::INDENT`` repeated ``level`` times.
    fn make_indent(level: usize) -> String {
        let mut indent = String::with_capacity(Self::INDENT.len() * level);
        for _ in 0..level {
            indent += Self::INDENT;
        }
        indent
    }

    /// Make a string for indenting the directive's content and options
    ///
    /// Args:
    ///     :level: The level of the indentation.
    ///
    /// Returns:
    ///     A string that is ``Self::INDENT`` repeated ``level + 1`` times.
    fn make_content_indent(level: usize) -> String {
        let mut indent = String::with_capacity(Self::INDENT.len() * (level + 1));
        for _ in 0..=level {
            indent += Self::INDENT;
        }
        indent
    }

    /// Make a string for the ``:vis:`` option for the directive.
    ///
    /// Args:
    ///     :visibility: The visibility of the item as detected by ``syn``.
    ///     :inherited: The inherited visibility to use for the item.
    ///
    /// Returns:
    ///     A string can be used as the value of ``:vis:`` in RST or MD
    ///     directives.
    fn visibility_option(visibility: &Visibility, inherited: Option<&Visibility>) -> String {
        match visibility {
            Visibility::Public(_) => String::from("pub"),
            Visibility::Restricted(v) => {
                if v.path.to_token_stream().to_string() == "crate" {
                    String::from("crate")
                }
                else {
                    String::from("pvt")
                }
            }
            Visibility::Inherited => match inherited {
                None => String::from("pvt"),
                Some(v) => Self::visibility_option(v, None),
            },
        }
    }
}

/// Trait for directives that can be written as MD content
pub(crate) trait MdDirective {
    /// Generate MD text with the given fence size and inherited visibility.
    ///
    /// Implementations must provide a vec of the lines of the content of the
    /// item and all its members.
    ///
    /// Args:
    ///     :fence_size: The size of the fence for the directive. Use the
    ///         ``make_fence`` function to get the actual fence string.
    ///     :inherited_visibility: The ``Visibility`` value to use when the
    ///         directive inherits the parent's visibility. If ``None``, the
    ///         directive is for a private item.
    ///
    /// Returns:
    ///     The MD text for the documentation of the item and its members.
    fn get_md_text(
        self,
        fence_size: usize,
        inherited_visibility: Option<&Visibility>,
    ) -> Vec<String>;

    /// Make a string for the fences for the directive.
    ///
    /// Args:
    ///     :fence_size: The size of the fence, must be at least 3.
    ///
    /// Returns:
    ///     A string of colons of length ``fence_size``.
    ///
    /// Panics:
    ///     If the ``fence_size`` is less than 3.
    fn make_fence(fence_size: usize) -> String {
        if fence_size < 3 {
            panic!("Invalid depth for fence: {fence_size}");
        }
        generate_decoration(':', fence_size)
    }

    /// Calculate the fence size required for the item.
    ///
    /// The ``items`` are the members of the current item. So, for
    /// a struct, these will be the list of its fields, for an enum,
    /// the variants, for a module, the items defined in it, etc.
    ///
    /// The fence size for the item is 1 + the max fence size of all
    /// its members. If it has no members, the fence size is 3. So,
    /// the returned value is the minimum fence size required to properly
    /// document the item and its members in Markdown. Depending on the
    /// parent path of the item, the actual fence size used for documentation
    /// may be different, but at least the value returned by this function.
    ///
    /// Args:
    ///     :items: Items which are members of the current item.
    ///
    /// Returns:
    ///     The minimum fence size required to document the item.
    fn calc_fence_size(items: &[Directive]) -> usize {
        match items.iter().map(Directive::fence_size).max() {
            Some(s) => s + 1,
            None => 3,
        }
    }

    /// Return the fence size required for documenting the item.
    ///
    /// The default implementation returns ``3``, which is the size required
    /// for any item that has no members and the minimum size required by
    /// Markdown.
    ///
    /// Implementations may use ``calc_fence_size`` to override this.
    fn fence_size(&self) -> usize {
        3
    }
}
