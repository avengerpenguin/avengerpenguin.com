Let us walk through some of these use cases and discuss what might be
a good direction to think of better ways to solve them in the 21st
century. I do not have all the perfect answers to all of them,
otherwise I would have solved them all by now, but we can look at the
_approaches_ we might consider.

### Communicating with friends, family and colleagues

It could be argued that this has already been shifted into more
“instant” technologies such as Facebook Messenger, WhatsApp and other
messaging protocols such as XMPP and IRC.

In fact, if anything this has become quite fragmented between email
for “longer” messages and quicker, shorter chat over these other
technologies. Perhaps the solution here is to rethink what it is we
are trying to get out of all these technologies and produce something
distributed and federated that doesn’t lock us into one platform, but
is more suitable that traditional email.

This is one where Google did attempt a proper shift in the form of
Google Wave some years ago. The concept was to model conversation
threads as the main entity where people can drop out of group
conversations at will. There didn’t seem to be a push towards these
messages being short nor long, but still it didn’t really take off in
popularity.

One company failing to attract people to their platform shouldn’t
discourage us from rethinking this email use case at a protocol or
conceptual level though. What would the next evolution of SMTP, XMPP
or IRC look like if we designed a new protocol from scratch that
served modern use cases? Can we build open source platforms on an open
protocol, but in a way that still interfaces with proprietary
platforms that exist today? Can we ensure that companies that provide
their own locked-in platform are incentivised to integrate with this
system?

Can blockchain technology used by cryptocurrencies give us a way for
users to distribute a conversation between nodes and agree what that
conversation flow looked like? Can we keep these conversations
private, but openly shared amongst those whose public keys are
attached the chain?

What is it about email in the workplace where colleagues feel the need
to write a long form message to each other when many companies have
things like Microsoft Lync, Slack or IRC in place? Is it just a
culture where email is traditionally a first-class thing enabled on
company computers by IT (e.g. Outlook and Exchange are typically the
main services supported by any corporate IT)? If a company chose to
make their IT department set up all computers with a user-friendly
XMPP client pre-installed, would anyone really notice or care?

### Company updates and newsletters

We might end up on more newsletters from companies that we’d like. Too
many seem to find the right combination of box ticking or lack of box
unticking to get you to opt into communications unwittingly.

However, there are many brands that we might truly love and we really
do want to hear when they release something new or offer discounts to
loyal customers.

There is still something a little Faustian about receiving discounts
only in return for surrendering our email and implicitly opting in to
being sold to. There is no true way to opt out of email marketing
unless they choose to offer an “unsubscribe” mechanism, which feels
like the wrong balance of power.

In fact, I’d say it is this balance of power that makes our email such
a headache. There is no limit on how much a company can spam me and we
suffer from something I like to call “tragedy of the market” —
something I first coined when talking about loyalty cards.

With “points” or loyalty cards for shops and restaurants, it seems
like a win-win deal to register for free rewards (particularly when a
discount is offered on the day you register), but with the large
number of businesses I might use in a year, it doesn’t scale to have a
card per company (my wallet fills up very quickly. It is a situation
where each company is acting in a way that seems reasonable, but the
combined effect on the individual is problematic.

(As a aside, there will be people that read this and point out apps
that replace loyalty cards by using your phone as the unifying
mechanism. I would suggest for consideration whether virtualising
loyalty cards onto a single, proprietary app is a "faster horse" or a
genuine innovation. Have we just shifted the problem onto a
fragmentation of virtual loyalty card systems and apps?)

I think the same applies here to marketing emails. Clearly, an email
once a week from a company I love is fine, but if _every_ company I
register with sends me emails daily, I get overwhelmed and start
ignoring them.

We already have a shift here with Twitter and Facebook pushing for
companies to establish a presence on their networks such that users
can opt in to (and crucially opt out of) permission for companies to
publish to their feeds. This has the correct balance of power, but
still hasn’t managed to replace email properly.

I would suggest the closed nature of these platforms doesn’t give
users and marketers the most general way to keep in touch and,
frankly, perhaps giving the balance of power in terms of opt-in back
to users has deterred marketers from dropping their attempts to build
large email lists.

Maybe we won’t see companies offering incentives for personal
information until email no longer exists or maybe we need to approach
this in a way that please the marketers first so that they will drop
email in a heartbeat.

So, what can we build where users can freely opt in to feeds from
companies, opt out any time without losing control, but also still
allows marketers to incentivise people to use it? Can we make the
incentives stronger than badgering people for an email address?

It seems to me that such a system would be:

* something a user is exposed to daily (so marketers will reach
  them this way — this is the only reason TV advertising ever worked);
* something that doesn’t block the user seeing messages from friends
  or colleagues (thus avoids the “too many emails” problem); and
* something where the user is always in control, companies are
  dissuaded from spamming, but marketers are still empowered to keep
  giving people reasons to stay subscribed (marketers will keep
  emailing people if they can’t keep hold of subscribers on other
  platforms).

We could argue this is what Facebook and Twitter are _almost_ doing
except for the single feed issue where marketers can push out updates
from friends and family. Is the single feed necessary in order to meet
the first requirement that the user sees it daily? What kind of user
would switch to a TV channel that is entirely adverts? It does feel
they have the balance of power right though in that people are
choosing to “like” and actually opt in to content from companies so
long as they 1) love that company and 2) get content from those brands
that entertains them enough that they do not ending up opting out.

I think there is a lot here to rethink and people that solve this —
properly solve it in an open sustainable way, not in a proprietary,
closed way that is doomed to fail eventually — could monetise it quite
well. I don’t have too much in the way of concrete solutions except an
observation that we used to subscribe to content “feeds” habitually
via RSS and Atom in the past.

A revisit to these old subscription feed technologies (or at least the
intent behind them) would at least put us in a position where we can
consider having multiple “feeds” that people subscribe to in a way
where things are separated from other sources by design (and not
separated after the fact by “smart” Gmail features).

### Notifications

### Unique identities

There are multiple websites that ask for an email address when you
register and moreover ask you to verify that email as part of the
registration process.

So, why do they do this? There are likely a few reasons, but we can
pick out a few key ones:

* it ensures recovery of your account if you forget your password;
* it discourages spammers from creating multiple accounts in an
  automated way;
* it links your identity to the account; and
* the website can send you emails

The ability for the website to email you updates, newsletters, etc. is
clearly covered under the previous section on marketing emails. As for
the website emailing you notifications, we will cover that below as
the general purpose.
