#!/bin/bash


version=$1
code_freeze=$2
prod_deploy=$3

#login to Github
gh auth login --with-token < AgentRelease_token.txt

#Collecting Release data 
gh search prs --milestone $version --label "bugfix/functional" > bugfix_$version.csv
gh search prs --milestone $version --label "bugfix/performance" >> bugfix_$version.csv
gh search prs --milestone $version --label "bugfix/security" >> bugfix_$version.csv

sed -e 's/\t/|/g' bugfix_$version.csv > bugfix.csv

echo "$version PRs infos has been collected" 

python  process_prs.py $version



