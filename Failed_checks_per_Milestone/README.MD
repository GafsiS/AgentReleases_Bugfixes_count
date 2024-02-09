## Agent Releases - Processing PRs failed checks data

**Description**

This package contains two scripts 

* `FailedChecks_Milestone.sh` 
* `process_failed_checks.py`  

These script will be, for a specific `milestone` :
- Extracting all data related to:
  *  All PRs from Datadog-agent merged with Failed Checks
  *  Related to a certain milestone introduced as an external variable
- It will then be parsing this data to get:
  * The list of PRs that were merged with Failed Checks.
  * The teams pushing them
  * The date of merge
  * The impacted version of the Agent

**How to run it?**

- Make sure you have the token file to be able to auth to github
- Double check that the agent_failed_checks.csv file does exist in your folder and has the following header: `version,key,repo,pr_id,status,subject,labels,date,team`
- From your terminal run the following command: ` ./FailedChecks_Milestone.sh $version`,
Where:
- `$version`: The release version for which you would like to run the script

**How to have the data in Datadog?**
1. Update the [Agent_failed checks reference table](https://app.datadoghq.com/reference-tables/agent_failedchecks)
- Click on `Update Config` button and select your updated `agent_failed_checks.csv` file.
- The data will then be added and your graphs updated
2. Update the [Agent releases statistics Dashboard](https://app.datadoghq.com/dashboard/7yj-2r3-ai8/agent-release-statistics)
- Don't forget to add the new agent version in the dashboard variable to be able to filter on it
 
