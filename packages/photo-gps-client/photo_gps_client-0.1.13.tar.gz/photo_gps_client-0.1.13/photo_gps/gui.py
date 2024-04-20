import os
import threading
import time

import wx
import wx.grid
import wx.richtext

from .config import load_config
from .commands import set_gps


class PhotoGpsApp(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True


class MainFrame(wx.Frame):
    config: dict = None
    thread: threading.Thread = None

    def __init__(self):
        super(MainFrame, self).__init__(None, -1, title='Photo GPS', size=(600, 300))

        self.config = load_config()

        #
        # Панель с кнопками
        #

        panel_control = wx.Panel(self)
        dir_picker_label = wx.StaticText(panel_control, label="Folder:")
        self.dirPicker = wx.DirPickerCtrl(panel_control, message="Choose folder with potots to tag",
                                          style=wx.DIRP_DIR_MUST_EXIST|wx.DIRP_USE_TEXTCTRL)
        self.dirPicker.Bind(wx.EVT_DIRPICKER_CHANGED, self.on_dir_change)
        self.goButton = wx.Button(panel_control, label="Go")
        self.goButton.Disable()
        self.goButton.Bind(wx.EVT_BUTTON, self.on_btn_go)

        sizer_control = wx.BoxSizer(wx.HORIZONTAL)
        # s1.Add(dir_picker_label, proportion=0, flag=wx.ALL, border=20)
        # dir_picker_label должен быть выровнен по высоте с dirPicker
        sizer_control.Add(dir_picker_label, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=20)
        sizer_control.Add(self.dirPicker, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=20)
        sizer_control.Add(self.goButton, proportion=0, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=20)
        panel_control.SetSizer(sizer_control)

        #
        # Панель с прогрессбаром
        #
        panel_progress = wx.Panel(self)
        self.progress = wx.Gauge(panel_progress, range=100)
        self.progress.SetValue(0)
        sizer_progress = wx.BoxSizer(wx.HORIZONTAL)
        sizer_progress.Add(self.progress, proportion=1, flag=wx.ALL | wx.EXPAND)
        panel_progress.SetSizer(sizer_progress)

        #
        # Панель с данными
        #

        # panel_data = wx.Panel(self)
        # self.grid = wx.grid.Grid(panel_data)
        # self.grid.CreateGrid(100, 2)
        # self.grid.SetColLabelValue(0, "File")
        # self.grid.SetColLabelValue(1, "Status")
        # self.grid.SetRowLabelSize(0)
        # sizer_data = wx.BoxSizer(wx.VERTICAL)
        # sizer_data.Add(self.grid, proportion=1, flag=wx.ALL | wx.EXPAND)
        # panel_data.SetSizer(sizer_data)

        #
        # панель с логом
        #
        panel_log = wx.Panel(self)
        self.text_log = wx.richtext.RichTextCtrl(panel_log, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        sizer_log = wx.BoxSizer(wx.VERTICAL)
        sizer_log.Add(self.text_log, proportion=1, flag=wx.ALL | wx.EXPAND)
        panel_log.SetSizer(sizer_log)

        #
        # Сборка основного окна
        #

        s_vertical = wx.BoxSizer(wx.VERTICAL)
        s_vertical.Add(panel_control, proportion=0, flag=wx.ALL | wx.EXPAND)
        s_vertical.Add(panel_progress, proportion=0, flag=wx.ALL | wx.EXPAND)
        s_vertical.Add(panel_log, proportion=1, flag=wx.ALL | wx.EXPAND)
        # s_vertical.Add(panel_data, proportion=1, flag=wx.ALL | wx.EXPAND)

        self.SetSizer(s_vertical)
        self.SetMinSize((600, 300))
        self.Layout()
        self.log("App started")
        self.log(f"Authorized as: {self.config['auth']['user']}")

    def log(self, message, color=None):
        if color:
            self.text_log.BeginTextColour(wx.Colour(color))
        self.text_log.WriteText(message)
        if color:
            self.text_log.EndTextColour()
        self.text_log.Newline()
        last_position = self.text_log.GetLastPosition()
        # Прокручиваем к последней позиции
        self.text_log.ShowPosition(last_position)
        # print(message)

    def on_dir_change(self, event):
        # Обработка изменения выбранной директории
        path = self.dirPicker.GetPath()
        if os.path.isdir(path):
            self.goButton.Enable()
            self.log(f"Selected folder: {path}")
        else:
            self.goButton.Disable()
            # self.log(f"Path {path} does not exist!")

    def on_btn_go(self, event):
        # Обработка нажатия кнопки Go
        path = self.dirPicker.GetPath()
        if not os.path.isdir(path):
            wx.MessageBox(f'Path {path} does not exist!', 'Error', wx.OK | wx.ICON_INFORMATION)

        # disable dirPicker and goButton
        self.dirPicker.Disable()
        self.goButton.Disable()
        self.log(f"Start processing directory {path}")

        self.progress.SetValue(0)
        self.thread = threading.Thread(target=self.background_work, kwargs={
            "path": path,
            'config': self.config,
        })
        self.thread.daemon = True
        self.thread.start()

    def on_background_done(self):
        self.dirPicker.Enable()
        self.goButton.Enable()

    def background_work(self, path, config):
        # for i in range(10):
        #     time.sleep(1)
        #     wx.CallAfter(self.progress.SetValue, int(200 / 10 * (i + 1)))
        #     wx.CallAfter(self.log, f"{name}: {i + 1}")
        def log_func(message, color=None):
            wx.CallAfter(self.log, message, color)

        def progress_func(value):
            wx.CallAfter(self.progress.SetValue, value)

        set_gps(path, config['auth']['user'], config['auth']['token'], config, log_func, progress_func)
        wx.CallAfter(self.on_background_done)