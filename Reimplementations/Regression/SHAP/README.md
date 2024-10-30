<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Explanation of Shapley Values<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README covers installation details and provides a first overview of the content of the notebooks for the reimplementation of shapley values. 

# Getting Started

To run this notebook you just need

* A working python installation and jupyter notebook. For the development python version 3.10.0. was used.
* Necessary python packages to run the notebook are listed in the corresponding requirement file *requirements_SwedM_shap.txt.*
* The necessary dataset *SwedishMotorInsurance.csv* can be found on https://github.com/DeutscheAktuarvereinigung/WorkingGroup_eXplainableAI_Notebooks/tree/main/Reimplementations/Regression/SHAP/ and must be in the same folder as the notebook.

# Content overview

In this notebook we consider an regression example in car insurance and build a simple Decision Tree Regressor model with deepness 2 and explain the prediction of it on a single dataset with the help of the "shap" package. Moreover, we show how one could implement the shapley values ourselves, compare them with the shapley values of the package and give some hints concerning actuarial diligence.

## Author

Dr. Benjamin Müller (<a href="mailto:benjamin1985.mueller@t-online.de">benjamin1985.mueller@t-online.de</a>)

## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details.
