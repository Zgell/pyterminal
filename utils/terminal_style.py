from PyQt5.QtGui import QColor, QPalette, QFont

import json

class TerminalStyler:
    def __init__(self):
        CONFIG_FILE_LOCATION = 'utils/config.json'
        with open(CONFIG_FILE_LOCATION, 'r') as f:
            self.options = json.loads(f.read())

    def generate_palette(self) -> QPalette:
        '''Creates a QPalette object that styles the console'''
        palette = QPalette()
        palette.setColor(QPalette.Base, QColor(*self.options['Base']))
        palette.setColor(QPalette.Text, QColor(*self.options['Text']))
        palette.setColor(QPalette.Highlight, QColor(*self.options['Highlight']))
        palette.setColor(QPalette.HighlightedText, QColor(*self.options['HighlightedText']))

        return palette

    def generate_font(self, default_font: QFont) -> QFont:
        pass
        