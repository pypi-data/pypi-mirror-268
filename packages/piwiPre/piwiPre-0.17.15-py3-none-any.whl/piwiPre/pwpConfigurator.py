# ---------------------------------------------------------------------------------------------------------------
# piwiPre project
# This program and library is licenced under the European Union Public Licence v1.2 (see LICENCE)
# developed by fabien.battini(at)gmail.com
# ---------------------------------------------------------------------------------------------------------------

import sys
import os
import locale
import termcolor
import platform
import re
import shutil
import argparse

import tkinter
from tkinter import ttk
import tkinter.font
from tkinter import scrolledtext

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from piwiPre.pwpVersion import PwpVersion
from piwiPre.pwpLogoSmall import pwpLogo_png
from piwiPre.pwpParser import PwpParser
from piwiPre.pwpArgsIni import VST, ValueSetup, CVS, ItemValue


class Field:
    def __init__(self, label,
                 variable: tkinter.Variable or None,
                 item,
                 help_var: tkinter.Label or None,
                 checkbox=None):
        self.label = label
        self.variable = variable
        self.item = item
        self.help_var = help_var
        self.checkbox = checkbox

    def delete(self):
        self.label.destroy()
        del self.variable
        if self.item:
            self.item.destroy()
        if self.help_var:
            self.help_var.destroy()
        if self.checkbox:
            self.checkbox.destroy()


class PwpDirChooser:
    def __init__(self, father: 'PwpConfigUI', dir_name, self_test=False):
        self.dir_name = dir_name
        self.father = father
        self.root = tkinter.Tk()
        self.root.title("Directory chooser")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.do_dirs = tkinter.StringVar()
        self.all_lines = []

        row = 0
        # ----------------------- Logo and banner

        if father is None:
            self.logo = pwpLogo_png.tk_photo()
            tkinter.Label(self.frm, image=self.logo).grid(column=0, row=row, sticky="W")

        # ----------------------- Abort
        # row += 1

        title_font = tkinter.font.Font(size=10, family="Helvetica", weight="bold")
        lab = ttk.Label(self.frm, font=title_font,
                        text=" Change directory \n")
        lab.grid(column=0, row=row, columnspan=2, sticky="W")

        abort = tkinter.Button(self.frm, text=" Abort ", command=self.abort,
                               background='red', foreground="white",
                               activebackground="white", activeforeground='red')
        abort.grid(column=1, row=row, sticky="W")

        # ----------------------- sub directories
        row += 1
        self.first_row = row
        self.build_list()
        if self_test:
            self.root.after(2 * 1000, lambda: self.enter('..'))
            self.root.after(3 * 1000, lambda: self.select('..'))
            self.root.after(4 * 1000, lambda: self.abort())
        self.root.mainloop()

    def build_one_line(self, path, row, max_width):
        enter = tkinter.Button(self.frm, text=path, command=lambda: self.select(path), anchor="w", width=max_width,
                               background="#cccFFFccc", foreground="black",
                               activebackground="black", activeforeground="#cccFFFccc")
        enter.grid(column=0, row=row, sticky="W")
        choose = tkinter.Button(self.frm, text=" Enter ", command=lambda: self.enter(path),
                                background="#555555555", foreground="white",
                                activebackground="white", activeforeground="#555555555")
        choose.grid(column=1, row=row, sticky="W")

        return Field(enter, variable=None, item=choose, help_var=None)

    def build_list(self):
        row = self.first_row
        all_dirs = os.listdir(self.dir_name)
        for item in self.all_lines:
            item.delete()

        line_0 = f"[.]  {os.path.abspath(self.dir_name)}"
        line_1 = f"[..] {os.path.dirname(os.path.abspath(self.dir_name))}"
        max_width = 0
        max_width = max(max_width, len(line_0))
        max_width = max(max_width, len(line_1))
        for f in all_dirs:
            if os.path.isdir(self.dir_name + '/' + f):
                max_width = max(max_width, len(f))

        self.all_lines = []
        item = self.build_one_line(line_0, row=row, max_width=max_width)
        self.all_lines.append(item)
        row += 1
        item = self.build_one_line(line_1, row=row, max_width=max_width)
        self.all_lines.append(item)
        row += 1
        for f in all_dirs:
            if os.path.isdir(self.dir_name + '/' + f):
                self.all_lines.append(self.build_one_line(f, row=row, max_width=max_width))
                row += 1

    def abort(self):
        self.root.quit()

    def select(self, path: str):
        if path.startswith("[.]"):
            full_path = os.path.abspath(self.dir_name)
        elif path.startswith("[..]"):
            full_path = os.path.abspath(os.path.dirname(self.dir_name))
        else:
            full_path = os.path.abspath(self.dir_name + '/' + path)

        if self.father:
            self.father.select_dir(full_path)
        print(f"Chose '{full_path}'")
        self.abort()

    def enter(self, path):
        if path.startswith("[.]"):
            full_path = os.path.abspath(self.dir_name)
        elif path.startswith("[..]"):
            full_path = os.path.abspath(os.path.dirname(self.dir_name))
        else:
            full_path = os.path.abspath(self.dir_name + '/' + path)

        self.dir_name = full_path
        self.build_list()


