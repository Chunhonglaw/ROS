# Exemple de code d'un package service service  Unit 6: Service in ROS

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier launch
# DANS call_bb8_move_in_circle_service_server.launch
# -------------------------------------------------
<launch>
    <!-- Start Service Client for move_bb8_in_circle service -->
    <node pkg="ex4_2" type="bb8_move_in_circle_service_client.py" name="service_move_bb8_in_circle_client"  output="screen">
    </node>
</launch>
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier launch
# DANS start_bb8_move_in_circle_service_server.launch
# -------------------------------------------------
<launch>
    <node pkg="ex4_2" type="bb8_move_in_circle_service_server.py" name="service_move_bb8_in_circle_server"  output="screen">
    </node>
</launch>
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier src
# DANS bb8_move_in_circle_service_client.py
# -------------------------------------------------
#! /usr/bin/env python
import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest # you import the service message python classes generated from Empty.srv.

rospy.init_node('service_move_bb8_in_circle_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_circle') # Wait for the service client /move_bb8_in_circle to be running
move_bb8_in_circle_service_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty) # Create the connection to the service
move_bb8_in_circle_request_object = EmptyRequest() # Create an object of type EmptyRequest

result = move_bb8_in_circle_service_client(move_bb8_in_circle_request_object) # Send through the connection the path to the trajectory file to be executed
print result # Print the result given by the service called
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier src
# DANS bb8_move_in_circle_service_server.py
# -------------------------------------------------
#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist

def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    move_circle.linear.x = 0.2
    move_circle.angular.z = 0.2
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_circle")
    return EmptyResponse() # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_circle_server') 
my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rospy.loginfo("Service /move_bb8_in_circle Ready")
rospy.spin() # mantain the service open.
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------