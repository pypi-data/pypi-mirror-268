import signal
import time
from tooldelta import builtins, urlmethod
from tooldelta.frame import Frame
from tooldelta.frame import GameCtrl
from tooldelta.basic_mods import os, traceback
from tooldelta.color_print import Print
from tooldelta.plugin_load.PluginGroup import plugin_group
from tooldelta.plugin_load.injected_plugin import movent

frame = Frame()
def signal_handler(*arg):
    # 排除信号中断
    pass
signal.signal(signal.SIGINT, signal_handler)

def start_tool_delta():
    # 初始化系统
    plugin_group.set_frame(frame)
    try:
        frame.welcome()
        urlmethod.check_update()
        frame.basic_operation()
        frame.loadConfiguration()
        game_control = GameCtrl(frame)
        frame.set_game_control(game_control)
        frame.set_plugin_group(plugin_group)
        movent.set_frame(frame)
        plugin_group.read_all_plugins()
        frame.plugin_load_finished(plugin_group)
        builtins.tmpjson_save_thread()
        frame.launcher.listen_launched(game_control.Inject)
        game_control.set_listen_packets()
        # TODO: 自动更新需要时间间隔
        raise frame.launcher.launch()
    except (KeyboardInterrupt, SystemExit):
        pass
    except:
        Print.print_err("ToolDelta 运行过程中出现问题: " + traceback.format_exc())


def safe_jump(*, out_task=True, exit_directly=True):
    if out_task:
        frame.system_exit()
    frame.safelyExit()
    if exit_directly:
        for _ in range(2, 0, -1):
            Print.print_war(f"{_}秒后强制退出...", end="\r")
            time.sleep(1)
        Print.print_war("0秒后强制退出...", end="\r")
        Print.print_suc("ToolDelta 已退出.")
        os._exit(0)
    Print.print_suc("ToolDelta 已退出.")
