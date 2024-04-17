# Development

## Tests

Tests are run using PyTest. You can simply run this command to launch tests:

```bash
pytest
```

## Documentation

High-level documentation is handled by [Typer](https://typer.tiangolo.com/). You can update the generated `USAGE.md` file using this command:

```bash
make docs
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Note that before opening a pull requests, you may want to check formatting and tests of your changes:

```bash
make ci
```

You can also install git [pre-commit](https://pre-commit.com/) hooks to format code on commit with:

```bash
pip install -e .[dev]
pre-commit install
```

## Make a release

```bash
git checkout main
git pull

vim CHANGELOG.md					# Edit version + links at bottom
vim geopic_tag_reader/__init__.py	# Edit version
make docs ci

git add *
git commit -m "Release x.x.x"
git tag -a x.x.x -m "Release x.x.x"
git push origin main --tags
```
