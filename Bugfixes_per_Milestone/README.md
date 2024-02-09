## Agent Releases - Processing Bug Fixes data

**Description**

This package contains two scripts 

* `Bugfixes_Milestone.sh` 
* `process_prs.py`  

These script will be, for a specific `milestone` :
- Extracting all data related to:
  * Closed PRs from DataDog/datadog-agent
  *  having a label containing `bugfix`
  *  Related to certain milestone introduced as an external variable
- It will then be parsing this data to get:
  * The bug fix type (performance, security, functional)
  * The team pushing it
  * The date of merge
  * The impacted version of the Agent
  * If the fix will go through the QA process
  * If it will be part of the Release notes

**Entry Parameters**


**How to run it?**

- Make sure you have the token file to be able to auth to github
- Double check that the agent_bug_fixes.csv file does exist in your folder and has the following header: `version,repo,pr_id,status,subject,labels,team,bug_type,changelog,qa
`
- From your terminal run the following command: ` ./Bugfixes_Milestone.sh $version $code_freeze $prod_deploy`,
Where:
- `$version`: The release version for which you would like to run the script
- `$code-freeze`: The release code freeze date
- `$prod-deploy`: The release date
- 
**How to have the data in Datadog?**
1. Update the [Agent_bugfixes reference table](https://app.datadoghq.com/reference-tables/agent_bugfixes)
- Click on `Update Config` button and select your updated `agent_bug_fixes.csv` file.
- The data will then be added and your graphes updated
2. Update the [Agent releases statistics Dashboard](https://app.datadoghq.com/dashboard/7yj-2r3-ai8/agent-release-statistics)
- Don't forget to add the new agent version in the dashboard variable to be able to filter on it
 
