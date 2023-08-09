In this paper we explore a theoretic model of REST services.

```python trusted=true
from typing import cast, Tuple, Set, NewType, Callable, Dict
from rdflib import Graph, URIRef
from rdflib.term import Node


ClientState = Tuple[URIRef, Graph]
ServerState = Tuple[Graph]
```

```python trusted=true
context = {
    "dc11": "http://purl.org/dc/elements/1.1/",
    "ex": "http://example.org/vocab#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex:contains": {
      "@type": "@id"
    }
  }

g1 = Graph()
g1.parse(data="""
{
  "@context": {
    "dc11": "http://purl.org/dc/elements/1.1/",
    "ex": "http://example.org/vocab#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex:contains": {
      "@type": "@id"
    }
  },
  "@graph": [
    {
      "@id": "http://example.org/library",
      "@type": "ex:Library",
      "ex:contains": "http://example.org/library/the-republic"
    },
    {
      "@id": "http://example.org/library/the-republic",
      "@type": "ex:Book",
      "ex:contains": "http://example.org/library/the-republic#introduction",
      "dc11:creator": "Plato",
      "dc11:title": "The Republic"
    },
    {
      "@id": "http://example.org/library/the-republic#introduction",
      "@type": "ex:Chapter",
      "dc11:description": "An introductory chapter on The Republic.",
      "dc11:title": "The Introduction"
    }
  ]
}
""", format='json-ld')

server: ServerState = (g1, )

def σ(g: Graph, uri: URIRef) -> Graph:
    g2 = Graph()
    for t in g.query(f"DESCRIBE <{uri}>"):
        g2.add(cast(Tuple[Node, Node, Node], t))
    return g2

def GET(ss: ServerState, url: URIRef) -> ClientState:
    g, = ss
    return url, σ(g, url)

def render(cs: ClientState) -> None:
    uri, g = cs
    print(str(uri) + "\n\n" + g.serialize(format='json-ld', indent=2, context=context))

client = GET(server, URIRef("http://example.org/library"))
render(client)
```

```python trusted=true
def LO(g: Graph) -> Dict[str, URIRef]:
    return {
        p.fragment: o for p, o in g.predicate_objects()
        if type(o) == URIRef
    }


client = GET(server, LO(client[1])['contains'])
render(client)
```

```python trusted=true
from collections import defaultdict

class Client:
    def __init__(self, state: ClientState):
        self.state = state

    def __str__(self):
        uri, g = self.state
        return str(uri) + "\n\n" + g.serialize(format='json-ld', indent=2, context=context)

    def __repr__(self):
        return str(self)

    def LO(self):
        uri, g = self.state
        links = defaultdict(set)
        print(uri)
        for s, p, o in g: #.predicate_objects(subject=uri):
            print(s, type(s), uri, type(uri), s == uri)
            print(p, o)
            if type(o) == URIRef:
                links[p].add(o)
        return links

Client(GET(server, URIRef("http://example.org/library")).LO()
```
