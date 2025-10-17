# Documentation Guide

This document provides an overview of the documentation structure for the Clean Architecture FastAPI Template.

## 📖 Documentation Structure

```
docs/
├── conf.py                      # Sphinx configuration
├── index.rst                    # Main documentation page
├── requirements.txt             # Documentation dependencies
├── Makefile                     # Build commands
│
├── getting-started/             # Getting Started Guide
│   ├── installation.rst         # Installation instructions
│   ├── quickstart.rst          # Quick start tutorial
│   └── template-variables.rst  # Template variable reference
│
├── user-guide/                  # User Guide
│   ├── architecture.rst        # Clean Architecture overview
│   ├── project-structure.rst   # Project organization
│   ├── configuration.rst       # Configuration management
│   ├── database.rst            # Database setup and usage
│   ├── caching.rst             # Caching configuration
│   ├── message-brokers.rst     # Message broker integration
│   ├── testing.rst             # Testing guide
│   └── deployment.rst          # Deployment instructions
│
├── development/                 # Development Guide
│   ├── code-quality.rst        # Code quality standards
│   ├── docker.rst              # Docker development
│   ├── migrations.rst          # Database migrations
│   └── contributing.rst        # Contributing guidelines
│
├── advanced/                    # Advanced Topics
│   ├── customization.rst       # Template customization
│   ├── hooks.rst               # Cookiecutter hooks
│   ├── ci-cd.rst               # CI/CD setup
│   └── best-practices.rst      # Best practices
│
├── reference/                   # Reference Documentation
│   ├── makefile-commands.rst   # Makefile command reference
│   ├── environment-variables.rst # Environment variables
│   └── faq.rst                 # Frequently asked questions
│
├── changelog.rst                # Version history
└── license.rst                  # License information
```

## 🚀 Quick Start

### View Documentation Online

Visit [Read the Docs](https://clean-architecture-fastapi-project-template.readthedocs.io/) (coming soon)

### Build Documentation Locally

1. **Install dependencies:**

```bash
cd docs
pip install -r requirements.txt
```

2. **Build HTML documentation:**

```bash
make html
```

3. **Open in browser:**

```bash
# macOS
open _build/html/index.html

# Linux
xdg-open _build/html/index.html

# Windows
start _build/html/index.html
```

### Live Preview

For live preview during development:

```bash
pip install sphinx-autobuild
sphinx-autobuild docs docs/_build/html
```

Then open http://localhost:8000

## 📝 Documentation Format

Documentation is written in **reStructuredText** (`.rst`) format, which provides:

- Rich formatting options
- Cross-referencing
- Code highlighting
- Automatic API documentation
- PDF/ePub generation

## 🔧 Building Different Formats

### HTML (Default)

```bash
make html
```

### PDF

```bash
make latexpdf
```

### ePub

```bash
make epub
```

### Clean Build

```bash
make clean
```

## 📚 Key Documentation Pages

### For Users

- **[Installation](docs/getting-started/installation.rst)** - How to install and use the template
- **[Quickstart](docs/getting-started/quickstart.rst)** - Get started in 5 minutes
- **[Architecture](docs/user-guide/architecture.rst)** - Understanding Clean Architecture

### For Developers

- **[Code Quality](docs/development/code-quality.rst)** - Standards and tools
- **[Contributing](docs/development/contributing.rst)** - How to contribute

## 🛠️ Maintaining Documentation

### Adding New Pages

1. Create a new `.rst` file in the appropriate directory
2. Add it to the `toctree` in `index.rst` or parent page
3. Build and verify

Example:

```rst
.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user-guide/new-page
```

### Writing Style

- Use clear, concise language
- Include code examples
- Add cross-references
- Keep sections focused
- Use proper headings hierarchy

### Code Examples

```rst
.. code-block:: python

   def example():
       """Example function."""
       pass
```

### Cross-References

```rst
See :doc:`getting-started/installation` for details.
```

### External Links

```rst
`FastAPI Documentation <https://fastapi.tiangolo.com>`_
```

## 🔄 Automatic Deployment

Documentation is automatically built and deployed to Read the Docs on every commit to the main branch.

Configuration: `.readthedocs.yaml` in the repository root.

## 📦 Documentation Dependencies

All documentation dependencies are listed in `docs/requirements.txt`:

- **sphinx** - Documentation generator
- **sphinx-rtd-theme** - Read the Docs theme
- **sphinx-autodoc-typehints** - Type hints in documentation
- **sphinx-copybutton** - Copy button for code blocks
- **myst-parser** - Markdown support
- **sphinxcontrib-mermaid** - Diagram support

## 🎨 Customization

### Theme Configuration

Edit `docs/conf.py`:

```python
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "navigation_depth": 4,
}
```

### Extensions

Add extensions in `docs/conf.py`:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # Add more extensions
]
```

## 🐛 Troubleshooting

### Build Errors

```bash
# Clean and rebuild
make clean
make html
```

### Missing Dependencies

```bash
pip install -r docs/requirements.txt
```

### Broken Links

```bash
# Check for broken links
make linkcheck
```

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Peopl3s/clean-architecture-fastapi-project-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Peopl3s/clean-architecture-fastapi-project-template/discussions)
- **Documentation**: [Read the Docs](https://clean-architecture-fastapi-project-template.readthedocs.io/)

## 📄 License

Documentation is licensed under [MIT License](LICENSE).

---

**Happy documenting!** 📚✨
