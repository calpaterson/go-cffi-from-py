pyhello.o: hello.so hello_ffi_builder.py
	./hello_ffi_builder.py

hello.so: hello.go
	go build --buildmode=c-shared -o hello.so hello.go

run: pyhello.o
	LD_LIBRARY_PATH=$(shell pwd) ./hello.py
