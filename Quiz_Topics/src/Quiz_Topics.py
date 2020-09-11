
class Dog:                          # Création d'une classe Dog
    def __init__(self, name):       
        self.name = name

    def get_name (self):            # méthode get_name
        return self.name
    
Fido = Dog ('Fido')                 # Créer l'objet Fido     
Happy = Dog ('Happy')            
print (Fido.get_name())             # new comment 
print (Happy.get_name())            # new comment 

print ('Try push to Github')
print ('sur branch test')
#! /usr/bin/env python
#https://get-help.robotigniteacademy.com/t/trouble-with-ros-basics-in-5-days-topic-quiz/742

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import time

class MoveRobot:
    def __init__(self, speed):
        rospy.init_node('topics_quiz_node',anonymous=True)
        self.speed = speed
        self.time_turn = 5.0
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('kobuki/laser/scan', LaserScan, self.callback)
        self.rate = rospy.Rate(1)
        self.move = Twist()
        self.laser_msg = LaserScan()

    def callback(self,msg):
        self.laser_msg = msg                # corriger en ajouter self 

    def get_front_laser(self):
        time.sleep(1)
        return self.laser_msg.ranges[360]   # 360, in front of the laser

    def get_right_laser(self):
        time.sleep(1)
        return self.laser_msg.ranges[0]  

    def avoid_wall(self):
        while not rospy.is_shutdown():
            #Calculte move setting
            if self.get_front_laser() > 1 and self.get_right_laser() > 1:
                # move forward               
                self.move.linear.x = self.speed
                self.move.angular.z = 0
            
            else: 
                #turn left
                self.move.linear.x = 0
                self.move.angular.z = self.speed
            
            #publish move
            self.pub.publish(self.move)
            #sleep
            self.rate.sleep()

robot_quiz = MoveRobot(0.3)
robot_quiz.avoid_wall()