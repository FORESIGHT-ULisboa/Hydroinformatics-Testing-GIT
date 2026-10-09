"""toolbox - a four-person exercise package.

STAGE 2 WIRING BLOCK. Everyone edits the block below, on their own branch, at
the same time. That is deliberate: the second, third and fourth pull requests
will conflict here and you have to resolve them.

Keep the lines in alphabetical order and do not reformat the rest of the file.
"""

__version__ = "0.1.0"

# --- wiring block: add exactly one line for your module -----------------
from .stats import describe
# from .text import word_counts
# from .sequences import fibonacci
# from .validate import require_number
# --- end wiring block ---------------------------------------------------

__all__ = ["describe"]
