Notes on FOSDEM talk.

## My Summary/Thoughts

HTTP requires a server, which means centralisation is inevitible. Then things like layers, caches, HTTP/2 are created to deal with scale. The focus seems to be that P2P would be better and not have issues around centralisation, commercial interest capture and censorship.


## Web Eras

### 1991 Simplicity

Docker

- Feedback loop: consolidation -> scale -> complexituy -> consolidation

## Web Protocol Issues

- Security has always been an afterthought
- Privacy doesn't even come up -- you need your own web server
- Commercial interests drive innovation more than user interests

HTTP/2 and HTTP/3 are basically Google's SPDT and QUIC respectively. All changes are to do with scale and not for the case where you run your own web server.

- HTTP is and isn't CRUD
- Updates and partial retrieval are broken (range headers aren't used widely, POST/PATCH are not defined; it varies by type/resource intepretation)

"Hard to make a generic web client"

Therefore the server "owns" the data and only it knows how to work with it.

## HTML Issues

HTML 5 gave up on standardisation (living standard).

Google de fact owns HTML5 via WebKit.

HTML mixes data and representation. With JavaScript, it also mixes prrocessing.

This leads to data silos. Data only accessible via linked View/Controller.

## Strengths

HTTP and HTML are simple.

## Whither Web?

### Censorship

Centralised data means censorship is possible.

### Centralisation as Default

Signal creator things third party clients no longer have a place.

### Yielding Control as Default

Less concern for open exchange formats.

## Collaboration

Main need for a human-centric Internet is collaboration

### Mechanics

- Communication
- Sharing stuff (more of barter/trade than social media -- i.e. broadcasting/retweeting) -- Makes me think of [[Retweeting as voting]]
- Sharing skills
	- Updating parts of resource
	- Selling services

Requires:

- Real-time
- ACL/ownership
- Finer resolution thanentire rersource, e.g. update frame in video rather than upload entire video

### What is real-time?

- Consume data while it is in the prcess of being produced
- Produce, consume in chunks
- Data streaming, e.g. video is high bandwidth, but has low latency requirements

### Requirements

- Data streaming -- Something other than HTTP
- Access control -- E2E encryption (shared symmetric key)
- Ownership -- Encryption (private key)
- Server-side processing -- Remote APIs
- No MITM -- Something other than HTTP


### Data Locality

People have multiple devices, so personal data are fragmented.

- Web is client/server
	- Data is in central location
	- Allows for multiple clients

- Multiple personal devices
	- Multiple link technologies (WiFi/LTE)
	- each with own storage

- IoT/Smart sensors
	- Data is in hundreds of locations
	- IoT connectivity may not make devices ideal for "client" role. (BLE, LoRa)

Might be better to have local synchronisation rather than going back to a central server. (iCloud?!)

Additional requirements:

- Smooth handover -- Multi-home/-path/-link
- Selective sync -- PubSub
- Heterogenous link tech -- Overlay network
- No strict client/server -- P2P (My thought: what about DNS?)

## Drones

Toys, military, commercial

BVLOS: Beyond Visual Line of Sight

EASA requirements: reliable Command, Control and Comms (C3) links.

C3 link handover. When mast goes out of sight, satellite takes over. Like when your wifi drops out of the house and mobile device switches to 4G.

## Vision

### Human-Centric

- Our data will live on manay devices
- We can acess our data anytime, in part (fast) or in full (slow maybe)
- We can access our data from any device
- We can share and collaborate on our data
- We can selectively sloow access to our data from processing nodes

### Infra

Need more infrastructure protocols, not application frameworks.

## Peer-to-Peer

- Peer as in host


## Progress

- Liberate: https://gitlab.com/interpeer/liberate
- 