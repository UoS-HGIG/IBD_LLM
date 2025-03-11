# Inflammatory Bowel Disease (IBD) Large Language Model (LLM) Patient Structuring Toolkit

## Overview
The University of Southampton HGIG IBD-LLM toolkit is a specialised large language model fine-tuned for structuring inflammatory bowel disease (IBD) patient records. This model integrates genomic data, structured findings, and clinical information to improve precision in IBD research and patient stratification.


![IBD-LLM Abstract](https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/abstract.png))

### Reference
**Application of Generative Artificial Intelligence to Utilise Unstructured Clinical Data for Acceleration of Inflammatory Bowel Disease Research**  
Alex Z Kadhim, Zachary Green, Iman Nazari, Jonathan Baker, Michael George, Ashley Heinson, Matt Stammers, Christopher Kipps, R Mark Beattie, James J Ashton, Sarah Ennis  
medRxiv 2025.03.07.25323569; doi: [https://doi.org/10.1101/2025.03.07.25323569](https://doi.org/10.1101/2025.03.07.25323569)

## Pretrained on MIMIC-IV
The model builds on our fine-tuned MIMIC-LLM, trained on clinical records from the MIMIC-IV dataset.
- **MIMIC-LLM Weights**: `UoS-HGIG/MIMIC`
- **MIMIC-IBD Patient Imaging Record Trained Weights**: (See Hugging Face link)

## Features
- **Standardising free-text medical records**
- **Extracting structured clinical data for IBD**
- **Supporting AI-driven patient stratification**

## OntoGPT Integration
IBD-LLM utilises the **OntoGPT** package for ontology-based structuring of clinical data. See [OntoGPT's official site](https://monarch-initiative.github.io/ontogpt/) for installation instructions.

We provide:
- **IBD-specific templates** (combined and for individual entities) with prompt engineering: `IBD_LLM/OntoGPT_templates/`
- **Compatibility with any OntoGPT-compliant LLM**, including those using **Ollama** or the **OpenAI API**
- **MIMIC-IBD patient imaging record trained weights** for **Llama 3.1 8B** (see Hugging Face link)

## Additional Tool: HPO Mapper
The IBD-LLM toolkit includes an **HPO Mapper**, a supplementary tool designed to map patient findings to Human Phenotype Ontology (HPO) terms using semantic similarity. This enhances structured data integration by linking findings to relevant genomic data.

![HPO Mapping](https://github.com/UoS-HGIG/IBD_LLM/blob/main/img/hpo.png)

### HPO Mapper Workflow
1. **Extract Findings**: Load patient findings from JSON files.
2. **Find Best HPO Match**: Compute semantic similarity using `nomic-embed-text`.
3. **Retrieve Associated Genes**: Query the SQLite database (https://huggingface.co/datasets/UoS-HGIG/hpo_genes) for genes linked to the HPO term.
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

### Execution
Run the script to process all JSON files in the `patient_json_dir`:
```bash
python script.py
```

## Customization
- **Adjust Similarity Threshold**: Modify the threshold in `find_best_hpo_match()` for more/less strict matching.
- **Database Updates**: Ensure `hpo_genes.db` contains updated HPO embeddings and gene mappings.

## Troubleshooting
- **No HPO Match Found**: Check embedding consistency or lower similarity threshold.
- **Database Errors**: Ensure `hpo_genes.db` is accessible and correctly formatted.

## License
This project is licensed under the MIT License.
