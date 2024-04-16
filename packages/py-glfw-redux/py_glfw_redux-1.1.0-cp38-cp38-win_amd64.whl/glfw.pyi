"""
GLFW Windowing System
"""
from __future__ import annotations
import typing
__all__ = ['ACCUM_ALPHA_BITS', 'ACCUM_BLUE_BITS', 'ACCUM_GREEN_BITS', 'ACCUM_RED_BITS', 'ALPHA_BITS', 'ANY_RELEASE_BEHAVIOR', 'API_UNAVAILABLE', 'ARROW_CURSOR', 'AUTO_ICONIFY', 'AUX_BUFFERS', 'BLUE_BITS', 'CENTER_CURSOR', 'CLIENT_API', 'COCOA_CHDIR_RESOURCES', 'COCOA_FRAME_NAME', 'COCOA_GRAPHICS_SWITCHING', 'COCOA_MENUBAR', 'COCOA_RETINA_FRAMEBUFFER', 'CONNECTED', 'CONTEXT_CREATION_API', 'CONTEXT_NO_ERROR', 'CONTEXT_RELEASE_BEHAVIOR', 'CONTEXT_REVISION', 'CONTEXT_ROBUSTNESS', 'CONTEXT_VERSION_MAJOR', 'CONTEXT_VERSION_MINOR', 'CROSSHAIR_CURSOR', 'CURSOR', 'CURSOR_DISABLED', 'CURSOR_HIDDEN', 'CURSOR_NORMAL', 'CreateCursor', 'CreateStandardCursor', 'CreateWindow', 'Cursor', 'DECORATED', 'DEPTH_BITS', 'DISCONNECTED', 'DONT_CARE', 'DOUBLEBUFFER', 'DefaultWindowHints', 'DestroyCursor', 'DestroyWindow', 'EGL_CONTEXT_API', 'ExtensionSupported', 'FLOATING', 'FOCUSED', 'FOCUS_ON_SHOW', 'FORMAT_UNAVAILABLE', 'FocusWindow', 'GAMEPAD_AXIS_LEFT_TRIGGER', 'GAMEPAD_AXIS_LEFT_X', 'GAMEPAD_AXIS_LEFT_Y', 'GAMEPAD_AXIS_RIGHT_TRIGGER', 'GAMEPAD_AXIS_RIGHT_X', 'GAMEPAD_AXIS_RIGHT_Y', 'GAMEPAD_BUTTON_A', 'GAMEPAD_BUTTON_B', 'GAMEPAD_BUTTON_BACK', 'GAMEPAD_BUTTON_CIRCLE', 'GAMEPAD_BUTTON_CROSS', 'GAMEPAD_BUTTON_DPAD_DOWN', 'GAMEPAD_BUTTON_DPAD_LEFT', 'GAMEPAD_BUTTON_DPAD_RIGHT', 'GAMEPAD_BUTTON_DPAD_UP', 'GAMEPAD_BUTTON_GUIDE', 'GAMEPAD_BUTTON_LEFT_BUMPER', 'GAMEPAD_BUTTON_LEFT_THUMB', 'GAMEPAD_BUTTON_RIGHT_BUMPER', 'GAMEPAD_BUTTON_RIGHT_THUMB', 'GAMEPAD_BUTTON_SQUARE', 'GAMEPAD_BUTTON_START', 'GAMEPAD_BUTTON_TRIANGLE', 'GAMEPAD_BUTTON_X', 'GAMEPAD_BUTTON_Y', 'GREEN_BITS', 'Gamepadstate', 'Gammaramp', 'GetClipboardString', 'GetCurrentContext', 'GetCursorPos', 'GetError', 'GetFramebufferSize', 'GetGamepadName', 'GetGamepadState', 'GetGammaRamp', 'GetInputMode', 'GetJoyStickGUID', 'GetJoystickAxes', 'GetJoystickButtons', 'GetJoystickHats', 'GetJoystickname', 'GetKey', 'GetKeyName', 'GetKeyScancode', 'GetMonitorContentScale', 'GetMonitorName', 'GetMonitorPhysicalSize', 'GetMonitorPos', 'GetMonitorWorkarea', 'GetMonitors', 'GetMouseButton', 'GetPrimaryMonitor', 'GetTime', 'GetTimerFrequency', 'GetTimerValue', 'GetVersion', 'GetVersionString', 'GetVideoMode', 'GetVideoModes', 'GetWindowAttrib', 'GetWindowContentScale', 'GetWindowFrameSize', 'GetWindowMonitor', 'GetWindowOpacity', 'GetWindowPos', 'GetWindowSize', 'HAND_CURSOR', 'HAT_CENTERED', 'HAT_DOWN', 'HAT_LEFT', 'HAT_LEFT_DOWN', 'HAT_LEFT_UP', 'HAT_RIGHT', 'HAT_RIGHT_DOWN', 'HAT_RIGHT_UP', 'HAT_UP', 'HOVERED', 'HRESIZE_CURSOR', 'HideWindow', 'IBEAM_CURSOR', 'ICONIFIED', 'INVALID_ENUM', 'INVALID_VALUE', 'IconifyWindow', 'Image', 'Init', 'InitHint', 'JOYSTICK_1', 'JOYSTICK_10', 'JOYSTICK_11', 'JOYSTICK_12', 'JOYSTICK_13', 'JOYSTICK_14', 'JOYSTICK_15', 'JOYSTICK_16', 'JOYSTICK_2', 'JOYSTICK_3', 'JOYSTICK_4', 'JOYSTICK_5', 'JOYSTICK_6', 'JOYSTICK_7', 'JOYSTICK_8', 'JOYSTICK_9', 'JOYSTICK_HAT_BUTTONS', 'JoystickIsGamepad', 'JoystickPresent', 'KEY_0', 'KEY_1', 'KEY_2', 'KEY_3', 'KEY_4', 'KEY_5', 'KEY_6', 'KEY_7', 'KEY_8', 'KEY_9', 'KEY_A', 'KEY_APOSTROPHE', 'KEY_B', 'KEY_BACKSLASH', 'KEY_BACKSPACE', 'KEY_C', 'KEY_CAPS_LOCK', 'KEY_COMMA', 'KEY_D', 'KEY_DELETE', 'KEY_DOWN', 'KEY_E', 'KEY_END', 'KEY_ENTER', 'KEY_EQUAL', 'KEY_ESCAPE', 'KEY_F', 'KEY_F1', 'KEY_F10', 'KEY_F11', 'KEY_F12', 'KEY_F13', 'KEY_F14', 'KEY_F15', 'KEY_F16', 'KEY_F17', 'KEY_F18', 'KEY_F19', 'KEY_F2', 'KEY_F20', 'KEY_F21', 'KEY_F22', 'KEY_F23', 'KEY_F24', 'KEY_F25', 'KEY_F3', 'KEY_F4', 'KEY_F5', 'KEY_F6', 'KEY_F7', 'KEY_F8', 'KEY_F9', 'KEY_G', 'KEY_GRAVE_ACCENT', 'KEY_H', 'KEY_HOME', 'KEY_I', 'KEY_INSERT', 'KEY_J', 'KEY_K', 'KEY_KP_0', 'KEY_KP_1', 'KEY_KP_2', 'KEY_KP_3', 'KEY_KP_4', 'KEY_KP_5', 'KEY_KP_6', 'KEY_KP_7', 'KEY_KP_8', 'KEY_KP_9', 'KEY_KP_ADD', 'KEY_KP_DECIMAL', 'KEY_KP_DIVIDE', 'KEY_KP_ENTER', 'KEY_KP_EQUAL', 'KEY_KP_MULTIPLY', 'KEY_KP_SUBTRACT', 'KEY_L', 'KEY_LEFT', 'KEY_LEFT_ALT', 'KEY_LEFT_BRACKET', 'KEY_LEFT_CONTROL', 'KEY_LEFT_SHIFT', 'KEY_LEFT_SUPER', 'KEY_M', 'KEY_MENU', 'KEY_MINUS', 'KEY_N', 'KEY_NUM_LOCK', 'KEY_O', 'KEY_P', 'KEY_PAGE_DOWN', 'KEY_PAGE_UP', 'KEY_PAUSE', 'KEY_PERIOD', 'KEY_PRINT_SCREEN', 'KEY_Q', 'KEY_R', 'KEY_RIGHT', 'KEY_RIGHT_ALT', 'KEY_RIGHT_BRACKET', 'KEY_RIGHT_CONTROL', 'KEY_RIGHT_SHIFT', 'KEY_RIGHT_SUPER', 'KEY_S', 'KEY_SCROLL_LOCK', 'KEY_SEMICOLON', 'KEY_SLASH', 'KEY_SPACE', 'KEY_T', 'KEY_TAB', 'KEY_U', 'KEY_UNKNOWN', 'KEY_UP', 'KEY_V', 'KEY_W', 'KEY_WORLD_1', 'KEY_WORLD_2', 'KEY_X', 'KEY_Y', 'KEY_Z', 'LOCK_KEY_MODS', 'LOSE_CONTEXT_ON_RESET', 'ListWrapperF', 'ListWrapperMonitor', 'ListWrapperStr', 'ListWrapperUC', 'ListWrapperUS', 'ListWrapperVidmode', 'MAXIMIZED', 'MOD_ALT', 'MOD_CAPS_LOCK', 'MOD_CONTROL', 'MOD_NUM_LOCK', 'MOD_SHIFT', 'MOD_SUPER', 'MOUSE_BUTTON_1', 'MOUSE_BUTTON_2', 'MOUSE_BUTTON_3', 'MOUSE_BUTTON_4', 'MOUSE_BUTTON_5', 'MOUSE_BUTTON_6', 'MOUSE_BUTTON_7', 'MOUSE_BUTTON_8', 'MOUSE_BUTTON_LEFT', 'MOUSE_BUTTON_MIDDLE', 'MOUSE_BUTTON_RIGHT', 'MakeContextCurrent', 'MaximizeWindow', 'Monitor', 'NATIVE_CONTEXT_API', 'NOT_INITIALIZED', 'NO_API', 'NO_CURRENT_CONTEXT', 'NO_ERROR', 'NO_RESET_NOTIFICATION', 'NO_ROBUSTNESS', 'NO_WINDOW_CONTEXT', 'OPENGL_ANY_PROFILE', 'OPENGL_API', 'OPENGL_COMPAT_PROFILE', 'OPENGL_CORE_PROFILE', 'OPENGL_DEBUG_CONTEXT', 'OPENGL_ES_API', 'OPENGL_FORWARD_COMPAT', 'OPENGL_PROFILE', 'OSMESA_CONTEXT_API', 'OUT_OF_MEMORY', 'PLATFORM_ERROR', 'PRESS', 'PollEvents', 'PostEmptyEvent', 'RAW_MOUSE_MOTION', 'RED_BITS', 'REFRESH_RATE', 'RELEASE', 'RELEASE_BEHAVIOR_FLUSH', 'RELEASE_BEHAVIOR_NONE', 'REPEAT', 'RESIZABLE', 'RawMouseMotionSupported', 'RequestWindowAttention', 'RestoreWindow', 'SAMPLES', 'SCALE_TO_MONITOR', 'SRGB_CAPABLE', 'STENCIL_BITS', 'STEREO', 'STICKY_KEYS', 'STICKY_MOUSE_BUTTONS', 'SetCharCallback', 'SetCharModsCallback', 'SetClipboardString', 'SetCursor', 'SetCursorEnterCallback', 'SetCursorPos', 'SetCursorPosCallback', 'SetDropCallback', 'SetErrorCallback', 'SetFramebufferSizeCallback', 'SetGamma', 'SetGammaRamp', 'SetInputMode', 'SetJoystickCallback', 'SetKeyCallback', 'SetMonitorCallback', 'SetMouseButtonCallback', 'SetScrollCallback', 'SetTime', 'SetWindowAspectRatio', 'SetWindowAttrib', 'SetWindowCloseCallback', 'SetWindowContentScaleCallback', 'SetWindowFocusCallback', 'SetWindowIcon', 'SetWindowIconifyCallback', 'SetWindowMaximizeCallback', 'SetWindowMonitor', 'SetWindowPos', 'SetWindowPosCallback', 'SetWindowRefreshCallback', 'SetWindowShouldClose', 'SetWindowSize', 'SetWindowSizeCallback', 'SetWindowSizeLimits', 'SetWindowTitle', 'ShowWindow', 'SwapBuffers', 'SwapInterval', 'TRANSPARENT_FRAMEBUFFER', 'Terminate', 'UpdateGamepadMappings', 'VERSION_MAJOR', 'VERSION_MINOR', 'VERSION_REVISION', 'VERSION_UNAVAILABLE', 'VISIBLE', 'VRESIZE_CURSOR', 'Vidmode', 'VulkanSupported', 'WaitEvents', 'WaitEventsTimeout', 'Window', 'WindowHint', 'WindowHintString', 'WindowShouldClose', 'X11_CLASS_NAME', 'X11_INSTANCE_NAME', 'setWindowOpacity']
class Cursor:
    pass
