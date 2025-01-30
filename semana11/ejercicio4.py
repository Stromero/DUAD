class Head:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass

class Feet:
    def __init__(self):
        pass

class Leg:
    def __init__(self, feet_parameter):
        self.feet = feet_parameter
        pass

class Arm:
    def __init__(self, hand_parameter):
        self.hand = hand_parameter
        pass

class Torso:
    def __init__(self, head_parameter, leg_parameter, arm_parameter):
        self.head = head_parameter
        self.leg = leg_parameter
        self.arm = arm_parameter
        pass

class Human:
    def __init__(self, torso_parameter):
        self.torso = torso_parameter
        pass

main_head = Head()
right_hand = Hand()
right_feet = Feet()
right_leg = Leg(right_feet)
right_arm = Arm(right_hand)
main_torso = Torso(main_head,right_leg,right_hand)
body = Human = (main_torso)
