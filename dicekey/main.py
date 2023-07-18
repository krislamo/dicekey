#!/usr/bin/env python3

#    Dicekey. A Diceware passphrase generator.
#    Copyright (C) 2016, 2023  Kris Lamoureux
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Built-in
import sys
import tkinter as tk

# Local
from dicekey import diceware


class App:

    def __init__(self, master, passgen):

        frame = tk.Frame(master, padx=50, pady=50)
        frame.pack()

        msgtxt = "Here is a strong random passphrase for you!"
        msg = tk.Label(frame, pady=15, font=("Arial", 16), text=msgtxt)
        msg.pack()

        passwd = ' '.join(passgen.wordgen(7))
        text = tk.Label(frame, font=("FreeMono", 16), text=passwd)
        text.pack()


def main():

    pwgen = diceware.Gen()
    wordlist = pwgen.loadlist("dicekey/wordlist.asc")

    if len(sys.argv) > 1:
        if wordlist:
            if sys.argv[1].isdigit():
                print(' '.join(pwgen.wordgen(int(sys.argv[1]))))
            else:
                error = "Error: Argument '%s' is not an integer."
                print(error % (sys.argv[1]))
        else:
            print("Error: Incomplete or missing word list.")

    else:
        root = tk.Tk()
        root.wm_title("Dicekey - Passphrase Generator")
        app = App(root, pwgen)

        root.mainloop()

    sys.exit(0)


if __name__ == "__main__":
    main()
