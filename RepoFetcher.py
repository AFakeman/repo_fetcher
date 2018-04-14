import os
import subprocess

import gitlab


class RepoFetcher:
    GITLAB_URL = 'https://gitlab.com'

    def __init__(self, config, branch):
        self.api = gitlab.Gitlab(RepoFetcher.GITLAB_URL, private_token=config.PRIVATE_TOKEN)
        self.config = config
        self.branch = branch

    def get_projects(self):
        self.api.auth()

        groups = self.api.groups.list(search=self.config.GROUP_NAME)
        if len(groups) != 1:
            raise ValueError('Wrong number of groups')
        group = groups[0]

        return group.projects.list(all=True)

    @staticmethod
    def add_prefix_to_files(path, prefix):
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                new_file_path = os.path.join(dirpath, prefix + filename)
                os.rename(file_path, new_file_path)

    def check(self):
        projects = self.get_projects()

        subprocess.run(["rm", "-rf", self.config.TMPDIR])
        subprocess.run(["rm", "-rf", self.config.OUTPUT_DIR])

        for idx, project in enumerate(projects):
            project = self.api.projects.get(id=project.id)
            print("{}/{}".format(idx + 1, len(projects)))
            ssh_url = project.ssh_url_to_repo
            repo_name = project.name
            try:
                project.branches.get(self.branch)
            except gitlab.exceptions.GitlabGetError:
                print("{} doens't have a branch {}, skipping...".format(repo_name, self.branch))
                continue
            subprocess.run(["git", "clone", "--branch", self.branch, ssh_url, self.config.TMPDIR])
            subprocess.run(["rm", "-rf", "{}/.git".format(self.config.TMPDIR)])
            self.add_prefix_to_files(self.config.TMPDIR, repo_name + '_')
            subprocess.run(["rsync", "-a", self.config.TMPDIR + '/', self.config.OUTPUT_DIR + '/'])
            subprocess.run(["rm", "-rf", self.config.TMPDIR])
