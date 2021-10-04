Title: Mocking Nothing But Data
Date: 2018-02-05
Slug: mocking-data-only

There are a variety of arguments out there around the most effective
approaches to software testing. We have unit tests, functional tests,
smoke tests, property tests, integration tests, regression tests,
end-to-end tests, user acceptance tests and many more. Many of these
terms overlap and clearly a combination of these approaches is
required to get a true picture of whether our software is working as
intended.

We need isolated "unit tests" to give rapid feedback as to whether our
functions or algorithms are correct and whether edge cases are
effectively covered. However, these tests do not prove that the
various components assemble together to provide a cohesive, working
application. This is where end-to-end or acceptance tests come
in. These are usually more holistic, but come at a cost in that the
feedback loop can be far slower given the need to compile every
component and stage the application somewhere. For example, a mobile
app might need the latest iteration installed across multiple mobile
devices and then tested by hand.

I want to focus today on the area of unit testing, particularly in
modern software development where we commonly pull in multiple third
party libraries to do as much heavy lifting as possible. I believe
this has a lot of impact on how we think about unit testing today and
we might need to update our patterns and beliefs.

Specifically, I want to talk about the practice of mocking (or
stubbing) in unit tests and whether approaches to date even make sense
in the current software engineering landscape.

First, we must briefly look at how the composition of a modern
software application has changed over the last two to three decades.

## A little (personal) history

I personally started out with Java, PHP, Delphi and bits of Python and
JavaScript around the turn of the century (something like 1998 to 2002
for this period and I am not counting learning BASIC as a child around
1992). This brought me to these ecosystems later than some engineers
older than me, but notably early enough to experience writing simple
code projects with no package managers, no build "tools" and no
Github.

For PHP, there was no *composer* to download packages and I got by
with a zip file download of PHP and Apache HTTPD on Windows 98 (later
XP) using only the PHP standard library. For help, I had an offline
copy of the php.net documentation since dial-up Internet took long
enough to get the zip files.

For JavaScript, you could easily observe code on other websites to
learn the language (minification was rare) and, again, a simple text
editor like Notepad was enough and you can test HTML and JavaScript in
a browser locally quite easily with `file:///c:/My Documents/...`

For Java, I wrote code in a text editor (even in Notepad) and used
javac to compile "`*.java`". It was some years later before I would
even use *Ant*, let alone *Maven*.

In fact, I acquired the JDK for the first time by being handed a pack
of four Java CDs at a University open day. Across these CDs were the
JDK, other esoteric tools and offlne copies of the Javadocs for the
Sun Java standard library.

Why am I telling you all this? It's to paint a picture of how
downloading libraries from Github or package repositories is as easy
as breathing today, but there was a time when downloading a useful JAR
or JavaScript file was something you did by hand, so therefore did ad
hoc and less often. And I believe it shaped the composition of our
code bases.

## The rise of library use

I came to the industry a little after this period, but early enough to
work on do medium-sized Java web applications (Apache Struts) where a
significant percentage of the overall code was written by me. I (and
many other people) did not yet have a culture of trying to download a
third party library for every little "already-solved" problem.

It's not as if I was implementing from machine code up to a full HTTP
stack though. The Java standard library is doing a significant amount
of heavy lifting, the JVM is abstracting the OS system calls away from
me and frameworks like Apache Struts, the Servlet API (and Tomcat),
etc. probably end up marginalising my code to a small percentage of
the overall application. This is the "standing on the shoulders of
giants" that is crucial for the software industry to move forwards
year on year.

However, note that I can just about name all the platforms, frameworks
and libraries in a single sentence. In contrast to that, if I print
out the dependency tree of a more recent Java project, I see hundreds
of packages.  It's also a running joke in some circles that the
`node_modules` directory in a typical Node.js project can fill your
hard disk. It's not quite that extreme, but I have one project where
the `node_modules` directory totals over 600MB!

