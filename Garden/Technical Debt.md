Technical Debt is a very broad term, mostly used by engineers to refer to anything they'd like to change at some point.

## Definition

I prefer an interpretation closer to the original "debt" metaphor it leverages:

> Technical debt, like financial debt, is any liability in your project that costs you over time and would incur costs in "paying it off"

This includes bad design, bad builds, bad docs, bugs and a whole lot more, but crucially only things that actual have a cost. With this definition, we get to make the same trade-off decisions we would with financial debt:

- If the debt is low cost (low interest i.e. it doesn't cost you much to retain it), then you likely want to pay it off slowly over time as with a mortgage or indeed happily never pay it off
- If the debt is high interest/cost (it's costing you every day), then it likely needs you to stop paying into new features and pay the debt off instead. This follows nicely from the financial analogy where very high interest debts should probably be a priority over buying new, non-critical things.

Then we also get to factor in just how much it will take to clear these different scales of debt. We also get to consider when we need to call "bankrupcy" and start again.

Note that large companies happily take on huge amounts of financial debt as a matter of course if it's helping leverage more returns elsewhere. This is a key insight engineers may want to consider since it can be tempting to try to fix everything eventually, but we may wish to borrow this idea from finance that perpetually living with debt in business can be normal and not an aberration.

## Classification

There are two different categorisations I have found that I like for reasoning about technical debt (and therefore treating different categories differently):

- In [Understanding Technical Debt](http://www.michaelportwood.com/Quick-Tips/Understanding-Technical-Debt.htm), Michael Portwood lays out a classification based on the impact of the debt. I think this key as each category needs its own treatment and plan. It also follows that it might be worth classifying debt we find before fixing it right away.
- Back in 2009, Martin Fowler published a simpler [TechnicalDebtQuadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) to show a similar breakdown, highlighting that some debt is prudent, not always reckless.
- In [Towards an Ontology of Terms on Technical Debt](https://www.semanticscholar.org/paper/Towards-an-Ontology-of-Terms-on-Technical-Debt-Alves-Ribeiro/3ab6bd6fd72110a18f2d9d442cab03369a6017c5), the authors describe an ontology based on the technical aspects of the debt. Such a breakdown might be most useful when trying to _address_ the debt.
