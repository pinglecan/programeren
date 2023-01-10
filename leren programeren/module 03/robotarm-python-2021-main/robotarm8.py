from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 4
robotArm.moveRight()
for i in range (7):
    robotArm.grab()
    for q in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for w in range(8):
        robotArm.moveLeft()
robotArm.wait()