## 🕸🌱 Semantic Alignment of Gene and Trait Ontologies Using Vector Embeddings
This project bridges **distributional semantics** and **biological ontologies** to explore whether embedding models can recover and reason about relationships within and between genes (GO) and plant traits (PTO). By mapping biological concepts into a continuous vector space, we examine the feasibility of **trait categorisation**, **gene–trait inference**, and the future integration of **language-based generalisation** in bio-ontological knowledge systems.

**Impact**: This approach may enable scalable, **zero-shot categorisation** of novel traits and facilitate ontology-aware gene–phenotype predictions, contributing to both plant biology and semantic AI applications, such as knowledge graph completion, explainable trait discovery, and bio-NLP.

## Key Analyses and Findings
* **Ontology embeddings**: We used sentence-transformers to embed **1,682 trait** classes from PTO and **44,000+ gene function terms** from GO.
* **Trait clustering**:
  * K-Means clustering on embeddings showed a **low silhouette score (max ≈ 0.14)**, confirming that traits live in a **semantically continuous space**.
  * **Hierarchical clustering** provided a more interpretable taxonomy; visualised via TSNE and dendrograms.
    - Notably, traits with high semantic similarity (e.g., those containing terms like _seed_, _leaf_, _sterility_) clustered early with low dissimilarity values.
    - The resulting hierarchy is interpretable and biologically plausible, but further validation with domain experts is required. 
* **Gene–trait similarity**:
  - Cosine similarity was computed between GO–PTO pairs.
  - A curated demo set showed **no consistent distinction** in similarity scores across biologically positive, neutral, or negative gene–trait pairs.
  - Even **negatively correlated pairs** (e.g., _salt stress_ vs. _shoot dry weight_) yielded similarity scores as high or higher than positively associated ones.

## Interim Conclusions
- **Gene–trait semantic similarity** shows no systematic signal using SBERT-based cosine similarity. Scores were inconsistent across hypothesized positive, neutral, and negative pairs.
- Surprisingly, some **biologically unrelated or negatively correlated** pairs received higher similarity scores than truly related ones, suggesting that semantic closeness does not imply biological relevance.
- The outcome likely reflects a limitation of **distributional models**, which capture contextual co-occurrence rather than mechanistic or causal relationships.
- **Trait categorisation** via hierarchical clustering produced an interpretable structure; for example, traits with related biological terms (such as _leaf_, _seed_, and _sterility_) clustered together early, validating a certain degree of semantic grouping.
- These findings emphasise the need to supplement language-based models with **structured data** (e.g., ontologies, knowledge graphs) and expert validation for applications in functional biology.

## How to Use / Reproduce
1. Download data (.pkl) for ontologies and embeddings from the folder _data_ (optionally, you can also generate data yourself by following the next step)
2. Run notebook in order (in the folder _notebooks_):

_00_read_ontology_files.ipynb_: Read in ontologies (GO and PTO) and save them as .owl and .pkl

_01_ontology_to_embeddings.ipynb_: Encode ontology labels from owl-files into vector embeddings and save

_02_compare_embedding_based_clustering_WIP.ipynb_: Read PTO label embeddings for K-Means and Hierarchical Clustering

_03_predict_gene_phenotype_relationships_WIP.ipynb_: Read PTO and GO label embeddings and compute similarities

## Future Work
- Integrate **graph-based models** to improve biological specificity
- Explore **hybrid embedding strategies** using symbolic constraints
- Collaborate **with plant science experts** to curate and expand validation sets
