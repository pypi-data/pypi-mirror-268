from whyis.autonomic import UpdateChangeService
from whyis.namespace import NS

from whyis.plugin import Plugin
import rdflib
from flask import current_app


import json
import requests
#import numpy as np
#import matplotlib.pyplot as plt

from whyis.namespace import sioc_types, sioc, sio, dc, prov, whyis
schema = rdflib.URIRef("http://schema.org/")
request_url = "http://127.0.0.1:9191/"

class BackboneAgent(UpdateChangeService):
    activity_class = whyis.BackboneLoading # loading backbone embedding
    def get_query(self):
        return '''SELECT DISTINCT ?resource WHERE { 
                    ?resource a %s.
                    FILTER NOT EXISTS { ?resource a %s.}
                  }''' % ( self.getInputClass().n3() , self.getOutputClass().n3() )

    def getInputClass(self):
        return schema.ImageObject

    def getOutputClass(self):
        return whyis.BackboneProcessedImageObject

    def process(self, i, o):
        r = requests.post(request_url + "backbone_embedding",json = {"image_path":i.identifier})
        o.add(rdf.type,whyis.BackboneProcessedImageObject)
        o.add(sioc.content,r.content)
