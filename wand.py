
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

class Wand:
    def __init__(self, shuffle=False, percast=1, castdelay=0.15, rechargetime=0.33,
                 manamax=100, manachargespeed=25, capacity=3, spread=0, speed=1):
        self.shuffle = shuffle
        self.percast = percast
        self.castdelay = castdelay
        self.rechargetime = rechargetime
        self.manamax = manamax
        self.manachargespeed = manachargespeed
        self.capacity = capacity
        self.spread = spread
        self.speed = speed

        self.spells = []
        self.current_spell_index = 0
        self.castdelay_remaining = 0
        self.rechargetime_remaining = 0

    def setSpells(self, newspells):
        self.spells = newspells[:self.capacity]

    def draw(self, as_payload=False):
        next_spell = self.spells[self.current_spell_index]
        
        if not as_payload:
            if next_spell.castdelayoverride is not None:
                self.castdelay_remaining = next_spell.castdelayoverride
            else:
                self.castdelay_remaining += next_spell.castdelay
        self.rechargetime_remaining += next_spell.rechargetime

        self.current_spell_index += 1

        if isinstance(next_spell, ProjectileSpell):
            pass

        if self.current_spell_index >= len(self.spells):
            #apply recharge time
            pass



w = Wand()
w.setSpells([SparkBolt()])