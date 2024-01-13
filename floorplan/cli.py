from floorplan.config import Config, Dependency, PACKAGES_DIR, PROTOCOLS
from floorplan.compiler import Compiler
import logging
from rich.logging import RichHandler
import os
import shutil
import rich_click as click

LOG_LEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARN": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

@click.group()
def cli_add():
    pass

@cli_add.command()
@click.argument("name")
@click.option("--source", "-s", help='Source of floorplan package, must be a URL (git or http protocols) or a local path (file protocol)', required=True)
@click.option("--protocol", "-p", help=f'Protocol to use to retrieve package. Valid protocols are {", ".join(list(PROTOCOLS.keys()))}. Defaults to git', default='git', show_default=True, required=True)
@click.option("--username", help=f'Basic auth username for retrieval. Use env.<ENV VAR NAME> to pull value from an environment variable', default='')
@click.option("--password", help=f'Basic auth password for retrieval. Use env.<ENV VAR NAME> to pull value from an environment variable', default='')
@click.option("--version", "-v", help=f'version of the package to pull, only used with git protocol', default='main')
@click.option("--path", "-P", help='Path within remote object to package', default='')
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def add(name: str, source: str, protocol: str, username: str, password: str, version: str, log_level: str, path: str) -> None:
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    config = Config('', '', '', {})
    config.read_config()
    config.add_dependency(name, source, protocol, username, password, version, path)
    config.write_config()
    logging.info('Done!')

@click.group()
def cli_clean():
    pass

@cli_clean.group()
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def clean(log_level: str) -> None:
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    config = Config('', '', '', {})
    config.read_config()

    if os.path.exists(config.dist_dir):
        logging.debug(f'Removing existing dist directory at {config.dist_dir}')
        shutil.rmtree(config.dist_dir)
    
    if os.path.exists(f'{config.project_dir}/{PACKAGES_DIR}'):
        logging.debug(f'Removing existing packages directory at {config.project_dir}/{PACKAGES_DIR}')
        shutil.rmtree(f'{config.project_dir}/{PACKAGES_DIR}')

@click.group()
def cli_compile():
    pass

@cli_compile.command()
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def compile(log_level: str) -> None:
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    config = Config('', '', '', {})
    config.read_config()

    compiler = Compiler()
    compiler.do_compile(config)

@click.group()
def cli_init():
    pass

@cli_init.command()
@click.option("--path", "-p", help='Path to initialize floorplan at', required=True)
@click.option("--dist-dir", "-d", help='Relative path to output rendered files', default='dist', show_default=True)
@click.option("--static-dir", "-s", help='Relative path to static directory to copy over to dist directory', default='static', show_default=True)
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def init(path: str, dist_dir: str, static_dir: str, log_level: str) -> None:
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    logging.info(f"Initializing floorplan configuration at {path}/.floorplan.yaml")

    config = Config(f'{path}', f'{dist_dir}', f'{static_dir}', {'local': Dependency('local', 'src', '', '', 'src', 'file', '', '')})
    config.write_config()
    logging.info('Done!')

@click.group()
def cli_install():
    pass

@cli_install.command()
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def install(log_level: str) -> None:
    print('install!')
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    config = Config('', '', '', {})
    config.read_config()

    print(config.dependencies)
    names = list(config.dependencies.keys())
    for name in names:
        print(f'Removing {name}')
        dep = config.dependencies[name]
        config.remove_dependency(dep.name)
        config.add_dependency(dep.name, dep.source, dep.protocol, dep.username, dep.password, dep.version, dep.path)
        config.write_config()

@click.group()
def cli_remove():
    pass

@cli_remove.command()
@click.argument("name")
@click.option("--log-level", "-l", type=click.Choice(list(LOG_LEVELS.keys())), help=f'Log level to use, valid levels are {",".join(list(LOG_LEVELS.keys()))}', default="INFO", show_default=True)
def remove(name: str, log_level: str) -> None:
    logging.basicConfig(level=LOG_LEVELS[log_level], format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
    config = Config('', '', '', {})
    config.read_config()
    config.remove_dependency(name)
    config.write_config()
    logging.info('Done!')

click_cli = click.CommandCollection(sources=[cli_add, cli_clean, cli_compile, cli_init, cli_install, cli_remove])

if __name__ == '__main__':
    click_cli()
