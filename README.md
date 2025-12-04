# Conceptual Metaphor Theory Prompting (CMT-Prompting)

This repository contains the official implementation of **CMT-based prompting** for large language models.  
Conceptual Metaphor Theory (CMT), originating from cognitive psychology and cognitive linguistics, explains how humans understand abstract concepts through mappings to concrete experiences.  
This project adapts that mechanism for LLM prompting, improving interpretability and structured reasoning.

## Contents
- `prompts/cmt_prompt.txt` – A reusable prompt template encoding source–target metaphor mappings.
- `benchmark/benchmark.json` – A 100-task benchmark covering:
  - Metaphor Identification and Mapping (MIM)
  - Domain-Specific Reasoning (DSR)
  - Explanation and Teaching Tasks (ETT)
  - Reading Comprehension of Metaphors (RCM)
- `paper/cmt.pdf` – The full research paper describing the theory, benchmark, and experimental results.
- `examples/` – Minimal scripts demonstrating how to run tasks with your own LLM backend.

## Usage

Example: run a single benchmark item through your model.

```python
from pathlib import Path
import json

prompt = Path("prompts/cmt_prompt.txt").read_text()
benchmark = json.load(open("benchmark/benchmark.json"))

item = benchmark["MetaphorIdentificationMapping"][0]
full_prompt = prompt + "\n\nTask:\n" + item["problem_text"]
print(full_prompt)