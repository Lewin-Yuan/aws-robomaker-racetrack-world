import pybullet as p
from pybullet_utils import gazebo_world_parser
import time

p.connect(p.GUI)

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,0)

gazebo_world_parser.parseWorld( p, filepath = "worlds/racetrack_day.world")
    
shadowIntensityParam = p.addUserDebugParameter("shadowIntensity", 0, 1, 0.8)

p.configureDebugVisualizer(shadowMapResolution = 8192)
p.configureDebugVisualizer(shadowMapWorldSize = 25)
 
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,1)
dt = 1./240.

while (1):
  shadowMapIntensity = p.readUserDebugParameter(shadowIntensityParam)
  p.configureDebugVisualizer(shadowMapIntensity=shadowMapIntensity)
  p.stepSimulation()
  p.getCameraImage(640,480, renderer=p.ER_BULLET_HARDWARE_OPENGL )
  time.sleep(dt)
  
