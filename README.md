# build docker
sudo docker build . -t ws281x-docker-try

# run docker image
sudo  docker run --privileged ws281x-docker-try

# run docker image detached
sudo  docker run -d --privileged ws281x-docker-try
