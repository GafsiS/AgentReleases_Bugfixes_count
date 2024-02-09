#!/bin/bash


version=$1

#login to Github
gh auth login --with-token < ../AgentRelease_token.txt

#Collecting Release data

gh search prs --milestone $version --checks failure --merged -B main --limit 1000 > failed_checks_$version.csv
sed -e 's/\t/|/g' failed_checks_$version.csv > failed_checks.csv

echo "$version PRs infos has been collected"

python  process_failed_checks.py $version
