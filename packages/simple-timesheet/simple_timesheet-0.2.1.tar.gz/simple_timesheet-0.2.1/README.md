# Simple Timesheet
CLI thing to add entries to a date-based timesheet

## Installation
Theoretically you can just `pip install simple-timesheet`

## Usage
You should end up with a `ts` executable on your path. You can get help like this:

    ts --help
    Usage: ts [OPTIONS] COMMAND [ARGS]...

    Options:
      --db_file TEXT
      --help          Show this message and exit.

    Commands:
      add
      today  Dump the timesheet string for today
      week   Dump the timesheet string for 5 days starting at start date

You can also get command specific help with something like this:

    ts add --help
    Usage: ts add [OPTIONS] ENTRY

    Options:
      --help  Show this message and exit.

To add an entry, do `ts add "Your entry here"`. This will add a row to the database with the date and your string. Note that it has to be enclosed in quotes

You can dump todays timesheet string with `ts today` which will print something like `20240306: some stuff here, I did other things too, And I wrote this code`

And you can dump a whole week's worth with `ts week 2024-03-02` which will print lines like `ts today` for five days starting on the date you specify.
