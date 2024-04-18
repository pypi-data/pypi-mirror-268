# After updating local file in /0/bp/

* Update local github folder with remote by Pull from origin/master
* `rsync -avc --dry-run --exclude-from ~/0/bp/icalcli/exclude \
  /home/jrvarma/0/bp/icalcli/ /home/jrvarma/0/src/github/icalcli/`
* `rsync -avc --exclude-from ~/0/bp/icalcli/exclude \
  /home/jrvarma/0/bp/icalcli/ /home/jrvarma/0/src/github/icalcli/`
* Commit changes in local github folder
* Push to remote origin/master

# After updating repo

* `rsync -avc --dry-run  --exclude '.git/' --exclude screenshots\
  ~/0/src/github/icalcli/ ~/0/bp/icalcli/ `
* `rsync -avc  --exclude '.git/' \
  ~/0/src/github/icalcli/ ~/0/bp/icalcli/ `

## Update PyPi

* Bump version number (Edit `setup.py`)

```
cd ~/0/bp/icalcli
rm /0/bp/icalcli/dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

## Install new version from PyPi

```
pip install --upgrade icalcli
```
