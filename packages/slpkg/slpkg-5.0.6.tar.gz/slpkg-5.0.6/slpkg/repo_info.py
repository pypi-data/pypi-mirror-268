#!/usr/bin/python3
# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

from slpkg.configs import Configs
from slpkg.load_data import LoadData
from slpkg.utilities import Utilities
from slpkg.repositories import Repositories


class RepoInfo(Configs):

    def __init__(self, flags: list, repository: str):
        super(Configs, self).__init__()
        self.flags: list = flags
        self.repository: str = repository

        self.load_data = LoadData(flags)
        self.utils = Utilities()
        self.repos = Repositories()
        self.columns, self.rows = shutil.get_terminal_size()
        self.name_alignment: int = self.columns - 61

        if self.name_alignment < 1:
            self.name_alignment: int = 1

        self.enabled: int = 0
        self.total_packages: int = 0
        self.repo_data: dict = {}
        self.dates: dict = {}

        self.option_for_repository: bool = self.utils.is_option(
            ('-o', '--repository'), flags)

    def repo_information(self) -> dict:
        repo_info_json: Path = Path(f'{self.repos.repositories_path}', self.repos.repos_information)
        if repo_info_json.is_file():
            repo_info_json: Path = Path(f'{self.repos.repositories_path}', self.repos.repos_information)
            return self.utils.read_json_file(repo_info_json)
        return {}

    def info(self) -> None:
        """ Prints information about repositories. """
        self.dates: dict = self.repo_information()
        if self.option_for_repository:
            self.repo_data: dict = self.load_data.load(self.repository)
        else:
            self.repo_data: dict = self.load_data.load('*')
        self.view_the_title()

        if self.option_for_repository:
            self.view_the_repository_information()
        else:
            self.view_the_repositories_information()

    def count_the_packages(self, repository: str) -> int:
        if self.option_for_repository:
            count: int = len(self.repo_data.keys())
        else:
            count: int = len(self.repo_data[repository].keys())
        self.total_packages += count
        return count

    def view_the_title(self) -> None:
        title: str = f'repositories information:'.title()
        if self.option_for_repository:
            title: str = f'repository information:'.title()
        print(f'\n{title}')
        print('=' * (self.columns - 1))
        print(f"{'Name:':<{self.name_alignment}}{'Status:':<14}{'Last Updated:':<34}{'Packages:':>12}")
        print('=' * (self.columns - 1))

    def view_the_repository_information(self) -> None:
        date: str = 'None'
        count: int = 0
        color: str = self.red
        status: str = 'Disabled'
        if self.dates.get(self.repository):
            date: str = self.dates[self.repository].get('last_updated', 'None')

        if self.repos.repositories[self.repository]['enable']:
            status: str = 'Enabled'
            color: str = self.green
            count: int = self.count_the_packages(self.repository)

        self.view_the_line_information(self.repository, status, date, count, color)
        self.view_summary_of_repository()

    def view_the_repositories_information(self) -> None:
        for repo, item in self.repos.repositories.items():
            date: str = 'None'
            count: int = 0
            color: str = self.red
            status: str = 'Disabled'
            if self.dates.get(repo):
                date: str = self.dates[repo].get('last_updated', 'None')
    
            if item['enable']:
                self.enabled += 1
                status: str = 'Enabled'
                color: str = self.green
                count: int = self.count_the_packages(repo)

            self.view_the_line_information(repo, status, date, count, color)
        self.view_summary_of_all_repositories()

    def view_the_line_information(self, repository: str, status: str, date: str, count: int, color: str) -> None:
        repo_color: str = self.cyan
        if repository == self.repos.default_repository:
            repo_color: str = self.byellow
            repository: str = f'{repository} (default)'

        print(f"{repo_color}{repository:<{self.name_alignment}}{self.endc}{color}{status:<14}{self.endc}{date:<34}"
              f"{self.yellow}{count:>12}{self.endc}")

    def view_summary_of_repository(self) -> None:
        print('=' * (self.columns - 1))
        print(f"{self.grey}Total {self.total_packages} packages available from the '{self.repository}' repository.\n")

    def view_summary_of_all_repositories(self) -> None:
        print('=' * (self.columns - 1))
        print(f"{self.grey}Total of {self.enabled}/{len(self.repos.repositories)} "
              f"repositories are enabled with {self.total_packages} packages available.\n")
