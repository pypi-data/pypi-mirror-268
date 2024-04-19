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

class ObjectClassificationAgent(UpdateChangeService):
    activity_class = whyis.ObjectClassification # classifying object
    def get_query(self):
        return '''SELECT DISTINCT ?resource WHERE { 
                    ?resource a %s.
                    FILTER NOT EXISTS { ?resource a %s.}
                  }''' % ( self.getInputClass().n3() , self.getOutputClass().n3() )

    def getInputClass(self):
        return schema.ImageObject

    def getOutputClass(self):
        return whyis.ObjectClassifiedImageObject

    def process(self, i, o):
        r = requests.post(request_url + "object_classification",json = {"image_path":i.identifier})
        o.add(rdf.type,whyis.ObjectClassifiedImageObject)
        o.add(sioc.content,r.content)
