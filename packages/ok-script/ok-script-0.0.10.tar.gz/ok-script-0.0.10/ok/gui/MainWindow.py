from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QMessageBox, QTabWidget

from ok.gui.about.AboutTab import AboutTab
from ok.gui.debug.DebugTab import DebugTab
from ok.gui.tasks.TaskTab import TaskTab
from ok.logging.Logger import get_logger

logger = get_logger(__name__)


class Communicate(QObject):
    speak = Signal(str)


class MainWindow(QTabWidget):
    def __init__(self, tasks, debug=False, about=None, exit_event=None):
        super().__init__()
        self.exit_event = exit_event
        task_tab = TaskTab(tasks)
        self.addTab(task_tab, self.tr("Task"))
        if debug:
            debug_tab = DebugTab()
            self.addTab(debug_tab, self.tr("Debug"))
        # ... Add other tabs similarly
        if about:
            about_tab = AboutTab(about)
            self.addTab(about_tab, self.tr("About"))

        # Styling the tabs and content if needed, for example:
        self.setStyleSheet("""
                            QTabWidget::tab-bar {
                                alignment: center;
                            }
                            QTabBar::tab {
                                background: #333;
                                color: white;
                                border-radius: 5px;
                                padding: 10px;
                            }
                            QTabBar::tab:selected {
                                background: #555;
                                font-weight: bold;
                            }
                            QWidget {
                                background-color: #222;
                                color: #ddd;
                            }
                        """)
        self.setWindowTitle("Close Event Example")
        self.setTabPosition(QTabWidget.West)
        # self.setTabBar(QTabBar())
        self.comm = Communicate()
        self.comm.speak.connect(self.say_hello)

    @Slot(str)
    def say_hello(self, message):
        print(message)

    def btn_clicked(self):
        self.comm.speak.emit("Hello, PySide6 with parameters!")

    def closeEvent(self, event):
        # Create a message box that asks the user if they really want to close the window
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.exit_event.set()
            event.accept()
            logger.info("Window closed")  # Place your code here
        else:
            event.ignore()
