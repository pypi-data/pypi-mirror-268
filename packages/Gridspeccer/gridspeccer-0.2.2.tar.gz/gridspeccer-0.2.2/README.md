# gridspeccer

Plotting tool to make plotting with many subfigures easier, especially for publications. 
After installation `gridspeccer` can be used from the command line to create plots
```
gridspeccer [path]
```

[![install module](../../workflows/install%20module/badge.svg)](../../actions/workflows/run_setup.yaml)
[![gsExample with mpl mathtext](../../workflows/gsExample%20with%20pseudo%20tex/badge.svg)](../../actions/workflows/gsExample.yaml)
[![gsExample with latex math](../../workflows/gsExample%20with%20tex/badge.svg?branch=master)](../../actions/workflows/gsTexExample.yaml)

### Installation
You can install either from [PyPi](https://pypi.org/project/Gridspeccer/)
```
pip install [--user] gridspeccer
```
or the current version from GitHub
```
pip install [--user] git+https://github.com/gridspeccer/gridspeccer/
```
For a debug version where local changes are automatically in effect, clone the repository and install it with the editable flag `-e`
```
git clone https://github.com/gridspeccer/gridspeccer
cd gridspeccer
pip install -e [--user] .
```

### Usage
A standalone plot file that does not need data is `examples/fig_setup.py`, this is also used for testing, see [actions](https://github.com/gridspeccer/gridspeccer/actions).

* `gridspeccer` can be used on specific files `gridspeccer fig_setup.py` or on folders (no argument is equivalent to CWD `.`), in which files that satisfy `fig*.py` are searched for.
* with the optional argument `--mplrc [file]` one can specify a matplotlibrc to be used for plotting (two examples in `gridspeccer/defaults/`)
* default filetype of the plot is `.pdf`, for other filetypes specify, e.g., `--filetype .png`
* plots are saved to `../fig/` by default, can be specified by `--output-folder FOLDER`

### Requirements
* python3
* matplotlib
* LaTeX (in case you want true latex and not [matplotlib's Tex parser for mathtext](https://matplotlib.org/stable/tutorials/text/mathtext.html)

### Notes
* Don't install using `python setup.py install`, as this will create an `.egg`, and the default `matplotlibrc`s will not be accessible.
* Many old examples that are not executable at the moment can be found in `old_examples`, to serve as inspiration for other plots.
* For an example using `gridspeccer` see [JulianGoeltz/automised_latex_template](https://github.com/JulianGoeltz/automised_latex_template). Recent papers utilising `gridspeccer` include 
  * Göltz, J.∗, Kriener, L.∗, Baumbach, A., Billaudelle, S., Breitwieser, O., Cramer, B., ... & Petrovici, M. A. (2021). Fast and energy-efficient neuromorphic deep learning with first-spike times. [*Nature Machine Intelligence*, 3(9), 823-835.](https://www.nature.com/articles/s42256-021-00388-x), 3(9), 823-835. preprint at https://arxiv.org/abs/1912.11443
  * Haider, P., Ellenberger, B., Kriener, L., Jordan, J., Senn, W., & Petrovici, M. A. (2021). Latent equilibrium: A unified learning theory for arbitrarily fast computation with arbitrarily slow neurons. [*Advances in Neural Information Processing Systems*](https://papers.nips.cc/paper/2021/hash/94cdbdb84e8e1de8a725fa2ed61498a4-Abstract.html), 34, 17839-17851. preprint at https://arxiv.org/abs/2110.14549


### Todos
* make true tex standard?
* Format code to satisfy linting, then update linting workflow
[![linting](../../workflows/lint/badge.svg)](../../actions/workflows/lint.yaml)
