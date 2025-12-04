import json
from pathlib import Path

# Load the CMT system prompt
prompt_path = Path("prompts/cmt_prompt.txt")
cmt_prompt = prompt_path.read_text(encoding="utf-8")

# Load benchmark (a dict with category keys)
benchmark_path = Path("benchmark/benchmark.json")
with benchmark_path.open(encoding="utf-8") as f:
    benchmark = json.load(f)

# Select a category and the first task within it
mim_tasks = benchmark["MetaphorIdentificationMapping"]
task = mim_tasks[0]

task_description = task.get("task_description", "")
problem_text = task.get("problem_text", "")

# Build the full prompt exactly as the experimental pipeline expects
full_prompt = f"""{cmt_prompt}

Task: {task_description}

{problem_text}
"""

print("=== Prompt to send to the LLM ===")
print(full_prompt)