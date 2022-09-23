from PyQt5.QtGui import QColor, QPalette, QFont

import json

class TerminalStyler:
    def __init__(self):
        CONFIG_FILE_LOCATION = 'utils/config.json'
        with open(CONFIG_FILE_LOCATION, 'r') as f:
            self.options = json.loads(f.read())

        self.default_options = {
            "Base": [0, 0, 0],
            "Text": [255, 255, 255],
            "Highlight": [255, 255, 255],
            "HighlightedText": [0, 0, 0],
            "FontFamily": "Consolas",
            "PointSize": 10
        }

    def generate_palette(self) -> QPalette:
        '''Creates a QPalette object that styles the console'''
        palette = QPalette()
        palette.setColor(QPalette.Base, QColor(*self.options['Base']))
        palette.setColor(QPalette.Text, QColor(*self.options['Text']))
        palette.setColor(QPalette.Highlight, QColor(*self.options['Highlight']))
        palette.setColor(QPalette.HighlightedText, QColor(*self.options['HighlightedText']))

        return palette

    def generate_font(self, font: QFont) -> QFont:
        '''Edits a font to have settings as per the config, and returns it.'''
        font.setFamily(self.options['FontFamily'])
        font.setPointSize(self.options['PointSize'])

        return font
        