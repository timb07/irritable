=========
Irritable
=========


.. image:: https://img.shields.io/pypi/v/irritable.svg
        :target: https://pypi.python.org/pypi/irritable

.. image:: https://img.shields.io/travis/timb07/irritable.svg
        :target: https://travis-ci.org/timb07/irritable

.. image:: https://readthedocs.org/projects/irritable/badge/?version=latest
        :target: https://irritable.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/timb07/irritable/shield.svg
     :target: https://pyup.io/repos/github/timb07/irritable/
     :alt: Updates


Irritable implements broken iterators called irritables


* Free software: BSD license
* Documentation: https://irritable.readthedocs.io.


Features
--------

Iterators are defined in the docs_ ; the definition includes what
constitutes a broken implementation:

    4.5. Iterator Types

    [...]

    Once an iterator’s ``__next__()`` method raises StopIteration, it must
    continue to do so on subsequent calls. Implementations that do not
    obey this property are deemed broken.

*Irritables* are like iterables, but deliberately broken. The following
types of brokenness are supported:

- after ``next()`` first raises ``StopIteration``, subsequent calls will
  raise ``StopIrritation`` instead;

- if the irritator is instantiated with ``resume=True``, calling
  ``next()`` may raise ``StopIteration`` when items remain still remain in
  the container; subsequent calls to ``next()`` will return the remaining
  items as usual until none remain;

- if the irritator is instantiated with ``repeat=True``, after the
  iterator has been exhausted and raises ``StopIteration``, the iterator
  is reset and can be iterated over again ad infinitum; in this case
  ``next()`` will never raise ``StopIrritation``;


Credits
---------

The idea for irritators came during Trey Hunner's talk_ "Loop better:
a deeper look at iteration in Python" at DjangoCon AU 2017.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _docs: https://docs.python.org/3/library/stdtypes.html
.. _talk: https://2017.pycon-au.org/schedule/presentation/55/
