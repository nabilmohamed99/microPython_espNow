# ESPNow Communication with MicroPython

This repository contains code examples for setting up communication between ESP8266 modules using ESPNow in MicroPython.

## Introduction

ESPNow is a communication protocol developed by Espressif Systems that allows for low-power, peer-to-peer communication between ESP8266 and ESP32 devices. It is ideal for scenarios where devices need to communicate directly with each other without the need for a traditional Wi-Fi network infrastructure.

This repository provides simple examples of how to configure ESPNow on ESP8266 devices using MicroPython and demonstrates how to establish communication between two devices.

## Getting Started

### Requirements

- Two ESP8266 devices (such as NodeMCU)
- MicroPython firmware flashed on the devices
- `espnow.py` library (included in this repository)

### Installation

1. Flash the MicroPython firmware onto your ESP8266 devices.
2. Copy the `espnow.py` library to the root directory of each device.
3. Upload the appropriate code to each device (sender and receiver).

### Usage

1. Configure the devices to use the same channel and encryption key.
2. Upload the code to each device (see `sender.py` and `receiver.py`).
3. Power on the devices and observe the communication between them.

## File Structure

sender.py # Code for the sender device (ESP8266)
receiver.py # Code for the receiver device (ESP8266)
