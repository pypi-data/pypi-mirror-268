import cligenius


def main(project_name: str = cligenius.Option(..., prompt=True, confirmation_prompt=True)):
    print(f"Deleting project {project_name}")


if __name__ == "__main__":
    cligenius.run(main)
