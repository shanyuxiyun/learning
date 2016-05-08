#/bin/bash

rename_file()
{
  echo $1;
  echo $0;
}

[ -d ~/Desktop  -a ! -L ~/desktop ] && ln -s ~/Desktop ~/desktop
[ -d ~/Documents -a ! -L ~/documents ] && ln -s ~/Documents ~/documents
[ -d ~/Downloads -a ! -L ~/downloads ] && ln -s ~/Downloads ~/downloads
[ -d ~/Pictures -a ! -L ~/pictures ] && ln -s ~/Pictures ~/pictures
[ -d ~/Music -a ! -L ~/music ] && ln -s ~/Music ~/music
[ -d ~/Pictures -a ! -L ~/pictures ] && ln -s ~/Pictures ~/pictures
[ -d ~/Videos -a ! -L ~/videos ] && ln -s ~/Videos ~/videos

