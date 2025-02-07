from main import fizzbuzz

def test_fizz():
    assert fizzbuzz(4)[3] == "fizz"
    assert fizzbuzz(7)[6] == "fizz"
    assert fizzbuzz(10)[9] == "fizz"

def test_buzz():
    assert fizzbuzz(6)[5] == "buzz"
    assert fizzbuzz(11)[10] == "buzz"
    assert fizzbuzz(21)[20] == "buzz"

def test_fizzbuzz():
    assert fizzbuzz(16)[15] == "fizzbuzz"
    assert fizzbuzz(31)[30] == "fizzbuzz"
    assert fizzbuzz(46)[45] == "fizzbuzz"

def test_numbers():
    assert fizzbuzz(2)[1] == 1
    assert fizzbuzz(3)[2] == 2
    assert fizzbuzz(5)[4] == 4
