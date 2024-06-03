## Please see the instructions below

You just need to download the content of this repository in your local/virtual machine.

## Before start

1. Adjust the name and path of your python environment inside "setup_python_env.sh" and "activate_python_env.sh" code lines. Specifically, change:

yourpythonenv
pathtoyourpythonenv

2. Adjust the name and path to the input and output files from "gvsPlotArray.py" file. They are in lines:

https://github.com/gvittis/plotnumpyarray/blob/d8e562018a1e5c68b74954b350f2fcc89d16345c/gvsPlotArray.py#L119 -> change source_name

https://github.com/gvittis/plotnumpyarray/blob/d8e562018a1e5c68b74954b350f2fcc89d16345c/gvsPlotArray.py#L122 -> change "./pathtonpz/"

https://github.com/gvittis/plotnumpyarray/blob/d8e562018a1e5c68b74954b350f2fcc89d16345c/gvsPlotArray.py#L135 -> change "./nameoftheoutputpathofnotcompressedimages/nameofoutputfile"

https://github.com/gvittis/plotnumpyarray/blob/d8e562018a1e5c68b74954b350f2fcc89d16345c/gvsPlotArray.py#L137 -> change "./nameoftheoutputpathofcompressedimages/nameofoutputfile"

## Running the code

First, setup and activate your local python environment to allow some extra packages installation. Do this command once:

source setup_python_env.sh

Then, always do:

source activate_python_env.sh

when opening a fresh terminal.

Finally, make sure you inserted the name and path of the .npz arrays as well as the name and path where the images will be saved and do:

python3 gvsPlotArray.py

## Some useful parameters

https://github.com/gvittis/plotnumpyarray/blob/f73f3b339f5191fc80426183ec79c8a495ae4a86/gvsPlotArray.py#L124 -> Compress over x axis

https://github.com/gvittis/plotnumpyarray/blob/f73f3b339f5191fc80426183ec79c8a495ae4a86/gvsPlotArray.py#L125C3-L125C22 -> Compress over y axis

Increase the "scale" variable in lines 135 and 137 for bigger images.

Export as .pdf if you want images with full resolution.

Uncomment line 138 if you want to process just the first frame of the arrays.






