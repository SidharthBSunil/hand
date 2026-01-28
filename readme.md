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
sudo kill -9 36952 && sudo rm -f /var/lib/apt/lists/lock /var/lib/dpkg/lock* && sudo dpkg --configure -a && sudo apt update && sudo apt install -y openssh-server && sudo systemctl enable --now ssh && sudo ss -tlnp | grep :22

`````
sudo apt update && sudo apt install -y ubuntu-desktop-minimal tightvncserver

vncserver -kill :1 2>/dev/null; vncserver -kill :2 2>/dev/null; sudo apt install -y xfce4 xfce4-goodies && printf '#!/bin/sh\nunset SESSION_MANAGER\nunset DBUS_SESSION_BUS_ADDRESS\nexec startxfce4 &\n' > ~/.vnc/xstartup && chmod +x ~/.vnc/xstartup && vncserver :1
