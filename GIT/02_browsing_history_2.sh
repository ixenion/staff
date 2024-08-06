# See first part
# 02_browsing_history_1.sh

######################
#  VIEWING A COMMIT  #
######################

# 14. Go to the HEAD (last commit) and go 2 steps back
$ git show HEAD~2
# Output
'
commit 555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:26:49 2020 -0700

    Include the note about committing after staging the changes.

diff --git a/sections/creating-snapshots/staging-changes.txt b/sections/creating-snapshots/staging-changes.txt
index bddf7bd..506a158 100644
--- a/sections/creating-snapshots/staging-changes.txt
+++ b/sections/creating-snapshots/staging-changes.txt
@@ -7,3 +7,5 @@ To stage the changes, run:
 You can add multiple files separated by a space. 
 You can use a . to add all the files and subdirectories recursively.
 
+Once you stage the changes, you need to commit them to store the 
+proposed snapshot permanently. 
\ No newline at end of file
'

# But if we dont want to see changes,
# only final version in this commit?
# 15. Final version of the file stored in this commit:
$ git show HEAD~2:sections/creating-snapshots/staging-changes.txt
# Output:
'
STAGING CHANGES 
===============
To stage the changes, run:

> git add <filename>

You can add multiple files separated by a space. 
You can use a . to add all the files and subdirectories recursively.

Once you stage the changes, you need to commit them to store the 
proposed snapshot permanently.
'

# 16. Don't show changes, just files that have been modifyed.
# Shows only files that are modifyed, moved or deleted
# in this commit.
$ git show HEAD~2 --name-only
# Output
'
commit 555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:26:49 2020 -0700

    Include the note about committing after staging the changes.

sections/creating-snapshots/staging-changes.txt
'

# But additionally we cant see which was modifyed
# and which was deleted, so:
# 17. Show files changed with this information
$ git show HEAD~2 --name-status
# OUtput
'
commit 555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:26:49 2020 -0700

    Include the note about committing after staging the changes.

M       sections/creating-snapshots/staging-changes.txt
'



########################################
#  VIEWING THE CHANGES ACROSS COMMITS  #
########################################

# 18. Show diff across two commits
$ git diff HEAD~1 HEAD
# Output
'
diff --git a/audience.txt b/audience.txt
index 6b3f8f5..4cfef55 100644
--- a/audience.txt
+++ b/audience.txt
@@ -1,2 +1,4 @@
+AUDIENCE 
+
 This course is for anyone who wants to learn Git. 
-No prior experience is required.
+No prior experience is required.
\ No newline at end of file
...
'

# 19. Changes of a particular file
$ git diff HEAD~1 HEAD audience.txt

# 20. File names only across commits
$ git diff HEAD~1 HEAD --name-only
# Output
'
audience.txt
objectives.txt
sections/creating-snapshots/init.txt
sections/creating-snapshots/staging-changes.txt
toc.txt
'

# 21. Name and status
$ git diff HEAD~1 HEAD --name-status
# Output
'
M       audience.txt
M       objectives.txt
M       sections/creating-snapshots/init.txt
M       sections/creating-snapshots/staging-changes.txt
M       toc.txt
'



###########################
#  CHECKING OUT A COMMIT  #
###########################

# So this is the current log
$ git log --oneline
# Output
'
a642e12 (HEAD -> master) Add header to all pages.
50db987 Include the first section in TOC.
555b62e Include the note about committing after staging the changes.
91f7d40 Explain various ways to stage changes.
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 Initial commit.
'
# 22. Now I can restore working directory to the particular commit
$ git checkout dad47ed
# WARNING
# But here (in detached HEAD state) we should avodi creating
# commits, because this new commit is not reachable by any other
# commits or pointers. So it's like a dead commit.
# Git checks for commits like that periodically and
# removes them to save space.

# Check log
$ git log --oneline
# Output
'
dad47ed (HEAD) Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 Initial commit.
'
# To see all branches
$ git log --oneline --all
# Output
'
a642e12 (master) Add header to all pages.
50db987 Include the first section in TOC.
555b62e Include the note about committing after staging the changes.
91f7d40 Explain various ways to stage changes.
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed (HEAD) Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 Initial commit.
'

# 23. Attach HEAD pointer back to the last commit (master branch)
$ git checkout master



###############################
#  FINDING BUGS USING BISECT  #
###############################

# Fid 'bad' commit.
# 24. Enter 'bisect'
$ git bisect start

# 25. Tell git that last commit is 'bad' commit
$ git bisect bad

# Check git log
$ git log --oneline
# Output
'
a642e12 (HEAD -> master, refs/bisect/bad) Add header to all pages.
50db987 Include the first section in TOC.
555b62e Include the note about committing after staging the changes.
91f7d40 Explain various ways to stage changes.
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 Initial commit.
'

