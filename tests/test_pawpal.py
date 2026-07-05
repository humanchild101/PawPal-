from datetime import datetime

from pawpal_system import Owner, Pet, Scheduler, Task


def test_mark_complete_changes_task_status():
    task = Task(description="Walk", duration_minutes=10, priority=5)
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_modify_task_updates_the_given_field():
    task = Task(description="Walk", duration_minutes=10, priority=5)

    task.modify_task(priority=8)

    assert task.priority == 8


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    assert len(pet.task_list) == 0

    pet.add_task(Task(description="Walk", duration_minutes=10, priority=5))

    assert len(pet.task_list) == 1


def test_removing_task_decreases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    task = Task(description="Walk", duration_minutes=10, priority=5)
    pet.add_task(task)

    pet.remove_task(task)

    assert len(pet.task_list) == 0


def test_feed_updates_last_fed():
    pet = Pet(name="Mochi", species="dog")
    assert pet.last_fed is None

    pet.feed()

    assert isinstance(pet.last_fed, datetime)


def test_walk_updates_last_walked():
    pet = Pet(name="Mochi", species="dog")
    assert pet.last_walked is None

    pet.walk()

    assert isinstance(pet.last_walked, datetime)


def test_adding_pet_increases_owner_pet_count():
    owner = Owner()
    assert len(owner.pet_list) == 0

    owner.add_pet(Pet(name="Mochi", species="dog"))

    assert len(owner.pet_list) == 1


def test_removing_pet_decreases_owner_pet_count():
    owner = Owner()
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    owner.remove_pet(pet)

    assert len(owner.pet_list) == 0


def test_change_pref_updates_owner_time_preferences():
    owner = Owner()

    owner.change_pref("mornings only")

    assert owner.time_preferences == "mornings only"


def test_get_all_tasks_includes_tasks_from_every_pet():
    owner = Owner()
    dog = Pet(name="Mochi", species="dog")
    cat = Pet(name="Whiskers", species="cat")
    owner.add_pet(dog)
    owner.add_pet(cat)
    dog.add_task(Task(description="Walk", duration_minutes=10, priority=5))
    cat.add_task(Task(description="Feed cat", duration_minutes=5, priority=5))

    assert len(owner.get_all_tasks()) == 2


def test_build_plan_always_includes_required_tasks():
    owner = Owner()
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)
    feed = Task(description="Feed", duration_minutes=50, priority=1, required=True)
    pet.add_task(feed)

    scheduler = Scheduler()
    scheduler.set_available_minutes(10)
    plan = scheduler.build_plan(owner)

    assert feed in plan


def test_build_plan_excludes_completed_tasks():
    owner = Owner()
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)
    done = Task(description="Done", duration_minutes=10, priority=5, completed=True)
    pet.add_task(done)

    scheduler = Scheduler()
    scheduler.set_available_minutes(60)
    plan = scheduler.build_plan(owner)

    assert done not in plan
