<h1 align="center">
<img src="https://git.mpi-cbg.de/tothpetroczylab/picnic/-/raw/main/branding/logo/logo_picnic_v1.96113169.png" width="300">
</h1><br>

# PICNIC

PICNIC (Proteins Involved in CoNdensates In Cells) is a machine learning-based model that predicts proteins involved in biomolecular condensates. The first model (PICNIC) is based on sequence-based features and structure-based features derived from Alphafold2 models. Another model includes extended set of features based on Gene Ontology terms (PICNIC-GO). Although this model is biased by the already available annotations on proteins, it provides useful insights about specific protein properties that are enriched in proteins of biomolecular condensate. Overall, we recommend using PICNIC that is an unbiased predictor, and using PICNIC-GO for specific cases, for example for experimental hypothesis generation.

# External software

*IUPred2A*

IUPred2A is a tool that predicts disordered protein regions. It is available for download via the link https://iupred2a.elte.hu/download_new
The downloaded archive should be unpacked into the "src/files/" directory.

*STRIDE*

STRIDE is a software for protein secondary structure assignment 
Installation guide can be found here https://webclu.bio.wzw.tum.de/stride/

# Installation instructions

A binary installer for the latest released version is available at the Python Package Index (PyPI).

## Requirements

* Python versions >=3.9,<3.12
* Download and unpack IUPred2A
  * Add IUPred2A to PYTHONPATH
* Download and unpack STRIDE
  * Add STRIDE binary to your system PATH


## Install external requirements

### How to install STRIDE?

