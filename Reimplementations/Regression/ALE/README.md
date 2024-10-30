<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>Reimplementation of ALE for a Regression Problem with Simulated Data<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README includes installation instructions and provides an overview of the notebook related to the reimplementation of 'ALE'.

# Getting Started

We used the following packages to develop this notebook. 
- numpy==2.1.1 
- pandas==2.2.3 
- plotnine==0.13.6 
- scikit-learn==1.5.2 
- ipykernel==6.29.5
- pyale==1.2.0 


We included a requirements.txt file, which can be used to e.g. create a conda environment.


    conda create --name reimplementation_ale --file  requirements_ale_reimplementation.txt


If you are experiencing problems due to the strict use of version numbers, try using the requirements_ale_reimplementation_without_version_numbers.txt file or install the packages manually.





# Content overview

In this notebook, we reimplement the model-agnostic, global XAI method 'ALE' and compare our implementation to the one provided by the PyALE package.

## Authors

Florian Walla (<a href="mailto:Florian.Walla@hotmail.com">Florian.Walla@hotmail.com</a>)

Dr. Benjamin Müller (<a href="mailto:benjamin1985.mueller@t-online.de">benjamin1985.mueller@t-online.de</a>)

## Version History

* 1.0 Initial Release

## License


This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
