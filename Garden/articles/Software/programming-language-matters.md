Title: Why Programming Language Matters
Date: 2018-03-14
Status: published
Category: Software

Choice of programming language can be a source of religious wars
between software engineers and developers. It is one of the many areas
where people build a subjective opinion based on how "nice" or
"elegant" something is and whether they get joy working with it or
whether they find themselves fighting the language or tool every step
of the way.

Clearly, this is going to vary person-to-person as people's mental
models vary, as their idea of elegance varies and whether a technology
differs greatly from other tools with which the developer has a lot of
experience.

Due to the strong influence of subjectively, it is common for people
to put the programming language debate into the same camp as arguing
over tabs versus spaces for indentation or reoccurring arguments
around editors. All programming languages can do the same things, but
vary in their approach, so some feel it is a waste of time trying to
argue as if there are objective measures of quality.

I recently saw a strong example of this stance in the opening session
of [QCon London 2018](https://qconlondon.com/). Someone running a
track on using various languages in the back end asked the room if
anyone felt that choice of language mattered in back end applications
and only minority of people raised their hand who were then told they
were "wrong" if they felt it mattered.

I am someone who raised their hand and I would like to explain why it
is not "wrong" to care about choice of programming language in our
applications.

This is not meant to be a counter-argument or strong disagreement
though. My intention here is to expand on a deliberately blanket
statement like "it doesn't matter" as I think there is much value in
exploring the nuances on where that statement is true and where it is
false.

Firstly, I want to acknowledge the things that absolutely do not
matter (most of the time) so I do not give the impression I am
defending religious or flame wars. Then I want to remind the reasons
why subjectivity is important at times before finally unpacking what I
think are truly objective things that matter about a programming
language.

## Things that do not matter

I fully understand people who take the "it doesn't matter" stance
since most debates or discussion on language choice focus on trivial
aspects, things that people just do not "like" and other subjective
things.

### Whitespace

Yes, Python uses whitespace semantically and other languages do
not. No, it does not really matter. I personally like it as it removes
the redundancy of using braces, for example, to determine scope and
then also indenting for readability — i.e. when I indent I achieve
both scope and readability at once. If you do not like it, then that's
fine too and it doesn't affect your application at the end of the day
if you just get used to it or have appropriate tooling.

### Boilerplate

Yes, Java is verbose and Scala is not. Does it _really_ matter for
your project? Only if that boilerplate soaks up real time, which is
rare with appropriate tooling. Personally, I prefer to get going more
quickly with Python but that's because I like to do rapid prototyping
where I think there are some objective arguments that you can move
faster in more expressive languages. However, in that case you are
probably always better prototyping in languages you _know_ well, which
makes this a subjective point again.

### Typing (sort of)

With appropriate testing, you do get away with achieving the same
results with or without static or dynamic typing. There are debates
around bug rates and I have even personally seen bugs in Node.js
applications that any type checking would have trivially caught. I'll
leave it as an exercise for the reader to determine if there is
objective evidence around type checking and bugs.

For now, I'll assume this to be a subjective matter for the purposes
of my argument.

### Performance (sometimes…)

It was common maybe 10 years ago to hear lots of arguments that Python
was demonstrably slower than Java (or other languages) in a few
cases. I've not been following performance benchmarks recently, so
maybe the argument went away because Python is faster now. However, I
heard a very convincing argument from a speaker at PyCon UK around
that time in that Python (in her view) saves _developer_ time — which is
expensive — while trading off CPU time, which is arguably a lot
cheaper than developer salaries now.

So, while you could choose a language for optimal performance on the
back end of a web application, you might be delaying delivery (which
is what you get paid for) for the sake of performance tuning.

With the modern landscape of cloud computing, autoscaling and
serverless architectures we can paper over any need to micro-manage
performance with
caching,
[horizontal scaling](https://en.wikipedia.org/wiki/Scalability#Horizontal_and_vertical_scaling) or
[breaking up monolithic services](https://martinfowler.com/bliki/MonolithFirst.html). Of
course, I am not advocating for throwing performance out the window,
but we can obsess too much about milliseconds here and there when
really we're paid to deliver value not necessarily on CPU cycle
efficiency.

I hope it goes without saying that there are clearly embedded use
cases where high efficiency is key, but my focus here is on enterprise
and web applications.

## Sometimes subjective things do matter

I know this is not necessarily the intent when someone states that
programming language choice "doesn't matter", but it does avoid the
human side of the issue in that developers' happiness is important
too.

I think the assertion that all programming languages are equally
capable for a web back end comes from a very technical viewpoint
where, yes, a Ruby service could be rewritten in Rust and would work
equally well.

So, technically, yes, language does not matter if all that matters to
you is the technical capability.

Software engineering teams are made up of people who will have
personal feelings about languages, who will have various levels of
experience with languages and might even have various levels of
general software development experience. There's a reason Python gets
suggested to new programmers.

If a team is about to work on a new project, then factoring in
people's knowledge, opinions and, yes, even feelings is not wholly
irrational. In this context, it is objectively the case that a team
whose subjective needs are met will deliver the project sooner than a
team who is forced to work with tools they are unfamiliar with.

I realise that means I could be interpreted as supporting the argument
that "PHP is good because so many things are written in it and it's
easy to deploy." I do not
feel good about this and can only apologise.

## Objective differences that do matter

Does all this mean that there is no right choice of programming
language for a given application? Is it just about choosing something
you like or are some tools a better fit for certain jobs?

The argument gets thrown around that all languages are equally
capable. They are, after all, all Turing Complete (or we would not
likely call them programming languages at all) and for every
functional solution to a problem, you can rewrite it in an
object-oriented or imperative way. We know this is the case as there
are whole collections of solutions to things like the Towers of Hanoi
in multiple languages.

So, in this sense, all languages are capable of solving (nearly) all
problems, but are some objectively _better_ at certain problems? What
things make a language better?

### A language is more than just a language

As with the subjective differences, I do actually agree the choice
"doesn't matter" in the very technical sense that you could build
anything in any language (assuming you had people that knew it well or
time for them to learn). And again I disagree with that viewpoint on
the basis that it's missing a wider context that is important for
actual engineering of business systems and web applications.

The key piece missing here is considering a language in terms of its
syntax and semantics only, but in the real, applied discipline of
software engineering we do more than just write code. We also build
and deploy that code. We pull in dependencies, write tests and build
on top of frameworks.

It is important to consider the effectiveness of a language not just
in terms of the language, but the ecosystem and community built up
around it.

### Use cases where one language dominates

Consider how many people got into Python because they wanted to
use [Jupyter](http://jupyter.org/), [Numpy](http://www.numpy.org/)
or [Django](https://www.djangoproject.com/). Was it not just as good
to use PHP to get into data science? I mean, you _could_ implement
many machine learning algorithms yourself in PHP or JavaScript, but
why would you if you wanted to see results right away?

I personally only learnt Ruby because
of [Cucumber](https://cucumber.io/)
and [Capybara](http://teamcapybara.github.io/capybara/). I learnt some
Scala because of [Apache Camel](http://camel.apache.org/)
and [Groovy](http://groovy-lang.org/) due
to [Jenkins pipelines](https://jenkins.io/doc/book/pipeline/). Some of
these can be done in other languages, but there is a clear "right
choice" for many of these applications.

It is this capability in the _available libraries and frameworks_ that
I think is one of the strongest objective considerations around
language choice. It doesn't have to be the only consideration as you
can still use less mature libraries in a language your team is
familiar with if you understand what you're trading off.

A lot of experimental projects I do deal
with [Linked Data](https://en.wikipedia.org/wiki/Linked_data) and the
Semantic Web for which I
find [RDFLib](https://github.com/RDFLib/rdflib) — written in Python —
to be extremely powerful. It is useful for building applications that
deal with RDF which much of the details around the various RDF formats
abstracted away. In fact, I am yet to find an equivalent in _any_
other language where a common Graph model can be parsed out of various
formats. Most implementations elsewhere only deal with one format at a
time, so I always come back to Python when I want to move quickly and
not write objectively more boilerplate code.

### Alternatives can be less mature

I should expand a bit more on the Cucumber and Apache Camel examples
as someone is bound to point out
that [CucumberJVM](https://cucumber.io/docs/reference/jvm)
and [Cucumber.js](https://github.com/cucumber/cucumber-js)
exist. Also, there are other behaviour testing frameworks such
as
[Lettuce](http://lettuce.it/), [Nightwatch](http://nightwatchjs.org/)
and [Behat](http://behat.org/).

Apache Camel is just one implementation of message routing and there
are other ways to solve some of the problems it offers to solve.

However, it is this exact trap I want to highlight: a lot of the time
the tool in your preferred language could be less mature or playing
catch-up to the more established player. This might be ok for your use
case as the core features are enough for you or the familiarity of the
language is a strong enough consideration that you are willing to take
on the extra cost of implementing missing functionality, but so long
as you understand the choice you have made.

I have anecdotally seen too many people reach for alternatives to
Cucumber simply because they "don't like" Ruby, but without even a
moment's consideration of the sheer maturity of the ecosystem around
Cucumber, Capybara and RSpec. In this case, they are allowing a
subjective choice trump objective considerations and sometimes twist
the "language doesn't matter" argument to support going with their
preferred choice.

Node.js has matured recently and big, well-known frameworks like
Express.js have a lot of traction, but I have see these technologies
adopted in large, high-traffic enterprise systems back when they were
far less mature.

I struggled with memory management in Node.js as if I were dealing
with the JVM in the 90s and encountered really basic bugs like lack of
connecting pooling or socket reuse in various NPM libraries. I still
struggle to find good library support for Cache-Control and Vary
headers in HTTP client libraries and spend objectively more time on
things I simply do not think about when I do the same tasks in a Java
or Python project.

All of these are solvable, but it felt like developers who like
JavaScript used this subjective opinion to choose a back end
implementation that objectively soaked up more time when it came to
the [DevOps](https://en.wikipedia.org/wiki/DevOps) side of actually
deploying the application. Like I say, there is nothing wrong with
using what your team knows well, but I have rarely seen
acknowledgement that there were objective advantages of other
technologies.

### Communities matter

One thing that I think has really helped Node.js mature is having more
of a community form in that area. Having conferences dedicated to the
technology and online discussion areas really makes a language better
to work with in the enterprise.

Most enterprise engineers will rely heavily on Github issues, Stack
Overflow and other online forums to do their jobs. If we encounter
errors, we need to be able to put the error message into Google. If we
are trying to make two technologies work together, we can find
complete solutions in blogs on how to configure them (e.g. if you
search for "nginx node.js" you get countless examples of configuration
you can lift to set nginx up as a reverse proxy in front of a Node.js
app).

The help is only there if a community reaches a critical mass such
that 1) they have probably encountered most of your problems before
you and 2) a culture of sharing, blogging and helping out learners can
emerge.

I think only certain kinds of enterprises (perhaps brave ones!) are
really in a position to adopt newer things like Go or Rust before the
community is really established. There's a reason the JVM is still a
safe choice for the more cautious enterprise. I'm not saying bravery
is bad and I think many enterprises could do with being more
experimental and forward-thinking at times, but everything in
moderation or you won't actually deliver anything.

One of the things that keeps bring me back to Python is the
community. I can see newer users coming to the language for data
science or as children and there is a culture of nurturing and helping
inexperienced users.

## Programming language matters if you to do more than just "program"

I have played with semantics a bit here, but I think it's an important
message. Programming language doesn't matter if all you are doing is
programming -- i.e. just writing code -- but software engineering is
more than that.

As engineers, we are solving problems through code. We might want to
reuse solved problems in the form of libraries or we might want to
draw upon frameworks that abstract away lower-level concerns so we can
focus on the higher-level problems.

We want to create good teams that solve problems more quickly and more
effectively that one engineer can do alone.

Choosing a programming language will affect your ability to solve
these problems. Choosing different languages will have different
effects on your teams.

If you are truly a software engineer, I think it does matter to
consider your language carefully.
