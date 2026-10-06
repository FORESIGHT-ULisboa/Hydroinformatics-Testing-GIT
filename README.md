# toolbox

A very small Python toolbox, built by students, using git the
way a real project uses it.

Pure standard library: no installation, no dependencies.

## Use

```bash
python cli.py stats 3 1 4 1 5 9 2 6
python cli.py words "the quick brown fox jumps over the lazy dog"
python cli.py fib 10
python cli.py check 42
```

## Modules

| Module | What it does | Author |
|---|---|---|
| `toolbox.stats` | descriptive statistics for a list of numbers | |
| `toolbox.text` | word counting and frequencies | |
| `toolbox.sequences` | fibonacci, primes, collatz | |
| `toolbox.validate` | input checking helpers | |

## Tests

```bash
python -m unittest discover -s tests -v
```

## License

MIT — see `LICENSE`.
