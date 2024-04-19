import cligenius


def main():
    delete = cligenius.confirm("Are you sure you want to delete it?")
    if not delete:
        print("Not deleting")
        raise cligenius.Abort()
    print("Deleting it!")


if __name__ == "__main__":
    cligenius.run(main)