A complete installation guide can be found [here](https://webclu.bio.wzw.tum.de/stride/install.html) or simply
run the following commands:

```shell
$ mkdir stride
$ cd stride
$ curl -OL https://webclu.bio.wzw.tum.de/stride/stride.tar.gz
$ tar -zxf stride.tar.gz
$ make
$ export PATH="$PATH:$PWD"
```

### How to install IUPred2A?

IUPred2A software is available for free only for academic users and it cannot be used for commercial purpose.
If you are an academic user, then you can download IUPred2A by filling out the following form [here](https://iupred2a.elte.hu/download_new).

```shell
# Step 1: Fill out the form above and download the IUPred2A tar ball
$ tar -zxf iupred2a.tar.gz
$ cd iupred2a
$ export PYTHONPATH="$PWD"
```

## PICNIC is available on PyPI

PICNIC officially supports Python versions >=3.9,<3.12.

```shell
$ python3 --version
Python 3.11.5
$ python3 -m pip install picnic_bio
```

## PICNIC is also installable from source

```shell
$ git clone git@git.mpi-cbg.de:atplab/picnic.git
```

Once you have a copy of the source, you can embed it in your own Python package, or install it into your site-packages easily

```shell
$ cd picnic
$ python3 -m venv picnic-env
$ source picnic-env/bin/activate
(picnic-env) $ python -m pip install .
```

## How to install PICNIC using Conda?

There isn't any binary installer available on Conda yet. Though it is possible to install PICNIC within a virtual Conda environment.

Please note that in a conda environment you have to pre-install catboost, before installing picnic-bio itself, otherwise the installation will fail when compiling the catboost package from source code. Also it is recommended to use and set up [conda-forge](https://conda-forge.org/docs/user/introduction.html) to fetch pre-compiled versions of catboost.

Please also note that catboost=1.2.2 is incompatible with Python 3.12. The maintainers of catboost are working towards a fix right now.

We have documented how to get around the catboost installation issue.

```shell
$ conda config --add channels conda-forge
$ conda config --set channel_priority strict
$ conda create -n myenv python=[3.9, 3.10, 3.11] catboost=1.2.2
$ conda activate myenv
(myenv) $ python -m pip install picnic_bio
```

# How to use?

## Usage - Using PICNIC from command line

```
$ picnic <is_automated> <path_af> <protein_id> <is_go> --path_fasta_file <file>

usage: PICNIC [-h] [--path_fasta_file PATH_FASTA_FILE]
              is_automated path_af protein_id is_go

PICNIC (Proteins Involved in CoNdensates In Cells) is a machine learning-based
model that predicts proteins involved in biomolecular condensates.

positional arguments:
  is_automated          True if automated pipeline (works for proteins with
                        length < 1400 aa, with precalculated Alphafold2 model,
                        deposited to UniprotKB), else manual pipeline
                        (protein_id, Alphafold2 model(s) and fasta file are
                        needed to be provided as input)
  path_af               directory with pdb files, created by Alphafold2 for
                        the protein in the format. For smaller proteins ( <
                        1400 aa length) AlphaFold2 provides one model, that
                        should be named: AF-protein_id-F1-v{j}.pdb, where j is
                        a version number. In case of large proteins Alphafold2
                        provides more than one file, and all of them should be
                        stored in one directory and named: 'AF-
                        protein_id-F{i}-v{j}.pdb', where i is a number of
                        model, j is a version number.
  protein_id            protein identifier in UniprotKB (should correspond to
                        the name 'protein_id' for Alphafold2 models, stored in
                        directory_af_models)
  is_go                 boolean flag; if 'True', picnic_go score (picnic
                        version with Gene Ontology features) will be
                        calculated, Gene Ontology terms are retrieved in this
                        case from UniprotKB by protein_id identifier;
                        otherwise default picnic score will be printed
                        (without Gene Ontology annotation)

options:
  -h, --help            show this help message and exit
  --path_fasta_file PATH_FASTA_FILE
                        directory with sequence file in fasta format
```

## Examples

Run automated pipeline for a given UniProt Id:
```shell
$ picnic True notebooks/test_files/Q99720/ Q99720 True
```
Run manual pipeline for a given UniProt Id:
```shell
$ picnic False 'notebooks/test_files/O95613/' 'O95613' False --path_fasta_file 'notebooks/test_files/O95613/O95613.fasta.txt'
```
Run manual pipeline for your own protein sequence called MY_PROTEIN, which has no reference to UniProt:
```shell
$ picnic False 'notebooks/test_files/MY_PROTEIN/' 'MY_PROTEIN' False --path_fasta_file 'notebooks/test_files/MY_PROTEIN/my_protein.fasta'
```
Examples of using PICNIC are shown in a jupyter-notebook in notebooks folder.

## How to run the provided Jupyter notebook?

Examples of how to use and run PICNIC are shown in a provided Jupyter notebook. The notebook can be found under the
**notebooks** folder.

### What is Jupyter Notebook?

Please read documentation [here](https://saturncloud.io/blog/how-to-launch-jupyter-notebook-from-your-terminal/#what-is-jupyter-notebook).


### How to create a virtual environment and install all required Python packages.

Create a virtual environment by executing the command venv:
```shell
$ python -m venv /path/to/new/virtual/environment
# e.g.
$ python -m venv my_jupyter_env
```

Then install the classic Jupyter Notebook with:
```shell
$ source my_jupyter_env/bin/activate

$ pip install notebook
```
Also install picnic-bio from source in the same virtual environment...
```shell
$ pip install .
```

### How to Launch Jupyter Notebook from Your Terminal?

In your terminal source the previously created virtual environment...
```shell
$ source my_jupyter_env/bin/activate
```
Launch Jupyter Notebook...
```shell
$ jupyter notebook
```
Open the example notebook called 'picnic_examples.ipynb' under the notebooks folder.  

# Link to paper

[DOI: 10.1101/2023.06.01.543229](https://www.biorxiv.org/content/10.1101/2023.06.01.543229v2)

# Development

## Getting started

### Add your SSH key to GitLab

Before you start make sure you have a [SSH key generated](https://git.mpi-cbg.de/help/ssh/index#generate-an-ssh-key-pair) and the [public SSH Key added to your GitLab account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
You only have to do this once!

Every time you open a new console/terminal make sure your ssh-agent is running and all SSH keys are added.

```shell
$ eval `ssh-agent -s` && ssh-add
```

### Download and unpack IUPred2A

Fill out and submit the IUPred2A web form [here](https://iupred2a.elte.hu/download_new) to request the iupred2a.tar.gz archive.
Once you received the archive please unpack the TAR ball under the following project sub folder src/files/:

```shell
$ cd picnic/bin
$ cp blah/iupred2a.tar.gz .
$ tar -xvf iupred2a.tar.gz
$ cd iupred2a
$ export PYTHONPATH="$PWD"
```

## How to enable BuildKit?

This could be achieved in different ways. Follow documentation [here](https://brianchristner.io/what-is-docker-buildkit/).

There are 2 main options:

* Enable the BuildKit in your local Docker Desktop
* Enable the BuildKit in a fresh terminal

### Enable the BuildKit in a fresh terminal

```
export DOCKER_BUILDKIT=1
```

#### On Linux machines, you may also need:
```
export COMPOSE_DOCKER_CLI_BUILD=1
```

## Building your Docker images

```shell
$ docker build --build-arg="PYTHON_VERSION=3.10.13" . -f Dockerfile -t atplab/picnic-service
```

### Run your image as a container

```shell
$ docker run atplab/picnic-service

e.g.
$ docker run atplab/picnic-service True 'notebooks/test_files/Q99720/' 'Q99720' True
```

### Create an interactive bash shell in the container

```shell
$ docker run -it --entrypoint sh atplab/picnic-service
```

# Packaging and distribution

## Getting started

### Install packages required for building and distributing a Python project

```shell
// Create a new env - one off task
$ python3 -m venv packaging

$ source packaging/bin/activate

(packaging) $ pip install -r requirements-packaging.txt
```

### How to install and run the PICNIC package locally from the project root directory?

```shell
(venv) % cd /<path-to-project-root-folder>/picnic

(venv) % pip install .

# Type in the picnic command to found out if the installation was successfully
(venv) % picnic                                                                            
usage: PICNIC [-h] [--path_fasta_file PATH_FASTA_FILE] is_automated path_af protein_id is_go
PICNIC: error: the following arguments are required: is_automated, path_af, protein_id, is_go
```

### How to build the PICNIC package from the project root directory?

Run the following command from the root directory to build the package. This will create a dist 
folder where the wheel distribution is built along with a zip file.
```shell
(packaging) $ cd /<path-to-project-root-folder>/picnic

(packaging) $ python -m build

(packaging) $ ls -l dist 
picnic-bio-1.0.0b1.tar.gz
picnic_bio-1.0.0b1-py3-none-any.whl

(packaging) $ twine check dist/*
```

### How to upload distribution files to PyPi?

Finally, we need to upload these files to PyPi using Twine. Use the following command from the project root
directory. Enter the PyPi credentials to complete uploading the package.

```shell
(packaging) $ twine upload dist/*
```


### How to deactivate the virtual environment?

```shell
(packaging) $ deactivate
```