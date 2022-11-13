
from random import randint

import HammingTests
import HammingViewModel
import numpy
import Matrix


import math


def HammingCodeDriver():
    mode = input("Enter mode: ")
    total_bits, num_data_bits = (15, 11) if mode == "H1511" else (7, 4)

    message = numpy.array(HammingViewModel.generate_random_message(num_data_bits))
    print("Message          :", message)

    x = HammingViewModel.encodeMessage(Matrix.generator11,
                                       message) if total_bits == 15 else HammingViewModel.encodeMessage(Matrix.Generator4, message)
    print("Send Vector      :", x)

    # Creating error
    HammingViewModel.generate_error(x, total_bits)

    z = HammingViewModel.generateParityCheckMatrix(Matrix.Hamming11,
                                                   x) if total_bits == 15 else HammingViewModel.generateParityCheckMatrix(
        Matrix.Hamming4, x)
    print("Received Message :", x)

    print("Parity Check     :", z)

    # Convert
    z = z[::-1]

    if sum(z) == 0:
        print("Decoded Message  :", HammingViewModel.decodeMessage(Matrix.D11, x)) if total_bits == 15 else print(
            "Decoded Message  :",
            HammingViewModel.decodeMessage(
                Matrix.D4, x))
    else:
        x = HammingViewModel.errorCorrection(x, z)
        print("Corrected Message:", x)
        print("Decoded Message  :", HammingViewModel.decodeMessage(Matrix.D11, x)) if total_bits == 15 else print(
            "Decoded Message  :",
            HammingViewModel.decodeMessage(
                Matrix.D4, x))


def main():
    # To see the tests, uncomment for testing
    HammingTests.runTests()

    # For running code to see B, uncomment the following line
    HammingCodeDriver()


if __name__ == "__main__":
    main()
