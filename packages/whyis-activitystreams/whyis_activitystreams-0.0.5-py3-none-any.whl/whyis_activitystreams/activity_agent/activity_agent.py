from whyis.autonomic import UpdateChangeService
from whyis.namespace import NS

from whyis.plugin import Plugin
import rdflib
from flask import current_app


from whyis.namespace import sioc_types, sioc, schema, sio, dc, prov, whyis

prefixes = dict(
    skos = rdflib.URIRef("http://www.w3.org/2004/02/skos/core#"),
    foaf = rdflib.URIRef("http://xmlns.com/foaf/0.1/"),
    text = rdflib.URIRef("http://jena.apache.org/fulltext#"),
    schema = rdflib.URIRef("http://schema.org/"),
    owl = rdflib.OWL,
    rdfs = rdflib.RDFS,
    rdf = rdflib.RDF,
    dc = rdflib.URIRef("http://purl.org/dc/terms/"),
    ao = rdflib.URIRef("http://purl.org/arclight/ontology/"),
    ov = rdflib.URIRef("http://open.vocab.org/terms/"),
    act = rdflib.URIRef("https://www.w3.org/ns/activitystreams#"),
    mediatype = rdflib.URIRef("https://www.iana.org/assignments/media-types/"),
    pv = rdflib.URIRef("http://purl.org/net/provenance/ns#"),
    sio = rdflib.URIRef("htttp://semanticscience.org/resource/")
)

class ActivityAgent(UpdateChangeService):
    activity_class = whyis.ActivityResolution # resolving activities
    
    def get_query(self):
        return '''SELECT DISTINCT ?resource WHERE { 
                    ?resource rdf:type/rdf:subClassOf* %s.
                    FILTER NOT EXISTS { ?resource a %s.}
                  }''' % ( self.getInputClass().n3() , self.getOutputClass().n3() )

    def getInputClass(self):
        return rdflib.URIRef("https://www.w3.org/ns/activitystreams#Object")

    def getOutputClass(self):
        return whyis.ProcessedObject
    
    def process(self, i, o):
        o.add(rdf.type,whyis.ProcessedObject)
