import gitlab
import subprocess
import sys

GROUP_NAME = 'tpcc-course-2018'
PRIVATE_TOKEN = ''
BRANCH_NAME = sys.argv[1]
TMPDIR = 'tmp'
OUTPUT_DIR = 'output'

api = gitlab.Gitlab("https://gitlab.com", private_token=PRIVATE_TOKEN)
api.auth()

print("Searching for the group in your groups...", end='')
sys.stdout.flush()

groups = api.groups.list(search=GROUP_NAME)

print("Done")

assert(len(groups) == 1)

group = groups[0]

print("Loading projects data...", end='')
sys.stdout.flush()

projects = group.projects.list(all=True)

print("Done")

subprocess.run(["rm", "-rf", TMPDIR])
subprocess.run(["rm", "-rf", OUTPUT_DIR])

for idx, project in enumerate(projects):
    # GroupProject doesn't have branches field
    project = api.projects.get(id=project.id)
    print("{}/{}".format(idx + 1, len(projects)))
    ssh_url = project.ssh_url_to_repo
    repo_name = project.name
    try:
        project.branches.get(BRANCH_NAME)
    except gitlab.exceptions.GitlabGetError:
        print("{} doens't have a branch {}, skipping...".format(repo_name,
                                                                BRANCH_NAME))
        continue
    subprocess.run(["git", "clone", "--branch", BRANCH_NAME, ssh_url, TMPDIR])
    subprocess.run(["rm", "-rf", "{}/.git".format(TMPDIR)])
    new_name_mask = '{{}}_{}'.format(repo_name)
    subprocess.run(["find", TMPDIR, "-type", "f", "-exec", "mv", "{}",
                    new_name_mask, ";"])
    subprocess.run(["rsync", "-a", TMPDIR + '/', OUTPUT_DIR + '/'])
    subprocess.run(["rm", "-rf", TMPDIR])