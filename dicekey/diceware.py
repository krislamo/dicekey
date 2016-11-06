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
import random


# Generate Diceware numbers
def numgen(length=1):
    numlist = []

    for _ in range(length):
        number = ""

        for _ in range(5):
            PRNG = random.SystemRandom()
            digit = PRNG.randint(1, 6)
            number = number + str(digit)

        numlist.append(number)

    return numlist
