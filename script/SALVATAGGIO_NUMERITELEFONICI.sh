#!/bin/sh

#Il primo parametro indica quanto tempo aspettare dopo averli finiti, il secondo che gruppo prendere di utenti da processare e il terzo indica dopo quato fare unfollow
while [ true ] ; do

python3 ../InstagramGetFollows/RICERCA_INFLUENCER_prova.py $1 $2 $3

done

