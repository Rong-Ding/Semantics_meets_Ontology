This folder contains the Jupyter notebooks used to read in, encode and analyse embeddings for gene and plant trait terms.

## Explanation
**00_read_ontology_files.ipynb**: Read in ontologies (GO and PTO) and save them as .owl and/or .pkl

**01_ontology_to_embeddings.ipynb**: Encode ontology labels from owl-files into vector embeddings and save

**02_compare_embedding_based_clustering_WIP.ipynb**: Read PTO label embeddings for K-Means and Hierarchical Clustering

**03_predict_gene_phenotype_relationships_WIP.ipynb**: Read PTO and GO label embeddings and compute similarities
