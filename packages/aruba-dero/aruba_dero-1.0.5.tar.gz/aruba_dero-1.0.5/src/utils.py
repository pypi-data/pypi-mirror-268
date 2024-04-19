import os
from pathlib import PurePath
from platform import system
from socket import AddressFamily

import psutil
from bullet import Bullet, colors


def get_net_ifaces() -> list[dict[str, str]]:
    addrs = psutil.net_if_addrs()
    ifaces = []
    platform = system()

    for adapter in addrs:
        mac, ip, ip6 = None, None, None

        for net_entry in addrs[adapter]:
            if net_entry.family == AddressFamily.AF_INET:
                ip = net_entry.address
            if net_entry.family == AddressFamily.AF_INET6:
                ip6 = net_entry.address
            if platform == "Windows" and net_entry.family == AddressFamily.AF_LINK:
                mac = net_entry.address
            elif platform == "Linux" and net_entry.family in (AddressFamily.AF_PACKET, AddressFamily.AF_NETLINK):
                mac = net_entry.address
        ifaces.append({"name": adapter, "mac": mac, "ip4": ip, "ip6": ip6})
    return ifaces


def cli_file_picker(prompt: str, root_path: str, current_path: str, allow_parent_dirs=False) -> str | None:
    choices = os.listdir(current_path)
    pp = PurePath(current_path)

    if allow_parent_dirs or pp.is_relative_to(root_path) and pp != PurePath(root_path):
        choices.insert(0, "..")
    elif not os.listdir(current_path):
        return None

    cli = Bullet(
        prompt=prompt,
        choices=choices,
        indent=0,
        align=5,
        margin=2,
        bullet="*",
        bullet_color=colors.bright(colors.foreground["cyan"]),
        word_color=colors.bright(colors.foreground["yellow"]),
        word_on_switch=colors.bright(colors.foreground["yellow"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["black"],
        pad_right=5,
        return_index=True
    )

    selection = cli.launch()
    selected_path = os.path.join(current_path, selection[0])

    if os.path.isdir(selected_path):
        return cli_file_picker(root_path=root_path, current_path=selected_path, prompt=prompt)

    if os.path.exists(selected_path):
        return selected_path
