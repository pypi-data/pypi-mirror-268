import time

import cligenius


def main():
    total = 1000
    with cligenius.progressbar(length=total) as progress:
        for batch in range(4):
            # Fake processing time
            time.sleep(1)
            progress.update(250)
    print(f"Processed {total} things in batches.")


if __name__ == "__main__":
    cligenius.run(main)
