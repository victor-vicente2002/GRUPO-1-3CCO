#!/bin/bash

sudo systemctl start
sudo docker container start algas
sudo docker status algas
sudo docker exec -it algas bash
