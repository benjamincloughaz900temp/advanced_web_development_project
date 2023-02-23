from dataclasses import dataclass
from utilities.custom_exceptions import VariableNotSetException
from utilities import JSON_utilities


@dataclass
class Set:
    _exercise: str
    muscle_group: str
    weight_kg: float
    repetitions: int

    def __init__(self, exercise: str = None,
                 muscle_group: str = None,
                 weight_kg: float = None,
                 repetitions: int = None):
        self._exercise = exercise
        self.muscle_group = muscle_group
        self.weight_kg = weight_kg
        self.repetitions = repetitions


    @property
    def exercise(self):
        if self._exercise:
            return self._exercise
        raise VariableNotSetException("exercise")


@dataclass
class Workout:
    _loaded_exercises: list[Set]

    def __init__(self, preloaded_exercises: list[Set] = None):
        if preloaded_exercises:
            self._loaded_exercises = preloaded_exercises
        else:
            self._loaded_exercises = []

    @property
    def exercises(self):
        if self._loaded_exercises:
            return self._loaded_exercises
        raise VariableNotSetException("loaded_exercises")

    def load_set(self, exercise: str, username: str, set_number: int):
        self.exercises.append("hi")



@dataclass
class User:
    loaded_workouts: list[Workout]
    username: str
    password: str
    forename: str
    surname: str

    def __init__(self, username: str, password: str, forename: str, surname: str,
                 preloaded_workouts: list[Workout] = None):
        if preloaded_workouts:
            self.loaded_workouts = preloaded_workouts
        else:
            self.loaded_workouts = []
        self.username = username
        self.password = password
        self.forename = forename
        self.surname = surname

    def load_workout(self):
