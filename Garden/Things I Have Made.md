This is a overview of various projects I am currently working on or have built in the past.

## Voltaire

[View Github repository](https://github.com/avengerpenguin/voltaire)

This is a bit of a "glue" project for the [Pelican static site generator](https://docs.getpelican.com/en/latest/) to provide a set of defaults and hooks to automatically "plug in" useful add-ons like search, google ads, etc. based on config.

The intent here is to provide minimal bootstrapping between creating a new vault in [Obisidian](https://obsidian.md/) (or indeed any method of managing a directory of markdown files) and a fully-feature static site.

The mission is to reduce overheads such that it is possible to manage multiple sites, apply broad updates across them all but still be able to configure things differently in each one where they need to diverge.

## Weblint

[View Github repository](https://github.com/avengerpenguin/webcheck)

A project wrapping [Scrapy](https://scrapy.org/) to provide a way to crawl and "lint" a whole website. The primary aim at first was to look for broken links but the vision is to create a full test suite for static sites which will pair nicely with Voltaire above.

## Hyperspace

General-purpose REST and hypermedia client written in Python. Implements support for multiple hypermedia types using Mike Amundsen's [[H Factor]] model.
