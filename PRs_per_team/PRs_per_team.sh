#!/bin/bash

gh auth login --with-token < ../AgentRelease_token.txt

# The following function creates a file that details for each team, the total number of PRs, the total number of security, performance and functional bug fixes for a certain release.
collect_bugfixes(){
    echo "Collecting number of PRs per team related to bugfixes"
  echo team ,total_prs , total_functional_bugfixes, total_security_bugfixes, total_performance_bugfixes > "$outfile"
  while read -r line
  do
    prs=$(gh search prs --milestone "$version" --label "$line" --limit 1000|wc -l)
    fun=$(gh search prs --milestone "$version" --label "$line" --label bugfix/functional --limit 1000|wc -l)
    sec=$(gh search prs --milestone "$version" --label "$line" --label bugfix/security --limit 1000|wc -l)
    perf=$(gh search prs --milestone "$version" --label "$line" --label bugfix/performance --limit 1000|wc -l)
    echo  "$line", "$prs", "$fun", "$sec", "$perf"
    sleep 15
  done < "$infile" >> "$outfile"
}

# The following function creates a file that details for each team, the total number of PRs, the total number of PRs that were QAed before merge, and the total number of PRs that are not impacting Agent code.
collect_QAed_PRs(){
  echo "Collecting number of PRs per team related to QA"
  echo team, total_prs, total_qaed_prs, total_prs_no_code_change > "$outfile2"
  while read -r line
  do
    prs=$(gh search prs --milestone "$version" --label "$line" --limit 1000 |wc -l)
    qa=$(gh search prs --milestone "$version" --label "$line" --label "qa/done" --limit 1000|wc -l)
    nc=$(gh search prs --milestone "$version" --label "$line" --label "qa/no-code-change" --limit 1000|wc -l)
    echo  "$line", "$prs", "$qa", "$nc"
    sleep 15
done < $infile >> "$outfile2"
}

###
# Main body of script starts here
###
echo -n "Please pick a milestone: " ;
read -r version

echo -n "What data do you need? QA/Bugfixes/both (qa/bf/both) " ;
read -r option

infile=AgentTeams.txt
outfile=ratio_perteam_$version.csv
outfile2=QAed_prs_$version.csv

case $option in
    qa|QA)
      collect_QAed_PRs
      ;;
    bugfixes|bf|BUGFIXES)
      collect_bugfixes
      ;;
    both|BOTH)
      collect_QAed_PRs
      collect_bugfixes
      ;;
    *)
      exit
      ;;
esac
