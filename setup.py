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

from setuptools import setup

NAME = "dicekey"
VERSION = "0.0.1"
AUTHOR = "Kris Lamoureux"
AUTHOR_EMAIL = "kris@lamoureux.io"
URL = "https://git.krislamo.org/kris/dicekey"
DESCRIPTION = "A Diceware passphrase generator"

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="GNU GPLv3",
    url=URL,
    py_modules = ["dicekey.diceware"],
    data_files = [("dicekey/wordlist.asc", '')],
    entry_points={
        'console_scripts': [
            'dicekey = dicekey.main:main',
        ],
    },
)
