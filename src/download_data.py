

from roboflow import Roboflow
rf = Roboflow(api_key="")
project = rf.workspace("cvcompvision").project("potholes-46jt9-bflgv")
version = project.version(1)
dataset = version.download("yolov8")
