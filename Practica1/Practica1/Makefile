CC=g++
CFLAGS=-Wall
main=Practica1
##link
$(main): $(main).o
    $(CC) $(CFLAGS) $(main).o -o $(main)

$(main):o: $(main).cpp
    $(CC) $(main).cpp -c

##clear
clean:
    rm -rf *.o $(main)
