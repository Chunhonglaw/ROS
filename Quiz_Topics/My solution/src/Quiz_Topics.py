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
        return self.laser_msg.ranges[100]  

    def get_left_laser(self):
        time.sleep(1)
        return self.laser_msg.ranges[460]

    def turn_left(self):
        self.move.linear.x = self.speed/4
        self.move.angular.z = self.speed*2    
        
    def turn_right(self):
        self.move.linear.x = self.speed/4
        self.move.angular.z = -self.speed*2

    def forward(self):
        self.move.linear.x = self.speed
        self.move.angular.z = 0       

    def avoid_wall(self):
        while not rospy.is_shutdown():
            #Calculte move setting
            if self.get_front_laser() > 1:
                # move forward               
                self.forward()
            
            elif self.get_front_laser() < 1: 
                #turn left
                self.turn_left()
            
            elif self.get_right_laser() < 1: 
                #turn left
                self.turn_left()  
           
            elif self.self.get_left_laser() > 1: 
                #turn right
                self.turn_right()

            #publish move
            self.pub.publish(self.move)
            #sleep
            self.rate.sleep()

robot_quiz = MoveRobot(0.3)
robot_quiz.avoid_wall()