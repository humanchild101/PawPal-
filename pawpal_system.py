from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    task: str
    duration_minutes: int
    priority: str
    completed: bool = False
    recurrence: str = ""

    def modify_task(self) -> None:
        pass


@dataclass
class PetSchedule:
    task_list: List[Task] = field(default_factory=list)
    available_minutes: int = 0

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def set_available_minutes(self, minutes: int) -> None:
        pass

    def get_reasoning(self) -> str:
        pass


@dataclass
class Pet:
    name: str
    species: str
    meds: list = field(default_factory=list)
    last_walked: Optional[datetime] = None
    last_bathed: Optional[datetime] = None
    last_fed: Optional[datetime] = None
    schedule: PetSchedule = field(default_factory=PetSchedule)
    special_info: str = ""

    def feed(self) -> None:
        pass

    def bathe(self) -> None:
        pass

    def walk(self) -> None:
        pass

    def play(self) -> None:
        pass

    def add_to_schedule(self, task: Task) -> None:
        pass

    def remove_from_schedule(self, task: Task) -> None:
        pass


@dataclass
class Owner:
    pet_list: List[Pet] = field(default_factory=list)
    time_preferences: str = ""

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def change_pref(self, pref: str) -> None:
        pass
