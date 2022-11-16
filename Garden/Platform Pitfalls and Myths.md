When building an internal platform for an organisation, there are a few traps people fall into.

The breakdown of this is largely thanks to [Scaling your business with platform thinking by Thoughtworks](https://www.thoughtworks.com/en-gb/what-we-do/enterprise-modernization-platforms-cloud/empc-hub/scaling-your-business-with-platform-thinking) with details filled in with my own experience with successful and unsuccessful platform initiatives.

For how to get it right, see [[Tenets for Platform Sucess]].

## 1. Build it and they will come

This is arguably an extension of product iniatives in general without fully understanding customer need or establishing effective feedback loops.

Sometimes we can be so sure we see a need for a platform or framework we presume people will simply _naturally_ want to come use it. This can be a combination of [Endowment effect](https://en.wikipedia.org/wiki/Endowment_effect) and [Escalation of commitment (aka Sunk costs fallacy)](https://en.wikipedia.org/wiki/Escalation_of_commitment) leading us to value the platform more than its potential customers.

There is a nonzero overhead and cost for customers to discover, understand and learn how to adopt your platform. That cost might even be higher than a team proceeding (at least initially) to build the capabilities themselves (especially when they already have the knowledge to do so).

I prefer to consider it in terms of Ecomonics or a market -- what is the incentive to use your platform over other options? This is very clear in open source tools -- users will adopt a framework when it clearly makes their development experience better and avoid them when the cost of adoption is too high.

## 2. Mandate to increase adoption

A natural follow-on from above is to use a high-level mandate within the business to force adoption of a platform. This is especially common in reaction to hitting the reality of the "build it and they will come" myth where in fact, they do not automatically come.

Again, arguing from Economics or indeed human behaviour, we can clearly empathise with the idea that teams will not willingly adopt a platform that only adds coupling to other teams or friction to their workflows.

## 3. Platforms help you beat Conway's Law

Conway's Law states that "Organizations, who design systems, are constrained to produce designs which are copies of the communication structures of these organizations."

Common outcomes of this include systems not being joined up if there is too much communication friction.

A temptation here is to build a platform that encourages everyone to collaborate, but organisational friction should be fixed by team structures and topologies. A platform cannot magically fix organisational friction (and again, the temptation is to mandate adoption when existing friction prevents it happening naturally).

## 4. Platforms are monoliths

Another temptation is to build platforms as a singular monolith with a highly-abstract API and a single use case.

In reality, successful platforms are a set of loosely coupled capabilities where teams can perhaps adopt it partially where they have solutions for some functionality already. Or theyy may wish to orchestrate the capabilities in newer ways.

The capabilities should be arrange to create a meaningful experience, built around use cases as they emerge.

