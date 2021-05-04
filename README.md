ET and REL

``` conda install pandas```

``` conda install -c conda-forge tqdm```

``` conda install -c conda-forge spacy```

``` conda install -c conda-forge nltk```

``` python -m spacy download en_core_web_sm ```

Docker env defined in .devcontainer
microsoft-anaconda3 base image
todo for container spinup: before apt-get install parts in Dockerfile:
    RUN mkdir -p /usr/share/man/man1 (hack for ubuntu 18.04 java installation)

For now upon launch to the following for mallet:

 - sudo apt-get update
 - mkdir -p /usr/share/man/man1
 - sudo apt-get install default-jre
 - sudo apt install ant
 - download mallet (git clone ...)
 - cd mallet
 - ant (to build)

good to go.