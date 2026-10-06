"""Command line entry point.

    python cli.py <command> [arguments]

STAGE 2 WIRING BLOCK, part two. Each of you adds one branch to the dispatcher
below. Expect a conflict; resolve it so that all four commands survive.
"""
import sys


def main(argv):
    if not argv:
        print(__doc__)
        print("commands: stats, words, fib, check")
        return 1

    command, args = argv[0], argv[1:]

    # --- wiring block: add exactly one branch for your command ----------
    # if command == "stats":
    #     from toolbox.stats import describe
    #     print(describe([float(a) for a in args]))
    #     return 0
    # --- end wiring block -----------------------------------------------

    print("unknown command: %s" % command)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