Another Node.js project I work on professionally has merely 100MB in
its `node_modules`, but that space is taken up by 590
dependencies. This is certainly no longer a list I can recall from
memory. Notably, it's also a list where -- on inspection -- I do not
even recognise some of the libraries I have supposedly downloaded that
are supposedly necessary for my application to run (this is likely not
to be true, but that's a whole other topic).

## Why did this change?

The turning point as far as I can see was the moment we automated
dependency resolution.

For Java projects in the 1990s, you might be willing to downloading a
JAR file for a useful library and put it on your CLASSPATH and compile
against it. If that library then had other dependencies, then you have
to track them down and put those on the CLASSPATH too. This clearly
dissuades library developers from having too many dependencies
(otherwise the library is too difficult to use) and encourages
application developers to solve simple problems themselves rather than
search for a library.

I had similar experience with JavaScript around the year 2000 in that
I was happy to download the odd library like jQuery and sometimes
another library (jQuery UI being one of them) would itself *depend* on
jQuery, but downloading two JavaScript files and writing two
`<script>` tags into my page was not too difficult.

With Java, Maven changed the cost-benefit ratio of library
usage. Today, it would be surprising to see people scatter their code
with helper functions for strings or dates when we have Apache
Commons, Jodatime, etc. For really difficult domains like time and
date manipulation, this is really important as you're delegating (and
centralising) effort to cover all the edge cases and domain
expertise. But for a simple helper that checks both if a string is
null or an empty string at once, this might seem less important, but
we bring in Apache Commons anyway as it's almost as cheap as
copy-pasting the solutions.

## How does this affect our code?

I think there are two crucial changes this effects in modernising
software development:

* it is possible to write an application with very little code
(e.g. microservices)
* the increase in quantity of dependencies causes great variation in
the quality of those dependencies.

Allow me to expand a little on both of these.

### Smaller code bases

The most extreme example I can think of where I have built very
powerful services with very little code has been when I worked in
messsage-based integration projects with ActiveMQ and Apache Camel.

For those who have not used it, Apache Camel is a full implementation
of Enterprise Integration Patterns in that it provides all the
building blocks for reading data from a variety of sources (IMAP,
HTTP, ActiveMQ, AWS S3/SNS, etc.), manipulating each chunk or
"message" of data (transformation, filtering splitting into smaller
chunks, aggregating into bigger chunks) and then sending that data to
some destination (again, IMAP, HTTP endpoint, etc.).

The main logic of your message-routing application is defined in an
implementation of their `RouteBuilder` that is essentially a
Domain-Specific Language (DSL) run once at start-up as configuration
and now you have a full application capable of solving a business
problem, potentially having only written the one Java class. This is
because of how much comes out of the box with Apache Camel.

Combine this with Spring and a Servlet container like Tomcat and with
perhaps only two configuration files (either in Java or XML) you can
have a web service that does something useful.

Another example is the Django framework in the Python world. Those
that use the framework refer to it has having "batteries included" due
to the amount that it does out of the box. From a simple project
skeleton you can have working authentication, a database set up and a
full admin interface that lets you manipulate any data models you
later define. In fact, the admin interface is so mature and polished
that many agencies and freelancers simply skin it nicely and present
to clients as the back end inteface for all web apps or web sites they
build.

The Django community likes to build and share "apps" for reuse within
the framework, so if I have a need for e.g. some ability to have
people rate or vote on some object in my database (for example, voting
up and down articles they like/dislike), then I have an app I can pull
in and mainly glue into my main project.

I think it's clear that you can make very powerful applications today
with very small amounts of code. I will cover how this affects unit
testing shortly.

### Quantity vs. quality of dependencies

Not only is it cheap to add dependencies to a project and quick to
download them, but it is also cheap to *publish* packages today.

A natural effect of this is that we have a long tail of libraries that
work fine for our use cases, but are lower in quality than very mature
frameworks.

This is not a comment on the ability of competence of individual
programmers.  It is true that less experienced programmers can publish
a useful package as part of their learning, but even very skilled
developers might quickly wrap up some business logic in a nice
package, but not have the time nor incentive to work out all the edge
cases or ensure full test coverage.

Perhaps this is a shift from big libraries being backed by large
companies to individuals being able to compete by fully writing,
publishing and maintaining a useful package all without help.

Note that also these individuals are so empowered to publish useful
open source code because they themselves can pull in dependencies and
build value on top of other people's work.

And so the cycle continues and I end up with a project with 590
Node.js dependencies. In fact, it seems that this effect is
exaggerated in newer ecosystems like Node.js. There is a combined
effect of multiple people publishing solutions to the same problem
rather than use each other's code (how many implementations of
promises are there?) and a culture of pathologically preferring reuse
via packages even for simple problems (see: left-pad or isarray).

This reduction in average quality of packages combined with our own
code shrinking with respect to the amount of code reused I believe
requires us to rethink traditional wisdom around unit testing.

## Unit testing: conventional wisdom

The principle behind "unit" testing is that you are trying to test
only a single function, class or module at a time. The advantage of
this is that the moment you introduce a bug to a particular block of
code, the tests for that block -- and only the tests for that block --
fail immediately and you know your most recent change must be the one
at fault.

In contrast integration testing might cover two or more components
working together and therefore any test failures indicate potential
fault in either component (or both). Conventional wisdom tells us the
failure is harder to pinpoint in this case, so it is better to have a
unit test fail before we get to that point.

