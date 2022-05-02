from dataclasses import dataclass
from skills import Skill, FuryPunch, FireBolt


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Воин",
    max_health=100.0,
    max_stamina=50.0,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch()
)

MageClass = UnitClass(
    name="Маг",
    max_health=50.0,
    max_stamina=100.0,
    attack=1.6,
    stamina=1.2,
    armor=0.6,
    skill=FireBolt()
)

unit_classes = {
    WarriorClass.name: WarriorClass,
    MageClass.name: MageClass
}
