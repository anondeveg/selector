import datetime
import os
import random
def listset(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


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


def CLEANER(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\ALL_CLEANER")
    except Exception:
        pass
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    listt = combo.readlines()
    random.shuffle(listt)
    nodupe = listset(listt)
    newlist = []
    for line in nodupe:
        if line == "" or line == " ":
            pass
        else:
            newlist.append(line.strip())
    namy = (
        "[CLEAN - RANDOMIZED] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\ALL_CLEANER\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as f:
        for line in nodupe:
            f.write(line.strip() + "\n")


def reverser(input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\COMBO_REVERSER")
    except Exception:
        pass
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    newc = []
    try:
        for line in combo:
            usr = line.split(":")[0]
            password = line.split(":")[1]
            reversed_pair = f"{password.strip()}:{usr.strip()}"
            newc.append(reversed_pair.strip())
    except Exception:
        pass
    namy = (
        "[DOMAIN - CHANGER] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\COMBO_REVERSER\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def combo_sorter(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\COMBO_SORTER")
    except Exception:
        pass
    sorted_lines = []
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    for line in combo:
        sorted_lines.append(line)
    namy = (
        "[COMBO - SORTER] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    sorted_lines.sort()
    with open(
        os.getcwd() + "\\results\\COMBO_SORTER\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in sorted_lines:
            file.write(line.strip() + "\n")


def shuffle(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\SHUFFLE_LIST")
    except Exception:
        pass
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    listt = combo.readlines()
    random.shuffle(listt)
    namy = (
        "[SHUFFlED] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\SHUFFLE_LIST\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as f:
        for line in listt:
            f.write(line.strip() + "\n")


def remove_dupes(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    start_time = None  # preserved structure; not used in modular version
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    listt = combo.readlines()
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\REMOVE_DUPES")
    except Exception:
        pass
    nodupe = listset(listt)
    namy = (
        "[REMOVED DUPES] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\REMOVE_DUPES\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as f:
        for line in nodupe:
            f.write(line.strip() + "\n")


def ComboLineCounter(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    c = []
    for line in combo:
        c.append(line.strip())
    print(f"\nYOUR COMBO HAVE: {format(len(c),',')} LINES")
    try:
        input_func("\nPRESS ANY THING TO COUNTINUE:")
    except Exception:
        pass


def LQTOHQ(input_func=input, fd=None):
    combo_path = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\LQTOHQ")
    except Exception:
        pass
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    listt = []
    for line in combo:
        try:
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip().capitalize() + "!" + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip().capitalize() + "123" + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip().capitalize() + "1" + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip().capitalize() + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip() + "!" + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip() + "123" + "\n"
            )
            listt.append(
                str(line.split(":")[0]) + ":" + str(line.split(":")[1]).strip() + "1" + "\n"
            )
            listt.append(line)
        except Exception:
            pass
    try:
        random.shuffle(listt)
    except Exception:
        pass
    namy = (
        "[LQ to HQ] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\LQTOHQ\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as f:
        for line in listt:
            f.write(line.strip() + "\n")