class Gamepadstate:
    @property
    def axes(self) -> ListWrapperF:
        ...
    @property
    def buttons(self) -> ListWrapperUC:
        ...
class Gammaramp:
    @property
    def blue(self) -> ListWrapperUS:
        ...
    @property
    def greeen(self) -> ListWrapperUS:
        ...
    @property
    def red(self) -> ListWrapperUS:
        ...
class Image:
    @property
    def height(self) -> int:
        ...
    @property
    def pixels(self) -> ListWrapperUC:
        ...
    @property
    def width(self) -> int:
        ...
class ListWrapperF:
    def __getitem__(self, arg0: int) -> float:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class ListWrapperMonitor:
    def __getitem__(self, arg0: int) -> Monitor:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class ListWrapperStr:
    def __getitem__(self, arg0: int) -> str:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class ListWrapperUC:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class ListWrapperUS:
    def __getitem__(self, arg0: int) -> int:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class ListWrapperVidmode:
    def __getitem__(self, arg0: int) -> Vidmode:
        ...
    def __iter__(self) -> typing.Iterator:
        ...
    def __len__(self) -> int:
        ...
class Monitor:
    pass
class Vidmode:
    @property
    def blueBits(self) -> int:
        ...
    @property
    def greenBits(self) -> int:
        ...
    @property
    def height(self) -> int:
        ...
    @property
    def redBits(self) -> int:
        ...
    @property
    def refreshRate(self) -> int:
        ...
    @property
    def width(self) -> int:
        ...
