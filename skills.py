from abc import ABC, abstractmethod


class Skill(ABC):
    def __init__(self, title, damage, need_stamina):
        self.title = title
        self.damage = damage
        self.need_stamina = need_stamina

    @abstractmethod
    def skill_effect(self):
        pass

    def use(self, user_stamina):

        if user_stamina > self.need_stamina:
            self.skill_effect()
        else:
            return "У вас не хватает выносливости"

class SkillWarrior(Skill):