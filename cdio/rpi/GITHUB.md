
## Make directory

$ mkdir folder-example

## Change to directory

$ cd folder-example

## Add readme

$ nano README.md\
edit markdown file
Ctrl+X\
Enter

## See list of files in directory

$ ls

## Create repository

$ git init

## Check new GIT files

$ ls -a

## Look inside .git file

$ ls -a .git

## Add element to repository

$ git add README.md

## Add all element in directory to repository

$ git add --all

## Repository status

$ git status

## Commit file

$ git commit -am 'add README.md'

## Add more files

$ git add -all\
$ git commit -am 'add python file'

## Commit after every significant change

$ git commit -am 'added function'

## Commit history of a file

$ git log example.py

## Restore file to an earlier version

$ git log example.py\
copy hash (long string of characters after word 'commit')\
$ git checkout 'hash'\
$ git commit -am 'restore file to an earlier version'

## Push to GitHub

$ git push origin master

## Add new files, commit and push to GitHub
$ git add --all\
$ git commit -am 'description'\
$ git push origin master

## Add .gitignore

$ nano .gitignore

- *.txt (ignore all .txt files)
- file.text (ignore this file in particular)
- folder/ (ignore this folder)

Ctrl+X\
Enter\
$ git add --all\
$ git commit -am 'added gitignore'\
$ git push origin master 

## Rerefences

- [Getting started with Git](https://projects.raspberrypi.org/en/projects/getting-started-with-git)
- [Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
- [Adding a new SSH key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)

