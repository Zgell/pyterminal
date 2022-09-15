### Random Technical Notes:
- PyQt6 may not install correctly if you have Anaconda installed on your system (because Anaconda comes pre-packaged with PyQt).
- To dynamically load UI: https://geekscoders.com/how-to-load-qt-designer-ui-file-in-pyqt6/
- To add the terminal widget, you can create an empty widget and build the console off of that (see qterm-borked for more info)
- Use the command `qt6-tools designer` to open the Qt Designer from the command line. Use `qt6-tools --help` for more info.
- Closable tabs: https://stackoverflow.com/questions/459372/putting-a-close-button-on-qtabwidget