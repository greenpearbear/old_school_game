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

    def skill_effect(self):
        return self.damage


class SkillMage(Skill):

    def skill_effect(self):
        return self.damage


Skill_Warrior = SkillWarrior(title='Рубящий удар', damage=10, need_stamina=15)
Skill_Mage = SkillMage(title='Огненный шар', damage=20, need_stamina=25)
