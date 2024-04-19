from enum import Enum

import cligenius


class NeuralNetwork(str, Enum):
    simple = "simple"
    conv = "conv"
    lstm = "lstm"


def main(
    network: NeuralNetwork = cligenius.Option(NeuralNetwork.simple, case_sensitive=False),
):
    print(f"Training neural network of type: {network.value}")


if __name__ == "__main__":
    cligenius.run(main)
