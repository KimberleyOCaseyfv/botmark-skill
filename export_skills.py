#!/usr/bin/env python3
"""Export BotMark skill definitions to JSON files for the GitHub repo.

Run from the project root:
  python botmark-skill/export_skills.py
"""
import json
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend', 'assessment-engine'))

from services.bot_eval_skill import get_skill_definition, SYSTEM_PROMPT_INJECTION, SKILL_VERSION

OUT_DIR = os.path.dirname(__file__)

FORMATS = ['openclaw', 'openai', 'anthropic', 'generic']

for fmt in FORMATS:
    skill = get_skill_definition(format=fmt)
    # Add server URL placeholder
    if isinstance(skill, dict):
        skill['server_url'] = 'https://botmark.cc'
        skill['skill_version'] = SKILL_VERSION
    path = os.path.join(OUT_DIR, f'skill_{fmt}.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(skill, f, indent=2, ensure_ascii=False)
    print(f"Exported: {path}")

# Export system prompt separately
prompt_path = os.path.join(OUT_DIR, 'system_prompt.md')
with open(prompt_path, 'w', encoding='utf-8') as f:
    f.write(SYSTEM_PROMPT_INJECTION)
print(f"Exported: {prompt_path}")

print(f"\nDone! Skill version: {SKILL_VERSION}")
