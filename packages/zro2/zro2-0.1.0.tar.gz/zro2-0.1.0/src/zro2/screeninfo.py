from functools import cache
import screeninfo
import pygetwindow as gw

@cache
def get_screen_dimensions(monitor_index=0):
    monitors = screeninfo.get_monitors()
    if monitor_index < 0 or monitor_index >= len(monitors):
        raise ValueError("Invalid monitor index")
    monitor = monitors[monitor_index]
    # Return both dimensions and the position of the monitor
    return (monitor.width, monitor.height, monitor.x, monitor.y)

def get_wnds_monitor(wnd : gw.Window):
    """Determine which monitor a window is currently on based on its position"""
    #(left, top, width, height)
    #wnd midpoint = (left + width / 2, top + height / 2)
    midpoint =(wnd.left + wnd.width / 2, wnd.top + wnd.height / 2)
    for monitor in screeninfo.get_monitors():
        if (monitor.x <= midpoint[0] < monitor.x + monitor.width and
                monitor.y <= midpoint[1] < monitor.y + monitor.height):
            return monitor
    return None  # Fallback if no monitor matches, should be handled appropriately