
# show all wariables of the system
declare -p

# create variable
declare myvariable

# give it a value
declare myvariable=22

# create read only var
declare -r pwdfile=/etc/passwd
echo $pwdfile
pwdfile=/etc/abc	# returns an error




