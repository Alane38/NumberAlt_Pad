import keyboard

alt_144 = "alt+&+\'" #14
alt_225 = "alt+é+(" #25
alt_128 = "alt+é+_" #28
alt_0149 = "alt+\'+ç" #49

keyboard.add_hotkey(alt_144, lambda: keyboard.write('É'), print('- Loaded alt+144 -> É (14)'))
keyboard.add_hotkey(alt_225, lambda: keyboard.write('ß'), print('- Loaded alt+225 -> ß (25)'))
keyboard.add_hotkey(alt_128, lambda: keyboard.write('Ç'), print('- Loaded alt+128 -> Ç (28)'))
keyboard.add_hotkey(alt_0149, lambda: keyboard.write('•'), print('- Loaded alt+0149 -> • (49)'))

# Stop script until 'alt + ²' is pressed.
recorded = keyboard.record(until='alt+²')