In a microservices architecture, it is inevitible that there will be duplication of work between different product teams. It is a somewhat necessary overhead that each team will have to do their own deployments, pipelines, automation and other fundamental work as a trade-off for having autonomy over their own product or service.

Therefore we must keep in mind two key things when considering a microservice approach:

1. Do we understand where and when to use microservices, what they are for and -- crucially -- when _not_ to use them?
2. How can we manage to minimise _wasted_ effort on duplication in this "heavy lifting" work common to all microservice product teams?

## Naive Solutions

I use the term "naive" in a sense that fits well with Computer Science -- that is, a naive solution or approach is the "obvious" one you start with as a first pass and then try to improve. This is similar to the red hat in [Edward de Bono's Six Thinking Hats](https://www.mindtools.com/pages/article/newTED_07.htm) -- it's a perfectly valid starting point, but then we can apply different thinking and do better.

### Return of the Monorepo/-lith

One instinctive reaction I have seen was the usual "hype curve" behaviour. Teams adopt microservices without truly understanding what they were for, hit all the issues with undifferentiated heavy lifting ramping up rapidly and then the natural reaction is to swimg back to monolithic approaches, but strangely not necessarily full monoliths.

There are a fair few trends at the moment to attempt to retain the Modular Aesthetic in a Mono_repo_ but either still deploy the parts independently or have some tooling to manage reassembling the parts into a single artefact.

The former gives you the worst of both worlds in that code changes across deployable parts are possible, but then deployments will not be atomic which could be problematic unless we specifically code or test for the interim state where the change is only briefly applied in one place before the second deployment finishes.

The latter -- deploying a single artefact -- avoids this but has a lot of complexity over simply organising code into directories. It is possible I have not fully understood the benefits.

In either case, this is a shift away from microservices which is good in cases where you have identified that microservices were not the right solution (yet?) but the "naivety" comes in if that shift to monoliths (or monorepos) is happening as a reaction to the undifferentiated lifting -- especially if it's reacting to a _perception_ that duplication is an issue without measuring that it is indeed an issue.

### In-house Frameworks

Another reaction to duplciated heavy lifting between teams is to try to create an in-house platform or framework on which everyone must build their services. The noble attempt is to create an abstraction that deals once with lower level concerns and then teams "just" write their business-level logic on top.

There are so many issues that can arise from this, it services better as a quick last to expand upon later:

- The [Inner-platform-effect](https://en.wikipedia.org/wiki/Inner-platform_effect) kicks in and we end up with poor replica of platform APIs provided directly by a Cloud provider.
- Something that arises from the previous point -- but also in other ways -- is that any in-house platform or APIs will require bespoke clients and command-line tools to create abstractions on par with open source tools like `awscli` or `terraform`.
- When your deployments are optimised for one approach, it may make it _more_ expensive for teams that simply need to deploy and build things differently for valid reasons. For example, there's little they can likely share in terms of tooling hard-wired for the in-house platform.
- It is easy to create single points of failure such that a bad deployment of the platform itself takes out your whole website or application, losing a key benefit of microservices -- particularly micro front ends -- where we get failure "bulk heads" that isolate outages to that part of the system.

## Managing Duplicated Heavy Lifting

So, if the previous appraoches are "naive", how do we manage undifferentiated lifting within a microservice architecture?

### Start with Monoliths

A good way to avoid lots of duplication is not to adopt microservices right away. This has all the benefits of retaining a monolith but notably avoids some of the "naive" solutions above where there are monolithic approaches _that naively attempt to retain the modularity of microservices_. As stated earlier, this appears to be a habit to retain a [[Modular Aesthetic]] -- where people like the "feel" of things being broken up without necessarily figuring out the best way to carve up and how best to do it.

Since [[Premature scaling can stunt system iteration]], a strong way to figure how the "best" way is to defer it and get there iteratively.

That is, start with a monolith service, avoid complex monorepo tooling and resist the urge to abstract out libraries, frameworks, etc. There is much to read on this such as the [Monolith to Microservices book](https://amzn.to/3n6Siou) and this allows a long term strategy along the lines of:

- Build a monolith system
- Find clear "seams" to break out some functionality into distinct services
- Note where you have to copy-paste code/scripts for build automation and deployment
- Accept there is some duplication for a while
- Over time -- and one at a time -- see if there's a robust way to abstract out build and deployment logic

What does that abstraction look like over time?

### Abstracting Automation

From observation and hands-on experience, I can see a set of clear "rules" (maybe guidelines) worth considering when trying to create good abstractions that reduce duplication between microservice teams:

1. **Iterate** -- first and foremost, we must emphasise that we won't solve all of it at once and up front. Without real world experience of the services we plan to build, we can't possible sink in up-front time to building all our tooling. In the most ideal cases, I have been able to have essentially zero explicit time put aside for developing tooling and have let it emerge while delivering business features.
2. **Open Source First** -- before writing _any_ code, it is worth thinking about how to be lazier about it or how to rely more on highly-maintained tools that already exist. Some might even get fun building their own tools to solve a problem and I think this drive falls out of that doing so in your own time is a great way to learn, but "Total Cost of Ownership" includes maintenance costs and not just the time it took to build. A custom script that took minutes to write could still be more expensive than a known CLI tool, a Jenkins plugin, a docker container, etc.
3. **Inheritance over Composition** -- perhaps a controversial way to phrase it (which I do to make people pause and think) but I argue that the Unix Philosophy tells us to make tools with sensible defaults, so a way to achieve this is to construct tooling such that each service "inherits" from a central place with local control to override. This is in opposition to having libraries of sharing functions but we still duplicate the coordination scripts that call those functions. That is, we should be making share tooling that encodes _flow_ and cedes control to the abstraction as opposed to simply wrapping up subroutines in function calls.
