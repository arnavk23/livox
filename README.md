# Livox Viewer - Point Cloud Capture and Visualization

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

This repository contains session files, screenshots, and supporting materials related to Livox Viewer — a GUI tool provided by Livox for real-time point cloud visualization and data capture from Livox LiDAR devices.

It is **not a ROS-based project**, but rather a workspace for working directly with **Livox Viewer** and analyzing `.lvx` point cloud capture files.

## Overview

[Livox Viewer](https://www.livoxtech.com/downloads/livox-viewer) is an official GUI tool to connect, visualize, and record point clouds from Livox LiDAR sensors like the Mid-40, Mid-70, Avia, Horizon, etc.

This repository documents:

- How Livox Viewer was used
- Captured `.csv` point cloud files
- Screenshots from 3D visualizations
- Configuration and calibration settings

## Repository Structure

livox/
├── record_files/ and record-files/ # Saved .csv files (point cloud captures)
├── screenshots/ # Screenshots from Livox Viewer
├── so/ # Intrinsic/extrinsic calibration files if any
└── README.md # This file

## Setup Instructions

1. **Download Livox Viewer**  
   https://www.livoxtech.com/downloads/livox-viewer  
   Supports Windows (64-bit) and allows plug & play over USB or Ethernet.

2. **Connect your Livox device**
   - Ensure the Livox SDK driver is installed
   - Launch Livox Viewer and detect your device

3. **Start Visualization**
   - Begin real-time streaming
   - Use filters (distance, intensity) if required

4. **Capture Data**
   - Press **"Start Record"** to generate `.lvx` files
   - Save screenshots as needed
