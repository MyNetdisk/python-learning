# AGENTS.md

## Repository overview

- This repository is a lightweight Python learning workspace rather than a packaged application.
- `README.md` is the main artifact: a Chinese 12-week study plan built around beginner Python practice.
- The numbered directories contain small exercise scripts that match early learning topics.

## Current structure

- `README.md` - Chinese study plan and workflow guidance.
- `01_Day_Introduction/helloworld.py` - introductory print and type examples.
- `02_Day_Variables_builtin_functions/variables.py` - variables, type conversions, and `input()` examples.

## Editing guidance

- Preserve the beginner-friendly teaching style. Prefer clarity and explicit code over clever abstractions.
- Treat the repository as a collection of study materials and small scripts, not as a library or production service.
- Keep the existing directory naming pattern for new lessons: `NN_Day_Topic/`.
- Keep explanatory documentation in Chinese unless the user asks for a different language.
- Short English identifiers and inline comments inside Python examples are acceptable when they help explain the lesson.
- Avoid introducing unnecessary dependencies, packaging files, CI setup, or heavy tooling unless the user explicitly requests them.
- When modifying example scripts, favor simple runnable snippets over reusable architecture.

## Verification

- Run scripts directly with Python from the repository root.
- Useful checks:
  - `python 01_Day_Introduction/helloworld.py`
  - `python 02_Day_Variables_builtin_functions/variables.py`
- Note: `02_Day_Variables_builtin_functions/variables.py` is interactive because it calls `input()`. If you verify it non-interactively, provide stdin or limit validation to syntax/basic execution expectations.
- There is currently no formal automated test suite in this repository.

## README and content updates

- Preserve the staged learning-plan structure in `README.md` when editing or extending it.
- If you add new day folders or learning assets, keep them aligned with the plan and reference them from `README.md` when appropriate.
- Do not remove user-authored notes or beginner exercise content unless the change is explicitly requested.
