Maybe you recognise this. You've picked up a ticket, discussed it, understood it, written the code and you now have a shippable change.

You push to remote, Github, Gitlab, whatever, raise a pull/merge request and then submit it for review.

Now we hit the issues with these [[Pesky Pull Request Reviews]].

You can assign reviewers in Github or Gitlab, but do your team really see those notifications?

Given the learned culture not to notice emails, you have a team norm to share the PR/MR on Slack. So you post a message:

"Hi, can someone please review "

Now you wait.

People are busy on their own work. Context switching is expensive. So you wait a while before nagging or chasing.

Maybe you could use this time to review other open merge requests, but some of the ones you saw are over 3000 lines changed so you look for an easier one. Since Slack is the source and nobody has posted there today, you've got some time while you wait.

So you pick up your next ticket to get a head start on it.

This usually goes one of two ways -- at least for me -- where either you end up with multiple open changes you're looking after or someone does add comments to your first change so you're context switching between the next feature you started and the one you originally raised.

Not only is this highly inefficient at a systemic level, but it bears a personal cost: now you're juggling maybe 5 to 10 pieces of work (yes, I've seen it go this high) treating your brain like a CPU job scheduler that swaps to a new task when the current one is blocked waiting for input.

Just maintaing branches isn't free either. Rebasing, fixing conflicts, fixing _test failures_ from those rebases.

The key learning here from the Lean methodology is while you feel productive because you kept yourself busy, you've not actually _shipped_ anything yet.

Lean and Kanban tell us that only done matters. All work in progress (WIP) is like hidden inventory in a shop -- taking up space but without being in front of customers. Space costs and your attention is a cost too.

Here's what we should be doing instead (and I'm continuously working on this for myself still): if you're waiting for someone, just stop.

Yes, stop. Don't pick up something else.

Stop starting, start finishing instead.

## So I just sit around and wait?

To some extent, yes, but with some nuance.

Firstly, if you're "sitting around" you're more available to unblock others. When _they_ raise a change, you can look at it right away. Your problem here was that nobody else was available to look at your change right away, so keep that in mind.

Secondly, would taking a break right now be so bad? Stand up, stetch your legs, get a drink. Some idleness might allow for better insights and deeper thinking about the problem space you're currently in, rather than jumping to the next one.

Thirdly, as with any rule, there's exceptions Maybe this is a good time to clear some emails, write up a some documentation on what you did, note some problems you saw while doing your change that we might want to fix later.

Finally, and this is the real issue, we shouldn't be allowed long-lived pull requests like this. Grab some time with someone in the calendar to talk about it, or better still avoid this situation by pairing on features in the first place so you get instant review.

## The Real Smell

This has focused on the personal cost of juggling too many tasks, particularly between contexts, but we can't ignore the systemic issue at play: slow hand-offs of work.

While it might not be something you can fix overnight to improve flows in your organisation, I don't think we help ourselves by "propping up" poor flows by trying to fill the time with more work, particularly busywork that doesn't move the needle.

Protect your brain, don't hide the inefficiences in the system by grinding harder, don't be a hero that likely doesn't even get noticed for shipping extra low value tickets. Save your energy for seeing valuable things all the way to production where there's much more chance people will note what you have done.
