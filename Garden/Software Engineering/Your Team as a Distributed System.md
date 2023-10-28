A software engineering team meets the definition of a distributed system:

1. Multiple processes (people)
2. Inter-process communication (interpersonal communication)
3. Disjoint address space (people have their own ideas of what they're working on)
4. Collective goal (we hope)

## Applying Fallacies of Distributed Systems

Applying [Fallacies of distributed computing - Wikipedia](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing) to teams:

### 1. The network is reliable

Messages between people get lost. Not every email or Slack message is received or read. Even things you say verbally might not get heard.

We can compensate for this by being more "TCP" than "UDP". That is, ensure things are acknowledged with more back and forth.

### 2. Latency is zero

Things get blocked while you're waiting for someone else to do something.

We can minimise this by processes for raising if there's deadlock or ensure we deal with conflicting work.

### 3. Bandwidth is infinite

There is only a finite amount of information we can give to another person. Face to face communicates more than a phone call where body language gone. Email is even worse.

Then when there's gaps in what is communicated, people fill it in with inference and their own assumptions.

We have to understand the trade-offs with low bandwidth communications. We need to understand when to upgrade to face-to-face (i.e. when we need to build up context).

### 4. Information is transmitted accurately

Twist on "The network is secure".

We can't assume that information we have sent is received accurately.

Firstly, we need to start with the base assumption that everyone is trying their best such things are dealt with well when miscommuniation happens.

We need to ensure what we heard is what was said and what we said is actually heard. In networks we use checksums for this. For people we might do active listening.

### 5. Topology doesn't change

Organisation structures can change any time. Don't rely on it staying the same.

### 6. There is one administrator

We can't assume there is one owner or stakeholder for something. We need to focus on consensus-building instead, which is notoriously hard for computer systems to solve.

### 7. Transport cost is zero

Communications have a cost. The "handshake" problem highlights the exponential growth of point-to-point communication.

### 8. The network is homogeneous

More diverse teams have a higher cumulative intelligence, but people's differences can lead to misunderstandings.

## Single Points of Failure

A lot of teams end up with the lead being a single point of failure. Could be a principal engineer or just a really skilled developer.

We need to apply patterns from carving up monoliths and ensure teams don't have these single individuals that don't scale.

Rockstar developers don't scale. They need to more like Jazz musicians who listen to each other when others are doing their solos.

## How do we scale teams?

### Monitoring

We need to monitor our teams. Does the team know where we're going? Can they articulate why they are doing what they're doing?

The best tool is the 1:1 meeting to check people's understandings.

### Conflict Resolution

We need to get people back on the same page when things get weird. This is like long-lived branches that, if left too long, become near impossible to merge back into the mainline.

### Communication

People need to make good decisions independently. This requires good communications of what we're doing and why.

### Redundant Communication

It's better to repeat yourself than under-communicate.

### Clarify of roles

We need to understand other people's goals. We need to be able to express our goals.

### Re-iterate Collective Goals

Keep reminding people of the goals.

### Culture eats strategy for breakfast

Culture is ultimately the driving force for how you scale.

Culture is the collective character of a group. It emerges from choices and decisions we make.

It's who we hire, who we fire, the behaviours we reward and the behaviours we reprimand.
