import datetime
import os
import random


def _getcombo(input_func, fd, title="FILE"):
    if fd is not None:
        try:
            file_obj = fd.askopenfile(title=title, filetypes=[("Text files", "*.txt")])
            if file_obj is not None:
                return str(file_obj.name).replace('"', "")
        except Exception:
            pass
    try:
        path = input_func(f"Enter path to {title} (.txt): ").strip()
        if path:
            return path
    except Exception:
        pass
    return None


def password_limit(limit, input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\PASSWORD_MINIMUM")
    except Exception:
        pass
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    apropriate = []
    for line in combo:
        try:
            password = line.split(":")[1]
            if len(password) >= int(limit):
                apropriate.append(line.strip())
        except Exception:
            pass
    namy = (
        "[Minimum - PASSWORD] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\PASSWORD_MINIMUM\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in apropriate:
            file.write(str(line).strip() + "\n")


def password_hex(limits, input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\PASSWORD_HEX")
    except Exception:
        pass
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    good = []
    for line in combo:
        try:
            password = line.split(":")[1]
            for character in password:
                if character in limits:
                    good.append(line.strip())
                    break
        except Exception:
            pass
    namy = (
        "[PASSWORD - HEX] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\PASSWORD_HEX\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in good:
            file.write(line.strip() + "\n")


def lowercase_pass(input_func=input, fd=None):
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + f"\\results\\LOWER_PASSWORD")
    except Exception:
        pass

    with open(combo_path, "r", encoding="utf-8", errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        try:
            password = line.split(":")[1]
            passowrd_low = password.lower()
            line = line.replace(password, passowrd_low)
            newc.append(line)
        except Exception:
            pass
    namey = (
        "[Lower - Password] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + f"\\results\\LOWER_PASSWORD\\" + namey,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def upper_password(input_func=input, fd=None):
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + f"\\results\\UPPER_PASSWORD")
    except Exception:
        pass

    with open(combo_path, "r", encoding="utf-8", errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        try:
            password = line.split(":")[1]
            passowrd_upper = password.upper()
            line = line.replace(password, passowrd_upper)
            newc.append(line)
        except Exception:
            pass
    namey = (
        "[Upper - Password] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + f"\\results\\UPPER_PASSWORD\\" + namey,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def add_prefix_to_password(input_func=input, fd=None):
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    prefix = input_func("Prefix: ")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + f"\\results\\PREFIX_PASSWORD")
    except Exception:
        pass

    with open(combo_path, "r", encoding="utf-8", errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        try:
            password = line.split(":")[1]
            passowrd_prefix = str((str(prefix).strip() + str(password).strip())).strip()
            line = line.replace(password, passowrd_prefix)
            newc.append(line)
        except Exception:
            pass
    namey = (
        "[Prefix - Password] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + f"\\results\\PREFIX_PASSWORD\\" + namey,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def add_suffix_to_password(input_func=input, fd=None):
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    suffix = input_func("Suffix: ")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + f"\\results\\SUFFIX_PASSWORD")
    except Exception:
        pass

    with open(combo_path, "r", encoding="utf-8", errors="ignore") as file:
        combo = file.readlines()
    for line in combo:
        try:
            password = line.split(":")[1]
            passowrd_suffix = str((password.strip() + suffix.strip())).strip()
            line = line.replace(password, passowrd_suffix)
            newc.append(line)
        except Exception:
            pass
    namey = (
        "[Suffix - Password] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + f"\\results\\SUFFIX_PASSWORD\\" + namey,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


