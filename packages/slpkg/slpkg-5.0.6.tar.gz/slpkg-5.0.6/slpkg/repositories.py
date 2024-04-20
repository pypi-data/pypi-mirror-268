#!/usr/bin/python3
# -*- coding: utf-8 -*-


try:
    import tomli
except ModuleNotFoundError:
    import tomllib as tomli

from pathlib import Path
from dataclasses import dataclass

from slpkg.configs import Configs
from slpkg.utilities import Utilities
from slpkg.toml_errors import TomlErrors


@dataclass
class Repositories:
    toml_errors = TomlErrors()
    utils = Utilities()

    repositories_toml_file: Path = Path(Configs.etc_path, 'repositories.toml')
    repositories_path: Path = Path(Configs.lib_path, 'repos')

    repos_config = {}
    repositories = {}
    repos_toml = {}

    data_json: str = 'data.json'
    repos_information: Path = Path(repositories_path, 'repos_information.json')
    default_repository: str = 'sbo'

    slackbuilds_txt: str = 'SLACKBUILDS.TXT'
    packages_txt: str = 'PACKAGES.TXT'
    checksums_md5: str = 'CHECKSUMS.md5'
    changelog_txt: str = 'ChangeLog.txt'

    sbo_repo: bool = True
    sbo_repo_name: str = 'sbo'
    sbo_repo_path: Path = Path(repositories_path, sbo_repo_name)
    sbo_repo_mirror: str = ''
    sbo_repo_tag: str = '_SBo'
    sbo_repo_tar_suffix: str = '.tar.gz'

    ponce_repo: bool = False
    ponce_repo_name: str = 'ponce'
    ponce_repo_path: Path = Path(repositories_path, ponce_repo_name)
    ponce_repo_mirror: str = ''
    ponce_repo_tag: str = '_SBo'
    ponce_repo_tar_suffix: str = '.tar.gz'

    slack_repo: bool = False
    slack_repo_name: str = 'slack'
    slack_repo_path: Path = Path(repositories_path, slack_repo_name)
    slack_repo_mirror: str = ''
    slack_repo_tag: str = ''

    slack_extra_repo: bool = False
    slack_extra_repo_name: str = 'slack_extra'
    slack_extra_repo_path: Path = Path(repositories_path, slack_extra_repo_name)
    slack_extra_repo_mirror_packages: str = ''
    slack_extra_repo_mirror_changelog: str = ''
    slack_extra_repo_tag: str = ''

    slack_patches_repo: bool = False
    slack_patches_repo_name: str = 'slack_patches'
    slack_patches_repo_path: Path = Path(repositories_path, slack_patches_repo_name)
    slack_patches_repo_mirror_packages: str = ''
    slack_patches_repo_mirror_changelog: str = ''
    slack_patches_repo_tag: str = ''

    alien_repo: bool = False
    alien_repo_name: str = 'alien'
    alien_repo_path: Path = Path(repositories_path, alien_repo_name)
    alien_repo_mirror_packages: str = ''
    alien_repo_mirror_changelog: str = ''
    alien_repo_tag: str = 'alien'

    multilib_repo: bool = False
    multilib_repo_name: str = 'multilib'
    multilib_repo_path: Path = Path(repositories_path, multilib_repo_name)
    multilib_repo_mirror_packages: str = ''
    multilib_repo_mirror_changelog: str = ''
    multilib_repo_tag: str = 'alien'

    restricted_repo: bool = False
    restricted_repo_name: str = 'restricted'
    restricted_repo_path: Path = Path(repositories_path, restricted_repo_name)
    restricted_repo_mirror_packages: str = ''
    restricted_repo_mirror_changelog: str = ''
    restricted_repo_tag: str = 'alien'

    gnome_repo: bool = False
    gnome_repo_name: str = 'gnome'
    gnome_repo_path: Path = Path(repositories_path, gnome_repo_name)
    gnome_repo_mirror: str = ''
    gnome_repo_tag: str = 'gfs'

    msb_repo: bool = False
    msb_repo_name: str = 'msb'
    msb_repo_path: Path = Path(repositories_path, msb_repo_name)
    msb_repo_mirror_packages: str = ''
    msb_repo_mirror_changelog: str = ''
    msb_repo_tag: str = 'msb'

    csb_repo: bool = False
    csb_repo_name: str = 'csb'
    csb_repo_path: Path = Path(repositories_path, csb_repo_name)
    csb_repo_mirror: str = ''
    csb_repo_tag: str = 'csb'

    conraid_repo: bool = False
    conraid_repo_name: str = 'conraid'
    conraid_repo_path: Path = Path(repositories_path, conraid_repo_name)
    conraid_repo_mirror: str = ''
    conraid_repo_tag: str = 'cf'

    slackdce_repo: bool = False
    slackdce_repo_name: str = 'slackdce'
    slackdce_repo_path: Path = Path(repositories_path, slackdce_repo_name)
    slackdce_repo_mirror: str = ''
    slackdce_repo_tag: str = 'dce'

    slackonly_repo: bool = False
    slackonly_repo_name: str = 'slackonly'
    slackonly_repo_path: Path = Path(repositories_path, slackonly_repo_name)
    slackonly_repo_mirror: str = ''
    slackonly_repo_tag: str = 'slonly'

    salix_repo: bool = False
    salix_repo_name: str = 'salix'
    salix_repo_path: Path = Path(repositories_path, salix_repo_name)
    salix_repo_mirror: str = ''
    salix_repo_tag: str = ''

    salix_extra_repo: bool = False
    salix_extra_repo_name: str = 'salix_extra'
    salix_extra_repo_path: Path = Path(repositories_path, salix_extra_repo_name)
    salix_extra_repo_mirror: str = ''
    salix_extra_repo_tag: str = ''

    slackel_repo: bool = False
    slackel_repo_name: str = 'slackel'
    slackel_repo_path: Path = Path(repositories_path, slackel_repo_name)
    slackel_repo_mirror: str = ''
    slackel_repo_tag: str = 'dj'

    slint_repo: bool = False
    slint_repo_name: str = 'slint'
    slint_repo_path: Path = Path(repositories_path, slint_repo_name)
    slint_repo_mirror: str = ''
    slint_repo_tag: str = 'slint'

    pprkut_repo: bool = False
    pprkut_repo_name: str = 'pprkut'
    pprkut_repo_path: Path = Path(repositories_path, pprkut_repo_name)
    pprkut_repo_mirror: str = ''
    pprkut_repo_tag: str = 'pprkut'

    try:
        if repositories_toml_file.is_file():
            with open(repositories_toml_file, 'rb') as repo:
                repos_config = tomli.load(repo)

            repos_config = utils.convert_dict_keys_to_lower(repos_config)

            default_repository: str = repos_config['default']['repo'].lower()

            sbo_repo: bool = repos_config['sbo']['enable']
            sbo_repo_mirror: str = repos_config['sbo']['mirror']

            ponce_repo: bool = repos_config['ponce']['enable']
            ponce_repo_mirror: str = repos_config['ponce']['mirror']

            slack_repo: bool = repos_config['slack']['enable']
            slack_repo_mirror: str = repos_config['slack']['mirror']

            slack_extra_repo: bool = repos_config['slack_extra']['enable']
            slack_extra_repo_url: str = repos_config['slack_extra']['mirror']
            slack_extra_repo_mirror_packages: str = slack_extra_repo_url
            slack_extra_repo_mirror_changelog: str = f"{'/'.join(slack_extra_repo_url.split('/')[:-2])}/"

            slack_patches_repo: bool = repos_config['slack_patches']['enable']
            slack_patches_repo_url: str = repos_config['slack_patches']['mirror']
            slack_patches_repo_mirror_packages: str = slack_patches_repo_url
            slack_patches_repo_mirror_changelog: str = f"{'/'.join(slack_patches_repo_url.split('/')[:-2])}/"

            alien_repo: bool = repos_config['alien']['enable']
            alien_repo_url: str = repos_config['alien']['mirror']
            alien_repo_mirror_packages: str = alien_repo_url
            alien_repo_mirror_changelog: str = f"{'/'.join(alien_repo_url.split('/')[:-3])}/"

            multilib_repo: bool = repos_config['multilib']['enable']
            multilib_repo_url: str = repos_config['multilib']['mirror']
            multilib_repo_mirror_packages: str = multilib_repo_url
            multilib_repo_mirror_changelog: str = f"{'/'.join(multilib_repo_url.split('/')[:-2])}/"

            restricted_repo: bool = repos_config['restricted']['enable']
            restricted_repo_url: str = repos_config['restricted']['mirror']
            restricted_repo_mirror_packages: str = restricted_repo_url
            restricted_repo_mirror_changelog: str = f"{'/'.join(restricted_repo_url.split('/')[:-3])}/"

            gnome_repo: bool = repos_config['gnome']['enable']
            gnome_repo_mirror: str = repos_config['gnome']['mirror']

            msb_repo: bool = repos_config['msb']['enable']
            msb_repo_url: str = repos_config['msb']['mirror']
            msb_repo_mirror_packages: str = msb_repo_url
            msb_repo_mirror_changelog: str = f"{'/'.join(msb_repo_url.split('/')[:-4])}/"

            csb_repo: bool = repos_config['csb']['enable']
            csb_repo_mirror: str = repos_config['csb']['mirror']

            conraid_repo: bool = repos_config['conraid']['enable']
            conraid_repo_mirror: str = repos_config['conraid']['mirror']

            slackdce_repo: bool = repos_config['slackdce']['enable']
            slackdce_repo_mirror: str = repos_config['slackdce']['mirror']

            slackonly_repo: bool = repos_config['slackonly']['enable']
            slackonly_repo_mirror: str = repos_config['slackonly']['mirror']

            salix_repo: bool = repos_config['salix']['enable']
            salix_repo_mirror: str = repos_config['salix']['mirror']

            salix_extra_repo: bool = repos_config['salix_extra']['enable']
            salix_extra_repo_mirror: str = repos_config['salix_extra']['mirror']

            slackel_repo: bool = repos_config['slackel']['enable']
            slackel_repo_mirror: str = repos_config['slackel']['mirror']

            slint_repo: bool = repos_config['slint']['enable']
            slint_repo_mirror: str = repos_config['slint']['mirror']

            pprkut_repo: bool = repos_config['pprkut']['enable']
            pprkut_repo_mirror: str = repos_config['pprkut']['mirror']
    except (tomli.TOMLDecodeError, KeyError) as error:
        toml_errors.raise_toml_error_message(error, repositories_toml_file)

    # Dictionary configurations of repositories.
    repositories = {
        sbo_repo_name: {
            'enable': sbo_repo,
            'path': sbo_repo_path,
            'mirror_packages': sbo_repo_mirror,
            'mirror_changelog': sbo_repo_mirror,
            'slackbuilds_txt': slackbuilds_txt,
            'changelog_txt': changelog_txt,
            'repo_tag': sbo_repo_tag,
            'tar_suffix': sbo_repo_tar_suffix},

        ponce_repo_name: {
            'enable': ponce_repo,
            'path': ponce_repo_path,
            'mirror_packages': ponce_repo_mirror,
            'mirror_changelog': ponce_repo_mirror,
            'slackbuilds_txt': slackbuilds_txt,
            'changelog_txt': changelog_txt,
            'repo_tag': ponce_repo_tag,
            'tar_suffix': ponce_repo_tar_suffix},

        slack_repo_name: {
            'enable': slack_repo,
            'path': slack_repo_path,
            'mirror_packages': slack_repo_mirror,
            'mirror_changelog': slack_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slack_repo_tag},

        slack_extra_repo_name: {
            'enable': slack_extra_repo,
            'path': slack_extra_repo_path,
            'mirror_packages': slack_extra_repo_mirror_packages,
            'mirror_changelog': slack_extra_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slack_extra_repo_tag},

        slack_patches_repo_name: {
            'enable': slack_patches_repo,
            'path': slack_patches_repo_path,
            'mirror_packages': slack_patches_repo_mirror_packages,
            'mirror_changelog': slack_patches_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slack_patches_repo_tag},

        alien_repo_name: {
            'enable': alien_repo,
            'path': alien_repo_path,
            'mirror_packages': alien_repo_mirror_packages,
            'mirror_changelog': alien_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': alien_repo_tag},

        multilib_repo_name: {
            'enable': multilib_repo,
            'path': multilib_repo_path,
            'mirror_packages': multilib_repo_mirror_packages,
            'mirror_changelog': multilib_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': multilib_repo_tag},

        restricted_repo_name: {
            'enable': restricted_repo,
            'path': restricted_repo_path,
            'mirror_packages': restricted_repo_mirror_packages,
            'mirror_changelog': restricted_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': restricted_repo_tag},

        gnome_repo_name: {
            'enable': gnome_repo,
            'path': gnome_repo_path,
            'mirror_packages': gnome_repo_mirror,
            'mirror_changelog': gnome_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': gnome_repo_tag},

        msb_repo_name: {
            'enable': msb_repo,
            'path': msb_repo_path,
            'mirror_packages': msb_repo_mirror_packages,
            'mirror_changelog': msb_repo_mirror_changelog,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': msb_repo_tag},

        csb_repo_name: {
            'enable': csb_repo,
            'path': csb_repo_path,
            'mirror_packages': csb_repo_mirror,
            'mirror_changelog': csb_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': csb_repo_tag},

        conraid_repo_name: {
            'enable': conraid_repo,
            'path': conraid_repo_path,
            'mirror_packages': conraid_repo_mirror,
            'mirror_changelog': conraid_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': conraid_repo_tag},

        slackdce_repo_name: {
            'enable': slackdce_repo,
            'path': slackdce_repo_path,
            'mirror_packages': slackdce_repo_mirror,
            'mirror_changelog': slackdce_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slackdce_repo_tag},

        slackonly_repo_name: {
            'enable': slackonly_repo,
            'path': slackonly_repo_path,
            'mirror_packages': slackonly_repo_mirror,
            'mirror_changelog': slackonly_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slackonly_repo_tag},

        salix_repo_name: {
            'enable': salix_repo,
            'path': salix_repo_path,
            'mirror_packages': salix_repo_mirror,
            'mirror_changelog': salix_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': salix_repo_tag},

        salix_extra_repo_name: {
            'enable': salix_extra_repo,
            'path': salix_extra_repo_path,
            'mirror_packages': salix_extra_repo_mirror,
            'mirror_changelog': salix_extra_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': salix_extra_repo_tag},

        slackel_repo_name: {
            'enable': slackel_repo,
            'path': slackel_repo_path,
            'mirror_packages': slackel_repo_mirror,
            'mirror_changelog': slackel_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slackel_repo_tag},

        slint_repo_name: {
            'enable': slint_repo,
            'path': slint_repo_path,
            'mirror_packages': slint_repo_mirror,
            'mirror_changelog': slint_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': slint_repo_tag},

        pprkut_repo_name: {
            'enable': pprkut_repo,
            'path': pprkut_repo_path,
            'mirror_packages': pprkut_repo_mirror,
            'mirror_changelog': pprkut_repo_mirror,
            'packages_txt': packages_txt,
            'checksums_md5': checksums_md5,
            'changelog_txt': changelog_txt,
            'repo_tag': pprkut_repo_tag}
    }

    all_repos = list(repos_config.keys())
    defaults_repos = list(repositories.keys())

    diff_repos = list(set(all_repos) - set(defaults_repos))
    diff_repos.remove('default')

    if diff_repos:
        for repo, data in repos_config.items():

            if repo in diff_repos:
                mirror_packages: str = data.get('mirror', '')
                mirror_changelog: str = mirror_packages
                if data.get('changelog'):
                    mirror_changelog: str = data.get('changelog', '')

                values = {
                    'enable': data.get('enable', False),
                    'path': Path(repositories_path, repo),
                    'mirror_packages': mirror_packages,
                    'mirror_changelog': mirror_changelog,
                    'packages_txt': packages_txt,
                    'checksums_md5': checksums_md5,
                    'changelog_txt': changelog_txt,
                    'repo_tag': data.get('tag', '')
                }
                repositories[repo] = values
