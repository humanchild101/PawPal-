from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    description: str
    duration_minutes: int
    priority: int  # 1 (lowest) to 10 (highest)
    time: Optional[datetime] = None
    frequency: str = ""
    completed: bool = False
    required: bool = False

    def modify_task(self, **updates) -> None:
        """Update any given attributes on this task in place."""
        for key, value in updates.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    meds: list = field(default_factory=list)
    last_walked: Optional[datetime] = None
    last_bathed: Optional[datetime] = None
    last_fed: Optional[datetime] = None
    last_played: Optional[datetime] = None
    task_list: List[Task] = field(default_factory=list)
    special_info: str = ""

    def feed(self) -> None:
        """Record that this pet was just fed."""
        self.last_fed = datetime.now()

    def bathe(self) -> None:
        """Record that this pet was just bathed."""
        self.last_bathed = datetime.now()

    def walk(self) -> None:
        """Record that this pet was just walked."""
        self.last_walked = datetime.now()

    def play(self) -> None:
        """Record that this pet was just played with."""
        self.last_played = datetime.now()

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.task_list.append(task)

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet's task list, if present."""
        if task in self.task_list:
            self.task_list.remove(task)


@dataclass
class Owner:
    pet_list: List[Pet] = field(default_factory=list)
    time_preferences: str = ""

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's pet list."""
        self.pet_list.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from this owner's pet list, if present."""
        if pet in self.pet_list:
            self.pet_list.remove(pet)

    def change_pref(self, pref: str) -> None:
        """Update this owner's time preferences."""
        self.time_preferences = pref

    def get_all_tasks(self) -> List[Task]:
        """Return every task across all of this owner's pets."""
        return [task for pet in self.pet_list for task in pet.task_list]


@dataclass
class Scheduler:
    available_minutes: int = 0
    plan: List[Task] = field(default_factory=list)
    remaining_minutes: int = 0
    unscheduled: List[Task] = field(default_factory=list)

    def build_plan(self, owner: Owner) -> List[Task]:
        """Build a plan of required tasks plus the highest-priority optional tasks that fit."""
        candidates = [task for task in owner.get_all_tasks() if not task.completed]
        required = sorted((t for t in candidates if t.required), key=lambda t: -t.priority)
        optional = sorted((t for t in candidates if not t.required), key=lambda t: -t.priority)

        plan: List[Task] = list(required)
        remaining_minutes = self.available_minutes - sum(t.duration_minutes for t in required)
        unscheduled: List[Task] = []

        for task in optional:
            if task.duration_minutes <= remaining_minutes:
                plan.append(task)
                remaining_minutes -= task.duration_minutes
            else:
                unscheduled.append(task)

        self.plan = plan
        self.remaining_minutes = remaining_minutes
        self.unscheduled = unscheduled
        return self.plan

    def set_available_minutes(self, minutes: int) -> None:
        """Set the time budget used by build_plan."""
        self.available_minutes = minutes

    def get_reasoning(self) -> str:
        """Explain why the current plan was chosen."""
        if not self.plan:
            if not self.unscheduled:
                return "No tasks were scheduled: there are no pending tasks to schedule."

            top = sorted(self.unscheduled, key=lambda task: (-task.priority, task.time or datetime.max))[0]
            time_str = top.time.strftime("%I:%M %p") if top.time else "unscheduled"
            deficit = top.duration_minutes - self.remaining_minutes
            return (
                "No tasks were scheduled: none fit within the available time. "
                f'The highest-priority pending task is "{top.description}" at {time_str} '
                f"(priority {top.priority}/10, {top.duration_minutes} min) — increase available "
                f"time by at least {deficit} minute(s) to fit it."
            )

        total_minutes = sum(task.duration_minutes for task in self.plan)
        lines = [
            f"Selected {len(self.plan)} task(s) totaling {total_minutes} of "
            f"{self.available_minutes} available minutes.",
            "Required tasks were guaranteed a slot first; remaining tasks were then added "
            "by priority (10 = highest, 1 = lowest) until the available time ran out:",
        ]
        for task in self.plan:
            tag = "required" if task.required else f"priority {task.priority}/10"
            lines.append(f"  - {task.description} ({tag}, {task.duration_minutes} min)")

        if self.remaining_minutes < 0:
            lines.append(
                f"Warning: required tasks alone need {abs(self.remaining_minutes)} more minute(s) "
                f"than your {self.available_minutes}-minute budget. All required tasks were still "
                "included; consider freeing up more time."
            )
        return "\n".join(lines)

    def format_schedule(self, title: str = "Daily Schedule") -> str:
        """Render the current plan, unscheduled tasks, and reasoning as a printable string."""
        by_time = sorted(self.plan, key=lambda task: task.time or datetime.max)

        lines = [f"=== {title} ==="]
        for task in by_time:
            time_str = task.time.strftime("%I:%M %p") if task.time else "unscheduled"
            tag = "required" if task.required else f"priority {task.priority}/10"
            lines.append(f"{time_str} — {task.description} ({task.duration_minutes} min, {tag})")

        if self.unscheduled:
            lines.append("")
            lines.append("Not scheduled:")
            for task in sorted(self.unscheduled, key=lambda task: task.time or datetime.max):
                time_str = task.time.strftime("%I:%M %p") if task.time else "unscheduled"
                lines.append(
                    f"{time_str} — {task.description} "
                    f"({task.duration_minutes} min, priority {task.priority}/10) [time conflict]"
                )

        lines.append("")
        lines.append(self.get_reasoning())
        return "\n".join(lines)
