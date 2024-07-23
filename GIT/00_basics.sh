# Instruction
# https://youtu.be/8JJ101D3knE?si=BJh0N-Qf4W3AWqlc


# Download git
$ sudo apt install git

# Configuration levels:
- system    # All users
- global    # All repositories of the current usre
- local     # THe current repository


#############
# Setup git #
#############

$ git config --global user.name "NAME"
$ git config --global user.email EMAIL@gmail.com
# set default editor
$ git config --global core.editor "nv"
# edit git global settings with default editor
$ git config --global -e
# How git should handle end of lines
# Windows: \r\n
# "\r" cariege return (CR) and "\n" new line (LF)
$ git config --global core.autocrlf true
# Linux: \n
# "\n" new line
$ git config --global core.autocrlf input

# Set up diff tool
# Set name for difftool. "vscode" not associated with any binary.
$ git config --global diff.tool vscode
# There are some tools for diff:
# KDiff3, P4Merge, WinMerge (Windows only), VSCode.
# How to launch vscode
$ git config --global difftool.vscode.cmd "code --wait --diff $LOCAL $REMOTE"

# Set up diff tool for nvim
git config --global diff.tool nvim
git config --global difftool.nvim.cmd "nvim -d $LOCAL $REMOTE"
# Check that settings applyed (usually 'local remote' part missing)
$ git config --global -e

   



############
# COMMANDS #
############

# 1. Create project folder

$ mkdir myproject


# 2. Initialise repository
# Once you have Git installed, the next step is to initialize
# a new repository. To do this, navigate to the root directory
# of your project in the command line or terminal and run the
# command git init. This will create a new .git directory in
# your project's root directory, which is where Git stores all
# of its metadata and version control information.
$ git init


# 3. Add files
# Once you'v created some files inside the dirrectory
# The next step is to start tracking changes to your
# project by adding files to the staging area.

# Add all files in current dir
$ git add -A

# Also there is:
$ git add .
# But it doesnt stage deletions.


# 4. Commit changes
# After adding files to the staging area, the next
# step is to commit the changes to your repository
# using the git commit command.

# When committing changes, it's important to provide
# a clear and descriptive message that explains what
# changes you made in the commit. This message will
# be used to track the changes in the repository's
# history and will help other contributors understand
# the changes you made.

$ git commit -m "Repository created."


# 5. Connect to a Remote Repository

# To share your changes with other developers or
# collaborate on a project, you can connect your local
# repository to a remote repository using Git.

# A remote repository is a copy of your repository that
# is hosted on a server, such as GitHub, GitLab, or
# BitBucket, and allows multiple contributors to work
# on the same codebase.

# To connect to a remote repository, use the git remote
# add command followed by the URL of the remote repository.

$ git remote add origin <repository URL>


# 6. Push your changes

# Once connected, you can push your changes to the remote
# repository using this git push -u <default branch> command.
# This command is often used when pushing changes for the
# first time to establish the relationship between the local
# branch and the remote branch.

$ git push -u <default branch>
# git push -u origin master
# # Or just
# git push




# 7. Fetches the latest changes

# The git pull command fetches the latest changes made by
# other contributors from a remote repository and automatically
# merges them into the current branch. By connecting to a remote
# repository, you can collaborate with other developers and
# contribute to open-source projects.

$ git pull


# 8. Create a branch
$ git branch <branch-name>


# 9. Switch to the branch

$ git checkout <branch-name>


# 10. Combine 8 & 9
$ git checkout -b <branch-name>



#############
#    PRO    #
#############

# 11. Merge branches

# To merge branches with git in the terminal, follow these steps:
#1. Ensure you are in the branch where you want to merge the changes. You can check by using the command git branch.
#2. Use the command git merge <branch_name> to merge the changes from <branch_name> into your current branch.
#3. Resolve any conflicts that arise during the merge process. Git will notify you of any conflicts and provide instructions on how to resolve them.
#4. After resolving any conflicts, add the changes to the staging area using git add and commit the merge using git commit.
#5. If you are using a remote repository, you may need to push the changes to the remote repository using git push.
#That's it! You have successfully merged the branches using Git in the terminal.

$ git merge <branch_name>

# After merging there no need to do "git add -A" and "git commit -m 'merge' "

# 12. Delete branch localy

$ git branch -d <branch>

# 13. Delete branch remotely

$ git push <remote> --delete <branch>


# 14. Rename branch
$ git branch -m main develop
# Push the renamed branch:
$ git push -u origin develop
   

# 15. 


#####################
# WORK WITH DEAFULT #
#####################

$ git symbolic-ref HEAD refs/heads/main
$ git branch -d master
