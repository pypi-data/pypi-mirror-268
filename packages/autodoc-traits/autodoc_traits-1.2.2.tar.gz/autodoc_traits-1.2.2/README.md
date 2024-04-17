# autodoc-traits

[![Latest PyPI version](https://img.shields.io/pypi/v/autodoc-traits?logo=pypi)](https://pypi.python.org/pypi/autodoc-traits)
[![GitHub](https://img.shields.io/badge/issue_tracking-github-blue?logo=github)](https://github.com/jupyterhub/autodoc-traits/issues)
[![Discourse](https://img.shields.io/badge/help_forum-discourse-blue?logo=discourse)](https://discourse.jupyter.org/c/jupyterhub)
[![Gitter](https://img.shields.io/badge/social_chat-gitter-blue?logo=gitter)](https://gitter.im/jupyterhub/jupyterhub)

`autodoc-traits` is a Sphinx extension that builds on [`sphinx.ext.autodoc`][]
to better document classes with [Traitlets][] based configuration.
`autodoc-traits` provides the [Sphinx directives][] `autoconfigurable` (use with
classes) and `autotrait` (use with the traitlets based configuration options).

The `sphinx.ext.autodoc` provided directive [`automodule`][], which can overview
classes, will with `autodoc-traits` enabled use `autoconfigurable` over
[`autoclass`][] for classes has trait based configuration. Similarly, the
`sphinx.ext.autodoc` provided `autoclass` directive will use `autotrait` over
[`autoattribute`][] if configured to present the traitlets attributes normally
not presented.

The `autoattribute` directive will provide a header looking like `trait
c.SampleConfigurable.trait = Bool(False)`, and as docstring it will use the
trait's configured help text.

## How to use it

1. Install `autodoc-traits`:

   ```shell
   pip install autodoc-traits
   ```

2. Configure Sphinx to use the `autodoc_traits` extensions in a Sphinx project's
   `conf.py` file:

   ```python
   # -- General Sphinx configuration --------------------------------------------
   # ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
   #
   extensions = [
       "autodoc_traits",
       # sphinx.ext.autodoc will be registered by autodoc_traits,
       # but can safely be registered again.
       # ...
   ]
   ```

3. Make use of the `sphinx.ext.autodoc` Sphinx directive like `automodule` that
   document classes, the `autodoc_traits` provided `autoconfigurable` that
   documents traitlets configurable classes, or the `autodoc_traits` provided
   `autotrait` that documents individual traitlets configuration options:

   From a .rst document:

   ```rst
   .. automodule:: sample_module
      :members:

   .. autoconfigurable:: sample_module.SampleConfigurable

   .. autotrait:: sample_module.SampleConfigurable.trait
   ```

## Use with MyST Parser

While you can use [`myst-parser`][], `sphinx.ext.autodoc`'s directives emits
unparsed rST, forcing us to parse the autodoc directives in a rST context.

From a .md document, with `myst-parser`:

````markdown
```{eval-rst}
.. autoconfigurable:: sample_module.SampleConfigurable
```
````

Due to this, also the Python docstrings are required to be in rST as well.
Addressing this can be tracked from [executablebooks/team-compass issue
#6](https://github.com/executablebooks/team-compass/issues/6).

[`sphinx.ext.autodoc`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[sphinx directives]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives
[`autoclass`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoclass
[`autoattribute`]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoattribute
[traitlets]: https://github.com/ipython/traitlets
[`traitlets.traittype`]: https://traitlets.readthedocs.io/en/stable/trait_types.html#traitlets.TraitType
[`myst-parser`]: https://myst-parser.readthedocs.io/en/latest/
