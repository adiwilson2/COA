from random import randint
import numpy


# Create the random message
def generate_random_message(num_data_bits):
    message = []
    for i in range(num_data_bits):
        message.append(randint(0, 1))
    return message


# Create an encoded Message
def encodeMessage(generator_matrix, message):
    total = numpy.matmul(generator_matrix, message) % 2
    return total


# Create the error
def generate_error(x, total_bits):
    chance_of_error = randint(0, total_bits)
    if chance_of_error > 0:
        loc = randint(1, total_bits)
        flip_bit(x, loc)
    return


# Creating the Parity Matrix
def generateParityCheckMatrix(parity_generator_matrix, fb):
    value2 = numpy.matmul(parity_generator_matrix, fb) % 2
    return value2


# Error correction
def errorCorrection(fb, parity_check_matrix):
    error_location = int("".join([str(bit) for bit in parity_check_matrix]), 2)
    flip_bit(fb, error_location)
    return fb


# Decode Message
def decodeMessage(decoder_matrix, syndrome_vector):
    value = numpy.matmul(decoder_matrix, syndrome_vector) % 2
    return value


# Flip the bit.
def flip_bit(x, loc):
    x[loc - 1] = 1 - x[loc - 1]
    return x[loc - 1]
