<!-- Simon-Style -->
<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Use Case SOA GLTD Experience Study<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This section covers installation details and provides a first overview of the content of the notebooks for the use case "SOA GLTD Experience Study". 

# Getting Started

The Society of Actuaries Group Disability Insurance Experience Committee has written a report which provides background on the use case and the data. It can be found at URL [GLTD report](https://www.soa.org/4a7e84/globalassets/assets/files/resources/experience-studies/2019/2019-gltd-study-report.pdf).

## Prerequisites

To run these notebooks you need

* Internet-access to download the original data from the SOA web site (see below)
* A Python environment including some means to install packages and display Jupyter notebooks (see below)
* At least 8GB of RAM (32GB recommended) 

## Python environment

We recommend the Miniconda package manager. Free download under [miniconda](https://docs.anaconda.com/free/miniconda/miniconda-other-installer-links/).
The notebooks were tested with Python 3.12.

Install packages

1.	Start Miniconda (anaconda) shell
2.	Run the commands

    ```
    conda update conda
    conda config --add channels conda-forge
    conda config --set channel_priority strict
    ```
3.	Create environment (here called "gltd")

    ```
    conda  create -n gltd
    conda activate gltd
    ```
4.	Install required libraries
    
    Either install current versions manually

    ```
    conda install scikit-learn pandas jupyter pyarrow glum matplotlib shap
    ```
    
    or use current versions as of time of writing of this ReadMe using the file "gltd_requirements.txt", which will instantiate a python 3.12 environment:

    ```
    conda create --name gltd --file ./requirements_gltd.txt
    ```

## Installation of the SOA GLTD data

1. Download the data from [https://cdn-files.soa.org/2019-group-ltd-exp-studies/2009-2013-gltd-consolidated-database.zip](https://cdn-files.soa.org/2019-group-ltd-exp-studies/2009-2013-gltd-consolidated-database.zip). For this description we assume that this zip-file is located in the working directory of the python session. If you choose to store it at a different location you have to edit the script in the next step and adjust the path to the data directory stored in `data_dir` from the current value of "./" to whatever is appropriate for your set up. The size of the zip-file is about 1.6GB.
2. Run the script "data_initialisation.ipynb". This script may take about 20 minutes to run. It only has to run once.
3. Run the script "data_preparation.ipynb". It contains some tests and an analysis of the data structure with comments. Furthermore it creates a data extract "gltd0913_work.feather", which is used in all subsequent notebooks.

This finalises the set-up. You can now run any of the other notebooks in any order.

## Content overview

Note that some of notebooks can take quite some time to run. In this case a rough estimate of run time is given in the introduction. You can always dial down (or up) the amount of processed data by adjusting `pct` in the notebooks.

* "data_eda": Marginal plots of raw data and exposures.
* "hptuning_tree" "hptuning_boost" *(coming soon)* Hyper-parameter tuning for the Gradient Boosted Tree (GBT) and the tree model.
* "rep_boost", "rep_tree", "rep_GLM": *(coming soon)* Fit and performance analysis of the three models of the use case.
* "rep_marginal": Marginal and calibration plots of the fitted models together with the raw data.
* "exp_pfi": Explanation method Permutation Feature Importance.
* "exp_drop1_boost", "exp_drop1_GLM": Explanation method drop1
* "edu_depPDP", "GLTD_SSA_extract.feather": Case study on impossible data and according data file.
* "exp_fanova", "edu_Hcorr": Analysis of interactions by variance analysis (correlated H-statistics)
* "gltd_utilities.py": purely technical file, contains a utility function as import
* "shap": SHAP Feature importance plots of the three models
* "cache_*.pkl" various files with internal data.

## Authors

Guido Grützner (<a href="mailto:guido.gruetzner@quantakt.com">guido.gruetzner@quantakt.com</a>)

Corinna Walk  (<a href="mailto:corinna.walk@viadico.com">corinna.walk@viadico.com</a>)

## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details