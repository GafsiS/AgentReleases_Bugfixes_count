# AgentReleases_Bugfixes_count

**Description
**

This script will be :
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
 

**How to run it?
**

- Make sure you have the token file to be able to auth to github
- Double check that the agent_bug_fixes.csv file does exist in your folder and has the following header: `version,repo,pr_id,status,subject,labels,team,bug_type,changelog,qa
`
- From your terminal run the following command: ` ./Bugfixes_Milestone.sh $version`. Replace $version by the agent version you're looking to get data for.

**How to have the data in Datadog?
**
- Go to the reference page
- Search for `agent_bugfixes` table anc click on it
- Click on `Update Config` button and select your updated `agent_bug_fixes.csv` file.
- The data will then be added and your graphes updated
- Don't forget to add the new agent version in the dashboard variable to be able to filter on it
 
