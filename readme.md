# LiDAR Classification Workflow Orchestrator

A production-ready desktop application for orchestrating LAStools binaries to perform comprehensive LiDAR point cloud classification with professional GUI, intelligent tiling, progressive classification, and comprehensive quality control.

## 🎯 Features

### Core Capabilities
- **Progressive Classification**: Buildings → Vegetation → Cars → Wires → Roads with overlap-safe ordering
- **Intelligent Tiling**: Point-count and spatial tiling with configurable overlap buffers (≤1.5M points per tile)
- **Quality Control**: False positive suppression, overlap resolution, comprehensive QC rules
- **Target Accuracy**: 80-85% overall accuracy with <1% false positives

### Professional GUI
- Multi-panel interface with configuration, progress tracking, and live log viewing
- Real-time command preview and parameter validation
- Save/load configuration presets (Urban Conservative, Balanced, High Recall)
- Cross-platform support (Windows/Linux)

### Supported Classes
- Ground (Class 2)
- Low Vegetation (Class 3)
- Medium Vegetation (Class 4)
- High Vegetation (Class 5)
- Buildings (Class 6)
- Cars/Vehicles (Class 8)
- Roads (Class 11)
- Wires (Class 14)

## 📋 Requirements

### System Requirements
- **Python**: 3.10 or higher (3.13 supported)
- **LAStools**: Downloaded from [rapidlasso.de](https://rapidlasso.de)
- **Operating System**: Windows 10/11 or Linux (Ubuntu 20.04+)
- **Memory**: 8GB RAM minimum (16GB recommended)
- **Storage**: 2-3x input file size for intermediate files

### Python Dependencies