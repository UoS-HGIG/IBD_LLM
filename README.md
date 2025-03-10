# IBD-LLM  

IBD-LLM is a specialised large language model fine-tuned for structuring inflammatory bowel disease (IBD) patient records. This model integrates genomic data, structured findings, and clinical information to improve precision in IBD research and patient stratification.  

🔗 **Pretrained on MIMIC-IV:** The model builds on our fine-tuned **MIMIC-LLM**, trained on clinical records from the MIMIC-IV dataset.  
📌 **MIMIC-LLM Weights:** [UoS-HGIG/MIMIC](https://huggingface.co/UoS-HGIG/MIMIC)  

## Features  
- Standardising free-text medical records  
- Extracting structured clinical data for IBD  
- Supporting AI-driven patient stratification  

## OntoGPT Integration  
IBD-LLM utilises the **OntoGPT** package for ontology-based structuring of clinical data. We provide:  
- **OntoGPT templates** for standardising outputs  
- **Python scripts** for **LLM-QC** and **HPO mapping**, ensuring high-quality structured data integration  

For further details, refer to our documentation or contact the **University of Southampton HGIG** team.
