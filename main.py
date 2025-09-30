import sys
import logging
import traceback
from pathlib import Path

# ADD THIS BLOCK AT THE TOP - BEFORE OTHER IMPORTS
# Add parent directory to Python path if running as script
if __name__ == "__main__":
    import os
    # Get the directory containing this file
    current_dir = Path(__file__).resolve().parent
    # Get the parent directory (project root)
    project_root = current_dir.parent
    # Add to Python path if not already there
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

# Try PySide6 first, fall back to PyQt6
try:
    from PySide6.QtWidgets import QApplication, QMessageBox
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QIcon
    print("Using PySide6")
except ImportError:
    try:
        from PyQt6.QtWidgets import QApplication, QMessageBox
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QIcon
        print("Using PyQt6")
    except ImportError:
        print("ERROR: Neither PySide6 nor PyQt6 is installed!")
        print("Please install one of them:")
        print("  pip install PySide6")
        print("  or")
        print("  pip install PyQt6")
        sys.exit(1)

from gui.main_window import MainWindow
from utils.subprocess_manager import setup_logging

def setup_application():
    """Setup the Qt application with proper styling and error handling."""
    app = QApplication(sys.argv)
    app.setApplicationName("LiDAR Classification Orchestrator")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("LiDAR Tools")
    
    # Enable high DPI scaling
    try:
        app.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)
    except:
        pass  # Older Qt versions
    
    return app


def handle_exception(exc_type, exc_value, exc_traceback):
    """Global exception handler."""
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    logger = logging.getLogger(__name__)
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    
    error_msg = f"An unexpected error occurred:\n\n{exc_type.__name__}: {exc_value}"
    try:
        QMessageBox.critical(None, "Application Error", error_msg)
    except:
        print(error_msg)


def main():
    """Main application entry point."""
    # Setup logging first
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Set global exception handler
    sys.excepthook = handle_exception
    
    try:
        # Create and setup application
        app = setup_application()
        
        # Create main window
        main_window = MainWindow()
        main_window.show()
        
        logger.info("Application started successfully")
        
        # Run application
        return app.exec()
        
    except Exception as e:
        logger.critical(f"Failed to start application: {e}", exc_info=True)
        print(f"CRITICAL ERROR: {e}")
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
