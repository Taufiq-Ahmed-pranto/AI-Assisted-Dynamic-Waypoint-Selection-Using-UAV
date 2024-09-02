# AI-Assisted Dynamic Waypoint Selection Using UAV

This repository contains the code and dataset for the project "AI-Assisted Dynamic Waypoint Selection Using UAV." The project's primary goal is to develop a system using Unmanned Aerial Vehicles (UAVs) to search forest areas for fire, smoke, human beings, and animals. The project leverages AI inference on edge devices, which are powered by solar harvesting batteries.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Implementation](#implementation)
  - [UAV Path Planning](#uav-path-planning)
  - [Object Detection Model](#object-detection-model)
  - [Model Optimization](#model-optimization)
- [Results](#results)
- [Future Work](#future-work)
- [How to Run](#how-to-run)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

The project is focused on developing a UAV-based system that efficiently detects fires, smoke, humans, and animals in forest areas. The UAVs are guided using Bayesian probability-based path planning, and the object detection is handled by a YOLOv8 model optimized for edge devices.

### Key Objectives:
- **UAV Path Planning**: Divide the search area into grids and guide the UAV based on the probability of encountering a rescue zone.
- **Detection Model**: Implement and optimize a lightweight YOLOv8 model to run efficiently on edge devices.
- **Optimization**: Reduce the model size to fit edge device constraints while maintaining high accuracy in detecting small objects.

## Dataset

The dataset used in this project is coolected from various open scources platfrom and consists of:
- **Training Data**: 70,000 aerial view images
- **Validation Data**: 8,000 images
- **Categories**: Fire, Smoke, Person, Animals

The dataset is divided into separate folders for training and validation. Images are annotated to facilitate training of the object detection model.

## Implementation

### UAV Path Planning

The UAV divides the forest into grids and navigates these grids based on Bayesian probability. The UAV marks grids with detected objects and follows an efficient search pattern to maximize coverage and detection accuracy.

### Object Detection Model

The project uses a YOLOv8n model, which is lightweight and optimized for small object detection. The model architecture includes:
- **Backbone**: CSPDarknet53 for feature extraction
- **Neck**: C2f Module for merging features
- **Head**: Multiple detection modules for prediction

### Model Optimization

The model was optimized to reduce its size from 6.5 MB to 2.5 MB, with a minimal loss in accuracy. This was achieved through gradual pruning, dynamic quantization, and fine-tuning of model parameters.

## Results

Post-optimization, the YOLOv8 model showed the following performance:
- **Model Size**: Reduced from 6.5 MB to 2.5 MB
- **Mean Average Precision (mAP50)**:
  - Fire: 0.43
  - Smoke: 0.59
  - Person: 0.84
  - Animal: 0.94

### Inference Results
- Inference on test data demonstrated effective detection of the targeted categories, even in optimized model conditions.

## Future Work

- **Integration with Edge Devices**: Deploy the optimized model on edge devices for real-time inference.
- **Solar-Powered System**: Develop a solar-powered system to support continuous UAV operations.
- **Priority-Based Rescue Pipeline**: Implement a detection pipeline to prioritize rescues based on the detected objects.

## How to Run

To run the project, if you send email at taufiqahmed806@gmail.com , we will be happy to share our work for the research purpose.

## Contributors

- **Taufiq Ahmed**
- **Abhishek Kumar**

