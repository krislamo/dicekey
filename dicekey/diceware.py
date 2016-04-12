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
import os


# Generate Diceware numbers
def numgen(length=1):
    numlist = []

    for _ in range(length):
        number = ""

        for _ in range(5):
            bytedata = os.urandom(1)
            intdata = int(bytedata.encode("hex"), 16)
            result = intdata * 5 / 255 + 1
            number = number + str(result)

        numlist.append(number)

    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist
