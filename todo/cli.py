import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select, SQLModel

from .config import settings
from .db import engine
from .models import User, Task, TaskStatus

main = typer.Typer(name="Todo CLI")


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "User": User,
        "Task": Task,
        "TaskStatus": TaskStatus,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(
            argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars
        )
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


@main.command()
def user_list():
    """Lists all users"""
    table = Table(title="Todo users")
    fields = ["id", "username"]
    for header in fields:
        table.add_column(header, style="magenta")

    with Session(engine) as session:
        users = session.exec(select(User))
        for user in users:
            table.add_row(str(user.id), user.username)

    Console().print(table)


@main.command()
def create_user(username: str, password: str):
    """Create user"""
    with Session(engine) as session:
        user = User(username=username, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
        typer.echo(f"created {username} user")
        return user


@main.command()
def delete_user(username: str):
    """Delete user"""
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).one()
        session.delete(user)
        session.commit()
        typer.echo(f"deleted {username} user")
        return user


@main.command()
def reset_db(
    force: bool = typer.Option(
        False, "--force", "-f", help="Run with no confirmation"
    )
):
    """Resets the database tables"""
    force = force or typer.confirm("Are you sure?")
    if force:
        SQLModel.metadata.drop_all(engine)
