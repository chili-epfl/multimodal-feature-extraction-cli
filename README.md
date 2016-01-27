# multimodal-feature-extraction-cli
A meta-tool for low- and mid-level feature extraction for multimodal machine learning applications

## Dependencies

* Python, Pypy, etc.
* [click](http://click.pocoo.org/) (a tool for creating Pyton command-line tools)

Other than these general dependencies, for the feature extraction the following is needed:

* [OpenSMILE](http://www.audeering.com/research/opensmile#download)

## Installation

TODO: Check exactly how it is distributed in binary form (it has setuptools support, see http://click.pocoo.org/6/setuptools/#setuptools-integration )


1. install [click](http://click.pocoo.org/)

    sudo pip install virtualenv
    pip install click

See other steps at https://www.youtube.com/watch?v=kNke39OZ2k0


## Usage


    mmfe [OPTIONS] [INPUTFILE] [OUTPUTFILE]

    For example:

    mmfe --features audio --format csv audio.wav features.csv 

