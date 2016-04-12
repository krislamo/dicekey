install:
	python setup.py build
	sudo checkinstall -Dy --fstrans=no python setup.py install

clean:
	sudo rm -r build *-pak dicekey_*.deb
