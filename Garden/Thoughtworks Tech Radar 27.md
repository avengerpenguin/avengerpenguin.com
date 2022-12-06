Notes and thoughts about the 27th volume of the Thoughtworks Tech Radar.

## Techniques

### Hold

Satellite workers without "remote native".

- Remote workers are starting to be exluded again from meetings etc. as we move into a more hybrid model.
- With remote workers, it's easy to add more people than is necessary to meetings.
- People remoted into a meeting room can't always hear everything being said.

Superficial cloud native.

- There's a return to the "lift and shift" of deploying monoliths on top of cloud vendor services as opposed to rethinking to maximise the value of cloud architecture.
- Elasticity is a key feature of true "cloud native"
- Thought experiment: can I turn it off automatically if it's not under load?

### Assess

CUPID

- A follow-on from "SOLID"
- Dan Terhorst-North's attempt to describe "properties" over "principles"
- Composable: plays well with others
- Unix philosophy: does one thing well
- Predictable: does what you expect
- Idiomatic: feels natural
- Domain-based: the solution domain models the problem domain in language and structure
- Properties lead to "joyful" coding.

### Adopt

Team Cognitive Load

- Comes from "Team Topologies"
- Measure the amount of knowledge needed for a team to get things done
- For example, a "front end" team might need to understand the whole business if they're the front layer to everything else
- Seems to feed better into cross-functional, vertical teams that own a domain slice, but across multiple technologies (e.g. microservices)

## Tools

### Trial

Excalidraw

- Online, collaborative whiteboard
- Makes diagrams look rough and hand-drawn

xbar for build monitoring

- Build failures on the Mac menu bar

### Assess

Teller

- Puts secrets in environment variables
- Uses multiple sources

### Hold

Online services for formatting or parsing code

- Using online JSON/YAML formatters
- Pasting potentially sensitive info into 3rd parties
- JSON from log files could have personal information -- would be a GDPR violation or even _exporting_ of personal data if the service is hosted in another country


## Platforms

### Adopt

Backstage

- Facilitates finding documentation for APIs (API Catalogue)
- Uses Markdown TechDocs
- Delegates writing of docs to the local repo, but centralises the discovery
- Can enable one-click quickstarts for projects
- Includes Kubernetes monitoring and management (from a service view, not a K8s admin view)
- There's quite a lot to it so it needs some management for rolling it out

### Assess

Dragonfly

- Alternative to Redis
- Uses new ring buffer algorithms
- Still uses LRU for evictions
- Provisional cache mechanism avoids high churn and thundering herd after outage

OrioleDB

- New storage engine for PostgreSQL
- Designed for SSD and NVRAM (original Postgres engine optimised for hard drives)

IAM Roles Anywhere

- Get temporary credentials to AWS services from outside of AWS


## Languages and Frameworks

### Assess

JonRunr

- Alternative to Quartz
- Job runner with built-in dashboard
- Schedule tasks and cron jobs via lambda expressions

Stable Diffusion

- Generates images from text prompts like DALL-E
- Raises more questions around the ethics of using artists' work and style
- More broadly, crowd-sourcing data with permission raises questions

Carbon Aware SDK

- Helps software to use less carbon

### Adopt

Kotest

- Previously KotlinTest
- Sensible default over JUnit
- Property testing built in
- Fluent DSL
- Rich matchers
