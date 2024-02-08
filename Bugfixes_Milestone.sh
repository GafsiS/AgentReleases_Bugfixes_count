#!/bin/bash


version=$1
code_freeze=$2
prod_deploy=$3

#login to Github
gh auth login --with-token < AgentRelease_token.txt

#Collecting Release data
gh search prs --milestone $version --label "bugfix/functional" --limit 1000 >> bugfix_$version.csv
gh search prs --milestone $version --label "bugfix/security" --limit 1000 >> bugfix_$version.csv

sed -e 's/\t/|/g' bugfix_$version.csv > bugfix.csv

echo "$version PRs infos has been collected"

echo "$version has code freeze on $code_freeze and was deployed on $prod_deploy"

python  process_prs.py $version $code_freeze $prod_deploy
