# ActiveCollab

## Overview
Library for Active Collab. Perform actions such as list projects, list users, add note, add task, get project detail.

## Download stats
[![Downloads](https://static.pepy.tech/badge/ActiveCollab)](https://pepy.tech/project/ActiveCollab)

## Installation
```console
pip install ActiveCollab
```
ActiveCollab supports Python 3+.

## Usage

### Default
```python
import ActiveCollab

host_url = 'host_url' # Active Collab hosted URL  

user_name = 'your_email' # Active Collab username or email

password = 'your_password' # Active Collab Password

ac = ActiveCollab.Connect(host_url,user_name,password)  # Login to Active Collab
```

### List all projects
```python
ac.list_projects()  # List out all project assigned to logged in user
```

### List all users
```python
ac.list_users()  # List out all users in your organization with id, name and email
```

### List Users in a Project
```python
ac.project_detail(project_id)  # List out all info like id, name, users/members of a project (project_id)
```

### + Add Note in a Project
```python
ac.add_note_in_project(project_id,note_title,note_content)  # Add note in the provided project_id
```

### + Add Task in a Project
```python
ac.add_task_in_project(project_id,task_title,task_description,task_assignee)  # Add task in the provided project_id
```

