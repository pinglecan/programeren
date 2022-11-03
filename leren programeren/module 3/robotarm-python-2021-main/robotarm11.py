from RobotArm import RobotArm
RobotArm('exercise 11')
RobotArm.speed = 3
for i in range(8):
    RobotArm.grab()
    if RobotArm.scan() == "white":
        for i in range(1):
            RobotArm.moveRight()
        RobotArm.drop()
    if RobotArm.scan() != "white":
        RobotArm.drop()
        RobotArm.moveRight()