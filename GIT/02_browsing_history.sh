####################
#      TOPICS      #
####################


# 1. Search for commits (by author, date, message, etc)
# 2. View a commit
# 3. Restore project to an earlier point
# 4. Compare commits
# 5. View a history of a file
# 6. Find a bad commit that introdused a bug

# SOURCE
# https://codewithmosh.com/p/the-ultimate-git-course

# Will be working with Venus.zip
# https://members.codewithmosh.com/courses/the-ultimate-git-course-1/lectures/24394028
# Download and extract it.



#########################
#  VIEWING THE HISTORY  #
#########################


# 1. Check commit history (log)
$ git log
# Shortened
$ git log --oneline


# 2. See all the files that have been changed in each commit
$ git log --oneline --stat
# Output:
'
a642e12 (HEAD -> master) Add header to all pages.
 audience.txt                                    | 4 +++-
 objectives.txt                                  | 1 +
 sections/creating-snapshots/init.txt            | 2 +-
 sections/creating-snapshots/staging-changes.txt | 2 +-
 toc.txt                                         | 2 +-
 5 files changed, 7 insertions(+), 4 deletions(-)
50db987 Include the first section in TOC.
 toc.txt | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
'

# Or full details of each commit:
$ git log --stat
# Output
'
commit a642e1229e3cb69be9bf075d9fe5e752e9a17458 (HEAD -> master)
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Tue Aug 18 09:23:19 2020 -0700

    Add header to all pages.

 audience.txt                                    | 4 +++-
 objectives.txt                                  | 1 +
 sections/creating-snapshots/init.txt            | 2 +-
 sections/creating-snapshots/staging-changes.txt | 2 +-
 toc.txt                                         | 2 +-
 5 files changed, 7 insertions(+), 4 deletions(-)

commit 50db98710ed4330773f1df55b2a177600d523c9e
Author: Moshfegh Hamedani <moshfegh@live.com.au>
Date:   Mon Aug 17 14:27:50 2020 -0700

    Include the first section in TOC.

 toc.txt | 6 +++++-
 1 file changed, 5 insertions(+), 1 deletion(-)
'

# 3. Get  actual changes in each commit:
$ git log --oneline --patch
# Output
'
a642e12 (HEAD -> master) Add header to all pages.
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
diff --git a/objectives.txt b/objectives.txt
index d31b40a..c882718 100644
--- a/objectives.txt
+++ b/objectives.txt
@@ -1,3 +1,4 @@
+OBJECTIVES 
 
 By the end of this course, you.ll be able to 
 - Create snapshots 
diff --git a/sections/creating-snapshots/init.txt b/sections/creating
-snapshots/init.txt
index 638729e..f63189e 100644
--- a/sections/creating-snapshots/init.txt
+++ b/sections/creating-snapshots/init.txt
@@ -1,5 +1,5 @@
 INITIALIZING A REPOSITORY
--------------------------
+
 The first step is to initialize a Git repository. 
 To do that run: 
 
...
'



###########################
#  FILTERING THE HISTORY  #
###########################

# 4. View last three commits
$ git log --oneline -3


# 5. Filter by author
$ git log --oneline --author="Mosh"


# 6. Filter by date
# Absolute date
$ git log --oneline --after="2020-08-17"
$ git log --oneline --before="2020-08-17"
# Relative date
$ git log --oneline --before="yesterday"
$ git log --oneline --before="one day ago"
$ git log --oneline --before="two weeks ago"
$ git log --oneline --before="three months ago"


# 7. Filter by commit message (or subject) - Case sensetive.
git log --oneline --grep="Some pattern"


# 8. Filter history by content
# Example: Find all the commits that have added
# or removed a function declaration.
$ git log --oneline -S"hello()"     # Returns commit_uid
# To see changes in the file (not whole commit)
$ git log --oneline -S"hello()" --patch
# For whole commit use
$ git show <commit_uid>


# 9. Filter the history by the range of commits
# This is all commits:
$ git log --oneline
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
# Lets filter from fb0 to edb
$ git log --oneline fb0d184..edb3594
# Output
'
edb3594 First draft of staging changes.
24e86ee Add command line and GUI tools to the objectives.
36cd6db Include the command prompt in code sample.
9b6ebfd Add a header to the page about initializing a repo.
fa1b75e Include the warning about removing .git directory.
dad47ed Write the first draft of initializing a repo.
'


# 10. Find all the commits that touch a particular file or a bunch of files.
$ git log --oneline toc.txt
# If git complains about file names
$ git log --oneline -- toc.txt
# If you want to see actual changes in this commits
$ git log --oneline --patch toc.txt



###############################
#  FORMATTING THE LOG OUTPUT  #
###############################


