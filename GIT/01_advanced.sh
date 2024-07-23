############
# ADVANCED #
############


# 1. Delete file
$ rm file1.txt
$ git add file1.txt
# Or
$ git rm file1.txt


# 2. Move file
$ git mv file1.txt file2.txt


# 3. Commit in one step
$ echo "test" > file1.txt
$ git commit -am "Some changes"


# 4. Check staged files
$ git ls-files


# 5. Ignore files
$ touch .gitignore
# Then fill in ".gitignore"
# Example:
# Check "02_gitignore_example.txt"


# 6. Remove files from stage but not from system
# In other word - stop tracking this file (just ignore it)
$ git rm -r --cached folder1/


# 7. Check exact changes before commiting (but after git add )
$ git diff --staged


# 8. Check exact changes before commiting
# (and before git add - aka not staged)
$ git diff


# 9. Use GUI tools for diff (check 00_basics.sh setup diff tool first)
$ git difftool --staged


# 10. Check commit history
$ git log


# 11. Short log
$ git log --oneline


# 12. Make log print from first to last
$ git log --reverse


# 13. Check exact changes in particular commit
$ git show ff9e2df
# View last commit
$ git show HEAD
# View previous commit
$ git show HEAD~1
# View particular file (without diff, just full content)
$ git show HEAD~1:bin/app.bin
# View commit tree, to get particular file (blob) or folder (tree) uid
$ git ls-tree HEAD~1
# Then can view content of file by uid
$ git show 1dcc30


# GIT DATABASE OBJECTS
# a. Commits
# b. Blobs (files)
# c. Trees (directories)
# d. Tags


# 14. Unstaging changes (undo add operation - uses last commit)
$ git restore --staged file1.txt file2.txt
# Or
$ git restore --staged file*.txt
# Or restore all in staged area
$ git restore --staged .


# 15. Discard local changes
$ git restore file1.txt
# But if it was newly created file
$ git clean -fd     # -f force; -d directories


# 16. Restore file to an older version
# Simulate file deletion
$ git rm file1.js
$ git commit -m "Delete file."
# Now there are two ways: undo (revert commit) and restoring file to a previous version (not undoing commit)
# So we are gona restore file from previous commit
# Get previous commit uid
$ git log --onefile ---reverse
# Restore file from previous commit
$ git restore --source=HEAD~1 file1.txt