class Window:
    pass
def CreateCursor(image: Image, xhot: int, yhot: int) -> Cursor:
    ...
def CreateStandardCursor(shape: int) -> Cursor:
    ...
def CreateWindow(width: int, height: int, title: str, monitor: Monitor = None, share: Window = None) -> Window:
    ...
def DefaultWindowHints() -> None:
    ...
def DestroyCursor(cursor: Cursor) -> None:
    ...
def DestroyWindow(window: Window) -> None:
    ...
def ExtensionSupported(extension: str) -> int:
    ...
def FocusWindow(window: Window) -> None:
    ...
def GetClipboardString(window: Window) -> str:
    ...
def GetCurrentContext() -> Window:
    ...
def GetCursorPos(window: Window) -> tuple:
    ...
def GetError() -> tuple:
    ...
def GetFramebufferSize(window: Window) -> tuple:
    ...
def GetGamepadName(jid: int) -> str:
    ...
def GetGamepadState(state: int) -> str:
    """
    jid_a
    """
def GetGammaRamp(monitor: Monitor) -> Gammaramp:
    ...
def GetInputMode(window: Window, mode: int) -> int:
    ...
def GetJoyStickGUID(jid: int) -> str:
    ...
def GetJoystickAxes(jid: int) -> ListWrapperF:
    ...
