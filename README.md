## 🚧 (PROJCET UNDER ACTIVE DEVELOPMENT) Orca is a litewieght gui made for dockerd
The goal of this application is to provide users a GUI to dockerd.
You can only install docker engine and not the docker desktop and this app can help you utilize docker via gui.

## What is this?
Orca is a small project that I am doing to learn about IPC, unix/tcp sockets, WSL, docker, Python, QT5. The byproduct is an app that maybe useful to those who don't want to install docker desktop on their machines but want a gui for their docker engine or to interact with dockerd.


## What this is not
Orca is not meant to be a replacement for docker-desktop, that application is huge and does too many things. Also this is not particularly fast nor feature-rich or nice looking. the goal is to learn not to disrupt the industry.


## Current state:
This app currently only shows the docker images found on host machine. in this case I am developing on windows and docker engine is running inside wsl. the docker daemon is configured to expect tcp connections on port `2375` so by doing REST API calls to `localhost:2375` we can communicate with dockerd from windows system. note wsl needs to be running otherwise the app will crash.

## To run this:
### Windows:
- Install WSL
- [Install Docker engine on wsl](https://gist.github.com/shoccho/71cdd84e23adba7838baf1ad71ed1bc5)
- [Configure dockerd to listen to tcp](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file)
- Run the main.py file
### Linux:
- Update coming soon
### MacOs:
- Update coming soon

