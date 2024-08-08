<!-- Simon-Style -->
<p style="font-size:19px; text-align:left; margin-top:    15px;"><i>German Association of Actuaries (DAV) — Working Group "Explainable Artificial Intelligence"</i></p>
<p style="font-size:30px; text-align:left; margin-bottom: 15px"><b>README: Use Case SOA GLTD Experience Study<br>
</b></p>
<p style="font-size:19px; text-align:left; margin-bottom: 15px; margin-bottom: 15px">

# Description

This README covers installation details and provides a first overview of the content of the notebooks for the use case "Insurance SCR". 

# Getting Started

To run these notebooks you just need

* A working R installation and the capability to execute Rmarkdown scripts 
* Access to CRAN or one of its mirrors to install some libraries

If you would like to run the "gradient" analysis you need in addition to the above

* A Python environment supporting PyTorch and GpyTorch (see installation instructions in the script)
* The R package `reticulate`


# Content overview

There are five Rmarkdown scripts, called "reports", covering various aspects of the use case "Insurance SCR". 

The actuarial ideas behind this use case and reasons for its relevance are described on    [this](https://aktuar.de/en/practice-areas/data-science/use-cases/use_case2/Pages/default.aspx) webpage. While the use case arises out of a question about life insurance within Solvency II, no familiarity with either life insurance or Solvency II is assumed or required. All reports can be read and understood on a stand-alone basis just viewing the data as a supervised regression problem.

The reports are:

* A consecutive set of three reports covering variance decomposition: "report_scr_maineff", "report_scr_interaction" and "report_scr_NonParametric". Since they build on each other and the models' complexity is gradually increased, it is probably best to read them in this sequence.
* A report focusing on tails and tail measures "report_scr_Tail"
* A report performing gradient analysis "report_gradient".

The latter two reports cover independent aspects and do not directly reference each other or the former three reports. The gradient analysis is done using PyTorch's auto-differentiation. Hence, it assumes basic familiarity with using Python runtime environments within R and `reticulate`. Beyond its substantive content, this report may be interesting for R users from a technical perspective. As it provides a non-trivial example for the smooth interplay between R and Python and the use of automatic differentiation. To support users unfamiliar with Python or PyTorch, the script contains references to detailed installation instructions.

All other reports are pure R respectively Rmarkdown and should run out-of-the-box after installation of the required packages. All packages can be found on CRAN or a mirror thereof. 

For quick browsing and overview a fully rendered HTML report is included for each executable script.
Note that Github itself just shows you the raw HTML. Like the Rmarkdown scripts you need to download and view them in your browser.   

## Author

Guido Grützner (<a href="mailto:guido.gruetzner@quantakt.com">guido.gruetzner@quantakt.com</a>)


## Version History

* 1.0 Initial Release

## License

This project is licensed under the GPLv3.0 License - see the LICENSE.md file for details