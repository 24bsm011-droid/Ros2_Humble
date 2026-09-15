# ROS 2 Talker and Listener (Publisher-Subscriber)

## Overview
* **Core Concept:** In ROS 2, nodes communicate with each other using **Topics**. A node that transmits data is called a **Publisher (Talker)**, and a node that consumes that data is called a **Subscriber (Listener)**.
* **Verification:** Successfully verified the publisher-subscriber communication loop after building ROS 2 Humble from source (`~/ros2_humble`).

## Key Demonstration Steps
* **Talker Node:** Publishes continuous data messages (e.g., `"Hello World"` with a sequence index).
* **Listener Node:** Subscribes to the topic and prints the received messages to the terminal (e.g., `I heard: [Hello World: 78]`).

## Useful Commands
* Running a standard publisher: