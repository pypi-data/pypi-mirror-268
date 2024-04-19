# Evaluate

Evaluate is a script that can be run to gather information about all projects of a GitLab

- Instance
- Group (including sub-groups)

This information is useful to the GitLab Professional Services (PS) team to accurately scope migration services.

[[_TOC_]]

## Contributions / Support

This tool is maintained by the Professional Services team and is not included in your GitLab Support if you have a license. For support questions please create [an issue](https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate/-/issues/new?issuable_template=evaluate-support) from our [Evaluate support issue template](./.gitlab/issue_templates/evaluate-support.md).

## Use Case

GitLab PS plans to share this script with a Customer to run against their GitLab instance or group. Then the customer can send back the output files to enable GitLab engagement managers to scope engagements accurately. There is a [single file generated](reading-the-output.md).

## Install Method

### (Recommended) Docker Container

[Docker containers with evaluate installed](https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate/container_registry) are also available to use.

```bash
docker pull registry.gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate:latest
```

### (Optional) pip Install

Requires at least Python 3.8.

```bash
pip install gitlab-evaluate
```

### Local Usage

```bash
# Spin up container
docker run --name evaluate -it registry.gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate:latest /bin/bash

# In docker shell
evaluate-gitlab -t <access-token-with-api-scope> -s https://gitlab.example.com
evaluate-jenkins -s https://jenkins.example.com -u <jenkins-admin-user> -t <access-token-or-password> # BETA
```


## Usage

### GitLab

#### System level data gathering

Evaluate is meant to be run by an **OWNER** (ideally system **ADMINISTRATOR**) of a GitLab instance to gather data about every project on the instance or group (including sub-groups).

1. A GitLab **OWNER** (ideally system **ADMINISTRATOR**) should provision an access token with `api` scope:
   - [Personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token) for instance
   - [Group access token](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html#create-a-group-access-token-using-ui) for group
2. Install `gitlab-evaluate` from the [Install](#install-method) section above,
3. Run :point_down:

    For evaluating a GitLab instance

    ```bash
    evaluate-gitlab -t <access-token-with-api-scope> -s https://gitlab.example.com
    ```

    For evaluating a GitLab group (including sub-groups)

    ```bash
    evaluate-gitlab -t <access-token-with-api-scope> -s https://gitlab.example.com -g 42
    ```

    See [Recommended Processes per Project Count](#recommended-processes-per-project-count) to specify the number of processes to use

4. This should create a file called `evaluate_report.xlsx`

   For more information on these files, see [reading the output](reading-the-output.md)
5. If you're coordinating a GitLab PS engagement, email these files to the GitLab account team.

#### Recommended Processes per Project Count

Evaluate uses 4 processes by default, which is sufficient for smaller GitLab instances, but may result in a slower scan time for larger instances. Below is a table covering recommended processes based on the overall number of projects on an instance:

| Number of Projects | Recommended Processes |
| --- |  --- | 
| < 100 | 4 (default) |
| < 1000 | 8 |
| < 10000 | 16 |
| < 100000 | 32 | 
| > 100000 | 64-128 |

The number of processes is limited by a few factors:

- API rate limits on the GitLab instance itself
- Overall stability of the GitLab instance
- Not as critical as the first two, but overall available memory on the machine running Evaluate is another factor to consider

You can ramp up the number of processes on a smaller instance to speed up the scans, but the performance gains for a large number of processes on a smaller instance will eventually plateau.


#### Command help screen

```text
Usage: evaluate-gitlab [OPTIONS]

Options:
  -s, --source TEXT     Source URL: REQ'd
  -t, --token TEXT      Personal Access Token: REQ'd
  -o, --output          Output Per Project Stats to screen
  -i, --insecure        Set to ignore SSL warnings.
  -g, --group TEXT      Group ID. Evaluate all group projects (including sub-
                        groups)
  -f, --filename TEXT   CSV Output File Name. If not set, will default to
                        'evaluate_output.xlsx'
  -p, --processes TEXT  Number of processes. Defaults to number of CPU cores
  --help                Show this message and exit.
```

### [BETA] Jenkins

Evaluate supports scanning a Jenkins instance to retrieve basic metrics about the instance

#### Usage

Evaluate is meant to be run by an admin of a Jenkins instance to gather data about jenkins jobs and any plugins installed on the instance.

1. A Jenkins **ADMINISTRATOR** should provision an API token for Evaluate to use during the scan.
2. Install `gitlab-evaluate` from the [Install](#install-method) section above,
3. Run :point_down:

    ```bash
    evaluate-jenkins -s https://jenkins.example.com -u <jenkins-admin-user> -t <access-token-or-password>
    ```

4. This should create a file called `evaluate_jenkins.xlsx`
5. If you're coordinating a GitLab PS engagement, email these files to the GitLab account team.

#### Command help screen

```
Usage: evaluate-jenkins [OPTIONS]

Options:
  -s, --source TEXT  Source URL: REQ'd
  -u, --user TEXT    Username associated with the Jenkins API token: REQ'd
  -t, --token TEXT   Jenkins API Token: REQ'd
  --help             Show this message and exit.
```

## GitLab Project Thresholds

_Below are the thresholds we will use to determine whether a project can be considered for normal migration or needs to have special steps taken in order to migrate_

### Project Data

- Project Size - 20GB
- Pipelines - 5,000 max
- Issues - 5,000 total (not just open)
- Merge Requests - 5,000 total (not just merged)
- Container images - 20GB per project
- Packages - Any packages present

### Repository Data

- Repository Size - 5GB
- Commits - 50K
- Branches - 1K
- Tags - 5K
