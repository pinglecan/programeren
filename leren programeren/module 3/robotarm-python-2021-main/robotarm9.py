from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
x = 1
for i in range(4):
    for i in range(x):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()
    x += 1