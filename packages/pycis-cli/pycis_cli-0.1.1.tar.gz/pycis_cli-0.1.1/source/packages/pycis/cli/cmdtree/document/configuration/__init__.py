
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click


from pycis.cli.cmdtree.document.configuration.decrypt \
    import command_pycis_document_configuration_decrypt
from pycis.cli.cmdtree.document.configuration.encrypt \
    import command_pycis_document_configuration_encrypt


@click.group("configuration", help="Contains commands for working configuration documents.")
def group_pycis_document_configuration():
    return

group_pycis_document_configuration.add_command(
    command_pycis_document_configuration_decrypt
)
group_pycis_document_configuration.add_command(
    command_pycis_document_configuration_encrypt
)
