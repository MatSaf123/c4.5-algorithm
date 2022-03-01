from main import read_from_file, count_classes, count_class_occurances


def test_read_from_file():
    expected = [
        ["old", "yes", "swr", "down"],
        ["old", "no", "swr", "down"],
        ["old", "no", "hwr", "down"],
        ["mid", "yes", "swr", "down"],
        ["mid", "yes", "hwr", "down"],
        ["mid", "no", "hwr", "up"],
        ["mid", "no", "swr", "up"],
        ["new", "yes", "swr", "up"],
        ["new", "no", "hwr", "up"],
        ["new", "no", "swr", "up"],
    ]

    assert read_from_file("data/gielda.txt") == expected


def test_count_classes():
    expected = [3, 2, 2, 2]
    assert count_classes(read_from_file("data/gielda.txt")) == expected


def test_count_class_occurances():
    expected = [
        {"old": 3, "new": 3, "mid": 4},
        {"yes": 4, "no": 6},
        {"swr": 6, "hwr": 4},
        {"down": 5, "up": 5},
    ]
    assert count_class_occurances(read_from_file("data/gielda.txt")) == expected
