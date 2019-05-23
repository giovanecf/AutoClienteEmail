from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget


class TimerThread(QThread):
    update = pyqtSignal()

    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.02):
            self.update.emit()

class FrontEnd(QWidget):
    def __init__(self):
        super().__init__()

        # code as in your original

        stop_flag = Event()
        self.timer_thread = TimerThread(stop_flag)
        self.timer_thread.update.connect(self.update_ui)
        self.timer_thread.start()

