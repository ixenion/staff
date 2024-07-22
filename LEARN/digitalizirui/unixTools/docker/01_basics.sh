# instruction at:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04

# weight ~ 400mb
# debian image ~ 120mb


############
# comamnds #
############

# disable docker
$ systemctl stop docker
$ systemctl disable docker

# enable docker
$ systemctl start docker

# search iso
$ docker search debian

# download latest iso
$ docker pull debian

# create container
$ docker run -it --name debian debian

# create temporary container (will be deleted after exit)
$ docker run -it --rm --name debian debian

# exit container
# (as usual terminal exit)
$ exit

# check active containers
$ docker ps

# check inactive (all) containers
$ docker ps -a

# ckeck latest used containers
$ docker ps -l

# check installed iso (images)
$ docker images

# stop container
# <id|name> can be retreived with "docker ps -a"
$ docker stop <id|name>

# start container
# <id|name> can be retreived with "docker ps -a"
$ docker start <id|name>

# remove (delete) contaimer
# <id|name> can be retreived with "docker ps -a"
$ docker rm <id|name>

# remove (delete) image
$ docker image rm <imageName>
