from RobotArm import RobotArm
RobotArm('exercise 10')
RobotArm.speed = 4
rechts = 9
Links = 8
for i in range(5):
    RobotArm.grab()
    for i in range(rechts):
        RobotArm.moveRight()
    RobotArm.drop()
    for i in range(Links):
        RobotArm.moveLeft()
    rechts = rechts - 2
    Links = Links - 2