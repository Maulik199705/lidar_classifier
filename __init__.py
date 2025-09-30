"""
LiDAR Classification Workflow Orchestrator.
A production-ready desktop application for LiDAR point cloud classification.
"""

__version__ = "1.0.0"
__author__ = "LiDAR Tools Team"

from lidar_classifier.core.orchestrator import WorkflowOrchestrator
from lidar_classifier.pipeline.presets import get_preset_configs

__all__ = ['WorkflowOrchestrator', 'get_preset_configs']