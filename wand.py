import Spells
import board
import neopixel
import time
import colorsys
import math
import RPi.GPIO as GPIO

pixels = neopixel.NeoPixel(board.D18, 6, brightness=1.0)

spell_map = [None, Spells.Chainsaw(), Spells.DoubleSpell(), Spells.SparkBolt()]

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

    def draw(self, as_payload=False, wrapping=False):
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

sensor_pins = [
        6, 13, 19, 26, 
        5, 0, 11, 9,
        22, 27, 17, 10
]
sensors = [0] * len(sensor_pins)
old_sensors = [0] * len(sensor_pins)

for pin in sensor_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

hue = 0
saturation = 1.0
brightness = 1.0

count = 0
active = 0
try:
    while True:
        hue += 0.01
        if hue >= 1.0: hue = 0


        for i in range(3):
            brightness = abs(math.sin((hue * 2*math.pi) + (i * (2*math.pi/3))))
            c = colorsys.hsv_to_rgb(hue + (i * 0.33), saturation, brightness)
            c = [int(x*255) for x in c]
            pixels[i+3] = c

        update = False
        for i, pin in enumerate(sensor_pins):
            sensors[i] = 0 if GPIO.input(pin) == 1 else 1
            if sensors[i] != old_sensors[i]:
                update = True
            old_sensors[i] = sensors[i]
        
        if update:
            slot1 = (sensors[0] << 3) + (sensors[1] << 2) + (sensors[2] << 1) + sensors[3]
            slot2 = (sensors[4] << 3) + (sensors[5] << 2) + (sensors[6] << 1) + sensors[7]
            slot3 = (sensors[8] << 3) + (sensors[9] << 2) + (sensors[10] << 1) + sensors[11]

            current_spells = [spell_map[slot1], spell_map[slot2], spell_map[slot3]]
            for i, s in enumerate(current_spells):
                if s is not None: c = s.color
                else: c = (0, 0, 0)
                pixels[2-i] = c
            print(current_spells)

        pixels.show()
        time.sleep(0.015)

except Exception as e:
    print(e)

GPIO.cleanup()


