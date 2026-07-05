# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

=== Today's Schedule ===
08:30 AM — Spyder Feed (10 min, required)
11:00 AM — Jasmine Feed (5 min, required)
11:10 AM — Spyder Feed (10 min, required)
02:30 PM — Squash feed (5 min, required)

Not scheduled:
02:00 AM — Jasmine Play (30 min, priority 4/10) [time conflict]
04:30 AM — give squash a squash (5 min, priority 5/10) [time conflict]
08:00 AM — Jasmine Walk (30 min, priority 4/10) [time conflict]
09:00 AM — Spyder litter box clean (15 min, priority 4/10) [time conflict]
10:00 AM — Squash litter box cleaning (15 min, priority 4/10) [time conflict]

Selected 4 task(s) totaling 30 of 10 available minutes.
Required tasks were guaranteed a slot first; remaining tasks were then added by priority (10 = highest, 1 = lowest) until the available time ran out:
  - Jasmine Feed (required, 5 min)
  - Spyder Feed (required, 10 min)
  - Spyder Feed (required, 10 min)
  - Squash feed (required, 5 min)
Warning: required tasks alone need 20 more minute(s) than your 10-minute budget. All required tasks were still included; consider freeing up more time.

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:
=========================================== test session starts ===========================================
platform darwin -- Python 3.12.1, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/nikhila/Desktop/Important/Code/CodePath/PawPal-
plugins: anyio-4.14.1
collected 43 items                                                                                        

tests/test_pawpal.py ...........................................                                    [100%]

=========================================== 43 passed in 0.08s ============================================


The tests cover filtering, conflict messages, time conflict cases, time availability warnings, adding/remving tasks/pets, and sortings

Confidence level that it works properly: 4.4/5

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | format_schedule| directly sorts the tasks in order of time when formatting the schedule content / text for display|
| Filtering | filter_tasks|There are 2 options to either filterr by pet name or task completion status. |
| Conflict handling | find_time_conflicts, times_overlap.  | returns conflicting task pairs, finds overlapping time windows |
| Recurring tasks | complete_task| if this method sees that there is a recurrence interval like daily or weekly, it will create a new Task for the next day/week |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Add pet name called Potato if species cat and a cat named Onion
2. Add a new task for onion called "Feed", 5 mins, 10/10 priority, required, 8 am, daily
3. Add the same for Potato at the same time, but change the name to "Feed Potato Now"
4. Add a task for potato called play with mouse doll, 30 mins, 7/10, 9:15 am, weekly
5. onion --> "outdoor exposure", 30 mins, 8/10,  2:45 PM, daily
6. Set available time to 20 minutes, generate schedule
7. "2 task(s) are scheduled at overlapping times — see the items marked in red below." - Feeding potato and onion are at the same time, and therefore flagged. ⚠️ Warning: Not Enough Time for Required Tasks Required tasks alone need 20 more minute(s) than your 20-minute budget
8. set time availablee to 200 minutres and add feed onion task at 9 am after removing original feed onion task. Output is normal
9. Set feed potato task to complete. A new feed potato task will automatically appear as pending. if you use the filterr, now you will see the completed task with teh completion filter. 

```
python3 main.py
=== Daily Schedule ===
04:30 AM — give squash a squash (5 min, priority 5/10)
08:30 AM — Spyder Feed (10 min, required)
09:00 AM — Spyder litter box clean (15 min, priority 4/10)
11:00 AM — Jasmine Feed (5 min, required)
11:10 AM — Spyder Feed (10 min, required)
02:30 PM — Squash feed (5 min, required)

Not scheduled:
02:00 AM — Jasmine Play (30 min, priority 4/10) [insufficient time]
08:00 AM — Jasmine Walk (30 min, priority 4/10) [insufficient time]
09:00 AM — Squash litter box cleaning (15 min, priority 4/10) [insufficient time]

Selected 6 task(s) totaling 50 of 60 available minutes.
Required tasks were guaranteed a slot first; remaining tasks were then added by priority (10 = highest, 1 = lowest) until the available time ran out:
  - Jasmine Feed (required, 5 min)
  - Spyder Feed (required, 10 min)
  - Spyder Feed (required, 10 min)
  - Squash feed (required, 5 min)
  - give squash a squash (priority 5/10, 5 min)
  - Spyder litter box clean (priority 4/10, 15 min)

Completed tasks:
  - Jasmine Feed
Pending tasks:
  - Jasmine Walk
  - Jasmine Play
  - Spyder Feed
  - Spyder Feed
  - Spyder litter box clean
  - Squash litter box cleaning
  - Squash feed
  - give squash a squash
Jasmine tasks:
  - Jasmine Walk
  - Jasmine Feed
  - Jasmine Play
```
**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