# 26. Tell git that last commit is 'bad' commit
$ git bisect good ca49180
# Output
'
Bisecting: 5 revisions left to test after this (roughly 3 steps)
[36cd6db402cfd897810d4cb33d97ac1e9d1ce2d8] Include the command prompt in code sample.
'
# And now Im no commit 36cd6db (6 commits before last)
# Run git log one more time
# Output
'
36cd6db (HEAD) Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 (refs/bisect/good-ca4918083ec471878d58612142572f3367faf5fd) Initial commit.
'
# And one more but all
$ git log --oneline --all
# Output
'
a642e12 (master, refs/bisect/bad) Add header to all pages.
50db987 Include the first section in TOC.
555b62e Include the note about committing after staging the changes.
91f7d40 Explain various ways to stage changes.
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db (HEAD) Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 (refs/bisect/good-ca4918083ec471878d58612142572f3367faf5fd) Initial commit.
'
# HEAD is not poining at the master any more.
# Now it's in the middle between good (ca49180) and bad 'a642e12'
# So, why we are here?
# We here to test our code to check if the issue is still here.
# If issue is here (36cd6db) - the bug was introdussed somewhere
# between 'ca49180' and '36cd6db'. So there is no need to examine top half.
# And opposite, if it's a good commit, the issue was introduced
# in the top half.

# So, lets assume, it's a good commit (36cd6db)
$ git bisect good
# Output
'
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[91f7d40d6d5bbc336a271607a0488216aaf50cd7] Explain various ways to stage changes.
'

# And it's a good commit also (91f7d40)
$ git bisect good   # Now we are on '50db987' commit.
# Output
'
Bisecting: 0 revisions left to test after this (roughly 1 step)
[50db98710ed4330773f1df55b2a177600d523c9e] Include the first section in TOC.
'

# And finaly, '50db987' seems to be bad (we checked it mannually or with 
# automation testing tools)
# Mark it as 'bad'
$ git bisect bad
# Output
'
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6] Include the note about committing after staging the changes.
'

# Check git log one more time
$ git log --oneline --all
# Output
'
a642e12 (master) Add header to all pages.
50db987 (refs/bisect/bad) Include the first section in TOC.
555b62e (HEAD) Include the note about committing after staging the changes.
91f7d40 (refs/bisect/good-91f7d40d6d5bbc336a271607a0488216aaf50cd7) Explain various ways to stage changes.
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db (refs/bisect/good-36cd6db402cfd897810d4cb33d97ac1e9d1ce2d8) Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
fb0d184 Define the audience.
1ebb7a7 Define the objectives.
ca49180 (refs/bisect/good-ca4918083ec471878d58612142572f3367faf5fd) Initial commit.
'

# Now we are down to '555b62e' commit.
# And lets assume it's bad too
$ git bisect bad
# Output
'
555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6 is the first bad commit
commit 555b62e1ebb92c97fc69910ad0981a7d6dbbf8c6
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:26:49 2020 -0700

    Include the note about committing after staging the changes.

 sections/creating-snapshots/staging-changes.txt | 2 ++
 1 file changed, 2 insertions(+)
'
# And now git knows first 'bad' commit.
# We have full information about this commit.
# When we are done, we have to attach the HEAD pointer to the 'master' branch.
# 27. So we do reset
$ git bisect reset
# Output
'
Previous HEAD position was 555b62e Include the note about committing after staging the changes.
Switched to branch 'master'
'
# Now we are on 'master'



#########################################
#  FINDING CONTRIBUTORS USING SHORTLOG  #
#########################################

# 28. Find all people that have commited to our project
$ git shortlog
# Output
'
Moshfegh Hamedani (13):
      Initial commit.
      Define the objectives.
      Define the audience.
      Write the first draft of initializing a repo.
      Include the warning about removing .git directory.
      Add a header to the page about initializing a repo.
      Include the command prompt in code sample.
      Add command line and GUI tools to the objectives.
      First draft of staging changes.
      Explain various ways to stage changes.
      Include the note about committing after staging the changes.
      Include the first section in TOC.
      Add header to all pages.
'

# 29. Sort output based on the number of commits (-n)
$ git shortlog -n
# Output
# Same as above

# 30. Sort output based on the number of commits (-n)
# and suppress commit messages (-s)
$ git shortlog -n -s
# Output
'
13  Moshfegh Hamedani
'


# For more keys use
$ git shortlog -h
# Output
'
usage: git shortlog [<options>] [<revision-range>] [[--] <path>...]
   or: git log --pretty=short | git shortlog [<options>]

    -c, --committer       group by committer rather than author
    -n, --numbered        sort output according to the number of commits per author
    -s, --summary         suppress commit descriptions, only provides commit count
    -e, --email           show the email address of each author
    -w[<w>[,<i1>[,<i2>]]]
                          linewrap output
    --group <field>       group by field
'

# Also we can use 'before' and 'after' options as we talked earlier etc.



###################################
#  VIEWING THE HISTORY OF A FILE  #
###################################

# 31. Lets find all the commits that have touched the file
$ git log toc.txt
# Output
'
commit a642e1229e3cb69be9bf075d9fe5e752e9a17458 (HEAD -> master)
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Tue Aug 18 09:23:19 2020 -0700

    Add header to all pages.

commit 50db98710ed4330773f1df55b2a177600d523c9e
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:27:50 2020 -0700

    Include the first section in TOC.

