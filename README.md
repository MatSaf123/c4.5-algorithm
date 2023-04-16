# C4.5 Algorithm

Implementation of [C4.5 decision tree generation algorithm](https://en.wikipedia.org/wiki/C4.5_algorithm), made as a part of machine learning classes at University of Economics in Katowice, 2022.

# Run

I don't recall installing any dependencies other than some linting/formatting tools, so it's possible it will work straight out of box. But if not, then do the usual python venv setup steps:

1. Create python venv via your favorite tool (e.g. `python3 -m venv venv`) and activate it.
2. Run
```
pip install -r requirements.txt
```
3. Run with `python3 main.py`.

Paths to the data files are hardcoded and partly commented out inside of `main.py`, on the bottom. If you want to switch files, you need to (un)comment some lines. Data present in `/data` directory was provided as part of university classes.
