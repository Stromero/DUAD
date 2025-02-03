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
        

class Arm:
    def __init__(self, hand_parameter):
        self.hand = hand_parameter
        

class Torso:
    def __init__(self, head_parameter, right_leg_parameter, left_leg_parameter, right_arm_parameter, left_arm_parameter):
        self.head = head_parameter
        self.right_hand = right_arm_parameter
        self.left_hand = left_arm_parameter
        self.right_leg = right_leg_parameter
        self.left_leg = left_leg_parameter
        

class Human:
    def __init__(self, torso_parameter):
        self.torso = torso_parameter
        

main_head = Head()
right_hand = Hand()
left_hand = Hand()
right_feet = Feet()
left_feet = Feet()
right_leg = Leg(right_feet)
left_leg = Leg(left_feet)
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
main_torso = Torso(main_head,right_leg, left_leg, right_arm,left_arm)
body = Human(main_torso)
