import Spells

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

        if isinstance(next_spell, Spells.ProjectileSpell):
            pass

        if self.current_spell_index >= len(self.spells):
            #apply recharge time
            pass



w = Wand()
w.setSpells([Spells.SparkBolt()])