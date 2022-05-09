from main import (
    compute_entropy,
    compute_gain,
    compute_gain_ratio,
    compute_info,
    compute_probabilities,
    compute_split_info,
    read_from_file,
    count_classes,
    count_class_occurances,
)


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

def test_compute_probabilities():
    expected = [0.5, 0.5]
    assert compute_probabilities(read_from_file("data/gielda.txt")) == expected


def test_compute_entropy():
    expected = 1
    assert (
        compute_entropy(compute_probabilities(read_from_file("data/gielda.txt")))
        == expected
    )


def test_compute_info():
    expected = 0.4
    assert compute_info(0, read_from_file("data/gielda.txt")) == expected


def test_compute_gain():
    expected = 0.6
    assert compute_gain(0, read_from_file("data/gielda.txt")) == expected


def test_compute_split_info():
    expected = 1.5709505944546684
    assert compute_split_info(0, read_from_file("data/gielda.txt")) == expected


def test_compute_gain_ratio():
    expected = 0.3819343537078458
    assert compute_gain_ratio(0, read_from_file("data/gielda.txt")) == expected
    # compute_gain_ratio(1, read_from_file("data/gielda.txt"))
