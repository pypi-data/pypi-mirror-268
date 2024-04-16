import click
import random

from base64 import b64encode

from praetorian_cli.handlers.utils import chaos
from praetorian_cli.handlers.utils import handle_api_error
from praetorian_cli.sdk.keychain import verify_credentials


@chaos.command('accounts')
@click.pass_obj
@handle_api_error
def my_accounts(controller):
    """ Fetch my associated accounts """
    result = controller.my(dict(key=f'#account'))
    for hit in result.get('accounts', []):
        print(f"{hit['key']}")


@chaos.command('link-chaos')
@click.pass_obj
@handle_api_error
@click.argument('username')
@click.option('-config', '--config', default="", help="Add an optional configuration")
def link_account(controller, username, config):
    """ Link another Chaos account to yours """
    result = controller.link_account(username=username, config=config)
    print(f"{result['key']}")


@chaos.command('unlink')
@click.pass_obj
@handle_api_error
@click.argument('username')
def unlink_account(controller, username):
    """ Unlink a Chaos account from yours """
    result = controller.unlink_account(username=username)
    print(f"{result['key']}")


@chaos.command('add-webhook')
@click.pass_obj
@handle_api_error
def add_webhook(controller):
    """ Authenticated URL for adding assets and risks """
    pin = str(random.randint(10000, 99999))
    controller.link_account(username="hook", config=pin)
    username = b64encode(controller.keychain.username.encode('utf8'))
    encoded_string = username.decode('utf8')
    encoded_username = encoded_string.rstrip('=')
    print(f'{controller.keychain.api}/hook/{encoded_username}/{pin}')


@chaos.command('link-slack')
@click.pass_obj
@handle_api_error
@click.argument('webhook')
def link_slack(controller, webhook):
    """ Send all new risks to Slack """
    controller.link_account('slack', webhook)


@chaos.command('link-jira')
@click.pass_obj
@handle_api_error
@click.argument('domain')
@click.argument('access_token')
@click.argument('project_key')
@click.argument('issue_type_id')
def link_jira(controller, domain, access_token, project_key, issue_type_id):
    """ Send all new risks to JIRA """
    config = {'domain': domain, 'accessToken': access_token, 'projectKey': project_key, 'issueId': issue_type_id}
    controller.link_account('jira', config)


@chaos.command('link-amazon')
@click.pass_obj
@handle_api_error
@click.argument('access_key')
@click.argument('secret_key')
def link_amazon(controller, access_key, secret_key):
    """ Enumerate Amazon for Assets """
    config = {'accessKey': access_key, 'secretKey': secret_key}
    controller.link_account('amazon', config)


@chaos.command('link-github')
@click.pass_obj
@handle_api_error
@click.argument('pat')
def link_github(controller, pat):
    """ Allow Chaos to scan your private repos """
    controller.link_account('github', pat)
