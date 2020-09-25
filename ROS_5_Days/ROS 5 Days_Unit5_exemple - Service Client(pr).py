# Exemple de code d'un package service Client  Unit 5: Service in ROS

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier launch
# DANS my_robot_arm_demo.launch
# -------------------------------------------------
<launch>

  <include file="$(find iri_wam_reproduce_trajectory)/launch/start_service.launch"/>

  <!-- Here will go our python script that calls the execute_trajectory service -->
    <node pkg ="unit_4_services"
        type="exercise_4_1.py"
        name="service_execute_trajectory_client"
        output="screen">
  </node>
 
</launch>
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# Dans le dossier src
# DANS excercice_4_1.py
# -------------------------------------------------
#! /usr/bin/env python
import rospkg
import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest # Import the service message used by the service /execute_trajectory

rospy.init_node('service_execute_trajectory_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/execute_trajectory') # Wait for the service client /execute_trajectory to be running
execute_trajectory_service_client = rospy.ServiceProxy('/execute_trajectory', ExecTraj) # Create the connection to the service
execute_trajectory_request_object = ExecTrajRequest() # Create an object of type ExecTrajRequest

"""
user:~/catkin_ws$ rossrv show iri_wam_reproduce_trajectory/ExecTraj
string file
---
"""
rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
trajectory_file_path = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"
execute_trajectory_request_object.file = trajectory_file_path # Fill the variable file of this object with the desired file path
result = execute_trajectory_service_client(execute_trajectory_request_object) # Send through the connection the path to the trajectory file to be executed
print result # Print the result type ExecTrajResponse
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
