# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The main classes that I am including are 
    Pet, Task, PetSchedule, Owner.
    - Pet will have attributes such as name, species, owner (Owner object), meds, last_walked, last_bathed, last_fed, schedule (PetSchedule object), special_info. Methods: feed, bathe, walk, play, add_to_schedule, remove_from_schedule.
    - Task will have attributes such as task, owner (Owner object), pet (optional Pet object, if you want this task to be for a specific pet task description.) Methods: modify_task
    - PetSchedule will have attributes such as pet (Pet object), owner (Owner object), task_list (list of Task objects), owner_time_preferences (text desc), owner_priorities (list of Task objects). Methods: add_task, remove_task, change_preference, change_priority 
    - Owner will have attributes such as pet_list (list of Pet objects), pet_schedule_list (list of PetSchedule objects) time_preferences. Methods: add_pet, remove_pet, change_pref 
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
