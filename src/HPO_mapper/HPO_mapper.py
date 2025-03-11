import os
import json
import sqlite3
import csv
import logging
import ollama
import numpy as np
from numpy.linalg import norm

# User-configurable paths
PATIENT_JSON_DIR = "<path_to_patient_jsons>"  # e.g., "/path/to/patient/files/"
DB_PATH = "<path_to_hpo_database>"  # e.g., "/path/to/hpo_genes.db"
OUTPUT_DIR = "<path_to_output_directory>"  # e.g., "/path/to/output/files/"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Setup Logging
logging.basicConfig(filename=os.path.join(OUTPUT_DIR, "pipeline.log"), level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def find_best_hpo_match(finding, region, model="nomic-embed-text", threshold=0.74):
    """
    Finds the best HPO match using semantic similarity with embeddings.
    The function generates an embedding for the input text (finding + region)
    and compares it to precomputed embeddings of HPO terms stored in a database.
    """
    query_text = f"{finding} in {region}"
    query_embedding = np.array(ollama.embeddings(model=model, prompt=query_text)["embedding"])
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT hpo_id, hpo_name, embedding FROM hpo_embeddings")
    
    best_match, best_score = None, -1

    for hpo_id, hpo_name, embedding_str in cursor.fetchall():
        hpo_embedding = np.array(json.loads(embedding_str))  # Convert JSON back to NumPy array
        
        # Compute cosine similarity
        similarity = np.dot(query_embedding, hpo_embedding) / (norm(query_embedding) * norm(hpo_embedding))

        if similarity > best_score:
            best_score = similarity
            best_match = {"hpo_id": hpo_id, "hpo_term": hpo_name}
    
    conn.close()
    return best_match if best_score > threshold else None  # Return match if above threshold


def get_genes_for_hpo(hpo_id):
    """Retrieves associated genes for a given HPO ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT genes FROM hpo_gene WHERE hpo_id = ?", (hpo_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0].split(", ") if result else []  # Return list of genes


def get_hpo_for_finding(finding, region):
    """Finds the best HPO term and retrieves associated genes."""
    hpo_match = find_best_hpo_match(finding, region)
    
    if hpo_match:
        hpo_match["genes"] = get_genes_for_hpo(hpo_match["hpo_id"])
    else:
        hpo_match = {"hpo_id": "NA", "hpo_term": "NA", "genes": []}
    
    return hpo_match


def process_patient_findings(patient_file):
    """Maps patient findings to HPO terms and retrieves relevant genes."""
    with open(patient_file, "r") as f:
        patient_data = json.load(f)

    subject_id = patient_data.get("subject_id", "Unknown")
    mapped_findings = []
    
    logging.info(f"Processing Patient: {subject_id}")

    for entry in patient_data.get("data", []):
        finding = entry.get("finding", "Unknown")
        region = entry.get("anatomical_region", "Unknown")
        hpo_match = get_hpo_for_finding(finding, region)
        
        mapped_findings.append({
            "finding": finding,
            "region": region,
            "hpo_id": hpo_match["hpo_id"],
            "hpo_term": hpo_match["hpo_term"],
            "genes": hpo_match["genes"]
        })
    
    mapped_hpo_csv = os.path.join(OUTPUT_DIR, f"{subject_id}_hpo_mapped.csv")
    with open(mapped_hpo_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["finding", "region", "hpo_id", "hpo_term", "genes"])
        for entry in mapped_findings:
            writer.writerow([entry["finding"], entry["region"], entry["hpo_id"], entry["hpo_term"], ", ".join(entry["genes"] )])
    
    logging.info(f"Saved HPO mapping for {subject_id}: {mapped_hpo_csv}")

# Process all patient files in the folder
for filename in os.listdir(PATIENT_JSON_DIR):
    if filename.endswith(".json"):
        patient_file = os.path.join(PATIENT_JSON_DIR, filename)
        process_patient_findings(patient_file)