def GetJoystickButtons(jid: int) -> ListWrapperUC:
    ...
def GetJoystickHats(jid: int) -> ListWrapperUC:
    ...
def GetJoystickname(jid: int) -> str:
    ...
def GetKey(window: Window, key: int) -> int:
    ...
def GetKeyName(key: int, scancode: int) -> str:
    ...
def GetKeyScancode(key: int) -> int:
    ...
def GetMonitorContentScale(monitor: Monitor) -> tuple:
    ...
def GetMonitorName(monitor: Monitor) -> str:
    ...
def GetMonitorPhysicalSize(monitor: Monitor) -> tuple:
    ...
def GetMonitorPos(monitor: Monitor) -> tuple:
    ...
def GetMonitorWorkarea(monitor: Monitor) -> tuple:
    ...
def GetMonitors() -> ListWrapperMonitor:
    ...
def GetMouseButton(window: Window, button: int) -> int:
    ...
def GetPrimaryMonitor() -> Monitor:
    ...
def GetTime() -> float:
    ...
def GetTimerFrequency() -> int:
    ...
def GetTimerValue() -> int:
    ...
def GetVersion() -> None:
    ...
def GetVersionString() -> str:
    ...
def GetVideoMode(monitor: Monitor) -> Vidmode:
    ...
def GetVideoModes(monitor: Monitor) -> ListWrapperVidmode:
    ...
def GetWindowAttrib(window: Window, attrib: int) -> int:
    ...
def GetWindowContentScale(window: Window) -> tuple:
    ...
def GetWindowFrameSize(window: Window) -> tuple:
    ...
def GetWindowMonitor(window: Window) -> Monitor:
    ...
def GetWindowOpacity(window: Window) -> float:
    ...
def GetWindowPos(window: Window) -> tuple:
    ...
def GetWindowSize(window: Window) -> tuple:
    ...
