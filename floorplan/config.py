import yaml
from dataclasses import dataclass
import shutil
import os
import logging
from dataclasses_json import dataclass_json
import sys
import subprocess

PACKAGES_DIR = ".floorplan-packages"
LOCAL_KEYWORD = "local"

DEPENDENCIES_KEYWORD = 'dependencies'
PROJECT_DIR_KEYWORD = 'project_dir'
DIST_DIR_KEYWORD = 'dist_dir'
STATIC_DIR_KEYWORD = 'static_dir'

@dataclass_json
@dataclass
class Dependency:
    name: str
    source: str
    username: str
    password: str
    install_path: str
    protocol: str
    version: str
    path: str

def add_git_dependency(dep: Dependency) -> None:
    if os.path.exists('.floorplan-git'):
        shutil.rmtree('.floorplan-git')
    os.makedirs(".floorplan-git", exist_ok=True)
    source = dep.source
    if dep.source.startswith('http'):
        if dep.username and dep.password:
            parts = source.split('://')
            source = f'{parts[0]}://{dep.username}:{dep.password}@{parts[1]}'
        elif dep.username:
            logging.error('Value passed for username but not password, bailing out')
            sys.exit(1)
        else:
            logging.error('Value passed for password but not username, bailing out')
            sys.exit(1)
    subprocess.run(['git', 'clone', '-b', dep.version, source, f'.floorplan-git/{dep.name}'])
    shutil.copytree(f'.floorplan-git/{dep.name}/{dep.path}', f'{PACKAGES_DIR}/{dep.name}')
    shutil.rmtree('.floorplan-git')
    
def add_http_dependency(dep: Dependency) -> None:
    logging.critical('HTTP dependencies not yet implemented')
    sys.exit(1)

def add_file_dependency(dep: Dependency) -> None:
    shutil.copytree(dep.source, f'{PACKAGES_DIR}/{dep.name}')

PROTOCOLS = {
    'git': add_git_dependency,
    'http': add_http_dependency,
    'file': add_file_dependency
}

@dataclass_json
@dataclass
class Config:
    project_dir: str
    dist_dir: str
    static_dir: str
    dependencies: dict[str, Dependency]

        
    def add_dependency(self, name: str, source: str, protocol: str, username: str, password: str, version: str, path: str) -> None:
        package_dir = f'{PACKAGES_DIR}/{name}'
        os.makedirs(package_dir, exist_ok=True)

        if os.path.exists(package_dir):
            logging.debug(f'Removing existing package directory at {package_dir}')
            shutil.rmtree(package_dir)
        
        if not protocol in PROTOCOLS:
            logging.error(f'Invalid protocol: {protocol}. Valid protocols are {", ".join(PROTOCOLS)}')
            sys.exit(1)

        dep = Dependency(name, source, username, password, package_dir, protocol, version, path)

        PROTOCOLS[protocol](dep)

        self.dependencies[name] = dep

        logging.info(f'{name} successfully added at {package_dir}!')

    def remove_dependency(self, name: str) -> None:
        package_dir = f'{PACKAGES_DIR}/{name}'
        if os.path.exists(package_dir):
            shutil.rmtree(package_dir)
        
        del self.dependencies[name]

        logging.info(f'{name} successfully removed from {package_dir}!')

    def read_config(self) -> None:
        config = {}

        logging.debug('Reading configuration...')
        with open(f'.floorplan.yaml', 'r', encoding='utf-8') as config_file:
            config = yaml.safe_load(config_file)

        logging.debug(f'Found dependencies {config[DEPENDENCIES_KEYWORD]}')
        self.dependencies = {key: Dependency.from_dict(val) for key, val in config[DEPENDENCIES_KEYWORD].items()}
        self.project_dir = config[PROJECT_DIR_KEYWORD]
        self.dist_dir = config[DIST_DIR_KEYWORD]
        self.static_dir = config[STATIC_DIR_KEYWORD]
        
        logging.debug('Done!')

    def write_config(self) -> None:
        output = {
            PROJECT_DIR_KEYWORD: self.project_dir,
            DIST_DIR_KEYWORD: self.dist_dir,
            STATIC_DIR_KEYWORD: self.static_dir,
            DEPENDENCIES_KEYWORD: {dep: self.dependencies[dep].to_dict() for dep in self.dependencies}
        }
        
        logging.debug(f'Writing out config {output}...')
        with open(f'{self.project_dir}/.floorplan.yaml', 'w', encoding='utf-8') as config_file:
            yaml.safe_dump(output, config_file)

        logging.debug('Done!')
