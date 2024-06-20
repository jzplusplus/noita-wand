class Spell:
    pass

class ProjectileSpell(Spell):
    def __init__(self, uses=-1, manadrain=0, castdelay=0, castdelayoverride=None, rechargetime=0, lifetime=1, trigger=False, color=(255, 255, 255)):
        self.uses = uses
        self.manadrain = manadrain
        self.castdelay = castdelay
        self.castdelayoverride = castdelayoverride
        self.rechargetime = rechargetime
        self.lifetime = lifetime
        self.trigger = trigger
        self.color = color

class SparkBolt(ProjectileSpell):
    def __init__(self):
        ProjectileSpell.__init__(manadrain=5, castdelay=0.05, color = (173, 113, 242))

class SparkBoltWithTrigger(ProjectileSpell):
    def __init__(self):
        ProjectileSpell.__init__(manadrain=5, castdelay=0.05, trigger=True, color = (173, 113, 242))

class Chainsaw(ProjectileSpell):
    def __init__(self):
        ProjectileSpell.__init__(manadrain=1, castdelayoverride=0, rechargetime=-0.17, color = (173, 113, 242))