def HideWindow(window: Window) -> None:
    ...
def IconifyWindow(window: Window) -> None:
    ...
def Init() -> int:
    ...
def InitHint(hint: int, value: int) -> None:
    ...
def JoystickIsGamepad(jid: int) -> bool:
    ...
def JoystickPresent(jid: int) -> bool:
    ...
def MakeContextCurrent(window: Window) -> None:
    ...
def MaximizeWindow(window: Window) -> None:
    ...
def PollEvents() -> None:
    ...
def PostEmptyEvent() -> None:
    ...
def RawMouseMotionSupported() -> bool:
    ...
def RequestWindowAttention(window: Window) -> None:
    ...
def RestoreWindow(window: Window) -> None:
    ...
def SetCharCallback(window: Window, callback: typing.Callable[[Window, int], None]) -> typing.Callable[[Window, int], None]:
    ...
def SetCharModsCallback(window: Window, callback: typing.Callable[[Window, int, int], None]) -> typing.Callable[[Window, int, int], None]:
    ...
def SetClipboardString(window: Window, string: str) -> None:
    ...
def SetCursor(window: Window, cursor: Cursor) -> None:
    ...
def SetCursorEnterCallback(window: Window, callback: typing.Callable[[Window, int], None]) -> typing.Callable[[Window, int], None]:
    ...
def SetCursorPos(window: Window, xpos: float, ypos: float) -> None:
    ...
def SetCursorPosCallback(window: Window, callback: typing.Callable[[Window, float, float], None]) -> typing.Callable[[Window, float, float], None]:
    ...
def SetDropCallback(window: Window, callback: typing.Callable[[Window, ListWrapperStr], None]) -> typing.Callable[[Window, ListWrapperStr], None]:
    ...
def SetErrorCallback(callback: typing.Callable[[int, str], None]) -> typing.Callable[[int, str], None]:
    ...
def SetFramebufferSizeCallback(window: Window, callback: typing.Callable[[Window, int, int], None]) -> typing.Callable[[Window, int, int], None]:
    ...
def SetGamma(monitor: Monitor, gamma: float) -> None:
    ...
def SetGammaRamp(monitor: Monitor, ramp: Gammaramp) -> None:
    ...
def SetInputMode(window: Window, mode: int, value: int) -> None:
    ...
def SetJoystickCallback(callback: typing.Callable[[int, int], None]) -> typing.Callable[[int, int], None]:
    ...
def SetKeyCallback(window: Window, callback: typing.Callable[[Window, int, int, int, int], None]) -> typing.Callable[[Window, int, int, int, int], None]:
    ...
def SetMonitorCallback(arg0: typing.Callable[[Monitor, int], None]) -> typing.Callable[[Monitor, int], None]:
    ...
def SetMouseButtonCallback(window: Window, callback: typing.Callable[[Window, int, int, int], None]) -> typing.Callable[[Window, int, int, int], None]:
    ...
def SetScrollCallback(window: Window, callback: typing.Callable[[Window, float, float], None]) -> typing.Callable[[Window, float, float], None]:
    ...
def SetTime(time: float) -> None:
    ...
def SetWindowAspectRatio(window: Window, numer: int, denom: int) -> None:
    ...
def SetWindowAttrib(window: Window, attrib: int, value: int) -> None:
    ...
def SetWindowCloseCallback(window: Window, callback: typing.Callable[[Window], None]) -> typing.Callable[[Window], None]:
    ...
def SetWindowContentScaleCallback(window: Window, callback: typing.Callable[[Window, float, float], None]) -> typing.Callable[[Window, float, float], None]:
    ...
def SetWindowFocusCallback(window: Window, callback: typing.Callable[[Window, int], None]) -> typing.Callable[[Window, int], None]:
    ...
def SetWindowIcon(window: Window, image: Image) -> None:
    ...
def SetWindowIconifyCallback(window: Window, callback: typing.Callable[[Window, int], None]) -> typing.Callable[[Window, int], None]:
    ...
def SetWindowMaximizeCallback(window: Window, callback: typing.Callable[[Window, int], None]) -> typing.Callable[[Window, int], None]:
    ...
def SetWindowMonitor(window: Window, monitor: Monitor, xpos: int, ypos: int, width: int, height: int, refreshRate: int) -> None:
    ...
def SetWindowPos(window: Window, xpos: int, ypos: int) -> None:
    ...
def SetWindowPosCallback(window: Window, callback: typing.Callable[[Window, int, int], None]) -> typing.Callable[[Window, int, int], None]:
    ...
