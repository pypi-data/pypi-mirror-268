#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path

from slpkg.configs import Configs
from slpkg.views.views import View
from slpkg.utilities import Utilities
from slpkg.downloader import Downloader
from slpkg.install_data import InstallData
from slpkg.repositories import Repositories
from slpkg.multi_process import MultiProcess
from slpkg.check_updates import CheckUpdates
from slpkg.sbos.sbo_generate import SBoGenerate


class UpdateRepositories(Configs):
    """ Updates the local repositories and install the data
        into the database.
    """

    def __init__(self, flags: list, repository: str):
        super(Configs, self).__init__()

        self.view = View(flags)
        self.multi_process = MultiProcess(flags)
        self.repos = Repositories()
        self.utils = Utilities()
        self.data = InstallData()
        self.generate = SBoGenerate()
        self.check_updates = CheckUpdates(flags, repository)
        self.download = Downloader(flags)

        self.repos_for_update: dict = {}

    def repositories(self) -> None:
        self.repos_for_update: dict = self.check_updates.updates()

        if not any(list(self.repos_for_update.values())):
            self.view.question(message='Do you want to force update?')
            # Force update the repositories.
            for repo in self.repos_for_update:
                self.repos_for_update[repo] = True

        self.run_update()

    def run_update(self) -> None:
        for repo, update in self.repos_for_update.items():
            if update:
                self.view_downloading_message(repo)
                if repo in [self.repos.sbo_repo_name, self.repos.ponce_repo_name]:
                    self.update_slackbuild_repos(repo)
                else:
                    self.update_binary_repos(repo)

    def view_downloading_message(self, repo: str) -> None:
        print(f"Syncing with the repository '{self.green}{repo}{self.endc}', please wait...\n")

    def update_binary_repos(self, repo: str) -> None:
        """ Updates the binary repositories. """
        urls: dict = {}

        self.utils.create_directory(self.repos.repositories[repo]['path'])
        self.utils.remove_file_if_exists(self.repos.repositories[repo]['path'],
                                         self.repos.repositories[repo]['changelog_txt'])
        self.utils.remove_file_if_exists(self.repos.repositories[repo]['path'],
                                         self.repos.repositories[repo]['packages_txt'])
        self.utils.remove_file_if_exists(self.repos.repositories[repo]['path'],
                                         self.repos.repositories[repo]['checksums_md5'])

        changelog: str = (f"{self.repos.repositories[repo]['mirror_changelog']}"
                          f"{self.repos.repositories[repo]['changelog_txt']}")
        packages: str = (f"{self.repos.repositories[repo]['mirror_packages']}"
                         f"{self.repos.repositories[repo]['packages_txt']}")
        checksums: str = (f"{self.repos.repositories[repo]['mirror_packages']}"
                          f"{self.repos.repositories[repo]['checksums_md5']}")

        urls[repo] = ((changelog, packages, checksums), self.repos.repositories[repo]['path'])

        self.download.download(urls)

        self.data.install_binary_data(repo)

    def update_slackbuild_repos(self, repo: str) -> None:
        """ Updates the slackbuild repositories. """
        self.utils.create_directory(self.repos.repositories[repo]['path'])
        self.utils.remove_file_if_exists(self.repos.repositories[repo]['path'],
                                         self.repos.repositories[repo]['slackbuilds_txt'])
        self.utils.remove_file_if_exists(self.repos.repositories[repo]['path'],
                                         self.repos.repositories[repo]['changelog_txt'])

        lftp_command: str = (f"lftp {self.lftp_mirror_options} {self.repos.repositories[repo]['mirror_packages']} "
                             f"{self.repos.repositories[repo]['path']}")

        self.multi_process.process(lftp_command)

        # It checks if there is a SLACKBUILDS.TXT file, otherwise it's going to create one.
        if not Path(self.repos.repositories[repo]['path'],
                    self.repos.repositories[repo]['slackbuilds_txt']).is_file():
            self.generate.slackbuild_file(self.repos.repositories[repo]['path'],
                                          self.repos.repositories[repo]['slackbuilds_txt'])

        self.data.install_sbo_data(repo)
