#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import time
from pathlib import Path
from multiprocessing import Process

from slpkg.configs import Configs
from slpkg.utilities import Utilities
from slpkg.blacklist import Blacklist
from slpkg.views.asciibox import AsciiBox
from slpkg.progress_bar import ProgressBar
from slpkg.repositories import Repositories


class LoadData(Configs):

    def __init__(self, flags=None):
        self.repos = Repositories()
        self.utils = Utilities()
        self.black = Blacklist()
        self.ascii = AsciiBox()
        self.progress = ProgressBar()

        if flags is None:
            flags = []

        self.bar_process = None

        self.option_for_progress_bar: bool = self.utils.is_option(
            ('-B', '--progress-bar'), flags)

    def load(self, repository: str, message=True) -> dict:
        if message:
            self.bar_progress()

        data: dict = {}
        if repository == '*':
            for repo, item in self.repos.repositories.items():
                if item['enable']:  # Check if the repository is enabled
                    json_data_file: Path = Path(self.repos.repositories[repo]['path'], self.repos.data_json)
                    data[repo] = self.read_data_file(json_data_file)
        else:
            json_data_file: Path = Path(self.repos.repositories[repository]['path'], self.repos.data_json)

            data: dict = self.read_data_file(json_data_file)

        blacklist: tuple = self.black.packages()
        if blacklist:
            if repository == '*':
                self._remove_blacklist_from_all_repos(data)
            else:
                self._remove_blacklist_from_a_repo(data)

        if message:
            self.done_process()
            # print(f'{self.bgreen}{self.ascii.done}{self.endc}')
        return data

    def read_data_file(self, file: Path) -> dict:
        """
        Read JSON data from the file.
        Args:
            file: Path file for reading.
        Returns:
            Dictionary with data.
        """
        json_data: dict = {}
        try:
            json_data: dict = json.loads(file.read_text(encoding='utf-8'))
        except FileNotFoundError:
            print(f'{self.bred}{self.ascii.failed}{self.endc}')
            print(f'\nFile {file} not found!')
            print('\nNeed to update the database first, please run:\n')
            print(f"{'':>2} $ {self.green}slpkg update{self.endc}\n")
            raise SystemExit(1)
        except json.decoder.JSONDecodeError:
            pass
        return json_data

    def _remove_blacklist_from_all_repos(self, data: dict) -> dict:
        # Remove blacklist packages from keys.
        for name, repo in data.items():
            blacklist_packages: list = self.utils.ignore_packages(list(data[name].keys()))
            for pkg in blacklist_packages:
                if pkg in data[name].keys():
                    del data[name][pkg]

        # Remove blacklist packages from dependencies (values).
        for name, repo in data.items():
            blacklist_packages: list = self.utils.ignore_packages(list(data[name].keys()))
            for pkg, dep in repo.items():
                deps: list = dep['requires']
                for blk in blacklist_packages:
                    if blk in deps:
                        deps.remove(blk)
                        data[name][pkg]['requires'] = deps
        return data

    def _remove_blacklist_from_a_repo(self, data: dict) -> dict:
        blacklist_packages: list = self.utils.ignore_packages(list(data.keys()))
        # Remove blacklist packages from keys.
        for pkg in blacklist_packages:
            if pkg in data.keys():
                del data[pkg]

        # Remove blacklist packages from dependencies (values).
        for pkg, dep in data.items():
            deps: list = dep['requires']
            for blk in blacklist_packages:
                if blk in deps:
                    deps.remove(blk)
                    data[pkg]['requires'] = deps
        return data

    def bar_progress(self) -> None:
        if self.progress_bar or self.option_for_progress_bar:
            message: str = 'Database loading'
            self.bar_process = Process(target=self.progress.progress_bar, args=(message,))
            self.bar_process.start()
        else:
            print('\rDatabase loading... ', end='')

    def done_process(self) -> None:
        if self.progress_bar or self.option_for_progress_bar:
            time.sleep(0.1)
            self.bar_process.terminate()
            self.bar_process.join()
            print('\x1b[?25h')
        else:
            print(f'{self.bgreen}{self.ascii.done}{self.endc}')
