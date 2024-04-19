import cligenius


def main():
    delete = cligenius.confirm("Are you sure you want to delete it?", abort=True)
    print("Deleting it!")


if __name__ == "__main__":
    cligenius.run(main)
