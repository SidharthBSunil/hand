`````
pip install opencv-python mediapipe
`````
````
python3 -m venv venv
````
`````
source venv/bin/activate
`````
`````
source /opt/ros/humble/setup.bash source ~/raju_brain_ws/install/setup.bash ros2 run raju_brain raju_brain

`````
sudo apt update && sudo apt install -y ubuntu-desktop-minimal tightvncserver

vncserver -kill :1 2>/dev/null; vncserver -kill :2 2>/dev/null; sudo apt install -y xfce4 xfce4-goodies && printf '#!/bin/sh\nunset SESSION_MANAGER\nunset DBUS_SESSION_BUS_ADDRESS\nexec startxfce4 &\n' > ~/.vnc/xstartup && chmod +x ~/.vnc/xstartup && vncserver :1
