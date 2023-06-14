from pets import Dog, Cat, Flea

phydeaux = Dog(name='Phydeaux')
assert phydeaux.genus == 'canis'
assert phydeaux.get_sound() == 'woof'
assert phydeaux.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phydeaux.'

# We should be able to name our dog anything we want.
phred = Dog(name='Phred')
assert phred.get_sound_meaning() == 'Hello, I\'m a dog and my name is Phred.'

phelix= Cat(name='Phelix')
assert phelix.genus == 'felis'
assert phelix.get_sound() == 'meow'
assert phelix.get_sound_meaning() == 'Hello, I\'m a cat and my name is Phelix.'

phiphi = Flea(name='PhiPhi')
assert phiphi.genus == 'pulex'
assert phiphi.get_sound() == 'zzz'
assert phiphi.get_sound_meaning() == 'Hello, I\'m a flea and my name is PhiPhi.'
