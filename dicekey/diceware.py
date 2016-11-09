#    Dicekey. A Diceware passphrase generator.
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
import re


class Gen:

    def __init__(self):
        self.wordlist = {}
        self.PRNG = random.SystemRandom()

    # Generate Diceware numbers
    def numgen(self, length=1):
        numlist = []

        for _ in range(length):
            number = ""

            for _ in range(5):
                digit = self.PRNG.randint(1, 6)
                number = number + str(digit)

            numlist.append(number)

        return numlist


    # Load list of numbers/words
    def loadlist(self, listloc):
        listfile = open(listloc, "Ur")
        data = listfile.readlines()

        for line in data:
            if not line.find("\t") is -1:
                number, word = line[:-1].split("\t", 1)

                if re.match("^[1-6]{5}$", number):
                    if not number in self.wordlist:
                        self.wordlist[number] = word

        # Ensure the list is complete
        if len(self.wordlist) == 7776:
            return self.wordlist
        else:
            self.wordlist = None
            return None


    # Generate passphrase
    def wordgen(self, length):
        words = []

        for dicenum in self.numgen(length):
            words.append(self.wordlist[dicenum])

        return words
