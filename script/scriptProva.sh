#!/bin/sh

#mi apsetto che come primo input sia lo username, secondo pasametro la password, il terzo parametro il target e il quarto una
#stringa del tipo USER1,USER2,USER3....
while [ true ] ; do

python3 ../InstagramGetFollows/SaveUsersToFollowIntoDatabase.py $1 $2 $3 $4
done

