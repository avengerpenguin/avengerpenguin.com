reMarkable .lines file, version=6          
One thing 
at a time
aybe you recognise th
is. 
You've picked up
 a ticket, discussed it, under
stood it, written the code and you
 now have a shippable change.
You push to remote, Github, 
Gitlab, whatever, r
se a 
pull/merge request and then submit it for review.
Now we hit the issues with the
pesky pull requests
You can
 assign
 rev
iewers in G
ithub or Gitlab, but do your team really see those notifications?
Given the l
earned culture not to notice emails, you
 have a team n
orm to 
share the PR/MR on 
lack
 So you post 
a message:
"Hi, can someone ple
e revi
ew <link>
Now you wait.
People are busy on their own 
work. Context switching i
s e
xpensive. So you wait a while before nagging
 or ch
asing.
Maybe you could use t
his time to review other open merge requests, but 
some of the ones you saw are over 3000 lines changed so you look for an easier one
. Since Slack is the source 
and nobody has 
posted there today, you
e got
 some time while you wait.
So you pick up your next ticket to get a head start on it.
This usually goes one of two wa
ys -- at least for me -- where either you end up with multip
le open changes you
're looking after or someone does add comments to your first c
han
ge so you're context switching betwe
 the 
next fea
ture you s
tarted and the one you originally raised.
Not only is this highly inefficient at a systemic level, but it bears a personal cost
: now you're juggling m
aybe 5 to 10 pi
eces of work (yes, I've seen
 it 
go this high) tr
ting your brain like a CPU job schedul
er tha
t swaps to a new task when 
the current one is block
ed w
aiting for input.2
Just maintaing branches i
sn't free either. 
Rebasing, fixing conflicts, fixing _te
t failures_ from thos
e rebases.q
The key learning here from the Lean methodology is while you feel productive because you 
kept yourself b
usy, you've not actually _shipped_ 
anything 
yet.
Lean and Kanban tell us that only done matters. All work in progress 
(WIP) is like 
hidden e
inventory in a shop -- taking up space but without being in front of customers
. S
pace 
costs and your attention is a cost too.
Here
's what
 we should be doing instead (and
 I'm contin
uously working on this for myself still): if you're 
waiting for someone, just stop.
Yes, stop. Don't pick up something else.
## So I just sit
 around and wait?
To some extent, yes, but with 
some nuance.
Firstly, if you're 
"sitting around" you're more available 
to unblock others. When _they_ raise a c
hange, you can look at it right away. Your problem here was that nobody else was avai
lable to look at your change right away, so keep that in mind.
Secondly, would taking a b
eak right now be so bad? Stand up, stetch your legs, get a drink. Some idle
ness might allow for bet
ter insights and deeper th
inking about the 
problem 
space you're currently in, rather than jumping to the ne
xt one.
Thirdly, as with any rule, t
here's exceptions Maybe this is a good time to clear some emails, write up a s
ome documentation on what you did, 
ote some pr
oblems you sa
w while doing your change that we might wan
t to fix later.
Finally, and this is 
the real issue, we shouldn't be allowed long
-lived pull requests like this. Grab some time with someone in the calendar to talk about it, or better still avoid this situat
ion by pairing on 
feature
s in the first plac
e so you get instant review.
## The Real Smell
This has focused on the personal cost of juggling too many tasks, 
en context
s, bu
t we can
't ignore the systemic is
sue at 
play: slow hand-offs of work.
While it might not be something you can fix overnight
 to improve flows in your organisation, I don
't think we help ourselves by "propping up" poor flows by trying to fill the time with more work, 
Protect your brain, 
don't 
hide the i
nefficiences in the system by grinding harder, d
on't be a hero that likely doesn't even ge
t noti
ced for shipping extra low v
alue tickets. Save you
r energy for seeing valuable th
ings all the way to production where there's
much more chance people will note 
what you have done.
@m@D
Layer 1<
