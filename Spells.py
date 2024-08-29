class Spell:
    def __init__(self, uses=-1, manadrain=0, castdelay=0, castdelayoverride=None, rechargetime=0, color=(255, 255, 255)):
        self.uses = uses
        self.manadrain = manadrain
        self.castdelay = castdelay
        self.castdelayoverride = castdelayoverride
        self.rechargetime = rechargetime
        self.color = color

class ProjectileSpell(Spell):
    def __init__(self, lifetime=1, trigger=False, **kwargs):
        super().__init__(**kwargs)
        self.lifetime = lifetime
        self.trigger = trigger

class SparkBolt(ProjectileSpell):
    def __init__(self):
        super().__init__(manadrain=5, castdelay=0.05, color = (173, 113, 242))

class SparkBoltWithTrigger(ProjectileSpell):
    def __init__(self):
        super().__init__(manadrain=5, castdelay=0.05, trigger=True, color = (173, 113, 242))

class Chainsaw(ProjectileSpell):
    def __init__(self):
        super().__init__(manadrain=1, castdelayoverride=0, rechargetime=-0.17, color = (253, 252, 184))

class DoubleSpell(Spell):
    def __init__(self):
        super().__init__(color = (255, 255, 255))
