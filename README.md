# Starting kit for the Paris_Accident prediction RAMP challenge

*Nayel Bettache (ENSAE), Axel Marchand (ENSAE), Solène Cochennec (HEC-ENSAE), Rodrigue Rillardon (ENSAE)*
For every single road accident (meaning an accident that occured on a road open to the public) that took part between at least
one vehicle, there are a lot of informations that are recorded and constituting a database made available publicly with
the Open Data Gouv Movement.

We have joined this road accident with traffic information extracted from Open Paris Data. The aim of the challenge 
is clear, try to guess the number of road accident in a Paris neighbourhood during an hour.

## Getting started

This starting kit requires Python and the following dependencies:


* `numpy`
* `scipy`
* `pandas`
* `scikit-learn>=0.20`
* `matplotlib`
* `jupyter`
* `folium`
* `geopandas`
* `shapely`
* `tqdm`
* `os`
* `GoogleDriveDownloader`
* `seaborn`
* `ramp-workflow`



You can get started on this RAMP challenge with the
[dedicated notebook](France_Accidents_Prediction_Starting_KIT.ipynb) by running the following command
from the root directory:

```
jupyter notebook France_Accidents_Prediction_Starting_KIT.ipynb
```

For more information on the [RAMP](http:www.ramp.studio) ecosystem go to
[`ramp-worflow`](https://github.com/paris-saclay-cds/ramp-workflow).