import functools
from kafkapy.constants import CommandMeta


def set_cmd_description(command_meta: CommandMeta) -> str:
    """Automatic uniform command descriptions."""
    description, danger = command_meta
    if not description.endswith("."):
        description += "."

    def deco(function):
        prefix = ""
        if not danger:
            emoji = ":star2:"
        else:
            prefix = "[b][red][Danger][/red][/b] "
            emoji = ":triangular_flag_on_post:"
        function.__doc__ = f"[b][white]{prefix}{description}[/b][/white] {emoji}"

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

        return wrapper

    return deco
