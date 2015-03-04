
all:

	python3 tool/cythonize.py build_ext --build-lib src

test:

	find src -name "*.py" -type f | xargs python3 -m doctest

testv:

	find src -name "*.py" -type f | xargs python3 -m doctest -v

clean:

	rm -f src/*.c
	rm -f src/*.so
	rm -rf build/
	rm -rf __pycache__/

boot:

	pip3 install numpy
	pip3 install cython
