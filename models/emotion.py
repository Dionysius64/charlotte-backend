from enum import IntEnum

class Emotion(IntEnum):
    NEUTRAL = 0
    HAPPY = 1
    SAD = 2
    ANGRY = 3
    SCARED = 4
    SHOCKED = 5
    EXCITED = 6
    FLUSTERED = 7

    @classmethod
    def describe(cls):
        return {
            e.value: e.name.lower()
            for e in cls
        }