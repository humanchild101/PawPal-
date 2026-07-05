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

Yes it did change. One change was that I had pet_schedule in multiple classes and it was redundant, especially because it was pointing to the same pet and owner. I used Claude to fix this. Along with this, when first creatinng the classes, I failed to add proper attributes for the Task class. Claude also added duration, completion status, recurrence, which are attributes of any real work task. This was a good change because if I didn't add it, I would have come across this again when implementing the scheduling system and it would have been confusing or difficult to fix then instead of making the change while the classes are still being designed and implemented. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
My scheduler considers the user's preferences with regards to their personal schedule/timings. Along with that, the priority tasks are considered before medium/low priority, especially given time constraints. I decided that these would be the most important constraints because they consider any inconveniences that the user may have along with the important needs of the pet to create a schedule that gives the owner a chance to properly take care of the pet. 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes. 
- Why is that tradeoff reasonable for this scenario?
The scheduler cannot assign a mandatory amount of time that the user is available. Things like feeding the pet, taking them for a walk, and other general responsibilities when taking care of a pet are ultimately left to the user to decide whether they are 'important' or not. If the owner puts that they are availabe for 0 minutes of the day, the system cannot necessarily deny it or display an error because there may be circumstances when the owner is out or asks someone else to take care of the pet. The user may put that they only have an hourr of available time on a given day, and the program may only select some priority tasks until that time limit is reached, even if there are still priority tasks remaining, such as feeding a second pet that needs feeding. This is a reasonable tradeoff though, because most of the time, the use knows the priorities of their pets, and will set aside time. Some may need more or less caring than others. They can assign priority of tasks when Task objects are created from a scale of 1-10 (1 being lowest, 10 being highest) so that the highest priority tasks are given first. Even the user does not appear to have enough available time, the tasks are still displayed as not scheduled with a priority mark and a time conflict makr so the user can decide on their own if they need to do them. additionally, if a certain very high priority task is later in the day and the user doesn't have enough time, the program suggests that the user extends their available time. All tasks that are 'required' are still shown regardless of the user's given time. Ultimately its up to the user to choose in that case. 
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
