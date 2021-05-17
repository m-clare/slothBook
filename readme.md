# slothBook

This is a proof of concept for rendering ipython notebooks for calculation packages for standard structural engineering calcs (similar to TEDDS or Mathcad). Initial findings required significant duplification of LaTeX expressions for browser rendering and then a final LaTeX setup to generate the report using [PyLaTeX](https://jeltef.github.io/PyLaTeX/current/). Other aspects explored with this concept included batch calculation using [Papermill](https://papermill.readthedocs.io/en/latest/).

A significantly more developed and thought out implementation of this idea can be seen in in the [HandCalcs library](https://github.com/connorferster/handcalcs) by Conner Ferster.
