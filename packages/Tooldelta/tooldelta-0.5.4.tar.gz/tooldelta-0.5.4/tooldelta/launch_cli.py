"""客户端启动器框架"""

import os
import threading
import shlex
import uuid
import time
import json
import random
import subprocess
import platform
from typing import Callable, Optional
import requests
import ujson

import tooldelta
from tooldelta import constants
from .cfg import Cfg
from .fb_conn import fbconn
from .builtins import Builtins
from .color_print import Print
from .basic_mods import socketio
from .sys_args import sys_args_to_dict
from .packets import Packet_CommandOutput, PacketIDS
from .urlmethod import download_file_singlethreaded, get_free_port

Config = Cfg()


class SysStatus:
    """系统状态码

    LOADING: 启动器正在加载
    LAUNCHING: 启动器正在启动
    RUNNING: 启动器正在运行
    NORMAL_EXIT: 正常退出
    FB_LAUNCH_EXC: FastBuilder 启动异常
    CRASHED_EXIT: 启动器崩溃退出
    NEED_RESTART: 需要重启
    """
    LOADING = 100
    LAUNCHING = 101
    RUNNING = 102
    NORMAL_EXIT = 103
    FB_LAUNCH_EXC = 104
    CRASHED_EXIT = 105
    NEED_RESTART = 106
    launch_type = "None"


class StandardFrame:
    """提供了标准的启动器框架, 作为 ToolDelta 和游戏交互的接口"""
    launch_type = "Original"

    def __init__(self, serverNumber, password, fbToken, auth_server_url):
        self.serverNumber = serverNumber
        self.serverPassword = password
        self.fbToken = fbToken
        self.auth_server = auth_server_url
        self.system_type = platform.uname().system
        self.inject_events = []
        self.packet_handler: Callable | None = lambda pckType, pck: None
        self.need_listen_packets = {9, 63, 79}
        self._launcher_listener = None
        self.exit_event = threading.Event()
        self.status = SysStatus.LOADING

    def add_listen_packets(self, *pcks: int):
        for i in pcks:
            self.need_listen_packets.add(i)

    @staticmethod
    def launch():
        raise Exception("Cannot launch this launcher")

    def listen_launched(self, cb):
        self._launcher_listener = cb

    @staticmethod
    def get_players_and_uuids():
        return None

    @staticmethod
    def get_bot_name():
        return None

    def update_status(self, new_status):
        self.status = new_status
        if new_status == SysStatus.NORMAL_EXIT:
            tooldelta.safe_jump(out_task=True)
            self.exit_event.set()  # 设置事件，触发等待结束
        if new_status == SysStatus.CRASHED_EXIT:
            tooldelta.safe_jump(out_task=False)
            self.exit_event.set()

    get_all_players = None

    @staticmethod
    def sendcmd(cmd: str, waitForResp: bool = False, timeout: int | float = 30) -> Optional[Packet_CommandOutput]:
        ...

    @staticmethod
    def sendwscmd(cmd: str, waitForResp: bool = False, timeout: int | float = 30) -> Optional[Packet_CommandOutput]:
        ...

    @staticmethod
    def sendwocmd(cmd: str) -> None:
        ...

    @staticmethod
    def sendfbcmd(cmd: str) -> None:
        ...

    @staticmethod
    def sendPacket(pckID: int, pck: str) -> None:
        ...

    @staticmethod
    def sendPacketJson(pckID: int, pck: str) -> None:
        ...

    @staticmethod
    def is_op(player: str) -> bool:
        ...