commit ca4918083ec471878d58612142572f3367faf5fd
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:17:15 2020 -0700

    Initial commit.
'

# 32. Get changes with statistics
$ git log --oneline --stat toc.txt
# Output
'
a642e12 (HEAD -> master) Add header to all pages.
 toc.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
50db987 Include the first section in TOC.
 toc.txt | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
ca49180 Initial commit.
 toc.txt | 1 +
 1 file changed, 1 insertion(+)
'

# 33. View tha actual changes
$ git log --oneline --patch toc.txt
# Output
'
a642e12 (HEAD -> master) Add header to all pages.
diff --git a/toc.txt b/toc.txt
index d019492..cc0798f 100644
--- a/toc.txt
+++ b/toc.txt
@@ -1,5 +1,5 @@
 TABLE OF CONTENT
-================
+
 Creating Snapshots
   - Initializing a repository
   - Staging changes
\ No newline at end of file
50db987 Include the first section in TOC.
diff --git a/toc.txt b/toc.txt
index 8b13789..d019492 100644
--- a/toc.txt
+++ b/toc.txt
@@ -1 +1,5 @@
-
+TABLE OF CONTENT
+================
+Creating Snapshots
+  - Initializing a repository
+  - Staging changes
\ No newline at end of file
...
'


##############################
#  RESTORING A DELETED FILE  #
##############################

# Recover deleted file from the history
# So, 'acidently' remove file:
$ git rm toc.txt
$ git commit -m "Removed toc.txt"
# Now find all commits that touched 'toc.txt'
$ git log --oneline -- toc.txt
# Output
'
9bd8f08 (HEAD -> master) Removed toc.txt.
a642e12 Add header to all pages.
50db987 Include the first section in TOC.
ca49180 Initial commit.
'
# To restore the file, we should look at 'a642e12'
# with the latest wesion of the file.

# 34. Check out only deleted file
$ git checkout a642e12 toc.txt
# Output
'
Updated 1 path from 246d37c
'
# Git status
$ git status -s
# Output
'
A  toc.txt
'

# Restore deleted file.
$ git commit -m "Restore toc.txt"



############################################
#  FINDING THE AUTHOR OF LINE USING BLAME  #
############################################

# 35. Find author with file
$ git blame -e audience.txt
# -e    show email
# Output
'
a642e122 (<moshfegh@live.com.au> 2020-08-18 09:23:19 -0700 1) AUDIENCE 
a642e122 (<moshfegh@live.com.au> 2020-08-18 09:23:19 -0700 2) 
fb0d184c (<moshfegh@live.com.au> 2020-08-17 14:18:09 -0700 3) This course is for anyone who wants to learn Git. 
a642e122 (<moshfegh@live.com.au> 2020-08-18 09:23:19 -0700 4) No prior experience is required.
'

# If there are a lots of changes (commits), we can show only a few
# 36. Show first three lines
$ git blame -e -L 1,3 audience.txt
# -e    show email
# -L    set interval to show
# Output
'
a642e122 (<moshfegh@live.com.au> 2020-08-18 09:23:19 -0700 1) AUDIENCE 
a642e122 (<moshfegh@live.com.au> 2020-08-18 09:23:19 -0700 2) 
fb0d184c (<moshfegh@live.com.au> 2020-08-17 14:18:09 -0700 3) This course is for anyone who wants to learn Git.
'



#############
#  TAGGING  #
#############

# 37. Give tag (version in this particular case) to the last commit
$ git tag v1.0.0
# It's just a reference, a pointer to a particullar commit.

# Tag previous commits
$ git tag v1.0.0 a642e12
# Output
'
6035e56 (HEAD -> master) Restore toc.txt
9bd8f08 Removed toc.txt.
a642e12 (tag: v1.0.0) Add header to all pages.
50db987 Include the first section in TOC.
555b62e Include the note about committing after staging the changes.
91f7d40 Explain various ways to stage changes.
...
'

# So now we can reference this commit by tag
# Checkout commit
$ git checkout v1.0.0

# See all tags w ehave created
$ git tag


# ANNOTATED TAG
$ git tag -a v1.1.0 -m "My version 1.1.0"
# -a    for annotated
# -m    supply message
# So we assotiated message with a tag.
# Now lets have a look at tags
$ git tag -n
# -n    Show tag messages
# Output
'
v1.0.0          Add header to all pages.
v1.1.0          My version 1.1.0
'

# Additional info aboubt annotated tag
$ git show v1.1.0
# Output
'
tag v1.1.0
Tagger: ixenion <stridjj@gmail.com>
Date:   Tue Aug 6 23:50:21 2024 +0300

My version 1.1.0

commit 6035e5630bba3b264647e4ac7b2c3335d0e32ce9 (HEAD -> master, tag: v1.1.0)
Author: ixenion <stridjj@gmail.com>
Date:   Tue Aug 6 23:37:52 2024 +0300

    Restore toc.txt

diff --git a/toc.txt b/toc.txt
new file mode 100644
index 0000000..cc0798f
...
'

# 38. Delete tag
$ git tag -d v1.1.0
