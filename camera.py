# modified from: https://stackoverflow.com/a/52306032

import sys
import vlc
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import argparse

RESOLUTION = 'profile1'

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.sizeHint = lambda: QSize(1280, 900)
        self.move(100, 10)
        self.mainFrame = QFrame()
        self.setCentralWidget(self.mainFrame)
        t_lay_parent = QGridLayout()
        # t_lay_parent.setContentsMargins(0, 0, 0, 0)

        # ------------------------------------------- NODE 0 FRAME -----------------------------------------------------
        self.videoFrame = QFrame()
        self.videoFrame.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        t_lay_parent.addWidget(self.videoFrame, 0, 0)
        self.vlcInstance = vlc.Instance(['--video-on-top'])
        self.videoPlayer = self.vlcInstance.media_player_new()
        self.videoPlayer = self.vlcInstance.media_player_new()
        self.videoPlayer.video_set_mouse_input(False)
        self.videoPlayer.video_set_key_input(False)
        self.videoPlayer.set_mrl("rtsp://192.168.1.14:554/live/video/{}".format(RESOLUTION), "network-caching=300")
        self.videoPlayer.audio_set_mute(True)
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.videoPlayer.set_xwindow(self.videoFrame.winId())
        elif sys.platform == "win32": # for Windows
            self.videoPlayer.set_hwnd(self.videoFrame.winId())
        elif sys.platform == "darwin": # for MacOS
            self.videoPlayer.set_nsobject(int(self.videoFrame.winId()))

        self.videoPlayer.play()

        # ------------------------------------------- NODE 1 FRAME -----------------------------------------------------
        self.videoFrame1 = QFrame()
        t_lay_parent.addWidget(self.videoFrame1, 0, 1)
        self.videoFrame1.mouseDoubleClickEvent = self.mouseDoubleClickEvent1
        self.vlcInstance1 = vlc.Instance(['--video-on-top'])
        self.videoPlayer1 = self.vlcInstance1.media_player_new()
        self.videoPlayer1 = self.vlcInstance1.media_player_new()
        self.videoPlayer1.video_set_mouse_input(False)
        self.videoPlayer1.video_set_key_input(False)
        self.videoPlayer1.set_mrl("rtsp://192.168.1.24:554/live/video/{}".format(RESOLUTION), "network-caching=300")
        self.videoPlayer1.audio_set_mute(True)
        if sys.platform.startswith('linux'): # for Linux using the X Server
            self.videoPlayer1.set_xwindow(self.videoFrame1.winId())
        elif sys.platform == "win32": # for Windows
            self.videoPlayer1.set_hwnd(self.videoFrame1.winId())
        elif sys.platform == "darwin": # for MacOS
            self.videoPlayer1.set_nsobject(int(self.videoFrame1.winId()))

        self.videoPlayer1.play()

        # ------------------------------------------- NODE 2 FRAME -----------------------------------------------------
        self.videoFrame2 = QFrame()
        t_lay_parent.addWidget(self.videoFrame2, 1, 0)
        self.videoFrame2.mouseDoubleClickEvent = self.mouseDoubleClickEvent2
        self.vlcInstance2 = vlc.Instance(['--video-on-top'])
        self.videoPlayer2 = self.vlcInstance2.media_player_new()
        self.videoPlayer2 = self.vlcInstance2.media_player_new()
        self.videoPlayer2.video_set_mouse_input(False)
        self.videoPlayer2.video_set_key_input(False)
        self.videoPlayer2.set_mrl("rtsp://192.168.1.34:554/live/video/{}".format(RESOLUTION), "network-caching=300")
        self.videoPlayer2.audio_set_mute(True)
        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.videoPlayer2.set_xwindow(self.videoFrame2.winId())
        elif sys.platform == "win32": # for Windows
            self.videoPlayer2.set_hwnd(self.videoFrame2.winId())
        elif sys.platform == "darwin": # for MacOS
            self.videoPlayer2.set_nsobject(int(self.videoFrame2.winId()))

        self.videoPlayer2.play()

        # ------------------------------------------- CONTROL FRAME ----------------------------------------------------
        self.controlFrame = QFrame()
        t_lay_parent.addWidget(self.controlFrame, 1, 1)
        layout_control_frame = QGridLayout()
        self.controlFrame.setLayout(layout_control_frame)
        self.label_test = QLabel('this is under development')
        layout_control_frame.addWidget(self.label_test)

        self.mainFrame.setLayout(t_lay_parent)
        self.show()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.windowState() == Qt.WindowNoState:
                self.videoFrame.show()
                self.videoFrame1.hide()
                self.videoFrame2.hide()
                self.controlFrame.hide()
                self.setWindowState(Qt.WindowFullScreen)
            else:
                self.videoFrame1.show()
                self.videoFrame2.show()
                self.controlFrame.show()
                self.setWindowState(Qt.WindowNoState)

    def mouseDoubleClickEvent1(self, event):
        if event.button() == Qt.LeftButton:
            if self.windowState() == Qt.WindowNoState:
                self.videoFrame.hide()
                self.videoFrame1.show()
                self.videoFrame2.hide()
                self.controlFrame.hide()
                self.setWindowState(Qt.WindowFullScreen)
            else:
                self.videoFrame.show()
                self.videoFrame2.show()
                self.controlFrame.show()
                self.setWindowState(Qt.WindowNoState)

    def mouseDoubleClickEvent2(self, event):
        if event.button() == Qt.LeftButton:
            if self.windowState() == Qt.WindowNoState:
                self.videoFrame.hide()
                self.videoFrame1.hide()
                self.videoFrame2.show()
                self.controlFrame.hide()
                self.setWindowState(Qt.WindowFullScreen)
            else:
                self.videoFrame.show()
                self.videoFrame1.show()
                self.controlFrame.show()
                self.setWindowState(Qt.WindowNoState)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage='camera.py',
                                     description='view camera feeds from antennas')
    parser.add_argument('-r', '--resolution', help="video resolution (low, med, high) [medium]",
                        default='med')
    args = parser.parse_args()
    if args.resolution == 'high':
        RESOLUTION = 'profile1'
    elif args.resolution == 'med':
        RESOLUTION = 'profile2'
    elif args.resolution == 'low':
        RESOLUTION = 'profile3'
    else:
        print('unsupported resolution')
        sys.exit()
    app = QApplication(sys.argv)
    app.setApplicationName("VLC Test")

    window = MainWindow()
    app.exec_()
