import cligenius


def main(good: bool = True):
    message_start = "everything is "
    if good:
        ending = cligenius.style("good", fg=cligenius.colors.GREEN, bold=True)
    else:
        ending = cligenius.style("bad", fg=cligenius.colors.WHITE, bg=cligenius.colors.RED)
    message = message_start + ending
    cligenius.echo(message)


if __name__ == "__main__":
    cligenius.run(main)
