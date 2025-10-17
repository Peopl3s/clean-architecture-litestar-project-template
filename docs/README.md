# Documentation

This directory contains the Sphinx documentation for the Clean Architecture Litestar Template.

## Building Documentation

### Prerequisites

Install documentation dependencies:

```bash
pip install -r requirements.txt
```

### Build HTML Documentation

```bash
make html
```

The documentation will be available in `_build/html/index.html`.

### Build PDF Documentation

```bash
make latexpdf
```

### Clean Build Files

```bash
make clean
```

## Documentation Structure

```
docs/
├── conf.py                 # Sphinx configuration
├── index.rst              # Main documentation page
├── getting-started/       # Installation and quickstart guides
├── user-guide/            # User documentation
├── development/           # Development guides
├── reference/             # Reference documentation
├── changelog.rst          # Version history
└── license.rst           # License information
```

## Writing Documentation

### Format

Documentation is written in reStructuredText (`.rst`) format.

### Adding New Pages

1. Create a new `.rst` file in the appropriate directory
2. Add it to the `toctree` in `index.rst` or parent page
3. Build and verify

### Code Examples

Use code blocks with language specification:

```rst
.. code-block:: python

   def example():
       pass
```

### Cross-References

Link to other pages:

```rst
See :doc:`getting-started/installation` for details.
```

## Live Preview

For live preview during development:

```bash
pip install sphinx-autobuild
sphinx-autobuild . _build/html
```

Then open http://localhost:8000 in your browser.

## Read the Docs

Documentation is automatically built and published to Read the Docs on every commit to the main branch.

Configuration: `.readthedocs.yaml` in the repository root.