class PwpConfigUI:
    def __init__(self, father: "PwpConfigurator"):
        self.configurator: PwpConfigurator = father
        self.root = tkinter.Tk()
        self.root.title("piwiPre configurator")
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()

        self.txt_language = tkinter.StringVar()

        self.do_language = tkinter.StringVar()
        self.do_piwigo = tkinter.StringVar()
        self.do_album = tkinter.StringVar()
        self.do_web = tkinter.StringVar()
        self.do_dirs = tkinter.StringVar()
        self.do_file = tkinter.StringVar()

        self.fields: dict[str, Field] = {}

        self.stage = 0  # can be 0 or 1

        row = 0
        radio_width = 7
        button_width = 12

        # next frames are there only to set the width of the columns
        ttk.Label(self.frm, text="", width=35).grid(column=0, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=1, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=2, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=3, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=4, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=5, row=row, sticky="W")
        ttk.Label(self.frm, text="", width=20).grid(column=6, row=row, sticky="W")

        # CAVEAT: logo MUST be stored in an attribute, otherwise it is garbage collected !
        self.logo = pwpLogo_png.tk_photo()
        try:
            tkinter.Label(self.frm, image=self.logo).grid(column=0, row=row, sticky="W")
        except tkinter.TclError:
            pass
            # ONLY during coverage test, we try to build 2 times the label
            # but BytesIO do not support it, and the underlying image has been destroyed
            # so, the construction fails.
            # but with normal usage, everything is OK

        title_font = tkinter.font.Font(size=14, family="Helvetica", weight="bold")
        lab = ttk.Label(self.frm, font=title_font,
                        text=f" piwiPre Configurator version {PwpVersion.spec} \n")
        lab.grid(column=2, row=row, columnspan=5, sticky="W")

        # -------------- language
        row += 1
        self.txt_language = ttk.Label(self.frm, text="", anchor="w", padding=4)
        self.txt_language.grid(column=0, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="en", text="en", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_language).grid(column=1, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="fr", text="fr", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_language, ).grid(column=2, row=row, sticky="W")

        # -------------- Menu

        self.menu_row = row
        self.menu_column = 4
        ttk.Label(self.frm, text=" Action : ", anchor="e", padding=4, width=25).grid(column=3, row=row, sticky="W")

        self.next_button = tkinter.Button(self.frm, text="   Next   ", command=self.next, width=button_width,
                                          background="green", foreground="white",
                                          activebackground="white", activeforeground="green")

        self.back_button = tkinter.Button(self.frm, text="Back", command=self.back, width=button_width,
                                          background="#555555555", foreground="white",
                                          activebackground="white", activeforeground="orange")

        self.run_button = tkinter.Button(self.frm, text="Build Ini File", command=self.run, width=button_width,
                                         background="green", foreground="white",
                                         activebackground="white", activeforeground="orange")

        tkinter.Button(self.frm, text="  Quit  ", command=self.exit, width=button_width,
                       background="red", foreground="white",
                       activebackground="white", activeforeground="red"
                       ).grid(column=self.menu_column + 2, row=row, sticky="W")

        # -------------- Separator
        row += 1
        self.sep1 = self.separator(row=row, text="Change ini file to build")

        # -------------- HOME
        row += 1
        ttk.Label(self.frm, text="HOME :", anchor="w", padding=4,
                  ).grid(column=0, row=row, sticky="W")

        val = os.path.abspath(self.configurator.home)
        val += " (changed with --chdir)" if val != os.path.abspath(os.path.expanduser("~")) else ""
        ttk.Label(self.frm, text=val, anchor="w", width=80, ).grid(column=1, row=row, sticky="W", columnspan=4)

        # -------------- ini file
        row += 1
        ttk.Label(self.frm, text="ini file :", anchor="w", padding=4,
                  ).grid(column=0, row=row, sticky="W")

        self.do_file = ttk.Label(self.frm, text=self.configurator.file, anchor="w", width=80, )
        self.do_file.grid(column=1, row=row, sticky="W", columnspan=4)

        self.change_button = tkinter.Button(self.frm, text="Change dir",
                                            command=self.change_dir, width=button_width,
                                            background="green", foreground="white",
                                            activebackground="white", activeforeground="green")
        self.change_button.grid(column=5, row=row, sticky="W")

        self.reset_button = tkinter.Button(self.frm, text=" reset to HOME ",
                                           command=self.reset_to_home, width=button_width,
                                           background="green", foreground="white",
                                           activebackground="white", activeforeground="green")
        self.reset_button.grid(column=6, row=row, sticky="W")

        # -------------- Separator
        row += 1
        self.sep2 = self.separator(row=row, text="Change server configuration")

        # -------------- piwigo
        row += 1
        ttk.Label(self.frm, text="piwigo :", anchor="w", padding=4,
                  ).grid(column=0, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="true", text="used", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_piwigo).grid(column=1, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="false", text="unused", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_piwigo).grid(column=2, row=row, sticky="W")

        # -------------- album
        row += 1
        ttk.Label(self.frm, text="album :", anchor="w", padding=4,
                  ).grid(column=0, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="local", text="local", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_album).grid(column=1, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="mount", text="mount", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_album).grid(column=2, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="remote", text="remote", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_album).grid(column=3, row=row, sticky="W")

        # -------------- web
        row += 1
        ttk.Label(self.frm, text="web :", anchor="w", padding=4,
                  ).grid(column=0, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="local", text="local", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_web).grid(column=1, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="mount", text="mount", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_web).grid(column=2, row=row, sticky="W")

        ttk.Radiobutton(self.frm, value="remote", text="remote", command=self.refresh_default_values, width=radio_width,
                        variable=self.do_web).grid(column=3, row=row, sticky="W")

        # -------------- Separator
        row += 1
        self.separator(row=row, text="Configurator: messages")

        # -------------- Feedback
        row += 1

        font = tkinter.font.Font(size=10, family="Courier")
        self.msg = scrolledtext.ScrolledText(self.frm, background="#e00e00e00",
                                             padx=3, pady=3,
                                             font=font,
                                             width=140, height=5,
                                             )
        self.msg.grid(column=0, row=row, columnspan=7)
        self.msg.tag_config('warning', foreground="red")

        # -------------- Separator
        row += 1
        self.sep3 = self.separator(row=row, text="Change settings")

        # -------------- Variable items
        row += 1
        self.max_common_row = row
        self.reset_to_home()
        if father.args.test:
            self.root.after(1 * 1000, lambda: PwpDirChooser(self, os.path.dirname(self.do_file['text']),
                                                            self_test=True))
            self.root.after(2 * 1000, self.next)
            self.root.after(3 * 1000, self.back)
            self.root.after(5 * 1000, self.exit)
        self.from_python_to_ui()

    def separator(self, row, text):
        tkinter.Frame(self.frm, width=900, height=15, ).grid(column=0, row=row, columnspan=8)  # noqa

        tkinter.Frame(self.frm, width=900, height=5, relief='sunken', background="#ccccccccc",
                      ).grid(column=0, row=row, columnspan=8)  # noqa

        sep = ttk.Label(self.frm, text=text, padding=4)
        sep.grid(column=0, row=row, columnspan=8)
        return sep

    def main_loop(self):
        self.root.mainloop()
        self.root.quit()

    def select_dir(self, path):
        self.configurator.set_dir(path)
        self.do_file['text'] = self.configurator.file

    def change_dir(self):
        PwpDirChooser(self, os.path.dirname(self.do_file['text']))

    def reset_to_home(self):
        self.select_dir(self.configurator.home)

    def refresh_default_values(self):
        self.from_ui_to_python()
        self.configurator.compute_values()
        self.from_python_to_ui()

    def from_python_to_ui(self):
        self.txt_language['text'] = "language :" if self.configurator.language == "en" else "langue :"

        self.sep1['text'] = ("Change ini file to build" if self.configurator.language == "en" else
                             "Changer le fichier .ini à construire")
        self.sep2['text'] = ("Change piwigo server configuration" if self.configurator.language == "en" else
                             "Changer la configuration du serveur piwigo")

        self.sep3['text'] = ("Change settings" if self.configurator.language == "en" else
                             "Changer les valeurs")

        self.do_language.set(self.configurator.language)
        self.do_piwigo.set(self.configurator.piwigo)
        self.do_album.set(self.configurator.album)
        self.do_web.set(self.configurator.web)

        # self.configurator.compute_values()
        row = self.max_common_row

        if self.stage == 0:
            self.next_button.grid(column=self.menu_column, row=self.menu_row, sticky="W")
            self.back_button.grid_remove()
            self.run_button.grid_remove()
        else:
            self.next_button.grid_remove()
            self.back_button.grid(column=self.menu_column, row=self.menu_row, sticky="W")
            self.run_button.grid(column=self.menu_column + 1, row=self.menu_row, sticky="W")

        for name in self.fields:
            self.fields[name].delete()

        radio_width = 10
        self.fields = {}
        password = None  # we need to set a specific variable for the ONLY password entry

        for name in self.configurator.items:
            father: 'PwpConfigurator' = self.configurator
            current = father.get_values(name)
            if current.name is None or current.state == VST.SILENT:
                continue
            if self.stage == 0 and current.state == VST.BOOL:
                continue
            if self.stage == 1 and current.state != VST.BOOL:
                continue

            label = ttk.Label(self.frm, text=name, anchor="w", padding=4)
            label.grid(column=0, row=row, sticky="W")

            variable = tkinter.StringVar()
            variable.set(current.value)

            off_var = None
            if current.state == VST.BOOL:
                item = ttk.Radiobutton(self.frm, value="true", text="true", width=radio_width, variable=variable)
                item.grid(column=1, row=row, sticky="W")
                off_var = ttk.Radiobutton(self.frm, value="false", text="false", width=radio_width, variable=variable)
                off_var.grid(column=2, row=row, sticky="W")
            elif current.state == VST.PASSWORD:
                item = tkinter.Entry(self.frm, background="#dddFFFddd", width=45, textvariable=variable, show='*')
                item.grid(column=1, row=row, sticky="W", columnspan=2)
                password = item
                off_var = tkinter.Button(self.frm, text=" Show/Hide",
                                         command=lambda: self.show_password(password),
                                         # this works only because there is only 1 password entry
                                         background="green", foreground="white",
                                         activebackground="white", activeforeground="green")
                off_var.grid(column=3, row=row, sticky="W")
            else:
                item = tkinter.Entry(self.frm, background="#dddFFFddd", width=75, textvariable=variable)
                item.grid(column=1, row=row, sticky="W", columnspan=3)

            help_var = ttk.Label(self.frm, text=current.helps, anchor="w", padding=4, width=70)
            help_var.grid(column=4, row=row, sticky="W", columnspan=3)

            self.fields[name] = Field(label, variable, item, help_var, off_var)
            row += 1

    @staticmethod
    def show_password(item: tkinter.Entry):
        item['show'] = "*" if item['show'] == '' else ''

    def from_ui_to_python(self):

        new_language = self.do_language.get() or 'en'
        new_piwigo = self.do_piwigo.get()
        new_album = self.do_album.get()
        new_web = self.do_web.get()

        if new_piwigo == "false":
            if new_album == "remote":
                new_album = "local"
                self.add_msg("WARNING : in this configuration, album = remote is not possible\n", "warning")
            new_web = "false"

        if new_piwigo == "true" and new_web == "false":
            new_web = "local"

        if (self.configurator.language != new_language or
                self.configurator.piwigo != new_piwigo or
                self.configurator.album != new_album or
                self.configurator.web != new_web):
            self.stage = 0
            self.configurator.setup_has_changed = True
        else:
            self.configurator.setup_has_changed = False

        self.configurator.language = new_language
        self.configurator.piwigo = new_piwigo
        self.configurator.album = new_album
        self.configurator.web = new_web

        for name in self.fields.keys():
            field = self.fields[name]
            self.configurator.set_value(name, field.variable.get())

    def exit(self):
        self.root.quit()

    def back(self):
        self.stage = 0
        self.refresh_default_values()

    def next(self):
        self.stage = 1
        self.refresh_default_values()

    def run(self):
        self.from_ui_to_python()
        self.configurator.run()

    def add_msg(self, line, tag=None):
        if tag is None:
            self.msg.insert(tkinter.END, line)
        else:
            self.msg.insert(tkinter.END, line, tag)
        self.msg.yview(tkinter.END)


