Over the years I've worked on teams at various stages of how quickly they can ship software changes safely at pace. Anyone who has worked in a variety of companies will have some various examples on the spectrum from teams that manually verify and deploy changes (and therefore has a bias to batching lots of change together) to teams that are raising small pull requests/merge requests and shipping multiple times a day.

I have been for some years trying to assemble my own maturity model for Continuous Delivery in the year 2026 and beyond, particularly as I think it has implications for AI agents working on code.

Most of this is from my own independent observations but I am aware of the [Thoughtworks CD maturity model](https://info.thoughtworks.com/rs/thoughtworks2/images/continuous_delivery_a_maturity_assessment_modelfinal.pdf) from 2013. At the very least I hope to build on that over a decade later.s

## The Model

I will first lay out the model I am proposing then seek to justify it, improving these thoughts over time. Following that I have attempted to compare to and argue how my model builds on the Thoughtworks one from 2013 despite not really basing mine on it initially.

The following is a condensed version I plan to expand on in time. It also notes where each level enables AI automatic which is a topic I plan to cover in a future article.

- Level 0: **Manual Chaos**. **AI creates inventory, not throughput.**
- Level 1: **Stewarded Pipeline**. **AI can create change, but humans still steward in a repeatable process**
- Level 2: **Merge Means Prod Automatically Unless it Fails**. **AI can work as fast as humans can review**.
- Level 3: **Selective Autonomy for Safe Changes**.  **AI starts to shine in the safe, boring fixes.**
- Level 4: **Full Automated Change Cycle**. **Humans fully above the loop with observability as indicators along with an AI Andon cord.**

## Comparison to the original Thoughtworks model

In 2013, [Thoughtworks published a Continuous Delivery Model](https://info.thoughtworks.com/rs/thoughtworks2/images/continuous_delivery_a_maturity_assessment_modelfinal.pdf). It describes a progression from ad hoc and manual deployment patterns common at the time through to adopting CI and CD principles and eventually hypothesis-driven delivery.

This was relevant to the time. I myself was copying files to a server over Windows shared drives up until 2009. In 2010, it was considered cutting edge in the team I joined that releases were done after every two week sprint and while we had to manually asking Ops via Jira tickets to release our Linux package files, we had automation right up to the test environment from which those files were taken. Increasingly I noticed Ops were automating converting the release Jira tickets into deployment scripts. Crucially, our sandbox and test environments were designed from the start to be production-like which is noted in level 2 of their maturity model.

I believe my own model does in retrospect build on this older model, in two key ways:

- I start from a more advanced base, assuming certain things have moved on and that the original level 1 is no longer common -- or at least if someone is still copying files by hand to servers in 2026, then they are not the target audience
- My top level is a layer above the original. It's clear even at the time they were very forward-thinking in terms of a level 5 where A/B testing, feature toggles, etc. are enablers of being quicker from code to merge to deploy. My level 3 does require a lot of that to be able to automatically merge _without review_ certain things e.g. you could merge all changes behind a flag automatically. I believe my level 4 is a stretch where you are happily allowing any change to do out so long as it passes checks and there's an AI Andon cord to halt anything.

### Mapping the levels

| Thoughtworks/Forrester 2013 | Rough modern mapping | Notes |
|---|---|---|
| Level 1 — Initial / ad hoc deployments | Below my model / out of scope | Manual copying, heroics, painful integration. Important historically, but not the intended audience for an AI/CD autonomy model. |
| Level 2 — Managed / time-boxed planned releases | My Level 0 — Manual/Planned Release | There is some automation and a known release process, but releases are still planned and stewarded as events. This remains a hard barrier to AI-generated change because agents cannot usefully navigate human release planning. |
| Level 3 — Defined / regular releases, CI, scripted DB changes | My Level 1 — Stewarded Pipeline | An actual pipeline exists. Deployments are scripted and repeatable, but humans still press buttons, approve stages, remember context, and push work through. |
| Level 4 — Quantitatively managed / release on demand | My Level 2 — Merge Means Prod | Trunk is kept deployable. We do not merge changes we would not put into production. Human judgement shifts pre-merge; after merge, the system carries the change to prod unless it fails. |
| Level 5 — Optimizing / hypothesis-driven delivery | Partly overlaps my Level 3 — Selective Autonomy | Their Level 5 focuses on techniques like feature flags, dark launching, A/B testing, and metrics to make valuable product changes safer and faster to merge. My Level 3 generalises this into selective/eager merging for classes of change the system can judge, including boring changes such as patches, docs, tests, and dependency updates. |
| New layer beyond the 2013 model | My Level 4 — Full Automated Change Cycle | AI makes plausible a new level where agents can raise, revise, merge, and ship certain bug fixes/features under encoded policy, observability, rollback, and an AI Andon cord. This was less socially/technically imaginable in 2013. |
