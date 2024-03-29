# -*- coding: utf-8 -*-
# Name:         controller_main.py
# Author:       小菜
# Date:         2024/3/21 15:26
# Description:

from views import ViewMain


class ControllerMain:

    def __init__(self, animate_on_startup=True):
        self.view = ViewMain(animate_on_startup)
