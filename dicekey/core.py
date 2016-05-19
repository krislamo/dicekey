#    Dicekey. A Diceware password generator.
#    Copyright (C) 2016  Kris Lamoureux
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
import Tkinter as tk

# Local
import diceware


class GUI:

    def __init__(self, master):

        frame = tk.Frame(master, padx=50, pady=50)
        frame.pack()

        msgtxt = "Here are some random Diceware numbers for you!"
        msg = tk.Label(frame, pady=15, font=("Arial", 16), text=msgtxt)
        msg.pack()

        for number in diceware.numgen(7):
            text = tk.Label(frame, font=("FreeMono", 16), text=number)
            text.pack()


def main():

    root = tk.Tk()
    root.wm_title("Dicekey – Password Generator")
    interface = GUI(root)

    root.mainloop()
    sys.exit(0)


if __name__ == "dicekey.core":
    main()
