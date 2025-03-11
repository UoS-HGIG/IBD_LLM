# Inflammatory Bowel Disease (IBD) Large Language Model (LLM) Patient Structuring Toolkit
<p align="center">
  <img width="250" height="250" src="https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/llamas.png">
</p>
## Overview
The University of Southampton Human Genetics and Informatics Group IBD-LLM toolkit is a specialised large language model-based kit fine-tuned for structuring inflammatory bowel disease (IBD) patient records. This model convert unstructured free text into structured and standardised formats, allowing the integration of genomic data, structured findings, and clinical information to improve precision in IBD research and patient stratification.

<p align="center">
  <img src="https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/abstract.png">
</p>

### Reference
**Application of Generative Artificial Intelligence to Utilise Unstructured Clinical Data for Acceleration of Inflammatory Bowel Disease Research**  
Alex Z Kadhim, Zachary Green, Iman Nazari, Jonathan Baker, Michael George, Ashley Heinson, Matt Stammers, Christopher Kipps, R Mark Beattie, James J Ashton, Sarah Ennis  
medRxiv 2025.03.07.25323569; doi: [https://doi.org/10.1101/2025.03.07.25323569](https://doi.org/10.1101/2025.03.07.25323569)

## OntoGPT Integration
Our framework utilises the **OntoGPT** package for ontology-based structuring of clinical data. See [OntoGPT's official site](https://monarch-initiative.github.io/ontogpt/) for installation instructions.

We provide:
- IBD-specific templates (combined and for individual entities) with prompt engineering: `IBD_LLM/OntoGPT_templates/`
- Compatibility with any OntoGPT-compliant LLM, including those using [Ollama](https://ollama.com/) or the OpenAI API
- MIMIC-IBD patient imaging record [trained weights for Llama 3.1 8B](https://huggingface.co/UoS-HGIG/MIMIC)

![Example Input/Output](https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/example.png)


## Additional Tool: HPO Mapper
The IBD-LLM toolkit includes an **HPO Mapper**, a supplementary tool designed to map patient findings to Human Phenotype Ontology (HPO) terms using semantic similarity. This enhances structured data integration by linking findings to relevant genomic data.

![HPO Mapping](https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/hpo.png)

### HPO Mapper Workflow
1. **Extract Findings**: Load patient findings from JSON files.
2. **Find Best HPO Match**: Compute semantic similarity using `nomic-embed-text`.
3. **Retrieve Associated Genes**: Query our [HPO SQLite database](https://huggingface.co/datasets/UoS-HGIG/hpo_genes) for genes linked to the HPO term.
4. **Store Results**: Save the mapped findings in a CSV file.
5. **Logging**: Logs are stored in `pipeline.log`.

### Requirements
Ensure you have the following dependencies installed:

```bash
pip install numpy ollama sqlite3
```
Additionally, you must pull the `nomic-embed-text` model before running the script:

```bash
ollama pull nomic-embed-text
```
and have obtained the [HPO embeddings](https://huggingface.co/datasets/UoS-HGIG/hpo_genes)

### Input Format
Each patient's findings should be as on JSON file:
````
{
    "subject_id": "",
    "data": [
        {
            "finding": "",
            "anatomical_region": ""
        }
    ]
}
````
https://github.com/UoS-HGIG/IBD_LLM/blob/main/src/HPO_mapper/hpo_input_template.json

## Customisation
- **Adjust Similarity Threshold**: Modify the threshold in `find_best_hpo_match()` for more/less strict matching.
- **Database Updates**: Ensure `hpo_genes.db` contains updated HPO embeddings and gene mappings.

## License
This project is licensed under the MIT License.
