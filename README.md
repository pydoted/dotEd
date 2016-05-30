dotEd - A graphic editor for DOT graphs
========================================================
![dotEd logo](https://cloud.githubusercontent.com/assets/10775422/15577572/5d88e09e-235d-11e6-8c5b-8ac4f9ebaced.png)

## Requirements
 * [Python 3](https://www.python.org/)
 * [PyQt5](https://riverbankcomputing.com/software/pyqt/intro)

## Installation
```bash
python setup.py install
```

## Run
```bash
doted 
```

## Uninstall
```bash
pip uninstall doted
```

## Notes
To avoid problems when importing a DOT file, all statements must end with a semicolon.  
If nodes statements do not have a **pos** attribute, you can automatically generate them with **xdot** :
```bash
dot -T xdot file.dot
```
