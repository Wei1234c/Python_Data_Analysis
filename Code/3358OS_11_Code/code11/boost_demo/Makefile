CC = g++
PYLIBPATH = $(shell python-config --exec-prefix)/lib
LIB = -L$(PYLIBPATH) $(shell python-config --libs) -L ${HOME}/Boost/lib -lboost_python
OPTS = $(shell python-config --include) -O2 -I${HOME}/Boost/include

default: rain.so
	@python ./rain_demo.py

rain.so: rain.o
	$(CC) $(LIB)  -Wl,-rpath,$(PYLIBPATH) -shared $< -o $@

rain.o: boost_rain.cpp Makefile
	$(CC) $(OPTS) -c $< -o $@

clean:
	rm -rf *.so *.o

.PHONY: default clean
