input = "11100001110010110100111011101110100010000001010001101100110000111011011100010110010011000010100000111100001110100101110110101011011111101001110111001010001100110110111111100101101101110000111101000101000110111111100101100100010100011000110101001010110001000100110000011011111000100100010010100101000001100110110111111100100100000110001101000001101001110111001000001111000010101111100101100101111000011100100101000010100011110000101100010100101010010101001010100101010000100111111000011100101101001110111011101000100000010100011011001100001110110111000101100100110000101000001111000011101001011101101010110111111010011101110010100011001101101111111001011011011100001111010001010001101111111001011001000101000110001101010010101100010001001100000110111110001001000100101001010000011001101101111111001001000001100011010000011010011101110010000011110000101011111001011001011110000111001001010000101000111100001011000101001010100101010010101001010011101011000101001"




list = [input[i:i+7] for i in range(0, len(input), 7)]
outlist = []
output = ""
for binchar in list:
    if binchar == "0100000":
        outlist.append(" ")
    if binchar == "0100001":
        outlist.append("!")
    if binchar == "0100010":
        outlist.append('"')
    if binchar == "0100011":
        outlist.append("#")
    if binchar == "0100100":
        outlist.append("$")
    if binchar == "0100101":
        outlist.append("%")
    if binchar == "0100110":
        outlist.append("&")
    if binchar == "0100111":
        outlist.append("'")
    if binchar == "0101000":
        outlist.append("(")
    if binchar == "0101001":
        outlist.append(")")
    if binchar == "0101010":
        outlist.append("*")
    if binchar == "0101011":
        outlist.append("+")
    if binchar == "0101100":
        outlist.append(",")
    if binchar == "0101101":
        outlist.append("-")
    if binchar == "0101110":
        outlist.append(".")
    if binchar == "0101111":
        outlist.append("/")
    if binchar == "0110000":
        outlist.append("0")
    if binchar == "0110001":
        outlist.append("1")
    if binchar == "0110010":
        outlist.append("2")
    if binchar == "0110011":
        outlist.append("3")
    if binchar == "0110100":
        outlist.append("4")
    if binchar == "0110101":
        outlist.append("5")
    if binchar == "0110110":
        outlist.append("6")
    if binchar == "0110111":
        outlist.append("7")
    if binchar == "0111000":
        outlist.append("8")
    if binchar == "0111001":
        outlist.append("9")
    if binchar == "0111010":
        outlist.append(":")
    if binchar == "0111011":
        outlist.append(";")
    if binchar == "0111100":
        outlist.append("<")
    if binchar == "0111101":
        outlist.append("=")
    if binchar == "0111110":
        outlist.append(">")
    if binchar == "0111111":
        outlist.append("?")
    if binchar == "1000000":
        outlist.append("@")
    if binchar == "1000001":
        outlist.append("A")
    if binchar == "1000010":
        outlist.append("B")
    if binchar == "1000011":
        outlist.append("C")
    if binchar == "1000100":
        outlist.append("D")
    if binchar == "1000101":
        outlist.append("E")
    if binchar == "1000110":
        outlist.append("F")
    if binchar == "1000111":
        outlist.append("G")
    if binchar == "1001000":
        outlist.append("H")
    if binchar == "1001001":
        outlist.append("I")
    if binchar == "1001010":
        outlist.append("J")
    if binchar == "1001011":
        outlist.append("K")
    if binchar == "1001100":
        outlist.append("L")
    if binchar == "1001101":
        outlist.append("M")
    if binchar == "1001110":
        outlist.append("N")
    if binchar == "1001111":
        outlist.append("O")
    if binchar == "1010000":
        outlist.append("P") 
    if binchar == "1010001":
        outlist.append("Q")
    if binchar == "1010010":
        outlist.append("R")
    if binchar == "1010011":
        outlist.append("S")
    if binchar == "1010100":
        outlist.append("T")
    if binchar == "1010101":
        outlist.append("U")
    if binchar == "1010110":
        outlist.append("V")
    if binchar == "1010111":
        outlist.append("W")
    if binchar == "1011000":
        outlist.append("X")
    if binchar == "1011001":
        outlist.append("Y")
    if binchar == "1011010":
        outlist.append("Z")
    if binchar == "1011011":
        outlist.append("[")
    if binchar == "1011100":
        outlist.append("\\")
    if binchar == "1011101":
        outlist.append("]")
    if binchar == "1011110":
        outlist.append("^")
    if binchar == "1011111":
        outlist.append("_")
    if binchar == "1100000":
        outlist.append("`")
    if binchar == "1100001":
        outlist.append("a")
    if binchar == "1100010":
        outlist.append("b")
    if binchar == "1100011":
        outlist.append("c")
    if binchar == "1100100":
        outlist.append("d")
    if binchar == "1100101":
        outlist.append("e")
    if binchar == "1100110":
        outlist.append("f")
    if binchar == "1100111":
        outlist.append("g")
    if binchar == "1101000":
        outlist.append("h")
    if binchar == "1101001":
        outlist.append("i")
    if binchar == "1101010":
        outlist.append("j")
    if binchar == "1101011":
        outlist.append("k") 
    if binchar == "1101100":
        outlist.append("l")
    if binchar == "1101101":
        outlist.append("m")
    if binchar == "1101110":
        outlist.append("n")
    if binchar == "1101111":
        outlist.append("o")
    if binchar == "1110000":
        outlist.append("p")
    if binchar == "1110001":
        outlist.append("q")
    if binchar == "1110010":
        outlist.append("r")
    if binchar == "1110011":
        outlist.append("s")
    if binchar == "1110100":
        outlist.append("t")
    if binchar == "1110101":
        outlist.append("u")
    if binchar == "1110110":
        outlist.append("v")
    if binchar == "1110111":
        outlist.append("w")
    if binchar == "1111000":
        outlist.append("x")
    if binchar == "1111001":
        outlist.append("y")
    if binchar == "1111010":
        outlist.append("z")
    if binchar == "1111011":
        outlist.append("{")
    if binchar == "1111100":
        outlist.append("|")
    if binchar == "1111101":
        outlist.append("}")
    if binchar == "1111110":
        outlist.append("~")
for character in outlist:
    output += character
print(output)