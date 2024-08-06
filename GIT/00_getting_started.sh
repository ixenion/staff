#######################
#   GETTING STARTED   #
#######################


# SOURCE
# https://youtu.be/8JJ101D3knE?si=BJh0N-Qf4W3AWqlc
# FULL COURSE
# https://codewithmosh.com/p/the-ultimate-git-course


# Download git
$ sudo apt install git

# Configuration levels:
- system    # All users
- global    # All repositories of the current usre
- local     # The current repository


#############
# Setup git #
#############

$ git config --global user.name "NAME"
$ git config --global user.email EMAIL@gmail.com
# set default editor
$ git config --global core.editor "nvim"
# edit git global settings with default editor
$ git config --global -e
# How git should handle end of lines
# Windows: \r\n
# "\r" cariege return (CR) and "\n" new line (LF)
$ git config --global core.autocrlf true
# Linux: \n
# "\n" new line
$ git config --global core.autocrlf input

# Set up diff tool for VSCode
# Set name for difftool. "vscode" not associated with any binary.
$ git config --global diff.tool vscode
# There are some tools for diff:
# KDiff3, P4Merge, WinMerge (Windows only), VSCode.
# How to launch vscode
$ git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"

# Set up diff tool for neo-vim
git config --global diff.tool nvim
git config --global difftool.nvim.cmd "nvim -d $LOCAL $REMOTE"
# Check that settings applyed (usually 'local remote' part missing)
$ git config --global -e
