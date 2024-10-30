<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Explanation of Individual Conditional Expectation, Partial Dependence Plot and Feature Importance<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README covers installation details and provides a first overview of the content of the notebooks for the reimplementation of "PDP", "ICE" and "FI" for tree-based models within "scikit-learn". 

# Getting Started

To run this notebook you just need

* A working python installation and jupyter notebook. For the development python version 3.10.0. was used.
* Necessary python packages to run the notebook are listed in the corresponding requirement file *requirements_SwedM_ICE_PDP_FI.txt.*
* The necessary dataset *SwedishMotorInsurance.csv* and some further python help functions in file *help_functions.py* can be found on https://github.com/DeutscheAktuarvereinigung/WorkingGroup_eXplainableAI_Notebooks/tree/main/Reimplementations/Regression/ICE_PDP_FI/ and must be in the same folder as the notebook.

# Content overview

In this notebook, we explore model-agnostic explainability methods, specifically **"Individual Conditional Expectation" (ICE)** as a local method and **"Partial Dependence Plot" (PDP)** as a global method. Additionally, we discuss the popular model-specific and global **"Feature Importance" (FI)** explanation method for tree-based models in *scikit-learn*. For these purposes a regression example in car insurance with categorical variables is considered. Moreover, some hints concerning actuarial diligence are given and the usage of one hot encoding within PDP and ICE is discussed.

## Author

Dr. Benjamin Müller (<a href="mailto:benjamin1985.mueller@t-online.de">benjamin1985.mueller@t-online.de</a>)

## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
