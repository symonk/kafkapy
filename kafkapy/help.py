from .constants import CommandMeta


def generate_help(command: CommandMeta) -> str:
    """Generates a consistent help text, utilised by all commands.  This
    guarantees emoji, colour and formatting is completely consistent.

    :param command: The help constant for the command."""
    description, danger = command
    if not description.endswith("."):
        description += "."
    if not danger:
        emoji, prefix = ":star2:", ""
    else:
        emoji, prefix = ":triangular_flag_on_post:", "[b][red][Danger][/][/] "
    return f"[b][white]{prefix}{description}[/][/] {emoji}"
