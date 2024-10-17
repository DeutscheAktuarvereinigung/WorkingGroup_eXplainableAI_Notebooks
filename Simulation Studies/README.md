<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: ALE and PDP for correlated features<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README covers installation details and provides a first overview of the content of the notebook for the simulation study "ALE and PDP for correlated features". 


# Getting Started

We used the following packages to develop this notebook. 
- numpy==2.1.1 
- pandas==2.2.3 
- plotnine==0.13.6 
- scikit-learn==1.5.2 
- ipykernel==6.29.5

We included a requirements.txt file in the repo, which can be used to e.g. create a conda environment.


    conda create --name ale --file  requirements_ale.txt

If you are experiencing problems due to the strict use of version numbers, try using the requirements_ale_without_version_numbers.txt file or install the packages manually.


# Content overview

In this notebook, we study the behaviour of ALE and PDP for correlated features. 

## Authors

Florian Walla (<a href="mailto:Florian.Walla@hotmail.com">Florian.Walla@hotmail.com</a>)

Guido Grützner (<a href="mailto:guido.gruetzner@quantakt.com">guido.gruetzner@quantakt.com</a>)

## Version History

* 1.0 Initial Release

## License


This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
