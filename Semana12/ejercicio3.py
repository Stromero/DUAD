# 3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo

class kaioken:
    
    def power_kaio_ken():
        print('My super power is execute the kaio ken technique')

class kameha:

    def power_kameha():
        print('My super power is execute the kameha technique')

class Makankosappo:

    def power_Makankosappo():
        print('My super power is execute the Makankosappo technique')

class Masenko:

    def power_Masenko():
        print('My super power is execute the Masenko technique')

class ballenergy():

    def power_ball_energy():
        print('My super power is execute the ball of energy technique')

class superhero(kaioken,kameha,Makankosappo, Masenko,ballenergy):

    def aura():
        print('Aura is being execute')

goku = superhero()
goku.aura
goku.power_kameha

gohan = superhero()
gohan.aura
gohan.power_Masenko

piccolo = superhero()
piccolo.power_Makankosappo

vegeta = superhero()
vegeta.aura
vegeta.power_ball_energy