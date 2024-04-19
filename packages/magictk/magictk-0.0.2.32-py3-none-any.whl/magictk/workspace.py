import os
import subprocess
import sys
from typing import Optional, Tuple


def get_windows_workspace_size() -> Optional[Tuple[int, int, int, int]]:
    try:
        import win32api
        # 获取工作区（不包括任务栏）的尺寸
        work_area = win32api.GetMonitorInfo(
            win32api.MonitorFromPoint((0, 0))).get('Work')
        x, y, width, height = work_area
        width -= x
        height -= y
        return x, y, width, height
    except ImportError:
        print("pywin32 library is not installed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return (0, 0, 1920, 1002)


def get_gtk_workspace_size() -> Optional[Tuple[int, int, int, int]]:
    try:
        # if 1:
        import gi

        screen = gi.gdk.screen_get_default()

        # 获取屏幕上显示器的数量
        num_monitors = screen.get_n_monitors()

        # 获取每个显示器的几何信息，并计算工作区的大小
        workarea_width = 0
        workarea_height = 0

        for i in range(num_monitors):
            monitor_geometry = screen.get_monitor_geometry(i)
            monitor_x = monitor_geometry.x
            monitor_y = monitor_geometry.y
            monitor_width = monitor_geometry.width
            monitor_height = monitor_geometry.height

            workarea_width += monitor_width
            workarea_height += monitor_height

        print("工作区大小（宽度 x 高度）：{} x {}".format(workarea_width, workarea_height))
    except ImportError:
        print("pygtk (PyGObject  pygtk) library is not installed.")
    except:
        pass
    return None


def get_macos_workspace_size() -> Optional[Tuple[int, int, int, int]]:
    try:
        output = subprocess.check_output(
            ['system_profiler', 'SPDisplaysDataType']).decode('utf-8')
        lines = output.split('\n')
        for line in lines:
            if 'Resolution:' in line:
                dimensions = line.split(':')[1].strip().split('x')
                width = int(dimensions[0])
                height = int(dimensions[1])
                # system_profiler does not provide the top-left corner directly, assuming (0, 0)
                return 0, 0, width, height
    except subprocess.CalledProcessError:
        pass
    return None


def get_workspace_size() -> Optional[Tuple[int, int, int, int]]:
    if sys.platform.startswith('win'):
        return get_windows_workspace_size()
    elif sys.platform.startswith('darwin'):
        return get_macos_workspace_size()
    return get_gtk_workspace_size()
