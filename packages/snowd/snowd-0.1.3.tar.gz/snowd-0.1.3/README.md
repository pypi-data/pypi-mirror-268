# README

This is a framework to integrate ServiceNow data into a CI/CD pipeline.

```python
   with Context("/table/mytable", validator=Record) as ctx:
      # if needed, filter records, grouping, further validation... can be done
      update_yaml("test.yaml", ctx.data)
```

We assume that the workflow is standard:
1. Get **one** resource from ServiceNow (e.g. "/table/incident")
2. Validate the data received
3. Store the data
4. Commit and push all changes

Nb: if needed, this library provide lower level utilities.

## How it works
* Every variables are taken from environment variables. (see below)
* This will create a `timestamp.txt` file with the last run.
  **This file must be cached for the next run**
* This will automaticly clone the target repository
* The data is retrieved and validated against a validator.
  **We recommend to use pydantic library for the validation**
* `ctx.data` will contain a list a dict containing at least `sys_id` entry that is unique

## Environment variables
Here is the list of the possible environment variables

### client.Client
* **SNOW_INSTANCE**: ServiceNow instance (e.g. "myinstance" in `https://myinstance.servicenow.com`)
* **SNOW_USER**: The ServiceNow user to use
* **SNOW_PASSWORD**: The password of the ServiceNow user
Additional:
* **SNOW_CLIENT_ID**: Used for OAuth2.0 protocol
* **SNOW_CLIENT_SECRET**: Used for OAuth2.0 protocol

### git.Git
* **GIT_URL**: git URL for http connection (it can contain the credentials, making GIT_USER/GIT_PASSWORD useless)
  E.g. "https://{login}:{password}@gitlab.com/owner/project.git"
Additional:
* **GIT_USER**: git user for http connection (injected into the provided url)
* **GIT_PASSWORD**: git password for http connection (injected into the provided url). For Gitlab, this can be the token
* **GIT_AUTHOR_NAME**: author of the commit
* **GIT_AUTHOR_EMAIL**: email of the commit author
* **GIT_BRANCH**: The branch to edit (create it if it doesn't exist). Default to the default branch
* **GIT_SRC_BRANCH**: The source branch from which to create the working branch
