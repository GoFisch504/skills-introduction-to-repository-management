pip install PyGithub
import csv
from github import Github

g = Github("YOUR_GITHUB_TOKEN")
repo = g.get_repo("GoFisch504/skills-introduction-to-repository-management")

with open('issues.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        repo.create_issue(
            title=row['Title'],
            body=row['Body'],
            labels=[label.strip() for label in row['Labels'].split(',')],
            assignees=[row['Assignee']] if row['Assignee'] else None
        )
