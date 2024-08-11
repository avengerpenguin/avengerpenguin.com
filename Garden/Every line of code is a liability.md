It's likely not stated like this verbatim, but one insight I got from [Eric S. Raymond's Cathedral & the Bazaar](https://amzn.to/3TVr6un) (one of the later essays) is that it's at best naive and at worst incorrect to treat code as an asset.

The way we have defined code as Intellectual Property like any other intangible work (writing, music) leads us down a path of therefore treating all code written within a company as an asset of that company, with the developers themselves as costs due to their salaries.

## Developers are not just costs

Firstly, Eric S. Raymond does explicitly point to cases where in fact the developers can be seen as assets. If we see software in terms of present and future value for its users, then developers who can support, fix and otherwise leverage their domain expertise are assets of the company. Sure, their salaries are costs.

## Code is not always an asset

Secondly, we can deconstruct the idea that code itself is an asset by starting with the extreme consequence of that assumption and working backwards. If we take this assumption at face value, we step into the old cliche in software engineering of why we don't pay developers per line of code produced.

That is, if code is _intrinsically_ as asset by virtue of being a form of writing alone, then we can immediately falsify that notion with a thought experiment of a team of developers writing lines and lines of pointless code.

## Maybe just good code is an asset?

Ok, so it's not that _all_ code is automatically an asset, but maybe we can still consider "good" code or "valuable" code to be an asset?

However, we all know full well that nobody is scrambling to get hands on code produced by vendors that no longer exist nor has there been any reason for us to see source code releases for old versions of Windows or older games.

We could try to argue that this is due to asset depreciation, but I prefer a different analogy to financial accounting.

## Code as a liability

My preferred analogy to accounting ledgers is to consider code itself as a liability, not an asset.

That is, each line of code -- or perhaps some more appropriate unit -- is a cost to a business in terms of having to write it, test it, maintain it. Each line increases the surface area for bugs to appear or for developers to break behaviour unintentionally.

The reason we write code at all then is because there _is_ an asset that arises from it, which is the value for its users now and in the future.

I will buy a game because of the future hours of enjoyment I get out of it and the price I will pay will be based on that enjoyment, not necessarily the amount of code to produce it.

To put it another way, if a company like Nintendo could sell me the same game at the same price, but with half the code to produce, test and patch post-release, surely it's not controversial to say they would take that option?

This model still allows for the idea that indeed it may take more code to produce a highly immersive, e.g. open world game with a huge amount of playing area and impressive graphics, music etc. This is fine as the company chooses to take on more liability for a better return -- perfectly normal business practice.

In fact, this boosts the validity of this model as we can clearly see that a company that invests heavily in such a complex game that then doesn't make it to market has lost out a huge amount more than one that was producing a smaller game. Granted, a lot of that is time, but note how there's no way to "sell off" the unused code "assets" like they could with other real assets.

## Maximising value

So now the game is how to I maximise that value for customers with the least amount of code needed to produce that. This plays nicely into the ideas that [[The best software has the fewest moving parts]] such that not only is less code a smaller liability but we can more readily make changes -- and therefore produce more value -- on top of minimal code.

## So why all the bloat?

A brief consideration of the model above might raise the immediate question: if this model holds, then why is it so common to have lots of spaghetti code and software bloat? Wouldn't businesses be striving for minimal code everywhere?

The simple explanation for this is that code is not the only cost or liability at play. There's time and there's also some liability in knowledge gaps among less experienced (and let's be honest also experienced) developers.

That is, it might take longer to get a more minimal code base. It might require expertise your developers do not have. It might be we could achieve less with a library or framework, but that brings on other liabilities like security (see the framework dilemma below).

Also, to consider again the accounting analogy, we might think of a company taking on debt as a liability, but only minimally to allow them to invest in assets and profit that should exceed that debt, However, we know full well not all decisions are fully calculated. A company may invest in the wrong thing or have to borrow to pay out fines for previous mistakes made.

The model that all code is a liability crucially holds in a world where we accept we will accidentally take on more liability than would be entirely optimal. That means excessive liability due to spaghetti code, poor design or bad decisions is our job in software engineering to manage.

## The Framework Dilemma

Finally, there is one interesting dilemma or debate that can fall out of this "code as a liability model" particularly when we consider the idea that [[The best software has the fewest moving parts]].

Take for example in Java where I could have:

```java
List list = ...;
for (int i = 0; i < list.size(); i++) {
  System.out.println(list.get(i));
}
```

This C-style for loop has multiple statements and moving parts where we could introduce bugs. We therefore may prefer in more modern Java to do:

```java
List list = ...;
list.stream().forEach(System.out::println);
```

Here we get into the power of declarative code being easier to observe as correct. However, have we really reduced the moving parts here? At the end of the day we are iterating over a list from 0 to its length, just in the latter case the code is part of the Java standard library.

What's really the difference between the complexity happening in my code versus inside the standard library?

This becomes a real debate when we consider frameworks and 3rd party libraries. I have seen people argue both ways which is more complex between, say using a dependency injection library:

```java
public class MyClass {
	@Inject
	MyOtherClass other;
}
```

over just constructing objects yourself:

```java
public class MyClass {
	MyOtherClass other;

	public MyClass(MyOtherClass other) {
		this.other = other;
	}

}
```

Clearly the version with Dependency Injection is "less" and in fact has no imperative code, but to achieve that we pull in a whole load of 3rd party libraries. So perhaps it's not so clear cut which final system has the least complexity and liability?

For the purposes of our liability model, we can leave this as an open debate, but I personally favour the library/framework delegation due to the idea that [[The Open Source Hive Mind is smarter than you]]. That is, complexity pushed into a library/framework that has multiple users finding bugs is favourable to complexity isolated in your code based with perhaps orders of magnitude less battle testing.

This argument gets harder to justify if you're bringing into a huge framework just to do one small thing. Or when people in the `npm` ecosystem hand off to packages very trivial things like [isarray](https://www.npmjs.com/package/isarray). As with most things we do in software, the rules aren't absolute, but we should continue to debate as it's in those discussions that we learn and improve.
