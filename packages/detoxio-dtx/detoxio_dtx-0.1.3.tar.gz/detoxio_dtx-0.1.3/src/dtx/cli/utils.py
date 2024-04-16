import click

def is_verbose() -> bool:
    return click.get_current_context().params.get("verbose", False)

def print_info(message):
    click.echo(click.style(f"[*] {message}", fg="blue"))

def print_error(message):
    click.echo(click.style(f"[!] {message}", fg="red"), err=True)

def print_success(message):
    click.echo(click.style(f"[+] {message}", fg="green"))

def print_warning(message):
    click.echo(click.style(f"[!] {message}", fg="yellow"))

def print_verbose(message):
    if is_verbose():
        click.echo(click.style(f"[v] {message}", fg="cyan"))

def get_torch_device():
    import torch

    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")