class FrameFBConn(StandardFrame):
    # 使用原生 FastBuilder External 连接
    cmds_reqs = []
    cmds_resp = {}

    def __init__(self, serverNumber, password, fbToken, auth_server):
        super().__init__(serverNumber, password, fbToken, auth_server)
        self.injected = False
        self.downloadMissingFiles()
        self.init_all_functions()

    def launch(self):
        try:
            free_port = get_free_port(10000)
            self.runFB(port=free_port)
            self.run_conn(port=free_port)
            Builtins.createThread(self.output_fb_msgs_thread)
            self.process_game_packets()
        except Exception as err:
            return err

    def runFB(self, ip="127.0.0.1", port=8080):
        if self.system_type == "Linux":
            os.system("/usr/bin/chmod +x ./phoenixbuilder")
            con_cmd = rf"./phoenixbuilder -A {self.auth_server} -t fbtoken --no-readline --no-update-check --listen-external {ip}:{port} -c {self.serverNumber} {f'-p {self.serverPassword}' if self.serverPassword else ''}"

        # windows updated "./PRGM" command.
        if self.system_type == "Windows":
            con_cmd = rf".\phoenixbuilder.exe -A {self.auth_server} -t fbtoken --no-readline --no-update-check --listen-external {ip}:{port} -c {self.serverNumber} {f'-p {self.serverPassword}' if self.serverPassword else ''}"
        self.fb_pipe = subprocess.Popen(
            con_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

    def run_conn(self, ip="127.0.0.1", port=8080, timeout=None):
        connect_fb_start_time = time.time()
        max_con_time = timeout or 10
        while 1:
            try:
                self.con = fbconn.ConnectFB(f"{ip}:{port}")
                Print.print_suc("§a成功连接上FastBuilder.")
                return 1
            except:
                if time.time() - connect_fb_start_time > max_con_time:
                    Print.print_err(f"§4{max_con_time}秒内未连接上FB，已退出")
                    self.close_fb()
                    raise SystemExit
                if self.status == SysStatus.FB_LAUNCH_EXC:
                    Print.print_err("§4连接FB时出现问题，已退出")
                    self.close_fb()
                    raise SystemExit

    def output_fb_msgs_thread(self):
        while 1:
            tmp: str = self.fb_pipe.stdout.readline().decode("utf-8").strip("\n")
            if not tmp:
                continue
            if " 简体中文" in tmp:
                # seems will be unable forever because it's no longer supported.
                try:
                    self.fb_pipe.stdin.write(f"{tmp[1]}\n".encode("utf-8"))
                    self.fb_pipe.stdin.flush()
                    Print.print_inf(f"语言已自动选择为简体中文： [{tmp[1]}]")
                except IndexError:
                    Print.print_war("未能自动选择为简体中文")
            elif "ERROR" in tmp:
                if "Server not found" in tmp:
                    Print.print_err(
                        f"§c租赁服号: {self.serverNumber} 未找到, 有可能是租赁服关闭中, 或是设置了等级或密码"
                    )
                    self.update_status(SysStatus.CRASHED_EXIT)

                elif "Unauthorized rental server number" in tmp:
                    Print.print_err(
                        f"§c租赁服号: {self.serverNumber} ，你还没有该服务器号的卡槽， 请前往用户中心购买"
                    )
                    self.update_status(SysStatus.CRASHED_EXIT)
                elif "Failed to contact with API" in tmp:
                    Print.print_err(
                        "§c无法连接到验证服务器, 可能是FB服务器崩溃, 或者是你的IP处于黑名单中"
                    )
                    try:
                        Print.print_war("尝试连接到 FastBuilder 验证服务器")
                        requests.get("http://user.fastbuilder.pro", timeout=10)
                        Print.print_err(
                            "??? 未知情况， 有可能只是验证服务器崩溃， 用户中心并没有崩溃"
                        )
                    except:
                        Print.print_err(
                            "§cFastBuilder服务器无法访问， 请等待修复(加入FastBuilder频道查看详情)"
                        )
                    self.update_status(SysStatus.CRASHED_EXIT)
                elif "Invalid token" in tmp:
                    Print.print_err("§cFastBuilder Token 无法使用， 请重新下载")
                    self.update_status(SysStatus.CRASHED_EXIT)
                elif "netease.report.kick.hint" in tmp:
                    Print.print_err(
                        "§c无法连接到网易租赁服 -> 网易土豆的常见问题，检查你的租赁服状态（等级、是否开启、密码）并重试, 也可能是你的网络问题"
                    )
                    self.update_status(SysStatus.CRASHED_EXIT)
                elif "Press ENTER to exit." in tmp:
                    Print.print_err("§c程序退出")
                    self.update_status(SysStatus.CRASHED_EXIT)
                else:
                    Print.print_with_info(tmp, "§b  FB  §r")

            elif "Transfer: accept new connection @ " in tmp:
                Print.print_with_info(
                    "FastBuilder 监听端口已开放: " + tmp.split()[-1], "§b  FB  "
                )
            elif "Successfully created minecraft dialer." in tmp:
                Print.print_with_info("§e成功创建于 Minecraft 的链接", "§b  FB  §r")
            elif tmp.startswith("panic"):
                Print.print_err(f"FastBuilder 出现问题: {tmp}")
            else:
                Print.print_with_info(tmp, "§b  FB  §r")

    def close_fb(self):
        try:
            self.fb_pipe.stdin.write("exit\n".encode("utf-8"))
            self.fb_pipe.stdin.flush()
        except:
            pass
        try:
            self.fb_pipe.kill()
        except:
            pass
        Print.print_suc("成功关闭FB进程")

    def process_game_packets(self):
        try:
            for packet_bytes in fbconn.RecvGamePacket(self.con):
                packet_type = packet_bytes[0]
                if packet_type not in self.need_listen_packets:
                    continue
                packet_mapping = ujson.loads(
                    fbconn.GamePacketBytesAsIsJsonStr(packet_bytes)
                )
                if packet_type == PacketIDS.CommandOutput:
                    cmd_uuid = packet_mapping["CommandOrigin"]["UUID"].encode()
                    if cmd_uuid in self.cmds_reqs:
                        self.cmds_resp[cmd_uuid] = [
                            time.time(), packet_mapping]
                self.packet_handler(packet_type, packet_mapping)
                if not self.injected and packet_type == PacketIDS.PlayerList:
                    self.injected = True
                    Builtins.createThread(self._launcher_listener)
        except StopIteration:
            pass
        self.update_status(SysStatus.CRASHED_EXIT)

    def downloadMissingFiles(self):
        "获取缺失文件"
        Print.print_with_info("§d将自动检测缺失文件并补全", "§d 加载 ")
        mirror_src = "https://tdload.tblstudio.cn/"
        file_get_src = (
            mirror_src
            + "https://raw.githubusercontent.com/ToolDelta/ToolDelta/main/require_files.json"
        )
        try:
            files_to_get = json.loads(
                requests.get(file_get_src, timeout=30).text)
        except json.JSONDecodeError:
            Print.print_err("自动下载缺失文件失败: 文件源 JSON 不合法")
            return False
        except requests.Timeout:
            Print.print_err("自动下载缺失文件失败: URL 请求出现问题: 请求超时")
            return False
        except Exception as err:
            Print.print_err(f"自动下载缺失文件失败: URL 请求出现问题: {err}")
            return False
        try:
            Print.print_with_info("§d正在检测需要补全的文件", "§d 加载 ")
            mirrs = files_to_get["Mirror"]
            files = files_to_get[self.system_type]
            for fdir, furl in files.items():
                if not os.path.isfile(fdir):
                    Print.print_inf(f"文件: <{fdir}> 缺失, 正在下载..")
                    succ = False
                    for mirr in mirrs:
                        try:
                            download_file_singlethreaded(
                                mirr + "/https://github.com/" + furl, fdir
                            )
                            succ = True
                            break
                        except requests.exceptions.RequestException:
                            Print.print_war("镜像源故障, 正在切换")
                    if not succ:
                        Print.print_err("镜像源全不可用..")
                        return False
                    Print.print_inf(f"文件: <{fdir}> 下载完成        ")
        except requests.Timeout:
            Print.print_err("自动检测文件并补全时出现错误: 超时, 自动跳过")
        except Exception as err:
            Print.print_err(f"自动检测文件并补全时出现错误: {err}")
            return False
        return True

    def init_all_functions(self):
        def sendcmd(cmd: str, waitForResp: bool = False, timeout: int | float = 30):
            uuid = fbconn.SendMCCommand(self.con, cmd)
            if waitForResp:
                self.cmds_reqs.append(uuid)
                waitStartTime = time.time()
                while 1:
                    res = self.cmds_resp.get(uuid)
                    if res is not None:
                        self.cmds_reqs.remove(uuid)
                        del self.cmds_resp[uuid]
                        return Packet_CommandOutput(res[1])
                    if time.time() - waitStartTime > timeout:
                        self.cmds_reqs.remove(uuid)
                        Print.print_war(f'sendcmd "{cmd}" 超时, 尝试 sendwscmd')
                        return self.sendwscmd(cmd, True, timeout)

        def sendwscmd(cmd: str, waitForResp: bool = False, timeout: int = 30):
            uuid = fbconn.SendWSCommand(self.con, cmd)
            if waitForResp:
                self.cmds_reqs.append(uuid)
                waitStartTime = time.time()
                while 1:
                    res = self.cmds_resp.get(uuid)
                    if res is not None:
                        self.cmds_reqs.remove(uuid)
                        del self.cmds_resp[uuid]
                        return Packet_CommandOutput(res[1])
                    if time.time() - waitStartTime > timeout:
                        self.cmds_reqs.remove(uuid)
                        raise TimeoutError("指令超时")
            else:
                return uuid

        self.sendcmd = sendcmd
        self.sendwscmd = sendwscmd
        self.sendwocmd = staticmethod(
            lambda cmd: fbconn.SendNoResponseCommand(self.con, cmd)
        )
        self.sendPacket = self.sendPacketJson = staticmethod(
            lambda pckID, pck: fbconn.SendGamePacketBytes(
                self.con,
                fbconn.JsonStrAsIsGamePacketBytes(
                    pckID, ujson.dumps(pck, ensure_ascii=False)
                ),
            )
        )
        self.sendfbcmd = staticmethod(
            lambda cmd: fbconn.SendFBCommand(self.con, cmd))
        self.is_op = None


class FrameNeOmg(StandardFrame):
    # 使用 NeOmega 框架连接到游戏
    launch_type = "NeOmega"

    def __init__(self, serverNumber, password, fbToken, auth_server):
        super().__init__(serverNumber, password, fbToken, auth_server)
        self.status = None
        self.launch_event = threading.Event()
        self.injected = False
        self.omega = None
        self.TDC = None
        self.neomg_proc = None
        self.set_tooldelta_cli()
        self.download_libs()
        self.init_all_functions()
        self.status = SysStatus.LOADING
        self.secret_exit_key = ""

    def set_omega(self, openat_port):
        from .neo_libs import neo_conn

        retries = 0
        while retries <= 10:
            try:
                self.omega = neo_conn.ThreadOmega(
                    connect_type=neo_conn.ConnectType.Remote,
                    address=f"tcp://localhost:{openat_port}",
                    accountOption=neo_conn.AccountOptions(
                        AuthServer=self.auth_server,
                        UserToken=self.fbToken,
                        ServerCode=self.serverNumber,
                        ServerPassword=str(self.serverPassword),
                    ),
                )
                retries = 0
                break
            except Exception as err:
                time.sleep(5)
                retries += 1
                Print.print_war(f"OMEGA 连接失败, 重连: 第 {retries} 次: {err}")
                if retries > 5:
                    Print.print_err("最大重试次数已达到")
                    raise SystemExit

    def set_tooldelta_cli(self):
        if type(self) == FrameNeOmg:
            self.TDC = ToolDeltaCli()

    def start_neomega_proc(self):
        free_port = get_free_port(24016)
        access_point_file = (
            f"neomega_{platform.uname().system.lower()}_access_point_{self.sys_machine}"
        )
        if "TERMUX_VERSION" in os.environ:
            access_point_file = f"neomega_android_access_point_{self.sys_machine}"
        if platform.system() == "Windows":
            access_point_file += ".exe"
        py_file_path = os.path.join(
            os.getcwd(), "tooldelta", "neo_libs", access_point_file
        )
        if platform.uname().system.lower() == "linux":
            os.system("chmod +x " + shlex.quote(py_file_path))
        # 只需要+x即可
        Print.print_inf(f"DEBUG: 将使用端口 {free_port}")
        self.neomg_proc = subprocess.Popen(
            [
                py_file_path,
                "-server",
                str(self.serverNumber),
                "-T",
                self.fbToken,
                "-access-point-addr",
                f"tcp://localhost:{free_port}",
                "-server-password",
                str(self.serverPassword),
                "-auth-server",
                self.auth_server,
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        return free_port

    def msg_show(self):
        def _msg_show_thread():
            while True:
                msg_orig = self.neomg_proc.stdout.readline().decode("utf-8").strip("\n")
                if msg_orig in ("", "SIGNAL: exit"):
                    with Print.lock:
                        Print.print_with_info(
                            "ToolDelta: NEOMG 进程已结束", "§b NOMG ")
                    self.update_status(SysStatus.NORMAL_EXIT)
                    return
                if "[neOmega 接入点]: 就绪" in msg_orig:
                    self.launch_event.set()
                elif f"STATUS CODE: {self.secret_exit_key}" in msg_orig:
                    with Print.lock:
                        Print.print_with_info("§a机器人已退出", "§b NOMG ")
                    continue
                with Print.lock:
                    Print.print_with_info(msg_orig, "§b NOMG ")

        Builtins.createThread(_msg_show_thread, usage="显示来自NeOmega的信息")

    def make_secret_key(self):
        self.secret_exit_key = hex(random.randint(10000, 99999))

    def launch(self):
        self.status = SysStatus.LAUNCHING
        openat_port = self.start_neomega_proc()
        self.msg_show()
        self.launch_event.wait()
        self.make_secret_key()
        self.set_omega(openat_port)
        self.update_status(SysStatus.RUNNING)
        Print.print_suc("已开启接入点进程")
        pcks = [
            self.omega.get_packet_id_to_name_mapping(i)
            for i in self.need_listen_packets
        ]
        self.omega.listen_packets(pcks, self.packet_handler_parent)
        self._launcher_listener()
        Print.print_suc("接入点已就绪!")
        self.exit_event.wait()  # 等待事件的触发
        if self.status == SysStatus.NORMAL_EXIT:
            return SystemExit("正常退出.")
        if self.status == SysStatus.CRASHED_EXIT:
            return Exception("NeOmega 已崩溃")
        return SystemError("未知的退出状态")

    def download_libs(self):
        """根据系统架构和平台下载所需的库。"""
        cfgs = Config.get_cfg("ToolDelta基本配置.json", constants.LAUNCH_CFG_STD)
        is_mir: bool = cfgs["是否使用github镜像"]
        if is_mir:
            mirror_src = "https://tdload.tblstudio.cn/" + \
                "https://raw.githubusercontent.com/ToolDelta/ToolDelta/main/"
            depen_url = "https://tdload.tblstudio.cn/" + \
                "https://raw.githubusercontent.com/ToolDelta/DependencyLibrary/main/"
        else:
            mirror_src = "https://raw.githubusercontent.com/ToolDelta/ToolDelta/main/"
            depen_url = "https://raw.githubusercontent.com/ToolDelta/DependencyLibrary/main/"
        try:
            require_depen = json.loads(
                requests.get(
                    f"{mirror_src}require_files.json", timeout=5
                ).text
            )
        except Exception as err:
            Print.print_err(f"获取依赖库表出现问题: {err}")
            self.update_status(SysStatus.CRASHED_EXIT)
            return
        self.sys_machine = platform.machine().lower()
        if self.sys_machine == "x86_64":
            self.sys_machine = "amd64"
        elif self.sys_machine == "aarch64":
            self.sys_machine = "arm64"
        if "TERMUX_VERSION" in os.environ:
            sys_info_fmt: str = f"Android:{self.sys_machine.lower()}"
        else:
            sys_info_fmt: str = f"{platform.uname().system}:{self.sys_machine.lower()}"
        source_dict: list[str] = require_depen[sys_info_fmt]
        commit_remote = requests.get(
            f"{depen_url}commit", timeout=5
        ).text
        commit_file_path = os.path.join(
            os.getcwd(), "tooldelta", "neo_libs", "commit")
        replace_file = False
        if os.path.isfile(commit_file_path):
            with open(commit_file_path, "r", encoding="utf-8") as f:
                commit_local = f.read()
            if commit_local != commit_remote:
                Print.print_war("依赖库版本过期, 将重新下载")
                replace_file = True
        else:
            replace_file = True
        for v in source_dict:
            pathdir = os.path.join(os.getcwd(), "tooldelta", "neo_libs", v)
            url = depen_url + v
            if not os.path.isfile(pathdir) or replace_file:
                Print.print_with_info(f"正在下载依赖库 {pathdir} ...", "§a 下载 §r")
                try:
                    download_file_singlethreaded(url, pathdir)
                except Exception as err:
                    Print.print_err(f"下载依赖库出现问题: {err}")
                    self.update_status(SysStatus.CRASHED_EXIT)
                    return
        if replace_file:
            # 写入commit_remote，文字写入
            with open(commit_file_path, "w", encoding="utf-8") as f:
                f.write(commit_remote)
            Print.print_suc("已完成依赖更新！")

    def get_players_and_uuids(self):
        players_uuid = {}
        for i in self.omega.get_all_online_players():
            players_uuid[i.name] = i.uuid
        return players_uuid

    def get_bot_name(self):
        return self.omega.get_bot_name()

    def packet_handler_parent(self, pkt_type, pkt):
        pkt_type = self.omega.get_packet_name_to_id_mapping(pkt_type)
        self.packet_handler(pkt_type, pkt)

    def init_all_functions(self):
        def sendcmd(cmd: str, waitForResp: bool = False, timeout: int | float = 30):
            if waitForResp:
                res = self.omega.send_player_command_need_response(
                    cmd, timeout)
                if res is None:
                    raise TimeoutError("指令超时")
                return res
            self.omega.send_player_command_omit_response(cmd)
            return

        def sendwscmd(cmd: str, waitForResp: bool = False, timeout: int = 30):
            if waitForResp:
                res = self.omega.send_websocket_command_need_response(
                    cmd, timeout)
                if res is None:
                    raise TimeoutError("指令超时")
                return res
            self.omega.send_websocket_command_omit_response(cmd)
            return

        def sendwocmd(cmd: str):
            self.omega.send_settings_command(cmd)

        def sendPacket(pktID: int, pkt: str):
            self.omega.send_game_packet_in_json_as_is(pktID, pkt)

        def sendfbcmd(_):
            raise AttributeError("NeOmg模式无法发送FBCommand")

        def is_op(player: str):
            return self.omega.get_player_by_name(player).command_permission_level > 2

        self.sendcmd = sendcmd
        self.sendwscmd = sendwscmd
        self.sendwocmd = sendwocmd
        self.sendPacket = self.sendPacketJson = sendPacket
        self.sendfbcmd = sendfbcmd
        self.is_op = is_op


class FrameNeOmgRemote(FrameNeOmg):
    def __init__(self, serverNumber, password, fbToken, auth_server):
        super().__init__(serverNumber, password, fbToken, auth_server)

    def launch(self):
        try:
            openat_port = int(sys_args_to_dict().get(
                "access-point-port", "24020"))
            if openat_port not in range(65536):
                raise AssertionError
        except (ValueError, AssertionError):
            Print.print_err("启动参数 -access-point-port 错误: 不是1~65535的整数")
        if openat_port == 0:
            Print.print_war(
                "未用启动参数指定链接neOmega接入点开放端口, 尝试使用默认端口 24015"
            )
            Print.print_inf("可使用启动参数 -access-point-port 端口 以指定接入点端口.")
            openat_port = 24015
            return SystemExit
        Print.print_inf(f"将从端口 {openat_port} 连接至接入点(等待接入中).")
        self.set_omega(openat_port)
        Print.print_suc("已连接上接入点进程.")
        pcks = [
            self.omega.get_packet_id_to_name_mapping(i)
            for i in self.need_listen_packets
        ]
        self.omega.listen_packets(pcks, self.packet_handler_parent)
        self._launcher_listener()
        Print.print_suc("接入点已就绪")
        self.exit_event.wait()
        self.update_status(SysStatus.NORMAL_EXIT)
        if self.status == SysStatus.NORMAL_EXIT:
            return SystemExit("正常退出.")
        if self.status == SysStatus.CRASHED_EXIT:
            return Exception("接入点已崩溃")
        return SystemError("未知的退出状态")

    def download_libs(self):
        Print.print_inf("以 Remote 启动, 将不会检查库完整性")


class MCBEWebSocket(StandardFrame):
    def __init__(self, serverNumber, password, fbToken, auth_server):
        global fcwslib
        import fcwslib
        self.ws_lib = fcwslib.server.Server(serverNumber, password)
        self.ws_lib
        self.ws_lib.run_forever()


class ToolDeltaCli(object):
    def __init__(self, address: dict = {"host": "tdaus.tooldelta.fit", "port": 0}) -> None:
        # def __init__(self, address: dict = {"host": "127.0.0.1", "port": 9002}) -> None:
        self.NoPort: bool = address.get("port", 0) == 0
        self.S_ADDRESSS: dict = address
        self.protocol: str = "http"
        self.url: str = f'{self.protocol}://{self.S_ADDRESSS["host"]}:{self.S_ADDRESSS["port"]}' if self.NoPort == False else f'{self.protocol}://{self.S_ADDRESSS["host"]}'
        self.SocketIO: socketio.Client = socketio.Client()
        self.data_received_event: threading.Event = threading.Event()
        self.connected_to_server: bool = True
        threading.Thread(target=self.conn_aus, name="SocketIO_Conn").start()
        while not self.SocketIO.connected and self.connected_to_server:
            time.sleep(0.1)

    def init_auth_v(self) -> None:
        self.feature_code: str = str(uuid.uuid5(
            uuid.NAMESPACE_DNS, str(time.perf_counter())))
        self.token_ec: tuple = (self.feature_code, self.get_new_token())

    def get_new_token(self) -> None:
        try:
            response = requests.post(
                url=f'{self.url}/api/signin', data=json.dumps({"feature_code": self.feature_code}), timeout=5)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.ConnectionError as err:
            return "null"

    def conn_aus(self) -> None:
        try:
            self.init_auth_v()
            self.SocketIO.connect(
                self.url, namespaces='/api', headers={'Authorization': f'Bearer {self.token_ec[1]}'})
            Print.print_suc("ToolDelta成功连接到至Api服务器[Socket-IO]!")
            while True:
                if not self.SocketIO.connected:
                    try:
                        self.init_auth_v()
                        self.SocketIO.connect(
                            self.url, namespaces='/api', headers={'Authorization': f'Bearer {self.token_ec[1]}'})
                        Print.print_suc("ToolDelta与Api服务器断开连接,已重新连接成功!")
                    except:
                        Print.print_war(
                            "ToolDeltaApi服务器可能存在故障或当前网络环境异常，将停止使用ToolDeltaApi服务器!")
                        break
                time.sleep(10)
        except Exception as err:
            Print.print_war("ToolDelta无法连接至Api服务器,将停止使用其提供的功能!")
            self.connected_to_server = False
            threading.Thread(target=self.reconnect_to_server).start()

    def reconnect_to_server(self, interval=20):
        while not self.connected_to_server:
            try:
                self.init_auth_v()
                self.SocketIO.connect(
                    self.url, namespaces='/api', headers={'Authorization': f'Bearer {self.token_ec[1]}'})
                Print.print_suc("ToolDelta成功重新连接至Api服务器!")
                self.connected_to_server = True
            except Exception as err:
                time.sleep(interval)

    def get_depends_table_data(self) -> dict:
        if self.SocketIO.connected:
            @self.SocketIO.on('depends_table_data', namespace='/api')
            def handle_depends_table_data(data):
                self.data_received_event.set()
                self.depend_table_data = data
            self.SocketIO.emit('get_depends_table', namespace='/api')
            self.data_received_event.wait()  # 等待数据返回
            self.data_received_event.clear()
            return self.depend_table_data
        else:
            Print.print_war(
                "Namespace /api is not connected yet. Please wait for connection.")

    def get_version_updates(self) -> any:
        if self.SocketIO.connected:
            @self.SocketIO.on('version_updates', namespace='/api')
            def handle_version_updates_data(data):
                self.data_received_event.set()
                self.latest_version_data = data

            self.SocketIO.emit('get_version_update', namespace='/api')
            self.data_received_event.wait()
            self.data_received_event.clear()
            return self.latest_version_data["latest_version_str"]
