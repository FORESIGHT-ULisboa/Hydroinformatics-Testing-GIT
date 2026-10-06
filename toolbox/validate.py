"""Student D. Input checking helpers used by the other three modules.

Standard library only. See docs/TASKS.md, issue 4.
"""


def require_number(value, name="value"):
    """Return value as a float.

    Accept int, float, and strings such as "3.5". Raise TypeError for bool,
    and ValueError with a message naming `name` for anything else.
    """
    raise NotImplementedError("Student D: implement require_number()")


def require_non_empty(sequence, name="sequence"):
    """Return the sequence unchanged, or raise ValueError if it is empty."""
    raise NotImplementedError("Student D: implement require_non_empty()")
