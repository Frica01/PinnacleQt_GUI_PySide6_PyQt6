# -*- coding: utf-8 -*-
# Name:         config.py
# Author:       小菜
# Date:         2024/3/22 15:19
# Description:


class DarkConfig:
    QSS_FILE = 'views/resources/themes/py_dracula_dark.qss'

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: #ff79c6;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: rgb(40, 44, 52);
        """

    # MANUAL STYLES
    MANUAL_STYLES = {
        'lineEdit': "background-color: rgb(33, 37, 43);",
        'pushButton': "background-color: rgb(52, 59, 72);",
        'plainTextEdit': "background-color: rgb(33, 37, 43);",
        'tableWidget': "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }",
        'scrollArea': "QScrollBar:vertical {background: rgb(52, 59, 72);} QScrollBar:horizontal {background: rgb(52, 59, 72);}",
        'comboBox': "background-color: rgb(33, 37, 43);",
        'horizontalScrollBar': "background: rgb(52, 59, 72);",
        'verticalScrollBar': "background: rgb(52, 59, 72);",
        'commandLinkButton': "color: rgb(255, 121, 198);",
    }

    # APP SETTINGS
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500


class LightConfig:
    QSS_FILE = 'views/resources/themes/py_dracula_light.qss'

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: #495474;"
    BTN_RIGHT_BOX_COLOR = "background-color: #495474;"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

    # MANUAL STYLES
    MANUAL_STYLES = {
        'lineEdit': "background-color: #6272a4;",
        'pushButton': "background-color: #6272a4;",
        'plainTextEdit': "background-color: #6272a4;",
        'tableWidget': "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }",
        'scrollArea': "QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }",
        'comboBox': "background-color: #6272a4;",
        'horizontalScrollBar': "background-color: #6272a4;",
        'verticalScrollBar': "background-color: #6272a4;",
        'commandLinkButton': "color: #ff79c6;"
    }

    # APP SETTINGS
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500
