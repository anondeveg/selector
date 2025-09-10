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


def domain_changer(dom, input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\DOMAIN_CHANGER")
    except Exception:
        pass
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    try:
        for line in combo:
            try:
                user = line.split("@")[0]
                password = line.split(":")[1]
                new = user.strip() + dom.strip() + ":" + password.strip()
                newc.append(new.strip())
            except Exception:
                pass
    except Exception:
        pass
    namy = (
        "[DOMAIN - CHANGER] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\DOMAIN_CHANGER\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def email_extracor(input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\EMAIL_EXTRACTOR")
    except Exception:
        pass
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    for line in combo:
        try:
            email = line.split(":")[0]
            newc.append(email.strip())
        except Exception:
            pass
    namy = (
        "[EMAIL - EXTRACTOR] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\EMAIL_EXTRACTOR\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def password_extracor(input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\PASSWORD_EXTRACTOR")
    except Exception:
        pass
    newc = []
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    for line in combo:
        try:
            email = line.split(":")[1]
            newc.append(email.strip())
        except Exception:
            pass
    namy = (
        "[PASSWORD - EXTRACTOR] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\PASSWORD_EXTRACTOR\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newc:
            file.write(line.strip() + "\n")


def filter_combo_by_domain(domain, input_func=input, fd=None):
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\DOMAIN_FILTRER")
    except Exception:
        pass
    try:
        domain = domain.replace("@", "")
    except Exception:
        pass
    combo_path = _getcombo(input_func, fd, "combo-file")
    combo = open(combo_path, "r", errors="ignore", encoding="utf-8")
    newc = []
    try:
        for line in combo:
            try:
                doma = str(line.split("@")[1]).split(":")[0]
                if str(doma) == str(domain):
                    newc.append(line.strip())
            except Exception:
                pass
    except Exception:
        pass
    try:
        namy = (
            "[FILTER - DOMAIN] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
        )
        with open(
            os.getcwd() + "\\results\\DOMAIN_FILTRER\\" + namy,
            "a",
            encoding="utf-8",
            errors="ignore",
        ) as file:
            for line in newc:
                file.write(line.strip() + "\n")
    except Exception:
        pass


def EP_TO_UP(input_func=input, fd=None):
    filename = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + "\\results\\EP_TO_UP")
    except Exception:
        pass
    combo = open(filename, "r", errors="ignore", encoding="utf-8")
    combo = combo.readlines()
    newcombo = []
    for line in combo:
        try:
            user = line.split("@")[0]
            password = line.split(":")[1]
            new = f"{user.strip()}:{password.strip()}"
            newcombo.append(new.strip())
        except Exception:
            pass
    namy = (
        "[EP-UP] {" + str(datetime.datetime.now())[:-7].replace(":", "-") + "}.txt"
    )
    with open(
        os.getcwd() + "\\results\\EP_TO_UP\\" + namy,
        "a",
        encoding="utf-8",
        errors="ignore",
    ) as file:
        for line in newcombo:
            file.write(line.strip() + "\n")


def domain_sorter(input_func=input, fd=None):
    filename = _getcombo(input_func, fd, "combo-file")
    try:
        os.mkdir(os.getcwd() + "\\results")
    except Exception:
        pass
    try:
        os.mkdir(os.getcwd() + f"\\results\\DOMAIN_SORTER")
    except Exception:
        pass
    combo = open(filename, "r", errors="ignore", encoding="utf-8")
    try:
        for line in combo:
            try:
                domain = str(line.split("@")[1]).split(":")[0]
                with open(
                    os.getcwd() + f"\\results\\DOMAIN_SORTER\\{domain}.txt",
                    "a",
                    encoding="utf-8",
                    errors="ignore",
                ) as f:
                    f.write(line.strip() + "\n")
            except Exception:
                pass
    except Exception:
        pass


