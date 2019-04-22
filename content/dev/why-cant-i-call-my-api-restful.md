Title: Why can't I call my API RESTful?
Slug: why-cant-i-call-my-api-restful
Date: 2017-02-19
Status: published
Tags: REST, Semantics, HATEOAS

Semantic debates are fun, aren't they? I can build an API and call it
a REST API, then someone can say it isn't truly REST and now we're
back to arguing about what is and isn't REST.
The most common point of contention is whether or not to follow the
HATEOAS constraint.

## HATEOAS

For those not familiar,
[HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) is one part of the
"Uniform Interface" constraint. Let's look at those constraints
in full for context:

* **Identification of resources** -- This basically amounts to using URLs
  for each resource as described above (assuming we're using HTTP as the
  protocol, of course...)
* **Manipulation of resources through representations** -- Send a
  resource represented in e.g. an XML or JSON format of some kind and
  that should be enough for a client to read or update the resource.
* **Self-descriptive messages** -- Use headers like `Content-Type` to make
  it clear how to parse responses.
* **Hypermedia as the engine of application state (HATEOAS)** -- A
  client should only be able to move between resources by following
  hypermedia links and controls on a particular representation.

The definition of HATEOAS above is an attempt to summarise it in a
single sentence, but if you're not familiar with it at all, it's not
likely to be any clearer that that actually *means* but also *why* you
might use it.

In fact, Roy Fielding -- who
[coined REST in his famous PhD thesis](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm)
-- has himself in the past
[attacked HTTP APIs](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven)
that claim to be "REST" APIs when they do not. There have also been
examples of
[disagreements on whether HATEOAS is needed](http://www.ben-morris.com/the-restafarian-flame-wars-common-points-of-disagreement-over-rest-api-design/)
for a REST API. That there is a significant level of confusion or even
disagreements and arguments suggests a lack of clarity around what
HATEOAS truly is and why you might use it.

The argument usually boils down to people pointing
that out failure to follow the REST constraint does not a REST API
make. The common retort is that it is *zealous* or purist to ask for
this constraint to be followed.

A whole camp of API designers will furthermore claim the
REST-minus-HATEOAS architectural style to be valid in its own
right. Some even use terms such as
[Pragmatic REST](http://www.ben-morris.com/pragmatic-rest-apis-without-hypermedia-and-hateoas/) to describe/justify/differentiate their "non-purist" API design.

What's missing in these arguments? Something that's missing
in a lot of discussion on the web about this: any concrete discussion
of the properties of the thing originally built.

## Semantics

There's two distinct fallacies that appear when a debate around a
definition or semantics emerges:

* we talk too much about whether something truly fits a definition
*without actually discussing the merits of that thing*; or
* we dismiss opinions of those who disagree with us by incorrectly
regarding a debate as being "just semantics".

If you already have an opinion on the REST vs. "pragmatic" debate, you
might well recognise one of those fallacies in those with whom you
disagree, but be careful of falling into the other fallacy in your
own views.

Both of these fallacies can be seen as extreme ends of a spectrum where
at one end we get sucked into pointless debates over definitions and at
the other end we see no value in discussing definitions *at all*,
which is also irrational.

It is indeed the case that an argument about whether my API is RESTful
or not is not going to make much progress if we only discuss back and
forth as to what REST is or whether it's useful to use the word only
in a purist sense or whether we can allow for "pragmatic" takes on the
term. What's lacking here is discussing it
*in the context of the API I am building*.

Conversely, we should not be so quick to shoot down those that point
out where my API does not conform to REST. It is tempting to call such
a person zealous or a purist and frame any of their arguments as
irrational and therefore not worth hearing by definition.

The more rational, balanced position is to discuss the definition in
terms of *why* all the REST constraints exist and also in the *context*
of a particular problem domain being solved by a "RESTful" API. Here
we can rationally see if the constraints not being followed would
help or hinder us; we can revisit the advantages brought by lesser-used
constraints such as HATEOAS. In this context, the definition is
certainly useful and we are not longer arguing "just semantics".

## Does it matter?

So, surely it's still my business whether I call my API RESTful or not?
Well, sort of.

Semantics -- as in the meaning of words -- relies at least to some
extent to people loosely agreeing what words mean. If you present
a software system or a technology and use certain words to describe it,
then expect confusion when you use a word differently to how others
use it. I'm not saying we need to be overly pedantic about words, but
if you build an API and call it RESTful, expect some confusion by
some who will expect to call it in line with *all* of the REST constraints.

In some ways, I would plead with people to avoid using the term REST
if they are consciously choose not to follow the architectural style
fully, but I fear we may have lost control of the term by now to the
point where it's hard to trust any meaning has been followed. In
practical terms, it means that if someone presents an API to me and tells
me it's a REST API, I still don't quite know what to expect until I
see it. It is less than ideal for any word to get to a point where
it doesn't actually convey information any more. This is especially
true in a technical industry like software engineering.

So, technically you *can* call your API what you want and really the debates
should centre around what is and isn't useful for the problem you
are trying to solve. However, it is worth being mindful of what you
are intending to communicate when you use a technical term. Expect
people to be confused if you follow a mutated definition of a term.

I personally like to follow they hypermedia/HATEOAS constraints for
RESTful APIs and in later posts I'll discuss why that is and the
decoupling people are missing out on. It is also my contention at times
that if you do not want the full decoupling of REST in our distributed
systems, then it's questionable why you needed to use any of REST in
the first place. That certainly warrants a whole other post.
