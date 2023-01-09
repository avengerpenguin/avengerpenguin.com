# Languages & Frameworks

These are languages and frameworks on my radar at various levels. See the top-level [[Tech Radar]] for other categories.

Note that I rarely look at whole new languages as I have a bias towards frameworks and libraries that help me build things over improving the act of writing code itself. A language might have promise on here if its ecosystem of libraries and frameworks mature around it since that's a key feature for me over aethetics of syntax or language semantics.

## Sanic

- Status: Assess

Sanic is a Python web server and web framework that's written to go fast. See [Sanic on Github](https://github.com/sanic-org/sanic).

## Quart

- Status: Assess

See [Quart docs](https://pgjones.gitlab.io/quart/index.html).

## IDOM

- Status: Hold

It's React, but in Python! While interesting, I'm yet to think this is a good idea over, say, htmx. See [IDOM docs](https://ryanmorshead.com/articles/2021/idom-react-but-its-python/article/)

## htmx

- Status: Trial

A solid attempt to extend HTML affordances in a standard way user agents could well support natively in future. I think this is a strong approach than bloated UI frameworks like React. See [</> htmx - high power tools for html](https://htmx.org/).

## Typer

- Status: Adopt

I'm a big fan of libraries that use decorators etc. effectively so you can write your code as you normally would and it "just works" to turn it into e.g. a CLI tool as is the case with Typer. There's an extra appeal with it using type hints to do some magic that other libraries like `clize` need help with. I certainly don't know why anyone would continue using `ArgumentParser` in Python today.

See [Typer](https://typer.tiangolo.com/).
