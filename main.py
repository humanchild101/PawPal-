from datetime import date, datetime, time

from pawpal_system import Owner, Pet, Scheduler, Task

today = date.today()

owner = Owner(time_preferences="morning preferred, i have daily meetings at 3 pm from Monday-Friday. On Sunday, I have a class at 7 pm.")

jasmine = Pet(name="jasmine", species="dog")
spyder = Pet(name="spyder", species="cat")
squash = Pet(name="squash", species="cat")

owner.add_pet(jasmine)
owner.add_pet(spyder)
owner.add_pet(squash)

jasmine.add_task(Task(
    description="Jasmine Walk",
    duration_minutes=30,
    priority=4,
    time=datetime.combine(today, time(8, 0)),
))
jasmine.add_task(Task(
    description="Jasmine Feed",
    duration_minutes=5,
    priority=4,
    required=True,
    time=datetime.combine(today, time(11, 0)),
))
jasmine.add_task(Task(
    description="Jasmine Play",
    duration_minutes=30,
    priority=4,
    time=datetime.combine(today, time(2, 0)),
))
spyder.add_task(Task(
    description="Spyder Feed",
    duration_minutes=10,
    priority=4,
    required=True,
    time=datetime.combine(today, time(8, 30)),
))

spyder.add_task(Task(
    description="Spyder Feed",
    duration_minutes=10,
    priority=4,
    required=True,
    time=datetime.combine(today, time(11, 10)),
))

spyder.add_task(Task(
    description= "Spyder litter box clean",
    duration_minutes=15,
    priority=4,
    time=datetime.combine(today, time(9, 0)),
))

squash.add_task(Task(
    description="Squash litter box cleaning",
    duration_minutes=15,
    priority=4,
    time=datetime.combine(today, time(10, 0)),
))

squash.add_task(Task(
    description="Squash feed",
    duration_minutes=5,
    priority=4,
    required=True,
    time=datetime.combine(today, time(14, 30)),
))

squash.add_task(Task(
    description="give squash a squash",
    duration_minutes=5,
    priority=5,
    time=datetime.combine(today, time(4, 30)),
))



scheduler = Scheduler()
scheduler.set_available_minutes(10)
scheduler.build_plan(owner)

print(scheduler.format_schedule())
