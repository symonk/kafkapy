import typer


acls_app = typer.Typer(help="Manage ACLs", rich_markup_mode="rich", rich_help_panel="foo")


@acls_app.command()
def list():
    """List"""
