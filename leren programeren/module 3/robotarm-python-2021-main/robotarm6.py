from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight()
robotArm.grab()
for x in range (0,3):
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()