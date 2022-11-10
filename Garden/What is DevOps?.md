A common problem with any buzzword coined in the software industry is that we struggle to pin down a precise definition.
This is almost certainly the case with _DevOps_ with multiple companies, blogs and experts using the term to mean different things.

With a systems mindset, all the definitions out there are arguably all correct at some level, with the "true definition" actually dependent on what level of abstraction appropriate to the situation.

### My definition

I find it useful to use a definition of _DevOps_ (or indeed any other term) that is the most general while still being precise enough so we are clear what things fall under that term and what things do not.
To that end, my preferred definition of _DevOps_ is:

> Any practice, technique or tool in the software industry that is intended to speed up delivery of software changes.

First, allow me to unpack some of the parts of that definition and then I will explain why the definition around the intent to "speed up" is the correct focus.
Finally, I will discuss how various practices and implementations we may be familiar with fit nicely within the resulting "DevOps" umbrella that follows from this definition.

### Practices, techniques, tools

A meme in blogs on this issue (with [Atlassian](https://www.atlassian.com/devops) an exemplar of this) is to emphasise DevOps as "cultural" or "philosophy" in contrast to specific technical practices.
Again, with a systems mindset, is is both -- just different things to different people at different levels of detail, but nobody is "wrong".

This is why I am keen to follow a definition that loosely allows for anything so long as the goal of speeding up delivery is achieved.

Do you practise Lean or Kanban to encourage small, incremental batches of change to go all the way to production as often as possible?

That's DevOps.

Do you employ techniques such as feature flags to make it easier to makes changes even more incremental?

Then that's DevOps too.

Do you make use of infrastructure as code tooling such as Terraform or use Docker to make it easier to keep development and production versions of code the same?

Also DevOps.

Note that we can acknowledge that engineers might consider the tools "their" way of viewing DevOps, but there's a definition that suits product managers too.
Everyone is equally correct to use their definition as they all fit under the umbrella of things that make us go faster.

### Software Changes

This definition stops short of saying features, preferring a looser term of "software changes". What does that encompass? A non-exhaustive list for consideration is:

* New features for users rolled out to a website
* New features to a library released to be used by other software applications
* Bug fixes in any of existing features in websites, libraries, applications
* Reconfiguration of production systems, such as increasing memory on a server that is struggling
* Changes to text copy


<a title="Kharnagy [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Devops-toolchain.svg"><img width="100%" alt="Devops-toolchain" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Devops-toolchain.svg"></a>
