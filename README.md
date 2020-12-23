# ProcessObserver

## OverView

A module that provides functions to observe process and keep itself running continuously.
It is supposed to be called regularly by crontab or systemd.

## Usage

### Installation

For install this, please execute this command shown below:

    pip install git+https://github.com/Enchan1207/ProcessObserving

### In your script

In your script, you can call this library to:

    from ProcessObserver.observer as observer

    observer.has...
    observer.register....

## Licence

All files included in this repository is published under MIT LICENCE.
In details, please see `LICENCE`.
