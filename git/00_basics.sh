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



