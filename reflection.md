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

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)? I used AI for design suggestions, implementation, and refactoring. Examples include asking it for suggestions with the initial design of the classes and asking it to implement changes to the scheduling system. 
- What kinds of prompts or questions were most helpful? Direct prompts that gave a clear idea of what to implement gave the best results. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
One of the AI suggestions was with regards to conflict handling. Its suggestion was quite simple and did not really address the conflicts. There are many issues to consider such as when the user did not input enough time available to complete any tasks, or barely enoguh time to finish tasks. Along with not resolving these, the Claude suggestion, also didn't account for what tasks might need to be counted as 'required'. I found these issues before testing but primarily saw them once i started running the program in the console. I directed Claude to add 'required' tags to the tasks deemed by teh user as requuired. Additioally, I changed the program such that when the user doesn't input that mucch time, the required tasks are still shown as part of the schedule btu with a warning. I also added another part to the output where it shows the tasks that werent scheduled, bevcause n the beginning Claude just left out whatever tasks didnt fit, even if they were priority, so diuspkaying the unscheduled tasks too would provide the user witjh more clarity and ultimately they can decide whether to stick to the suggested schedule or modify it if there was an unscheduled task with high priority. Initially the scale for priority was just 3 options, I tried a scale of 1-5 next, but it seemed to still cause confuaion if there weere mutliple tasks and there were some that were of the same priority in the program but not the same priority in reality (ex: feeding a dog vs caring for an animal that maybe doesnt need to be cared for as often but still needs it. feeding both is technically important but feeding the dog in this hypothetical example is more important). I finally changed it to a 1-10 scale. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test? 
- Why were these tests important?
I tested behaviors such as the sorting, filtering, and especially the conflicts/warnings display/handling as well as the reasoning display. There were others, but I thought these were most important. This is because they looked into waht was essentially the core logic of the program, and if those tests failed it would mean I needded to revise that logic and look into ways to improve it and the functionality. 
**b. Confidence**

- How confident are you that your scheduler works correctly? 4.4
- What edge cases would you test next if you had more time? I'd test with mutliple pets and also look more into the user preferences input in the very beginning of the application page to see if it's actually effecting the schedule and how so if it does. 

---

## 5. Reflection

**a. What went well**

I'm satisfied with the schedule display and the variations of the final display depending on conflicts and warnings
**b. What you would improve**

I would add more functionality to the user preferences input. Right now, it's kind of just there, and I don't think it really adds much to the program functionality. I would imrpove this app by looking into that and giving it a real purpose. Also, I would like to imrpove the formattinig of the app a little more.  
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project? Designing systems with AI requires a lot of going back and forth between the code and tests and the application, at least in my case. The AI suggestions are good much of the time, but it's important to also think beyond them, because while I was working on thsi project, I ntoiced several aspects that Claude did not consider. It's important to use the suggestions, but also provide Claude with morre context or additional information on what you need so that it can help you better. Relying on Claude for suggestions is fine, but I learned that I would also need to evaluate those suggestions on my own again. 
