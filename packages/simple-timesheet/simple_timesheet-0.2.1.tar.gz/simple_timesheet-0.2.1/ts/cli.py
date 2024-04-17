import sqlite3
from datetime import date, timedelta
from pathlib import Path

import click


def connect_db(db_file):
    """
    Check if the db_file exists, if not create it and
    set up the tables

    returns the connection
    """
    db_file_path = Path(db_file)
    # Ensure directory exists
    if not db_file_path.parent.exists():
        db_file_path.parent.resolve().mkdir(parents=True)

    if not db_file_path.exists():
        ## First setup
        con = sqlite3.connect(db_file_path)
        cur = con.cursor()
        cur.execute("CREATE TABLE timesheet(id, date, entry)")

    else:
        con = sqlite3.connect(db_file_path)

    return con


@click.group()
@click.option("--db_file", default=Path.home() / ".timesheet/timesheet.sqlite")
@click.pass_context
def cli(ctx, db_file):
    ctx.ensure_object(dict)
    ctx.obj["db_file"] = db_file


@cli.command()
@click.argument("entry", type=str)
@click.pass_context
def add(ctx, entry):
    """
    Add an entry for today
    """
    con = connect_db(ctx.obj["db_file"])

    cur = con.cursor()
    last_id = cur.execute("SELECT max(id) FROM timesheet").fetchone()[0]
    if last_id is None:
        next_id = 0
    else:
        next_id = last_id + 1
    cur.execute("INSERT INTO timesheet VALUES(?, ?, ?)", (next_id, date.today(), entry))
    con.commit()
    # con = sqlite3.connect(ctx.obj['db_file'])


@cli.command()
@click.pass_context
@click.argument("entry", type=str)
def add_yesterday(ctx, entry):
    """
    Add an entry for yesterday
    """
    con = connect_db(ctx.obj["db_file"])

    cur = con.cursor()
    last_id = cur.execute("SELECT max(id) FROM timesheet").fetchone()[0]
    if last_id is None:
        next_id = 0
    else:
        next_id = last_id + 1
    cur.execute(
        "INSERT INTO timesheet VALUES(?, ?, ?)",
        (next_id, date.today() - timedelta(1), entry),
    )
    con.commit()


@cli.command()
@click.argument("date", type=str)
@click.argument("entry", type=str)
@click.pass_context
def add_date(ctx, date, entry):
    """
    Add an entry on a specific date in YYYY-MM-DD format
    """
    con = connect_db(ctx.obj["db_file"])

    cur = con.cursor()
    last_id = cur.execute("SELECT max(id) FROM timesheet").fetchone()[0]
    if last_id is None:
        next_id = 0
    else:
        next_id = last_id + 1
    cur.execute("INSERT INTO timesheet VALUES(?, ?, ?)", (next_id, date, entry))
    con.commit()
    # con = sqlite3.connect(ctx.obj['db_file'])


@cli.command()
@click.pass_context
def today(ctx):
    """
    Dump the timesheet string for today
    """
    con = connect_db(ctx.obj["db_file"])
    cur = con.cursor()
    ## fetch all the stuff for today
    today = date.today()

    cur.execute(
        "SELECT date, group_concat(entry, ', ') FROM timesheet GROUP BY date HAVING date = ?",
        (today,),
    )
    res = cur.fetchone()
    prettified = f"{res[0].replace('-', '')}: {res[1]}"

    print(prettified)


@cli.command()
@click.pass_context
@click.argument("start")
def week(ctx, start):
    """
    Dump the timesheet string for 5 days starting at start date
    """
    con = connect_db(ctx.obj["db_file"])
    cur = con.cursor()
    ## fetch all the stuff for today

    week_timesheet = []
    start_date = date.fromisoformat(start)
    for i in range(0, 5):
        selected_date = start_date + timedelta(days=i)
        cur.execute(
            "SELECT date, group_concat(entry, ', ') FROM timesheet GROUP BY date HAVING date = ?",
            (selected_date,),
        )
        res = cur.fetchone()
        if res is None:
            prettified = f"{selected_date.isoformat().replace('-', '')}: Nothing"
        else:
            prettified = f"{res[0].replace('-', '')}: {res[1]}"
        week_timesheet.append(prettified)

    print("\n".join(week_timesheet))
