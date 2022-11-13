"""
    Testing
"""
import numpy
import HammingViewModel
import Matrix




def ConvertFBVectorToDecimal(print_results):
    flag = True
    for i in range(0, 16):
        if flag:
            binNum = [int(s) for s in str(bin(i))[2:].split(",")]
            # print(binNum)
            num = int("".join([str(a) for a in binNum]), 2)
            if num != i:
                print("Test ", i, " failed")
                flag = False
            if not flag:
                print("Test ", i, " Failed")
                break
            print("Test ", i, ": SUCCESS")
    if flag and print_results:
        print("Converting flipped bit Vector to Decimal: SUCCESS")


"""
    Tests For Hamming(7, 4)
"""


def Hamming74NoError(print_results):
    flag = True
    for i in range(0, 16):
        flag = True
        if print_results: print("Num: ", i)
        message = numpy.array([int(a) for a in list(bin(i)[2:].zfill(4))])
        x = HammingViewModel.encodeMessage(Matrix.Generator4, message)
        if print_results: print("Message: ", message)
        z = HammingViewModel.generateParityCheckMatrix(Matrix.Hamming4, x)[::-1]
        if print_results: print("Parity: ", z)
        if sum(z) == 0:
            if message.all() != HammingViewModel.decodeMessage(Matrix.D4, x).all():
                flag = False
        if not flag:
            print("Failed Test: ", i)
            break
    if flag:
        print("Hamming(7, 4) No Errors: SUCCESS")



def Hamming74WithError(print_results):
    context = True
    for i in range(0, 16):
        for error_location in range(0, 7):
            context = True
            if print_results: print("Num: ", i, "Error location: ", error_location)
            message = numpy.array([int(a) for a in list(bin(i)[2:].zfill(4))])
            if print_results: print("Message: ", message)
            x = HammingViewModel.encodeMessage(Matrix.Generator4, message)
            if print_results: print("Flipping Bit: ", x)
            HammingViewModel.flip_bit(x, error_location)
            if print_results: print("Flipping bit we: ", x)
            z = HammingViewModel.generateParityCheckMatrix(Matrix.Hamming4, x)[::-1]
            if print_results: print("Parity: ", z)
            x = HammingViewModel.errorCorrection(x, z)
            if print_results: print("Fixed flipped bit: ", x)
            if sum(z) == 0:
                if message.all() != HammingViewModel.decodeMessage(Matrix.D4, x).all():
                    context = False
            if not context:
                print("Failed Test: ", i)
                break
    if context:
        print("Hamming(7, 4) with Errors: SUCCESS")


"""
    Testing for Hamming(15,11)
"""

def Hamming1511NoError(print_results):
    context = True
    for i in range(0, 2048):
        context = True
        if print_results: print("Num: ", i)
        message = numpy.array([int(a) for a in list(bin(i)[2:].zfill(11))])
        x = HammingViewModel.encodeMessage(Matrix.generator11, message)
        if print_results: print("Message: ", message)
        z = HammingViewModel.generateParityCheckMatrix(Matrix.Hamming11, x)[::-1]
        if print_results: print("Parity: ", z)
        if sum(z) == 0:
            if message.all() != HammingViewModel.decodeMessage(Matrix.D11, x).all():
                context = False
        if not context:
            print("Failed Test: ", i)
            break
    if context:
        print("Hamming(15, 11) No Errors: SUCCESS")


def Hamming1511WithError(print_results):
    context = True
    for i in range(0, 2048):
        for error_location in range(0, 15):
            context = True
            if print_results: print("Num: ", i, "Error location: ", error_location)
            message = numpy.array([int(a) for a in list(bin(i)[2:].zfill(11))])
            if print_results: print("Message: ", message)
            x = HammingViewModel.encodeMessage(Matrix.generator11, message)
            if print_results: print("Flipping Bit: ", x)
            HammingViewModel.flip_bit(x, error_location)
            if print_results: print("Flipping bit we: ", x)
            z = HammingViewModel.generateParityCheckMatrix(Matrix.Hamming11, x)[::-1]
            if print_results: print("Parity: ", z)
            x = HammingViewModel.errorCorrection(x, z)
            if print_results: print("Fixed flipped bit: ", x)
            if sum(z) == 0:
                if message.all() != HammingViewModel.decodeMessage(Matrix.D11, x).all():
                    context = False
            if not context:
                print("Failed Test: ", i)
                break
    if context:
        print("Hamming(15, 11) with Errors: SUCCESS")


def runTests():
    print_results = False
    mode = input("Do you want to print the results? [Y/N]")
    if mode == 'Y' or mode == 'y':
        print_results = True
    context = input("Do you want to run tests for ConvertFBVectorToDecimal function? [Y/N] ")
    if context == 'Y' or context == 'y': ConvertFBVectorToDecimal(print_results)
    context = input("Do you want to run tests for Hamming74NoError function? [Y/N] ")
    if context == 'Y' or context == 'y': Hamming74NoError(print_results)
    context = input("Do you want to run tests for Hamming74WithError function? [Y/N] ")
    if context == 'Y' or context == 'y': Hamming74WithError(print_results)
    context = input("Do you want to run tests for Hamming1511NoError function? [Y/N] ")
    if context == 'Y' or context == 'y': Hamming1511NoError(print_results)
    context = input("Do you want to run tests for Hamming1511WithError function? [Y/N] ")
    if context == 'Y' or context == 'y': Hamming1511WithError(print_results)



