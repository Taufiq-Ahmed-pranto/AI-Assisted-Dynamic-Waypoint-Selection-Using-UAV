# **AI-Assisted UAV Path Planning for Rescue Operations**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Data Engineering and AI](#data-engineering-and-ai)
   - [Dataset Overview](#dataset-overview)
   - [Data Imbalance and Augmentation](#data-imbalance-and-augmentation)
   - [Model Optimization](#model-optimization)
3. [UAV Path Planning](#uav-path-planning)
   - [Dynamic Waypoint Selection](#dynamic-waypoint-selection)
   - [Algorithm Integration](#algorithm-integration)
4. [Results](#results)
   - [Performance Metrics](#performance-metrics)
   - [Ablation Studies](#ablation-studies)
5. [Future Work](#future-work)
6. [How to Run](#how-to-run)
7. [Contributors](#contributors)

---

## **Project Overview**
The **AI-Assisted UAV Path Planning for Rescue Operations** project leverages advanced AI techniques to develop an efficient UAV-based system for large-scale forest rescue missions. The system detects fire, smoke, humans, and animals in challenging environments using lightweight AI models optimized for edge devices. This includes implementing robust data engineering practices and deploying AI models on solar-powered UAVs for continuous operation.

Key Objectives:
- **Data Engineering**: Develop a diverse and balanced dataset to improve detection accuracy for fire, smoke, humans, and animals.
- **AI Optimization**: Use advanced model pruning, quantization, and rebalancing techniques to create lightweight, high-performance models.
- **UAV Path Planning**: Implement dynamic waypoint selection and obstacle avoidance algorithms to optimize UAV navigation and efficiency.

---

## **Data Engineering and AI**

### **Dataset Overview**
The dataset combines multiple sources to ensure broad coverage of target objects. It includes aerial images of **fire**, **smoke**, **humans**, **animals**, and **lakes**, with a focus on real-world scenarios.

- **Sources**: Fire and smoke detection datasets from RoboFlow, SAR datasets for human detection, and custom datasets generated during summer internships.
- **Current Dataset Statistics**:
  - **Smoke**: 28,769 files
  - **Fire**: 16,915 files
  - **Humans**: 18,525 files
  - **Lake**: 12,646 files

**Key Enhancements:**
1. Generated high-altitude test datasets and applied advanced annotation techniques.
2. Integrated fireman datasets into a custom YOLO-format dataset.
3. Applied AI tools to convert standard datasets into aerial views for improved relevance.

---

### **Data Imbalance and Augmentation**

Addressing data imbalance was critical to ensuring reliable object detection across all classes. The following strategies were implemented:

1. **Custom Dataloader**:
   - Developed a custom dataloader to balance training datasets by prioritizing underrepresented classes.
   - Integrated repeat-factor sampling techniques to address imbalance dynamically.

2. **Augmentation Techniques**:
   - Applied augmentation strategies to increase instances of underrepresented classes, including oversampling and synthetic data generation.
   - Conducted experiments to fine-tune the augmentation strategy based on model performance.

3. **Ablation Studies**:
   - Performed detailed analyses on the effectiveness of rebalancing techniques and transfer learning.

---

### **Model Optimization**

- **Architecture**: The lightweight YOLOv8n model was further optimized using:
  - **Pruning**: Removed redundant parameters to reduce the model size.
  - **Quantization**: Applied dynamic quantization to improve compatibility with edge devices.
  - **Instance-Aware Rebalancing**: Integrated techniques from cutting-edge research ([Instance-Aware Sampling](https://arxiv.org/abs/2305.08069)) to improve performance.

- **Current Metrics:**
  - **Model Size**: Reduced from 6.5 MB to **<2.5 MB**.
  - **mAP50 Performance**:
    - Fire: 0.26
    - Smoke: 0.73
    - Human: 0.78
    - Lake: 0.05

---

## **UAV Path Planning**

### **Dynamic Waypoint Selection**
The UAV employs AI-driven dynamic waypoint selection to maximize efficiency and coverage:
- **Bayesian Inference**: Guides UAV navigation by estimating the probability of detecting specific objects.
- **Dynamic Updates**: Continuously adjusts waypoints based on real-time detections.

### **Algorithm Integration**
The project integrates various algorithms to optimize UAV operations:
1. **RRT* Algorithm**: Used for obstacle avoidance and dynamic waypoint selection.
2. **Energy Optimization**:
   - Minimized energy consumption during hovering.
   - Utilized solar energy harvesting for inference tasks.
3. **Battery and Cost Monitoring**: Integrated into path planning algorithms to ensure efficient resource utilization.

---

## **Results**

### **Performance Metrics**
- **Aggregated Dataset Accuracy**:
  | Class  | mAP-50 |
  |--------|---------|
  | Fire   | 0.26    |
  | Smoke  | 0.73    |
  | Human  | 0.78    |
  | Lake   | 0.05    |
  | All    | 0.46    |

- **Improvements**:
  - mAP50 increased from 0.16 (fireman dataset alone) to 0.46 (aggregated dataset).
  - Significant accuracy gains for human and smoke classes due to improved dataset quality.

### **Ablation Studies**
- Conducted experiments to evaluate rebalancing techniques, augmentation strategies, and transfer learning.
- Established baselines for YOLOv11 Nano and Large models.
- Results informed improvements in dataset balancing and model optimization.

---

## **Future Work**
1. **Improve Detection for Underserved Classes**:
   - Enhance datasets for fire and lake detection.
   - Experiment with advanced augmentation techniques.
2. **Generalization**:
   - Train models to perform well in diverse environments (forest, city, etc.).
3. **Model Deployment**:
   - Deploy models on microcontroller units (MCUs) and measure energy consumption.
   - Develop UAV-ready solar-powered inference systems.
4. **Test Pipeline**:
   - Validate performance on real-world videos and high-altitude datasets.

---

## **How to Run**

### **Prerequisites**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/uav-ai-rescue.git
   cd uav-ai-rescue
   ```

2. **Set Up the Environment**:
   - Install Conda and create an environment:
     ```bash
     conda create -n uav_env python=3.12
     conda activate uav_env
     ```
   - Install dependencies:
     ```bash
     pip install ultralytics
     ```

3. **Prepare the Dataset**:
   - Structure the dataset as follows:
     ```bash
     data/
     ├── images/
     ├── labels/
     └── data.yaml
     ```

### **Run Training**
Execute the training script:
```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=100 imgsz=1024
```

---

## **Contributors**
- **Taufiq Ahmed**
- **Abhishek Kumar**

For any questions or contributions, please open an issue or contact the contributors at **taahmed23@student.oulu.fi**.

---
