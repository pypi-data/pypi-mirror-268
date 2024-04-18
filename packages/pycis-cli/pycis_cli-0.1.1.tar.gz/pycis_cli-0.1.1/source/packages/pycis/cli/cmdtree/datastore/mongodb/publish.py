
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import json
import os
import sys

from datetime import datetime, timedelta

import click

from mojo.xmods.xclick import NORMALIZED_STRING

from pycis.cli.cmdtree.datastore.constants import PYCIS_DB_BYPRODUCTS

HELP_HOST = "A MongoDB host name."
HELP_PORT = "The MongoDB port number."
HELP_CATEGORY = "The 'category' under which the document should be organized."
HELP_USERNAME = "The MongoDB username who can write to a database."
HELP_PASSWORD = "The MongoDB password for the specified user."
HELP_EXPIRY = "A number of days to persist the up uploaded results."
HELP_FILENAME = "The document to publish."

OPTION_TYPE_CATEGORY = click.Choice(['build', 'testrun'])

@click.command("publish")
@click.option("--host", required=True, type=NORMALIZED_STRING, help=HELP_HOST)
@click.option("--port", required=True, type=click.INT, default=27017, help=HELP_PORT)
@click.option("--category", required=True, type=OPTION_TYPE_CATEGORY, help=HELP_CATEGORY)
@click.option("--username", required=False, type=NORMALIZED_STRING, help=HELP_USERNAME)
@click.option("--password", required=False, type=NORMALIZED_STRING, help=HELP_PASSWORD)
@click.option("--expiry-days", required=False, type=click.INT, default=365, help=HELP_EXPIRY)
@click.argument('filename', metavar="<document>", type=click.Path(dir_okay=False))
def command_pycis_datastore_mongodb_publish(
    host: str, port: int, category:str, username: str, password: str,
    expiry_days: int, filename: str):
    
    try:
        import pymongo
    except ImportError:
        print("You must install 'MongoDB' in order to be able to publish to a MongoDB data store.", file=sys.stderr)
        exit(1)

    if not os.path.exists(filename):
        errmsg = f"The specified document does not exist. filename={filename}"
        click.BadParameter(errmsg)
    
    connection = f"{host}:{port}"
    if username is not None:
        if password is None:
            errmsg = "A 'password' parameter must be specified if a username is provided."
            click.BadArgumentUsage(errmsg)
        connection = f"{username}:{password}@{connection}"
    
    connection = f"mongodb+srv://{connection}"

    expiry_date = datetime.now() + timedelta(days=expiry_days)

    docobj = None
    with open(filename, 'r') as sf:
        docobj = json.load(sf)

    docobj["expiry_date"] = expiry_date.isoformat()

    database = ""

    from pymongo import MongoClient

    client = MongoClient(host, port)
    
    pycisdb = client[PYCIS_DB_BYPRODUCTS]

    testruns = pycisdb[category]
    testruns.insert_one(docobj)

    return