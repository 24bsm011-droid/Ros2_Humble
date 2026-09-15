# Configuring Environment

* **Kyun Zaroori Hai:** Terminal ko default nahi pata hota ki ROS 2 kahan install hai. `setup.bash` file ko source karne se terminal ko ROS 2 commands ki knowledge milti hai.
* **Main Command:** `source /opt/ros/humble/setup.bash` (Yeh main ROS 2 installation ko active karti hai).
* **Workspace Sourcing:** Jab hum apna custom package banate hain, toh humein apne workspace ki file bhi source karni padti hai: `source ~/ros2_ws/install/setup.bash`.
* **Permanent Setup:** Baar-baar source karne se bachne ke liye hum `.bashrc` file mein command add kar dete hain.
