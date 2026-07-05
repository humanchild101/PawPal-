from datetime import date, datetime

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+ — a pet care planning assistant. Add your pets, give them
tasks, and generate a daily schedule based on priority and available time.
"""
)

with st.expander("Scenario", expanded=False):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

if "owner" not in st.session_state:
    st.session_state.owner = Owner()

owner: Owner = st.session_state.owner

st.divider()

st.subheader("Owner Preferences")
preferences = st.text_input(
    "Time preferences",
    value=owner.time_preferences,
    placeholder="e.g. mornings only, meetings at 3pm on weekdays",
)

if st.button("Save preferences"):
    owner.change_pref(preferences)
    st.success("Preferences saved.")

st.divider()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", placeholder="e.g. Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"], index=None, placeholder="Select species")

if st.button("Add pet"):
    if not pet_name or not species:
        st.warning("Enter a pet name and select a species before adding.")
    else:
        owner.add_pet(Pet(name=pet_name, species=species))

if owner.pet_list:
    st.write("Current pets:", ", ".join(pet.name for pet in owner.pet_list))

    pet_to_remove = st.selectbox(
        "Remove a pet", [pet.name for pet in owner.pet_list], index=None,
        placeholder="Select a pet to remove", key="remove_pet_select",
    )
    if st.button("Remove pet"):
        if not pet_to_remove:
            st.warning("Select a pet to remove.")
        else:
            owner.remove_pet(next(pet for pet in owner.pet_list if pet.name == pet_to_remove))
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Add a Task")
st.caption("Tasks are added directly to the selected pet's task list.")

pet_names = [pet.name for pet in owner.pet_list]

if not pet_names:
    st.info("Add a pet above before scheduling tasks.")
else:
    selected_pet_name = st.selectbox("Pet", pet_names, index=None, placeholder="Select a pet", key="add_task_pet_select")

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", placeholder="e.g. Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=None)
    with col3:
        priority = st.number_input("Priority (1-10)", min_value=1, max_value=10, value=None)
    required = st.checkbox("Required (e.g. feeding, meds)")
    task_time = st.time_input("Time", value=None)
    frequency = st.selectbox("Repeats", ["", "daily", "weekly"], index=0)

    if st.button("Add task"):
        missing = []
        if not selected_pet_name:
            missing.append("pet")
        if not task_title:
            missing.append("task title")
        if duration is None:
            missing.append("duration")
        if priority is None:
            missing.append("priority")

        if missing:
            st.warning(f"Fill in: {', '.join(missing)}.")
        else:
            selected_pet = next(pet for pet in owner.pet_list if pet.name == selected_pet_name)
            selected_pet.add_task(Task(
                description=task_title,
                duration_minutes=int(duration),
                priority=int(priority),
                required=required,
                time=datetime.combine(date.today(), task_time) if task_time else None,
                frequency=frequency,
            ))

    st.markdown("##### Filter tasks")
    fcol1, fcol2 = st.columns(2)
    with fcol1:
        status_filter = st.selectbox("Status", ["All", "Pending", "Completed"], key="task_status_filter")
    with fcol2:
        pet_filter = st.selectbox("Pet", ["All"] + pet_names, key="task_pet_filter")

    completed_filter = {"All": None, "Pending": False, "Completed": True}[status_filter]
    pet_name_filter = None if pet_filter == "All" else pet_filter

    filtered_tasks = owner.filter_tasks(completed=completed_filter, pet_name=pet_name_filter)
    task_by_id = {id(task): pet for pet in owner.pet_list for task in pet.task_list}
    task_entries = [(task_by_id[id(task)], task) for task in filtered_tasks]

    if task_entries:
        st.write("Current tasks:")
        st.table([
            {
                "pet": pet.name,
                "task": task.description,
                "time": task.time.strftime("%I:%M %p") if task.time else "unscheduled",
                "duration_minutes": task.duration_minutes,
                "priority": task.priority,
                "repeats": task.frequency if task.frequency else "neither",
                "required": task.required,
                "completed": task.completed,
            }
            for pet, task in task_entries
        ])

        def task_label(entry):
            pet, task = entry
            status = "done" if task.completed else "pending"
            time_str = task.time.strftime("%I:%M %p") if task.time else "unscheduled"
            return f"{pet.name}: {task.description} at {time_str} ({status})"

        task_labels = [task_label(entry) for entry in task_entries]
        selected_task_label = st.selectbox(
            "Manage a task", task_labels, index=None,
            placeholder="Select a task", key="manage_task_select",
        )

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Mark complete"):
                if not selected_task_label:
                    st.warning("Select a task to mark complete.")
                else:
                    pet, task = task_entries[task_labels.index(selected_task_label)]
                    pet.complete_task(task)
        with col_b:
            if st.button("Remove task"):
                if not selected_task_label:
                    st.warning("Select a task to remove.")
                else:
                    pet, task = task_entries[task_labels.index(selected_task_label)]
                    pet.remove_task(task)
    elif owner.get_all_tasks():
        st.info("No tasks match the selected filters.")
    else:
        st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("Runs the scheduler across all pets' tasks to build today's plan.")

available_minutes = st.number_input("Available time today (minutes)", min_value=0, max_value=600, value=None)

if st.button("Generate schedule"):
    if available_minutes is None:
        st.warning("Enter the available time before generating a schedule.")
    else:
        scheduler = Scheduler()
        scheduler.set_available_minutes(int(available_minutes))
        scheduler.build_plan(owner)

        conflicted_ids = {id(task) for pair in scheduler.time_conflicts for task in pair}

        if scheduler.time_conflicts:
            st.warning(
                f"⚠️ {len(conflicted_ids)} task(s) are scheduled at overlapping "
                "times — see the items marked in red below."
            )

        st.markdown("#### 📅 Daily Schedule")
        by_time = sorted(scheduler.plan, key=lambda task: task.time or datetime.max)
        if by_time:
            for task in by_time:
                time_str = task.time.strftime("%I:%M %p") if task.time else "Unscheduled"
                tag = "🔒 Required" if task.required else f"⭐ Priority {task.priority}/10"
                line = f"- ⏰ **{time_str}** — {task.description} ({task.duration_minutes} min) · {tag}"
                if id(task) in conflicted_ids:
                    line += "  :red[⚠ Conflict]"
                st.markdown(line)
        else:
            st.info("No tasks were scheduled.")

        if scheduler.unscheduled:
            st.markdown("#### ⚠️ Not Scheduled — Insufficient Time")
            for task in sorted(scheduler.unscheduled, key=lambda task: task.time or datetime.max):
                time_str = task.time.strftime("%I:%M %p") if task.time else "Unscheduled"
                st.markdown(
                    f"- ⏰ **{time_str}** — {task.description} ({task.duration_minutes} min) "
                    f"· Priority {task.priority}/10"
                )

        if scheduler.time_conflicts:
            st.markdown("#### 🔀 Overlapping Tasks")
            for task_a, task_b in scheduler.time_conflicts:
                time_a = task_a.time.strftime("%I:%M %p")
                time_b = task_b.time.strftime("%I:%M %p")
                st.markdown(f"- **{task_a.description}** ({time_a}) overlaps **{task_b.description}** ({time_b})")

        st.markdown("#### 🧠 Why this plan")
        st.info(scheduler.get_reasoning())
