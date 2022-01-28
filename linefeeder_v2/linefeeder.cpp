// code in this file is not written by me
// this is mix of c and c++

#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <iostream>


void
read_from_pipe (int file)
{
  int fd_dup = dup(file);
  FILE *stream;
  int c;
  stream = fdopen (fd_dup, "r");
  while ((c = fgetc (stream)) != EOF && c!= '\n')
    putchar (c);
  putchar('\n');
  fclose (stream);
}

/* Write some random text to the pipe. */

void
write_to_pipe (int file, const char* line)
{
  int fd_dup = dup(file);
  FILE *stream;
  stream = fdopen (fd_dup, "w");
  fprintf (stream, line);
  fprintf (stream, "\n");
  fclose (stream);
}

int main(int argc, char *argv[]){
  pid_t pid;
  int inpipe[2];  
  int outpipe[2];
  pipe(inpipe);
  pipe(outpipe);
  
  if (argc < 2){
    std::cout << "Usage: ./a.out ./delayer.sh < data" << std::endl;
    return -1;
  }

  /* Create the child process. */
  pid = fork ();
  if (pid == (pid_t) 0){
    close(inpipe[1]);
    close(outpipe[0]);

    close(0);
    dup(inpipe[0]);
    close(inpipe[0]);
    close(1);
    dup(outpipe[1]);
    close(outpipe[1]);

    execvp(argv[1], argv+1);

    return EXIT_SUCCESS;

  } else if (pid < (pid_t) 0){
    fprintf (stderr, "Fork failed.\n");
    return EXIT_FAILURE;

  } else {

    close(inpipe[0]);
    close(outpipe[1]);
    std::stringstream ss;
    ss << argv[2];
    if (argc >= 4) {
      ss << " " << argv[3];
    }
 
    write_to_pipe(inpipe[1], ss.str().c_str());
    read_from_pipe(outpipe[0]);
    for(std::string s; std::getline(std::cin, s);){
      write_to_pipe(inpipe[1], s.c_str());
      read_from_pipe(outpipe[0]);
    }
    
    return EXIT_SUCCESS;
  }
}
