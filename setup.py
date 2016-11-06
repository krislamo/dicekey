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
from distutils.core import setup

NAME = "Dicekey"
VERSION = "1.2.0-prealpha"
AUTHOR = "Kris Lamoureux"
AUTHOR_EMAIL = "KrisPublicEmail@gmail.com"
URL = "https://github.com/Kris619/Dicekey/"
DESCRIPTION = "A Diceware password generator"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="GNU GPLv3",
    url=URL,
    scripts = ["dicekey/dicekey"],
    py_modules = ["dicekey.core", "dicekey.diceware"],
    package_data={"dicekey": ["dicekey/wordlist.asc"]}
    )
