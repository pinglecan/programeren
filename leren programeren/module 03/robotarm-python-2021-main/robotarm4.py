from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
for x in range(0,3):
    robotArm.moveRight()
robotArm.drop()
for x in range(0,3):
    robotArm.moveLeft()
robotArm.grab()
for x in range(0,3):
    robotArm.moveRight()
robotArm.drop()
for x in range(0,3):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for x in range (0 ,2):
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()