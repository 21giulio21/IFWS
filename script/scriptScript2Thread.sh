#!/bin/sh

#Il primo parametro indica quanto tempo aspettare dopo averli finiti, il secondo che gruppo prendere di utenti da processare
while [ true ] ; do

python ../InstagramGetFollows/script2Thread.py $1 $2

done

