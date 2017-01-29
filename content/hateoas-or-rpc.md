Title: It's either HATEOAS or it's RPC
Date: 2017-01-29
Slug: hateoas-or-rpc
Status: draft

Life is simple when you are working with only one
computer. Distributed systems are hard.

In fact, if you build software for a living or a hobby, can you think
of a time you last wrote something that didn't involve some kind of
inter-machine communication? Even with the shift back to bigger client
apps on smartphones, many require communication back to a central
service via an API.

It's arguably safe to assert even without real evidence that the most
common -- if not one of the most common -- approaches taken in
client-server architectures is for the server-side to present a
so-called *RESTful* API for the client application to consume.

## The REST Architecture

Many software developers, particularly those building web
applications, will have a passing familiarity with the REST
architectural style in simple terms:

* Different URLs are used for different "resources".
* You use all the HTTP verbs correctly: `GET` is read-only and
  cacheable, `DELETE` is used to remove a resource, etc.
* All requests are kept stateless.

And we're done. Oh, what's that? I forgot to talk about HATEOAS?

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
for a REST API. The argument usually boils down to people pointing
that out failure to follow the REST constraint does not a REST API
make. The common retort is that it is *zealous* or purist to ask for
this constraint to be followed.

A whole camp of API designers will furthermore claim the
REST-minus-HATEOAS architectural style to be valid in its own
right. Some even use terms such as
[Pragmatic REST}(http://www.ben-morris.com/pragmatic-rest-apis-without-hypermedia-and-hateoas/) to describe/justify/differentiate their "non-purist" API design.

I'd like to take a totally-non-zealot, rational position on this:

1. Of course you can build a working API following all REST constraints minus HATEOAS (many people clearly do it every day!)
2. If you do build a so-called "pragmatic REST" API, then calling it REST might invoke ire from purists, but more importantly it's not helpful to call it REST.
3. Whether you should is ultimately up to you, but you're missing out on some of the core benefits of the REST architectural style (and why it exists)
4. Also, if you're not going to benefit from the advantages of the REST architecture, it's not clear why you need to follow some of the other constraints. You might be making a trade-off you don't need.

I will attempt to justify these statements one-by-one, with the exception that I hope that 1) is obvious.

## Why can't I call my API RESTful?

Semantic debates are fun, aren't they? I can build an API and call it
a REST API, then someone can say it isn't truly REST and the classic debate quickly emerges.

What's missing in that hypothetical argument? Something that's missing
in a lot of discussion on the web about this: any concrete discussion
of the properties of the thing originally built.

This happens in multiple fields:

* Is some musical genre "real" music?
* Is modern art really art?
* Is this leader truly left wing?
* Is this programming language really a functional language?

The debate has broken down to arguing the ontological commitments made
by assigning something to a class or category, rather than discuss the
thing originally being discussed. Consider the productive discussions
we could have with each of these examples:



## Advantages of HATEOAS

### Why was REST even created?

### What is HATEOAS?

### Why is HATEOAS a good thing?

## Other RPC Approaches

### Java RMI

### CORBA

### Thrift and Protocol Buffers

### SOAP

### JSON-RPC

### Where these are better than REST

### Are any of these appropriate for me?
