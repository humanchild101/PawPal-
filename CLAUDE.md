# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This is a CodePath Module 2 course project ("PawPal+"). The class model has been designed and stubbed out, but scheduling logic and UI wiring are not implemented yet:

- `pawpal_system.py` is the backend/logic module: `Task`, `PetSchedule`, `Pet`, `Owner` as Python `@dataclass`es matching `diagrams/uml.mmd`. All methods are currently empty stubs (`pass` / implicit `None` return) — no scheduling behavior exists yet.
- `app.py` is a thin Streamlit scaffold — it only collects owner/pet/task info in the UI (into `st.session_state.tasks`, a plain list of dicts) and does **not** import or use `pawpal_system.py` yet. The "Generate schedule" button just shows a warning.
- `diagrams/uml.mmd` reflects the current (non-placeholder) design — see "Architecture notes" below for the shape.
- `reflection.md` has a first-draft "Initial design" section filled in but the rest of the assignment writeup sections are still blank; `ai_interactions.md` is still a blank template.
- There are no tests yet, despite the README documenting `pytest` as the test runner.

When working in this repo, expect to be **filling in stubbed logic against an established design**, not inventing the class model from scratch.

## Scenario / what to build

PawPal+ is meant to become a Streamlit app that helps a pet owner plan daily pet care tasks (walks, feeding, meds, enrichment, grooming) subject to constraints like available time, task priority, and owner preferences. Remaining work:

1. Implement scheduling logic in `pawpal_system.py` (selecting/ordering tasks under `PetSchedule.available_minutes` and `Task.priority`), filling in the method stubs incrementally — including `PetSchedule.get_reasoning()`, which should explain why the plan was chosen.
2. Add `pytest` tests for scheduling behavior.
3. Wire `pawpal_system.py` into `app.py`'s UI (replace the `st.session_state.tasks` dict-list with real `Task`/`Pet`/`Owner`/`PetSchedule` objects, and make "Generate schedule" call into the real logic).
4. Keep `diagrams/uml.mmd` in sync if the design changes during implementation.

Keep `README.md`'s "Smarter Scheduling" table, sample output, and demo walkthrough sections updated as functionality lands — they are currently placeholders expected to be filled in.

## Commands

```bash
# Setup (uses a venv already present at .venv/)
source .venv/bin/activate
pip install -r requirements.txt

# Run the app
streamlit run app.py

# Run tests (once tests exist)
pytest
pytest --cov
```

## Architecture notes

- Single-page Streamlit app (`app.py`) — no multi-page routing, no separate frontend/backend process. All business logic lives in `pawpal_system.py`, imported by `app.py` (once wired up), not inline in the Streamlit script.
- The domain model in `pawpal_system.py` is a **strict one-directional tree with no back-references**: `Owner "1"→"0..*" Pet "1"→"1" PetSchedule "1"→"0..*" Task`. A `Pet` does not point back to its `Owner`, and a `Task` does not point back to its `PetSchedule`/`Pet`/`Owner` — a task's owning pet is implied entirely by which `PetSchedule.task_list` it lives in. This was a deliberate design choice to avoid manually keeping bidirectional references in sync; preserve it rather than adding parent back-pointers.
- Priority and duration live on `Task` itself (`Task.priority`, `Task.duration_minutes`), not as a separate ordering list on `PetSchedule` — avoid reintroducing a parallel `owner_priorities`-style list, since that was deliberately removed to prevent it from drifting out of sync with per-task data.
- `PetSchedule.available_minutes` (an `int`) is the structured stand-in for "owner time preferences" — prefer extending this over reintroducing a free-text preferences field, since unstructured text can't be used in scheduling math.
- `st.session_state.tasks` in `app.py` is currently the only state held by the UI (a plain list of dicts with `title`, `duration_minutes`, `priority`) and is **not yet connected** to `pawpal_system.py`. When wiring the UI to the backend, replace this dict-list with real `Task`/`Pet`/`Owner`/`PetSchedule` objects rather than maintaining both.
- The grading scaffold (`ai_interactions.md`, `diagrams/uml.mmd`, reflection sections in `README.md`/`reflection.md`) has specific expected filenames/sections — don't rename or restructure these without checking if grading tooling depends on the exact names (e.g. `diagrams/uml.mmd` was deliberately renamed from `uml_draft.mmd` to match a grading expectation, per commit history).
