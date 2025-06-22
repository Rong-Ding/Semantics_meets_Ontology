import rdflib
from rdflib import Graph, RDFS, RDF, URIRef
import pandas as pd

OWL_CLASS = URIRef("http://www.w3.org/2002/07/owl#Class") # all class names
#print(OWL_CLASS)
IAO_DEF = URIRef("http://purl.obolibrary.org/obo/IAO_0000115")
# Information Artifact Ontology (IAO); this specific property (0000115) is used to store natural language definitions of ontology terms

def load_ontology_labels(file_path, format="xml"):
  """
  Load ontology classes with rdfs:label and IAO:0000115 definition from an OWL file.
  Return: pd.DataFrame with columns [URI, Label, Definition, Text]
  """
  g = rdflib.Graph()
  g.parse(file_path, format=format)

  uris, labels, defs = [], [], []
  for s in g.subjects(RDF.type, OWL_CLASS): # s = a class
      label = g.value(s, RDFS.label)
      definition = g.value(s, IAO_DEF)
      if label:
          uris.append(str(s))
          labels.append(str(label))
          defs.append(str(definition) if definition else "")

  df = pd.DataFrame({
      "URI": uris,
      "Label": labels,
      "Definition": defs
  })
  df["Text"] = df["Label"] + ". " + df["Definition"]
  return df
