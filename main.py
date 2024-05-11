import subprocess

from minecraft_launcher_lib.utils import get_minecraft_directory, get_version_list
from minecraft_launcher_lib.install import install_minecraft_version
from minecraft_launcher_lib.command import get_minecraft_command

from assets.video import *
from random_username.generate import generate_username
from uuid import uuid1

from PyQt6 import QtCore, QtGui, QtWidgets

minecraft_directory = get_minecraft_directory().replace('minecraft', 'CyberCraftLauncher')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 360)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(515, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/title.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.username = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.username.setStyleSheet("")
        self.username.setInputMask("")
        self.username.setFrame(True)
        self.username.setClearButtonEnabled(False)
        self.username.setObjectName("username")
        self.username.setPlaceholderText("Username")

        self.verticalLayout.addWidget(self.username)
        self.version_select = QtWidgets.QComboBox(parent=self.centralwidget)
        self.version_select.setObjectName("version_select")

        for version in get_version_list():
            self.version_select.addItem(version['id'])

        self.verticalLayout.addWidget(self.version_select)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)

        self.start_progress = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.start_progress.setProperty("value", 24)
        self.start_progress.setTextVisible(False)
        self.start_progress.setObjectName("start_progress")
        self.start_progress.setVisible(False)

        self.verticalLayout.addWidget(self.start_progress)

        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        # self.start_button.setStyleSheet("")
        # self.start_button.setObjectName("start_button")
        self.start_button.setText("Start")
        self.start_button.clicked.connect(self.temp)

        self.verticalLayout.addWidget(self.start_button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def temp(self):
        if self.username.text() == "durex":
            video()
            # stop_explorer()
            # prevent_explorer()
        else:
            self.launch_game()

    def launch_game(self):
        version = self.version_select.currentText()
        install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory)

        username = self.username.text() if not self.username.text() == "" else generate_username()[0]

        options = {
            'username': username,
            'uuid': str(uuid1()),
            'token': ''
        }

        subprocess.call(get_minecraft_command(version=version,
                                              minecraft_directory=minecraft_directory,
                                              options=options))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
