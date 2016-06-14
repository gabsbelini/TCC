# -*- coding: utf-8 -*-
import ontospy


g = ontospy.Graph("/home/gabsbelini/Documentos/ontologiaTeste.owl")
x = g.classes
for item in x:
    print(item)