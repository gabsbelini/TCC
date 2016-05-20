
import ontospy


g = ontospy.Graph("http://protege.cim3.net/file/pub/ontologies/travel/travel.owl")
#g = ontospy.Graph("/home/gabsbelini/Documentos/ontologiaTeste.owl")
x = g.classes
print(x)
print g.datatypeProperties