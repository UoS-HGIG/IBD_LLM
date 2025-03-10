import os
import yaml
import csv
import ollama
import time
import json

# User-configurable paths and parameters
INPUT_FOLDER = "<path_to_input_folder>"  # e.g., "/path/to/input/files/"
OUTPUT_TSV = "<path_to_output_tsv>"  # e.g., "/path/to/output/qc_results.tsv"
DETAILED_OUTPUT_FOLDER = "<path_to_detailed_output_folder>"  # e.g., "/path/to/detailed/reports/"
MODEL_NAME = "<model_name>"  # e.g., "llama3.3:70b-instruct-fp16"
NUM_CTX = 16000  # Context size for the model
MAX_RETRIES = 3  # Number of retries for querying the model

os.makedirs(DETAILED_OUTPUT_FOLDER, exist_ok=True)

# Helper to parse YAML file
def parse_yaml_file(file_path):
    """
    Parse the YAML file content and extract required sections.
    """
    try:
        with open(file_path, "r") as file:
            content = yaml.safe_load(file)
        return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Query the Ollama model
def query_with_retries(prompt, model=MODEL_NAME, num_ctx=NUM_CTX, retries=MAX_RETRIES):
    """
    Query the Ollama model with retries for handling incremental responses.
    """
    for attempt in range(retries):
        try:
            print(f"Querying model '{model}' (attempt {attempt + 1})...")
            response_stream = ollama.generate(model=model, prompt=prompt, options={"num_ctx": num_ctx})
            full_response = ""
            for chunk in response_stream:
                if isinstance(chunk, dict) and "response" in chunk:
                    full_response += chunk["response"]
                if isinstance(chunk, dict) and chunk.get("done", False):
                    break
            if full_response.strip():
                return full_response.strip()
            print(f"Warning: Empty response on attempt {attempt + 1}. Retrying...")
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
        time.sleep(2)
    print("Failed to retrieve a valid response after retries.")
    return None

# Perform quality check with the LLM
def quality_check_with_ollama(input_text, extracted_object, model=MODEL_NAME, num_ctx=NUM_CTX):
    """
    Use Ollama to perform quality checks on the extracted_object with a specific context size.
    """
    prompt = f"""
    Perform a quality control check on the extracted information below.
    
    Input Text:
    {input_text}
    
    Extracted Object:
    {extracted_object}
    
    Check for the following:
    1. Any missing findings in the extracted object that are mentioned in the input text.
    2. Any incorrect or misinterpreted findings in the extracted object mentioned in the input text.
    3. Any extraneous findings in the extracted object that are not present in the input text.
    
    Provide a structured response with:
    - Missing Findings:
    - Incorrect Findings:
    - Extraneous Findings:
    - Explanation: (Explain why these issues exist and provide specific details.)
    """
    
    response_text = query_with_retries(prompt, model=model, num_ctx=num_ctx)
    if not response_text:
        return {"missing": [], "incorrect": [], "extraneous": []}, "No explanation provided."
    
    issues = {"missing": [], "incorrect": [], "extraneous": []}
    explanation = ""
    
    try:
        if "Missing Findings:" in response_text:
            issues["missing"] = response_text.split("Missing Findings:")[1].split("Incorrect Findings:")[0].strip().split("\n")
        if "Incorrect Findings:" in response_text:
            issues["incorrect"] = response_text.split("Incorrect Findings:")[1].split("Extraneous Findings:")[0].strip().split("\n")
        if "Extraneous Findings:" in response_text:
            issues["extraneous"] = response_text.split("Extraneous Findings:")[1].split("Explanation:")[0].strip().split("\n")
        if "Explanation:" in response_text:
            explanation = response_text.split("Explanation:")[1].strip()
    except Exception as e:
        print(f"Error parsing LLM response: {e}")
        explanation = "Parsing error occurred."
    
    return issues, explanation

# Process each file
def process_file(file_path, detailed_output_folder, model=MODEL_NAME, num_ctx=NUM_CTX):
    data = parse_yaml_file(file_path)
    if not data:
        return None

    input_text = data.get("input_text", "")
    extracted_object = data.get("extracted_object", {})
    
    if not input_text or not extracted_object:
        print(f"Missing input_text or extracted_object in {file_path}")
        return None

    qc_results, explanation = quality_check_with_ollama(input_text, extracted_object, model=model, num_ctx=num_ctx)
    any_issues = bool(qc_results["missing"] or qc_results["incorrect"] or qc_results["extraneous"])
    
    detailed_output_path = os.path.join(detailed_output_folder, f"{os.path.basename(file_path)}.qc.yaml")
    with open(detailed_output_path, "w") as detailed_file:
        yaml.dump({
            "file_name": os.path.basename(file_path),
            "qc_results": qc_results,
            "explanation": explanation,
            "flag": "Y" if any_issues else "N"
        }, detailed_file)

    return {
        "file_name": os.path.basename(file_path),
        "missing": len(qc_results["missing"]),
        "incorrect": len(qc_results["incorrect"]),
        "extraneous": len(qc_results["extraneous"]),
        "flag": "Y" if any_issues else "N"
    }

# Process all files in the folder
results = []
for file_name in os.listdir(INPUT_FOLDER):
    if file_name.endswith(".txt"):
        input_file_path = os.path.join(INPUT_FOLDER, file_name)
        print(f"Processing file: {file_name}")
        qc_result = process_file(input_file_path, DETAILED_OUTPUT_FOLDER, model=MODEL_NAME, num_ctx=NUM_CTX)
        if qc_result:
            results.append(qc_result)

# Write results to a TSV file
with open(OUTPUT_TSV, "w", newline="") as tsv_file:
    writer = csv.DictWriter(tsv_file, fieldnames=["file_name", "missing", "incorrect", "extraneous", "flag"], delimiter="\t")
    writer.writeheader()
    writer.writerows(results)

print(f"Quality check completed. Summary saved to {OUTPUT_TSV}")
print(f"Detailed QC reports saved in {DETAILED_OUTPUT_FOLDER}")