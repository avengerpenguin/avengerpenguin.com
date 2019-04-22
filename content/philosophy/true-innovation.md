Title: True Innovation
Date: 2017-08-17
Slug: true-innovation
Status: draft

We live in a world where new technologies, software and hardware change at an
incredibly rapid pace.

Most notably, we speak of how portable and connected devices and software are.
Always-on access to the Internet and devices we can carry in our pockets or
wear (that themselves are also “always on”) open up all sorts of opportunities
to access information and sync data in ways staggeringly different to only 20
years ago.

Key selling points for many technologies at the moment are
“automation” and “convenience”. I don’t need to wait until I get to a
computer to check my email and there are many email apps that
intelligently pre-sort my email for me to make it easier to go through
them or spot the important ones.

Online office suites allow me to create a document that someone else can edit
with me in real time. And I can instantly sync spreadsheets between devices or
with colleagues with “cloud-based” applications and storage.

However, there is a phenomenon I have been observing for a number of years now
where some of these advances and more are at best simply speeding up boring
work and at worst giving us even more work to do than we had before.

## The Faster Horse

There is a urban legend of a quotation from Henry Ford that comes to mind here:

  >If I had asked people what they wanted, they would have said faster horses.

Now, it is questionable as to whether Mr. Ford actually said this, but it is
commonly applied to applaud the approaches of, say, Apple where companies will
push innovation that was not asked for, but it will succeed. It is used to
demonstrate that there is an amount of short-sighted thinking that will come
from your customers and the population in general. If you really think
— and truly innovate — then you will develop paradigm-shifting, game-changing,
“disruptive” innovations that are a step up from where we were before.

It is my assertion however, that big companies and innovators — yes, even Apple
and Google — sometimes do not shift paradigms as much as they should or could.
In fact, even some of the most notable developments are less than they appear
to be on closer inspect — or maybe at a higher level of abstraction — i.e. they
are more superficial than we might think.

However, it is not always their fault. Sometimes it feels there is a lack of
imagination — and I think that sometimes that is the case — but there are many
occasions where the ideas are willing, but there is substantial effort required
to overturn people’s expectations and habits.

## An example: email

Email is my favourite example for everything that is both right and wrong about
modern technology. It brings skeuomorphisms from its predecessor — mail or post
— in the form of envelope icons or indeed the “envelope” that appears in the
SMTP standard. The protocols certainly feel old when you start writing software
that deal with them, but it works really well and naturally suits a distributed
network.

Not only that, but it has been around for _decades_ with protocols such as IMAP
surviving from 1986 to this day. In timescales normally recognised by the
software and Internet industry, it is ancient technology. It pre-dates almost
any programming language in popular use on Github, pre-dates the Linux kernel
and pre-dates the World Wide Web.

So, what has actually developed in this realm? Yes, there are things
like ActiveSync that attempt to replace IMAP, but I should hope not to have to
justify just how dull a development that is and how little it really impacts
the end user who just sees their email sync between devices either way.
Instead, let us look at innovations that help users interact with and manage
their email.

An overly-chatty world and increasing spam has made email difficult to manage
over the years. It is also an oddly stateless and non-linear format where I can
only send someone a sequence of characters and they send characters back, with
the fact that it’s a reply to my first message only made clear by header
metadata and a convention to include my original reply in their email body.
Linear models like conversation threads and messages over time are extraced
only by clients out of stateless metadata. Does this model real communication
where there is usually some conversational context to each utterance?

It does the job it was built to do and it does it well, I suppose. So what are
the problems with it?

## Perceived Problems

Well, let me start with one _perceived_ problem that leads to the
imagination-lacking, less-innovative-than-you-might-think developments that are
the focus of this article: sheer volume of emails.

We receive too many emails. This should be evident to anyone with an email
address. In a relatively short time period, we can receive:

* spam
* notifications from automated systems
* auto-replies from companies
* delivery notifications from online shops
* spam
* mailing list updates from companies we signed up to hear from
* genuine messages from people we know
* alerts from social media sites
* spam spam

So, how do we solve this? Gmail has released features that
automatically categorise emails into different groups. This sounds
fantastic on the face of it in that I can see emails from my family
distinct from marketing nonsense.  This is in addition to a
long-running, effective spam filter that keeps the biggest noise out
of our inboxes.

There are other companies out there too trying to build client
applications that connect to your email, but present the information
in different ways or provide different controls and buttons. With
this, they hope to make it easier to sift through the information and
reply to people in a timely way.

So, I’ve called this a perceived problem but it is a real problem,
sure. So, what do I mean when I say "perceived"? What is the real
problem here?

I call his a “perceived” problem because it is actually more a symptom
of a larger problem. We perceive symptoms more easily and have a bias
towards solving the immediate consequences of these symptoms (I have a
lot more to write on this topic generally, but for now see “XY
Problem”)

So, the _perception_ or naïve interpretation of the situation is “I
have too many emails. If only Google could filter out some of them or
categorise them so I can go through them in a more structured way.” In
short, the naive belief is that we need machines to help us work
through all those emails.

## Finding the Real Problem

