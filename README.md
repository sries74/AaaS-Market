# AI Agent Automation System

A Web-App where users purchase credits and they can purchase pre-setup agents that do a specific task like create a social media post, update SEO on a website, run a competitor analysis, find a profitable niche with low competition, search social media sites for leads, create content for a website that passes tests to see if AI wrote it, build an e-mail marketing series, find products to resell, etc.

# Task List

create a task list setup by Phases then Features then Tasks then issues.  The following fields should be created in
the tasklist.md file: Milestones: Milestone-Number, Name, Priority{HOT, High, Medium, Low, Backlog}, Category{BackEnd,
FrontEnd, Research, Content}, Orchestrator-Approval, CEO-Approval, Total Time; Features: Feature-Number, Name,
Priority{HOT, High, Medium, Low, Backlog}, Category{BackEnd, FrontEnd, Research, Content}, Orchestrator-Approval, Total
 Time; Tasks: Task-Number, name, assignee(Agent's Name), time started, time completed, total time,
linting-completed(checkbox), headless-test-description, headless-test-results, headless-test-completed(checkbox),
e2e-test-description, e2e-test-results, e2e-completed(CHECKBOX); Issues: Issue-ID, AssociatedTaskName, Name,
Description, Assignee, linting-completed(checkbox), headless-test-description, headless-test-results,
headless-test-completed(checkbox), e2e-test-description, e2e-test-results, e2e-completed(CHECKBOX).  Use TDD in the
following manner: Once all the tasks for the feature are complete, then test each task.  If the task passes the test,
check the headless-tests and e2e tests checkboxes, document the results of the test in headless-results and
e2e-results.  If ALL tasks in a feature pass both headless and e2e tests, checkmark the feature's headless-tests &
e2e-tests checkboxes.  If a task does not pass, add an issue under the feature.