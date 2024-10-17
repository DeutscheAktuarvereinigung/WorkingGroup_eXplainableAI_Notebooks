<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Reimplementation ICE and PDP for a classification problem with continuous variables<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README covers installation details and provides a first overview of the content of the notebooks for the reimplementation of "PDP" and "ICE" in the context of a classification problem with continuous variables. 

# Getting Started

To run this notebook you just need

* A working python installation and jupyter notebook. For the development python version 3.10.0. was used.
* Necessary python packages to run the notebook are listed in the corresponding requirement file *requirements_hastie_ICE_PDP.txt.*

# Content overview

In this notebook we focus on the model-agnostic explainability methods **"Individual Conditional Expectation" (ICE)** and **"Partial Dependency Plot" (PDP)** as local respectively as a global explainability method. Aim of this notebook is to reimplement/understand the output of the XAI method *PartialDependenceDisplay* of the module *sklearn.inspection* for a quite simple binary classification problem and a Gradient Boosting model. Moreover, some hints concerning actuarial diligence are given.

## Author

Dr. Benjamin Müller (<a href="mailto:benjamin1985.mueller@t-online.de">benjamin1985.mueller@t-online.de</a>)

## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