It is my belief that we need to strive to be better at moving up the
levels of abstraction to get at the root of modern problems,
particularly where technology can solve them. In Systems Thinking, we
would think about the bigger, holistic system of which our email woes
are only one component. We might find that the system itself has
issues that cannot be fixed by addressing each problematic component
in isolation.

So, why do we have too many emails? I think this is answered in the
list above: we have emails from multiple sources such as spam,
marketing emails from companies, notifications from automated systems,
notifications of items being despatched as well as genuine messages
from colleagues, friends or family.

What are the real problems here? In my mind it is:

* A single inbox is mixing up critical alerts, FYI notices from
  systems, notifications of things like deliveries and proper human
  communication messages.
* No distinction between messages that need action (so, you’d want
  them there when you get back from being away so as to reply
  eventually) and updates that are not interesting once they get
  old. (Do I really need to sift through a backlog of alerts from
  systems at work once I get back from being away from 2 weeks? Won’t
  they all be addressed by colleagues in my absence?)
* Marketing emails might take more effort to opt out of than to create
  a filter to hide them. Or I might be interested in some updates from
  that company, but not all are interesting (so, again, if the
  newsletters haven’t been read for a week, then I don’t care
  anymore).
* Other transient emails like despatch notices from companies become
  very uninteresting if I see the email after I already have the item
  in my hands.
* The fact that spam exists. Not sure we can solve that one, but don’t
  dismiss it right away.
* Our email doubles up as an identity so that we can sign petitions or
  otherwise do things that need to be restricted to one account per
  person. It is also used for password recovery when we use it to sign
  up for an account on a website.

And these are just problems with my inbox. I can imagine finding further issues
if I looked at other people’s inboxes.

So, what can we do better here? Isn’t the first point exactly what
Google is trying to address with the auto-sorting features in Gmail?
Well, sort of.  Google is addressing the symptom by splitting up these
different kinds of emails and making it easier for users to see what’s
going on, but they aren’t actually addressing the underlying issue of
why we have this all mixed up in the first place.

There is a lot of administrative effort put on us by automated systems
and machines, so our solution is to use more machines to allow us to
get through that additional effort more quickly. In this respect,
Google and others are proposing Ford’s supposed “faster horse”. Nobody
is talking about “what if we didn’t have horses?” Or, to drop the
analogy, “what if we simply weren’t given the administrative effort in
the first place? Isn't it the whole purpose of machiens to have them
to repetitive work for us?

## Analysing the Real Problem

An important, but under-appreciated skill for the best software
engineers is to be able to step back from a mix of problems and
requirements and find the perfect level of abstraction at which 1)
many problems start to look like the same problem and 2) we can divide
our solutions amongst the different classes of problems rather than
repeatedly creating lots of one-off solutions for the problem right in
front of us.

If we attempt to find patterns in the list of problems I listed above, I can
pick out themes such as:

* Some emails require action (e.g. replying to a question), but some
  are transient (i.e. they become uninteresting if I do not read nor
  act on them by some date).
* Emails are used to let me know something has happened — either
  because something needs attention or to keep me posted about changes
  in an order status.
* Companies love to send us email to make us come buy more things and
  sometimes we want to hear about news and products from companies we
  like.
* Emails are used as an authentication mechanism so that websites with
  user accounts can control the number of spam accounts, attempt to
  tie at of their accounts to a real person or otherwise prevent
  people from skewing something with fake accounts (e.g. petitions,
  online polls)
* Some emails are from humans, some are from automated systems.

I’d say this is one level up in terms of abstraction in that the list
is in some ways just a re-wording of the list of problems I gave
above, but we are starting to blur some of the precision. Let us step
back a bit further and consider the use cases for email in light of
these observed patterns:

* A person you know (or a colleague you’ve not met) wishes to ask you
  a question and get a response.
* Someone you know quite well wants to engage in general conversation
  and keep in touch.
* Some companies want you to associate a unique identity to your
  online account so that spam accounts are harder to create.
* I want to keep up-to-date about new products from a brand or company
  I love (e.g. product launches, competitions, discounts/offers)
* Some companies want a way to identify you in the case you forget
  your password.
* Online petitions and polls want to ensure integrity by preventing
  people voting/signing twice.
* I want notification when online shops despatch and deliver my parcel
  so I know when you wait for it or when to expect it in case it
  doesn’t arrive and I have to chase it.
* People in a work setting might need some of their systems to notify
  them when something happens that needs attention (e.g. customer
  order placed, website has gone down, something else has gone wrong).

Note I have deliberately tried to avoid using word email in all of
these. This is the only way to get the right level of abstraction that
allows us to question the need for email *at all* in any of this and
free us up to think of completely new ideas to solve our problems.

## Real problems lead to true innovation

So, finding the _real_ problem is somewhat important if we actually
want to make our lives better with technology. I hope that now and
again I can convince people to step back ("why do we need to get so
much email in the first place?") and push their imaginations a little
further ("what if we replaced email for some use cases?") and we might
just get a better approach to things like email rather than having it
pre-sorted for you or allowing you to check it on the move.
