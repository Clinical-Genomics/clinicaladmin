# -*- coding: utf-8 -*-
import click
import ruamel.yaml

from clinicaladmin.database import ApplicationDetails


@click.group()
@click.pass_context
def root(context):
    """Interact with the admin database."""
    pass


@root.command()
@click.option('-v', '--version', is_flag=True, help='return latest version')
@click.argument('application_tag')
@click.pass_context
def apptag(context, version, application_tag):
    """Get information about an application tag."""
    apptag_query = (
        ApplicationDetails.query.filter_by(application_tag=application_tag))
    latest_tag = apptag_query.first()
    if latest_tag is None:
        click.echo("can't find application tag: {}".format(application_tag))
        context.abort()
    if version:
        click.echo(latest_tag.version)
    else:
        apptag_data = latest_tag.to_dict()
        dump = ruamel.yaml.dump(apptag_data)
        click.echo(dump)
