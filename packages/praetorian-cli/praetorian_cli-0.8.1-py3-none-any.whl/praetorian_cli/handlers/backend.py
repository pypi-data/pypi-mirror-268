import os
import click

from praetorian_cli.handlers.utils import chaos
from praetorian_cli.handlers.utils import Status
from praetorian_cli.handlers.utils import handle_api_error


@chaos.command('seeds')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_seeds(controller, seed):
    """ Fetch seed domains """
    result = controller.my(dict(key=f'#seed#{seed}'))
    for hit in result.get('seeds', []):
        print(f"{hit['key']}")


@chaos.command('assets')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_assets(controller, seed):
    """ Fetch existing assets """
    result = controller.my(dict(key=f'#asset#{seed}'))
    for hit in result.get('assets', []):
        print(f"{hit['key']}")


@chaos.command('risks')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_risks(controller, seed):
    """ Fetch current risks """
    result = controller.my(dict(key=f'#risk#{seed}'))
    for hit in result.get('risks', []):
        print(f"{hit['key']}")


@chaos.command('services')
@click.pass_obj
@handle_api_error
@click.option('-seed', '--seed', default="", help="Filter by seed domain")
def my_services(controller, seed):
    """ Fetch recently seen services """
    result = controller.my(dict(key=f'#service#{seed}'))
    for hit in result.get('services', []):
        print(f"{hit['key']}")


@chaos.command('jobs')
@click.pass_obj
@handle_api_error
@click.option('-updated', '--updated', default="", help="Fetch jobs since date")
def my_jobs(controller, updated):
    """ Fetch past, present and future jobs """
    result = controller.my(dict(key=f'#job#{updated}'))
    for hit in result.get('jobs', []):
        print(f"{hit['key']}")


@chaos.command('files')
@click.pass_obj
@handle_api_error
@click.option('-name', '--name', default="", help="Filter by relative path")
def my_files(controller, name):
    """ Fetch all file names """
    result = controller.my(dict(key=f'#file#{name}'))
    for hit in result.get('files', []):
        print(f"{hit['key']}")


@chaos.command('threats')
@click.pass_obj
@handle_api_error
@click.option('-source', '--source', type=click.Choice(['KEV']), default="KEV", help="Filter by threat source")
def my_threats(controller, source):
    """ Fetch threat intelligence """
    result = controller.my(dict(key=f'#threat#{source}'))
    for hit in result.get('threats', []):
        print(f"{hit['key']}")


@chaos.command('add-seed')
@click.pass_obj
@handle_api_error
@click.argument('seed')
@click.option('-status', '--status', type=click.Choice(['AA', 'AF']), required=False, default="AA")
@click.option('-comment', '--comment', default="", help="Add a comment")
def add_seed(controller, seed, status, comment=""):
    """ Add a new seed domain """
    controller.add_asset(seed, status=status, comment=comment)


@chaos.command('delete-seed')
@click.pass_obj
@handle_api_error
@click.argument('seed')
def delete_seed(controller, seed):
    """ Delete any seed """
    controller.delete_asset(f'#seed#{seed}')


@chaos.command('update-asset')
@click.pass_obj
@handle_api_error
@click.argument('key')
@click.option('-status', '--status', type=click.Choice(['AA', 'AF']), required=False, default="AA")
@click.option('-comment', '--comment', help="Add a comment")
def update_asset(controller, key, status, comment=''):
    """ Update any asset or seed """
    controller.update_asset(key, status=status, comment=comment)


@chaos.command('add-risk')
@click.pass_obj
@handle_api_error
@click.argument('key')
@click.option('-name', '--name', required=True, help="Generic risk identifier")
@click.option('-status', '--status', type=click.Choice([s.value for s in Status]), required=False, default='TO')
def add_risk(controller, key, name, status):
    """ Apply a risk to an asset key """
    print(controller.add_risk(key, name, status))


@chaos.command('upload')
@click.pass_obj
@handle_api_error
@click.argument('name')
def upload(controller, name):
    """ Upload a file """
    controller.upload(name)


@chaos.command('download')
@click.pass_obj
@handle_api_error
@click.argument('key')
@click.argument('path')
def download(controller, key, path):
    """ Download any previous uploaded file """
    controller.download(key, path)


@chaos.command('search')
@click.pass_obj
@handle_api_error
@click.option('-term', '--term', help="Enter a search term")
def search(controller, term=""):
    """ Query the data store for arbitrary matches """
    resp = controller.my(dict(key=term))
    for key, value in resp.items():
        if isinstance(value, list):
            for hit in value:
                print(f"{hit['key']}")


@chaos.command('test')
@click.pass_obj
def trigger_all_tests(controller):
    """ Run integration test suite """
    try:
        import pytest
    except ModuleNotFoundError:
        print("Install pytest using 'pip install pytest' to run this command")
    test_directory = os.path.relpath("praetorian_cli/sdk/test", os.getcwd())
    pytest.main([test_directory])
