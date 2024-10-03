Here's a refined version of the Git documentation for your project, "AI-Assisted Dynamic Waypoint Selection Using UAV":

---

# **AI-Assisted Dynamic Waypoint Selection Using UAV**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Implementation](#implementation)
   - [UAV Path Planning](#uav-path-planning)
   - [Object Detection Model](#object-detection-model)
   - [Model Optimization](#model-optimization)
4. [Results](#results)
5. [Future Work](#future-work)
6. [How to Run](#how-to-run)
7. [Contributors](#contributors)

## **Project Overview**
The **AI-Assisted Dynamic Waypoint Selection Using UAV** project aims to develop an efficient UAV-based system to search forest areas and detect fire, smoke, humans, and animals using AI-driven inference on edge devices powered by solar-harvested batteries. 

Key Objectives:
- **UAV Path Planning**: Utilize Bayesian probability to guide UAVs through a grid-based search area to maximize the likelihood of detecting rescue zones.
- **Object Detection**: Implement a lightweight YOLOv8 model optimized for deployment on edge devices to detect small objects with high accuracy.
- **Model Optimization**: Reduce the model size for compatibility with edge devices while maintaining strong performance on object detection tasks.

---

## **Dataset**
The dataset comprises aerial view images annotated for object detection, divided into categories of **Fire**, **Smoke**, **Person**, and **Animals**. The dataset has been sourced from multiple open platforms and split into training and validation sets:

- **Training Data**: 70,000 images
- **Validation Data**: 8,000 images

### **Dataset Sources**:
- **Fire Detection**: 
  - [Fire and Smoke Detection - RoboFlow](https://universe.roboflow.com/master-candidate/forest-fire-and-smoke-rf4pd)
  - [Fire and Smoke Detection - Browse](https://universe.roboflow.com/ai-faogz/fire-and-smoke-detection-9boih/browse?queryText=&pageSize=50&startingIndex=150&browseQuery=true)
- **Human Detection**:
  - [Human Detection - RoboFlow](https://universe.roboflow.com/monash-university-sluul/yolov8-y2l6b)
  - [SAR Custom Drone Dataset](https://universe.roboflow.com/university-of-engineering-and-technology-huotg/sar_custom_drone/dataset/10)
- **Animal Detection**:
  - [Wild Animal Detection - RoboFlow](https://universe.roboflow.com/shenkar-1d8w5/cownt-wild-dataset)

---

## **Implementation**

### **UAV Path Planning**
- **Grid-based Search**: The UAV divides the forest into grids and systematically searches them using Bayesian probability. The probability of encountering specific objects such as fire, smoke, animals, or humans influences the UAV’s flight path. 
- **Dynamic Waypoint Selection**: The UAV dynamically selects new waypoints based on real-time detection probabilities, improving search efficiency and detection rates.

### **Object Detection Model**
- **YOLOv8n Architecture**: A lightweight version of YOLOv8, optimized for edge devices. Key components include:
  - **Backbone**: CSPDarknet53, which provides efficient feature extraction.
  - **Neck**: C2f Module, which merges features at different scales.
  - **Head**: Detection modules that predict bounding boxes and class probabilities for the target objects (fire, smoke, humans, animals).
  
### **Model Optimization**
- **Model Pruning and Quantization**: The original YOLOv8 model (6.5 MB) was optimized using techniques such as pruning and dynamic quantization to reduce the model size to **2.5 MB**. This reduction was achieved with minimal loss in accuracy, making the model suitable for edge devices with limited computational power.

---

## **Results**
After optimization, the YOLOv8 model delivered strong performance in detecting target objects. Below are the key performance metrics:

- **Model Size**: Reduced from **6.5 MB** to **2.5 MB**
- **Mean Average Precision (mAP50)**:
  - Fire: **0.43**
  - Smoke: **0.59**
  - Person: **0.84**
  - Animal: **0.94**
  
- **Inference Time**: The model runs efficiently on edge devices, demonstrating low latency during inference.

---

## **Future Work**
1. **Integration with Edge Devices**: Deploy the optimized YOLOv8 model on solar-powered edge devices for real-time UAV-based object detection.
2. **Continuous Operation**: Develop a solar-powered system that ensures uninterrupted UAV operation in forest environments.
3. **Rescue Pipeline**: Implement a priority-based rescue pipeline, prioritizing responses based on detected objects (e.g., humans are prioritized over animals).

---

## **How to Run**
To run this project, you need access to the dataset and the optimized YOLOv8 model. Due to the sensitive nature of this project, we are happy to share the dataset and code for research purposes. Please contact **Taufiq Ahmed** at **taufiqahmed806@gmail.com** for access.

### **Setting Up the Environment**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/uav-ai-waypoint-selection.git
   cd uav-ai-waypoint-selection
   ```

2. **Create Conda Environment**:
   Make sure you have Conda installed. Then, create and activate the environment:
   ```bash
   conda create -n yolov8_env python=3.12
   conda activate yolov8_env
   ```

3. **Install Dependencies**:
   Install the required dependencies including the YOLOv8 library:
   ```bash
   pip install ultralytics
   ```

4. **Prepare the Dataset**:
   - Download the dataset from the provided links and structure it as follows:
     ```bash
     data/
     ├── images/
     ├── labels/
     └── data.yaml  # The dataset configuration file.
     ```
   
5. **Run YOLOv8 Training**:
   Execute the training script on your local machine or an HPC system:
   ```bash
   yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=1024
   ```

---

## **Contributors**
- **Taufiq Ahmed** 
- **Abhishek Kumar** 

For any questions or contributions, please open an issue or reach out to the contributors.

---
