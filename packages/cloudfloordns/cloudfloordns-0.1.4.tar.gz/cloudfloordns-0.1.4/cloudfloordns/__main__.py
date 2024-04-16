import click

# from nagra_network_misc_utils.logger import set_default_logger

# from cloudfloordns.utils import main

# This sets a convenient global handler for the logs
# set_default_logger()

# Display info logs (you can change the logging level)
# logging.getLogger().setLevel(logging.INFO)


# Keep it as the main entry point
@click.group()
def cli():
    pass


# Add here your subcommands if needed
# cli.add_command(main)

if __name__ == "__main__":
    cli()
