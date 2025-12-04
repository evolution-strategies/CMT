# Conceptual Metaphor Theory Prompting (CMT-Prompting)

This repository contains the official implementation of **CMT-based prompting** for large language models.  
Conceptual Metaphor Theory (CMT), originating from cognitive psychology and cognitive linguistics, explains how humans understand abstract concepts through mappings to concrete experiences.  
This project adapts that mechanism for LLM prompting, improving interpretability, explanation quality, and structured reasoning.

## Contents

- **prompts/cmt_prompt.txt** – A reusable system prompt that encodes the CMT framework (source→target mappings, inference rules, and examples).
- **benchmark/benchmark.json** – A 100-task benchmark covering:
  - Metaphor Identification and Mapping (MIM)
  - Domain-Specific Reasoning (DSR)
  - Explanation and Teaching Tasks (ETT)
  - Reading Comprehension of Metaphors (RCM)
- **examples/run_example.py** – Minimal script demonstrating how to combine the CMT system prompt with a benchmark task.

## Usage

Example: load the CMT system prompt, read a benchmark task, and build a full model-ready prompt.

```python
from pathlib import Path
import json

# Load CMT system prompt
cmt_prompt = Path("prompts/cmt_prompt.txt").read_text()

# Load benchmark
benchmark = json.load(open("benchmark/benchmark.json", "r", encoding="utf-8"))

# Select a task (first MIM item)
task = benchmark["MetaphorIdentificationMapping"][0]

task_description = task["task_description"]
problem_text = task["problem_text"]

# Assemble the final prompt
full_prompt = f"""{cmt_prompt}

Task: {task_description}

{problem_text}
"""

print(full_prompt)