class PwpConfigurator:
    def __init__(self, arguments=None):
        arguments = arguments or []

        self.ui = None
        parser = argparse.ArgumentParser(description='configures piwiPre on computer')
        parser.add_argument('--version',
                            help="prints help and exits",
                            action='store_true')
        parser.add_argument('--gui',
                            help="display the graphical UI",
                            action='store',
                            choices=['true', 'false'],
                            default="true")
        parser.add_argument('--test',
                            help="display the graphical UI for 5 seconds and exist, just for test",
                            action='store',
                            choices=['true', 'false'],
                            default="false")
        parser.add_argument('--chdir',
                            help="change the value of HOME. Still generates the .piwiPre.ini. Mainly used for test",
                            action='store')
        parser.add_argument('--dir',
                            help="builds piwiPre.ini (without starting '.') so HOME parameters are not built",
                            action='store')
        parser.add_argument('--piwigo',
                            help="use piwigo server",
                            action='store',
                            choices=['true', 'false'],
                            default="false")
        parser.add_argument('--album',
                            help="configuration of album directory",
                            action='store',
                            choices=['local', 'mount', 'remote'],
                            default="local")
        parser.add_argument('--web',
                            help="configuration of web directory for thumbnails",
                            action='store',
                            choices=['local', 'mount', 'remote'],
                            default="local")

        self.args = parser.parse_args(arguments)

        if self.args.version:
            print(f"pwpInstaller version {PwpVersion.spec}")
            exit(0)

        if self.args.chdir:
            if not os.path.isdir(self.args.chdir):
                os.makedirs(self.args.chdir)

        self.home = self.args.chdir or os.path.expanduser("~")

        self.build_for_home = None
        self.file = None
        self.set_dir(self.args.dir or self.home)

        self.parser = PwpParser()
        self.piwigo = CVS.TRUE if self.args.piwigo else CVS.FALSE
        self.album = CVS.LOCAL if self.args.album == "local" else CVS.MOUNT \
            if self.args.album == "mount" else CVS.REMOTE
        self.web = CVS.LOCAL if self.args.web == "local" else CVS.MOUNT if self.args.web == "mount" else CVS.REMOTE

        self.setup_has_changed = True  # if True, we need to compute again the default values
        self.items: dict[str, ItemValue] = {}

        loc, _ = locale.getlocale()
        self.language = 'fr' if loc == 'fr_FR' else 'en'
        self.compute_values()

        if self.args.gui == "false":
            self.run()
        else:
            print(f"GUI True {arguments}")
            self.ui = PwpConfigUI(self)
            self.ui.main_loop()

    def set_dir(self, path):
        path = os.path.abspath(path)
        self.build_for_home = (path == os.path.abspath(self.home))
        self.file = (path +
                     ('/' if platform.system() != "Windows" else '\\') +
                     ('.' if self.build_for_home else '') +
                     'piwiPre.ini')
        self.msg(f"target directory: {path}")
        if self.build_for_home:
            self.msg("target file: .piwiPre.ini with confidential information")
        else:
            self.msg("target file: piwiPre.ini ")

    def get_values(self, name) -> ItemValue:
        """
        get_values(self, name):
        :param name:
        :return: ItemValue
        """
        return self.items[name]

    def set_value(self, name, value):
        self.items[name].value = value

    def compute_values(self):
        if self.setup_has_changed:
            self.warning("Parameter values have changed: reset to default")
            setup = ValueSetup(piwigo=self.piwigo, album=self.album, web=self.web)
            self.items = self.parser.get_setup(setup=setup, lang=self.language)
            self.setup_has_changed = False
        pass

    def copy(self, src, dst):
        """
        copy src to dst, unless dryrun is True
        :param src: file to copy
        :param dst: destination filename
        :return: None
        """
        base = os.path.dirname(dst)
        if not os.path.isdir(base):
            os.makedirs(base, exist_ok=True)

        if not os.path.isfile(src):
            self.warning(f"FAILED copy '{src}' ->  '{dst}' : non existing source")

        shutil.copy2(src, dst)  # preserve metadata

        if os.path.isfile(dst):
            self.msg(f"copy '{src}' ->  '{dst}'")
        else:
            self.warning(f"copy '{src}' ->  '{dst}'")

    def backup(self, filename):
        if not os.path.isfile(filename):
            return

        m1 = re.match(r"(.*)\.bak$", filename)
        m2 = re.match(r"(.*)\.bak-(\d*)$", filename)
        if m1:
            bak = f"{m1.group(1)}.bak-1"
        elif m2:
            num = int(m2.group(2))
            bak = f"{m2.group(1)}.bak-{num + 1}"
        else:
            bak = filename + '.bak'

        self.backup(bak)
        self.copy(filename, bak)

    def run(self):
        # do what needs to be done
        self.backup(self.file)
        base = os.path.dirname(self.file)
        if not os.path.isdir(base):
            os.makedirs(base, exist_ok=True)

        with open(self.file, 'w', encoding="utf8") as f:
            def pp(cline: str):
                self.msg(cline)
                f.write(cline + "\n")

            pp("# file generated by piwiPre Configurator")
            pp("#")
            pp(f"# file    =  '{self.file}'")
            pp("#")
            pp(f"# piwigo  =  '{self.piwigo}'")
            pp(f"# album   =  '{self.album}'")
            pp(f"# web     =  '{self.web}'")
            pp("#")

            pp(f"language :  '{self.language}'")
            for k in self.items:
                uv = self.items[k].value
                val = (uv if uv in ["", 'true', 'false', 'TRIAGE', 'BACKUP', 'ALBUM', 'WEB', 'fr', 'en']
                       else int(uv) if self.items[k].i_type == int
                       else f'{self.items[k].value}')
                line = f"{k} : {val}"
                n = max(60 - len(line), 0)
                helps = self.items[k].helps
                pp(f"{line} {' ' * n} # {helps}")

            non_set = self.parser.get_non_setup(ValueSetup(piwigo=self.piwigo, album=self.album, web=self.web),
                                                self.language)

            pp("")
            pp("# Other values that you MAY want to change, even if this is not usual")
            pp("")

            for k in non_set:
                line = f"# {k} : "
                n = max(60 - len(line), 0)
                helps = non_set[k].helps
                pp(f"{line} {' ' * n} # {helps}")

        self.msg(f"Generated  '{self.file}' ")

    def msg(self, line):
        if self.ui:
            self.ui.add_msg(line + "\n")
        print(line)

    def warning(self, line):
        if self.ui:
            self.ui.add_msg("WARNING : " + line + '\n', "warning")

        print(termcolor.colored("WARNING : " + line, color='red', force_color=True))


def configurator_console():
    if '--gui' in sys.argv:
        PwpConfigurator(sys.argv[1:])
    else:
        PwpConfigurator(sys.argv[1:] + ['--gui', 'false'])


def configurator_gui():
    if '--gui' in sys.argv:
        PwpConfigurator(sys.argv[1:])
    else:
        PwpConfigurator(sys.argv[1:] + ['--gui', 'true'])


if __name__ == "__main__":
    PwpConfigurator(sys.argv[1:])
