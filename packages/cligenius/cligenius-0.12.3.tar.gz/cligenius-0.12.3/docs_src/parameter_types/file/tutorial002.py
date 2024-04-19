import cligenius


def main(config: cligenius.FileTextWrite = cligenius.Option(...)):
    config.write("Some config written by the app")
    print("Config written")


if __name__ == "__main__":
    cligenius.run(main)