def SetWindowRefreshCallback(window: Window, callback: typing.Callable[[Window], None]) -> typing.Callable[[Window], None]:
    ...
def SetWindowShouldClose(window: Window, value: int) -> None:
    ...
def SetWindowSize(window: Window, width: int, height: int) -> None:
    ...
def SetWindowSizeCallback(window: Window, callback: typing.Callable[[Window, int, int], None]) -> typing.Callable[[Window, int, int], None]:
    ...
def SetWindowSizeLimits(window: Window, minWidth: int, minHeight: int, maxWidth: int, maxHeight: int) -> None:
    ...
def SetWindowTitle(window: Window, title: str) -> None:
    ...
def ShowWindow(window: Window) -> None:
    ...
def SwapBuffers(window: Window) -> None:
    ...
def SwapInterval(interval: int) -> None:
    ...
def Terminate() -> None:
    ...
def UpdateGamepadMappings(string: str) -> int:
    ...
def VulkanSupported() -> int:
    ...
def WaitEvents() -> None:
    ...
def WaitEventsTimeout(timeout: float) -> None:
    ...
def WindowHint(hint: int, value: int) -> None:
    ...
def WindowHintString(hint: int, value: str) -> None:
    ...
def WindowShouldClose(window: Window) -> bool:
    ...
def setWindowOpacity(window: Window, opacity: float) -> None:
    ...
