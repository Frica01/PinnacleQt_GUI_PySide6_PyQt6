# -*- coding: utf-8 -*-
# Name:         main.py
# Author:       小菜
# Date:         2024/4/01 00:00
# Description:

import sys

from PySide6.QtWidgets import QApplication

from controllers import ControllerMain

if __name__ == '__main__':
    app = QApplication()
    # 默认以动画形式启动应用，如不需要可传入 animate_on_startup=False
    controller = ControllerMain(animate_on_startup=True)
    sys.exit(app.exec())
