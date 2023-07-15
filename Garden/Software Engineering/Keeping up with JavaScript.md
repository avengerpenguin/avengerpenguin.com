Title: The Simplest Way to "Keep Up" With the JavaScript Ecosystem
Date: 2018-03-16
Status: published
Tags: JavaScript, Web Development, Node.js

I often hear the frustration or jokes around how fast the JavaScript ecosystem
moves. Observations usually include things like "there's a new framework
every week" or that
[you need a huge number of tools just to get started](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f)
on a basic modern application.

The frustration can come from developers who either feel they need to learn
several tools just to get going, whereas in the past you just needed a text
editor and knowledge of HTML, CSS and JavaScript itself.

It can be even more frustrating when you have large application UIs built,
for example, in Angular but now everyone is using
[React](https://reactjs.org/). Your build process is
fully dependent on [Bower](https://bower.io/)
and [browserify](http://browserify.org/) but now everyone is using
[Yarn](https://yarnpkg.com/) and [Webpack](https://webpack.js.org/).

This is particularly difficult for enterprise application developers as you
tend to end up with large code bases where you have little justification going
in to "modernise" or refactor things if the application works just fine. This
is where Java was traditionally favoured in the enterprise as the language (and
platform) changes slowly, is (almost) always backwards compatible (so you can
upgrade tools without changing code) and the toolchain hasn't moved that
quickly either. Yes, we have [Ant](http://ant.apache.org/),
[Maven](https://maven.apache.org/) and [Gradle](https://gradle.org/) now, but
that's been a slow and steady progression.

So, clearly we don't want to move at a break-neck speed and keep refactoring
working code bases, but we also want to be able to held back by slow-moving
platforms. People might like the fast innovation and choice in the JavaScript
and Node.js ecosystems, but how do we keep up with all the frameworks and
tools?

Well, I have one suggestion to cope with "keeping up" with all the new tools
and libraries and frameworks coming out each week:

Don't.

Seriously, don't keep adopting new technologies as they emerge. While a new
build tool or framework might seem nicer than what you have, _wait until you
have an actual problem the new tool solves_ and be sceptical about migrating
your applications to new frameworks.

Even for newer projects, carefully consider the cost of adopting a new tool in
terms of having to learn it. Maybe stick with what you know and play with new
tools only on side projects or in "10% time" outside of your main work.

For frameworks whose popularity is short-lived, you will be able to skip right
over them and only move to things that stand the test of time. For frameworks
that stick around, you will be able to adopt them when best practices are
established and early bugs are fixed.

Learn to live with applications in older frameworks and on older versions of
Node.js and you will be able to focus more time on adding features and perhaps
even working on new, exciting things.