ACCUM_ALPHA_BITS: int = 135178
ACCUM_BLUE_BITS: int = 135177
ACCUM_GREEN_BITS: int = 135176
ACCUM_RED_BITS: int = 135175
ALPHA_BITS: int = 135172
ANY_RELEASE_BEHAVIOR: int = 0
API_UNAVAILABLE: int = 65542
ARROW_CURSOR: int = 221185
AUTO_ICONIFY: int = 131078
AUX_BUFFERS: int = 135179
BLUE_BITS: int = 135171
CENTER_CURSOR: int = 131081
CLIENT_API: int = 139265
COCOA_CHDIR_RESOURCES: int = 331777
COCOA_FRAME_NAME: int = 143362
COCOA_GRAPHICS_SWITCHING: int = 143363
COCOA_MENUBAR: int = 331778
COCOA_RETINA_FRAMEBUFFER: int = 143361
CONNECTED: int = 262145
CONTEXT_CREATION_API: int = 139275
CONTEXT_NO_ERROR: int = 139274
CONTEXT_RELEASE_BEHAVIOR: int = 139273
CONTEXT_REVISION: int = 139268
CONTEXT_ROBUSTNESS: int = 139269
CONTEXT_VERSION_MAJOR: int = 139266
CONTEXT_VERSION_MINOR: int = 139267
CROSSHAIR_CURSOR: int = 221187
CURSOR: int = 208897
CURSOR_DISABLED: int = 212995
CURSOR_HIDDEN: int = 212994
CURSOR_NORMAL: int = 212993
DECORATED: int = 131077
DEPTH_BITS: int = 135173
DISCONNECTED: int = 262146
DONT_CARE: int = -1
DOUBLEBUFFER: int = 135184
EGL_CONTEXT_API: int = 221186
FLOATING: int = 131079
FOCUSED: int = 131073
FOCUS_ON_SHOW: int = 131084
FORMAT_UNAVAILABLE: int = 65545
GAMEPAD_AXIS_LEFT_TRIGGER: int = 4
GAMEPAD_AXIS_LEFT_X: int = 0
GAMEPAD_AXIS_LEFT_Y: int = 1
GAMEPAD_AXIS_RIGHT_TRIGGER: int = 5
GAMEPAD_AXIS_RIGHT_X: int = 2
GAMEPAD_AXIS_RIGHT_Y: int = 3
GAMEPAD_BUTTON_A: int = 0
GAMEPAD_BUTTON_B: int = 1
GAMEPAD_BUTTON_BACK: int = 6
GAMEPAD_BUTTON_CIRCLE: int = 1
GAMEPAD_BUTTON_CROSS: int = 0
GAMEPAD_BUTTON_DPAD_DOWN: int = 13
GAMEPAD_BUTTON_DPAD_LEFT: int = 14
GAMEPAD_BUTTON_DPAD_RIGHT: int = 12
GAMEPAD_BUTTON_DPAD_UP: int = 11
GAMEPAD_BUTTON_GUIDE: int = 8
GAMEPAD_BUTTON_LEFT_BUMPER: int = 4
GAMEPAD_BUTTON_LEFT_THUMB: int = 9
GAMEPAD_BUTTON_RIGHT_BUMPER: int = 5
GAMEPAD_BUTTON_RIGHT_THUMB: int = 10
GAMEPAD_BUTTON_SQUARE: int = 2
GAMEPAD_BUTTON_START: int = 7
GAMEPAD_BUTTON_TRIANGLE: int = 3
GAMEPAD_BUTTON_X: int = 2
GAMEPAD_BUTTON_Y: int = 3
GREEN_BITS: int = 135170
HAND_CURSOR: int = 221188
HAT_CENTERED: int = 0
HAT_DOWN: int = 4
HAT_LEFT: int = 8
HAT_LEFT_DOWN: int = 12
HAT_LEFT_UP: int = 9
HAT_RIGHT: int = 2
HAT_RIGHT_DOWN: int = 6
HAT_RIGHT_UP: int = 3
HAT_UP: int = 1
HOVERED: int = 131083
HRESIZE_CURSOR: int = 221189
IBEAM_CURSOR: int = 221186
ICONIFIED: int = 131074
INVALID_ENUM: int = 65539
INVALID_VALUE: int = 65540
JOYSTICK_1: int = 0
JOYSTICK_10: int = 9
JOYSTICK_11: int = 10
JOYSTICK_12: int = 11
JOYSTICK_13: int = 12
JOYSTICK_14: int = 13
JOYSTICK_15: int = 14
JOYSTICK_16: int = 15
JOYSTICK_2: int = 1
JOYSTICK_3: int = 2
JOYSTICK_4: int = 3
JOYSTICK_5: int = 4
JOYSTICK_6: int = 5
JOYSTICK_7: int = 6
JOYSTICK_8: int = 7
JOYSTICK_9: int = 8
JOYSTICK_HAT_BUTTONS: int = 327681
KEY_0: int = 48
KEY_1: int = 49
KEY_2: int = 50
KEY_3: int = 51
KEY_4: int = 52
KEY_5: int = 53
KEY_6: int = 54
KEY_7: int = 55
KEY_8: int = 56
KEY_9: int = 57
KEY_A: int = 65
KEY_APOSTROPHE: int = 39
KEY_B: int = 66
KEY_BACKSLASH: int = 92
KEY_BACKSPACE: int = 259
KEY_C: int = 67
KEY_CAPS_LOCK: int = 280
KEY_COMMA: int = 44
KEY_D: int = 68
KEY_DELETE: int = 261
KEY_DOWN: int = 264
KEY_E: int = 69
KEY_END: int = 269
KEY_ENTER: int = 257
KEY_EQUAL: int = 61
KEY_ESCAPE: int = 256
KEY_F: int = 70
KEY_F1: int = 290
KEY_F10: int = 299
KEY_F11: int = 300
KEY_F12: int = 301
KEY_F13: int = 302
KEY_F14: int = 303
KEY_F15: int = 304
KEY_F16: int = 305
KEY_F17: int = 306
KEY_F18: int = 307
KEY_F19: int = 308
KEY_F2: int = 291
KEY_F20: int = 309
KEY_F21: int = 310
KEY_F22: int = 311
KEY_F23: int = 312
KEY_F24: int = 313
KEY_F25: int = 314
KEY_F3: int = 292
KEY_F4: int = 293
KEY_F5: int = 294
KEY_F6: int = 295
KEY_F7: int = 296
KEY_F8: int = 297
KEY_F9: int = 298
KEY_G: int = 71
KEY_GRAVE_ACCENT: int = 96
KEY_H: int = 72
KEY_HOME: int = 268
KEY_I: int = 73
KEY_INSERT: int = 260
KEY_J: int = 74
KEY_K: int = 75
KEY_KP_0: int = 320
KEY_KP_1: int = 321
KEY_KP_2: int = 322
KEY_KP_3: int = 323
KEY_KP_4: int = 324
KEY_KP_5: int = 325
KEY_KP_6: int = 326
KEY_KP_7: int = 327
KEY_KP_8: int = 328
KEY_KP_9: int = 329
KEY_KP_ADD: int = 334
KEY_KP_DECIMAL: int = 330
KEY_KP_DIVIDE: int = 331
KEY_KP_ENTER: int = 335
KEY_KP_EQUAL: int = 336
KEY_KP_MULTIPLY: int = 332
KEY_KP_SUBTRACT: int = 333
KEY_L: int = 76
KEY_LEFT: int = 263
KEY_LEFT_ALT: int = 342
KEY_LEFT_BRACKET: int = 91
KEY_LEFT_CONTROL: int = 341
KEY_LEFT_SHIFT: int = 340
KEY_LEFT_SUPER: int = 343
KEY_M: int = 77
KEY_MENU: int = 348
KEY_MINUS: int = 45
KEY_N: int = 78
KEY_NUM_LOCK: int = 282
KEY_O: int = 79
KEY_P: int = 80
KEY_PAGE_DOWN: int = 267
KEY_PAGE_UP: int = 266
KEY_PAUSE: int = 284
KEY_PERIOD: int = 46
KEY_PRINT_SCREEN: int = 283
KEY_Q: int = 81
KEY_R: int = 82
KEY_RIGHT: int = 262
KEY_RIGHT_ALT: int = 346
KEY_RIGHT_BRACKET: int = 93
KEY_RIGHT_CONTROL: int = 345
KEY_RIGHT_SHIFT: int = 344
KEY_RIGHT_SUPER: int = 347
KEY_S: int = 83
KEY_SCROLL_LOCK: int = 281
KEY_SEMICOLON: int = 59
KEY_SLASH: int = 47
KEY_SPACE: int = 32
KEY_T: int = 84
KEY_TAB: int = 258
KEY_U: int = 85
KEY_UNKNOWN: int = -1
KEY_UP: int = 265
KEY_V: int = 86
KEY_W: int = 87
KEY_WORLD_1: int = 161
KEY_WORLD_2: int = 162
KEY_X: int = 88
KEY_Y: int = 89
KEY_Z: int = 90
LOCK_KEY_MODS: int = 208900
LOSE_CONTEXT_ON_RESET: int = 200706
MAXIMIZED: int = 131080
MOD_ALT: int = 4
MOD_CAPS_LOCK: int = 16
MOD_CONTROL: int = 2
MOD_NUM_LOCK: int = 32
MOD_SHIFT: int = 1
MOD_SUPER: int = 8
MOUSE_BUTTON_1: int = 0
MOUSE_BUTTON_2: int = 1
MOUSE_BUTTON_3: int = 2
MOUSE_BUTTON_4: int = 3
MOUSE_BUTTON_5: int = 4
MOUSE_BUTTON_6: int = 5
MOUSE_BUTTON_7: int = 6
MOUSE_BUTTON_8: int = 7
MOUSE_BUTTON_LEFT: int = 0
MOUSE_BUTTON_MIDDLE: int = 2
MOUSE_BUTTON_RIGHT: int = 1
NATIVE_CONTEXT_API: int = 221185
NOT_INITIALIZED: int = 65537
NO_API: int = 0
NO_CURRENT_CONTEXT: int = 65538
NO_ERROR: int = 0
NO_RESET_NOTIFICATION: int = 200705
NO_ROBUSTNESS: int = 0
NO_WINDOW_CONTEXT: int = 65546
OPENGL_ANY_PROFILE: int = 0
OPENGL_API: int = 196609
OPENGL_COMPAT_PROFILE: int = 204802
OPENGL_CORE_PROFILE: int = 204801
OPENGL_DEBUG_CONTEXT: int = 139271
OPENGL_ES_API: int = 196610
OPENGL_FORWARD_COMPAT: int = 139270
OPENGL_PROFILE: int = 139272
OSMESA_CONTEXT_API: int = 221187
OUT_OF_MEMORY: int = 65541
PLATFORM_ERROR: int = 65544
PRESS: int = 1
RAW_MOUSE_MOTION: int = 208901
RED_BITS: int = 135169
REFRESH_RATE: int = 135183
RELEASE: int = 0
RELEASE_BEHAVIOR_FLUSH: int = 217089
RELEASE_BEHAVIOR_NONE: int = 217090
REPEAT: int = 2
RESIZABLE: int = 131075
SAMPLES: int = 135181
SCALE_TO_MONITOR: int = 139276
SRGB_CAPABLE: int = 135182
STENCIL_BITS: int = 135174
STEREO: int = 135180
STICKY_KEYS: int = 208898
STICKY_MOUSE_BUTTONS: int = 208899
TRANSPARENT_FRAMEBUFFER: int = 131082
VERSION_MAJOR: int = 3
VERSION_MINOR: int = 4
VERSION_REVISION: int = 0
VERSION_UNAVAILABLE: int = 65543
VISIBLE: int = 131076
VRESIZE_CURSOR: int = 221190
X11_CLASS_NAME: int = 147457
X11_INSTANCE_NAME: int = 147458
