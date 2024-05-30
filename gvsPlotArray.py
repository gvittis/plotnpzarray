import plotly.graph_objects as go
from plotly.subplots import make_subplots
from gvsCompress import get_closest_split, CompressOverY, CompressOverX

import numpy as np
import numpy.typing as npt


class SetupArray():
    data       : tuple[npt.NDArray, npt.NDArray, npt.NDArray]
    Nycompress : int 
    Nxcompress : int 
    xrange     : list[int, int]
    logScale   : bool

    def __init__(self, zList: npt.NDArray, xRange : list[int, int], Nycompression: int = 1, Nxcompression: int = 1, logScale = False) -> None:
        self.data       = (np.arange(*xRange), np.arange(zList.shape[1]), zList)
        self.xrange     = xRange
        if Nycompression > 1:
            self.Nycompress = get_closest_split(zList.shape[1], Nycompression)
        else:
            self.Nycompress = 1

        if Nxcompression > 1:
            self.Nxcompress = get_closest_split(zList.shape[0], Nxcompression)
        else:
            self.Nxcompress = 1

        self.logScale = logScale

    def get_data(self) -> tuple[npt.NDArray, npt.NDArray, npt.NDArray]:
        if self.Nycompress == 1 and self.Nxcompress == 1:
            return self.data
        else: 
            return (self.get_xList(), self.get_yList(), self.get_zList())

    def get_xList(self) -> npt.NDArray:
        if self.Nxcompress == 1:
            return self.data[0]

        return self.data[0][::self.Nxcompress]
    
    def get_yList(self) -> npt.NDArray:
        if self.Nycompress == 1:
            return self.data[1]

        return self.data[1][::self.Nycompress]

    def get_zList(self) -> npt.NDArray:

        _output = self.data[2]

        if not self.Nycompress == 1:
            _output = CompressOverY(_output, self.Nycompress)
        if not self.Nxcompress == 1:
            _output = CompressOverX(_output, self.Nxcompress)
    
        if self.logScale :
            return np.where(_output < 1, np.zeros(_output.shape), np.log10(_output))
        
        return _output

    def create_wirecell_plot(self, cbar_dict: dict = {"x": 1}) -> None:
        """
        Creates a heatmap plot using Plotly with given data.

        Parameters:
        -----------
        xyzList : tuple
            A tuple containing the data arrays to be plotted. Each element in the tuple should be a 2D numpy array.
        Xarrange : numpy.ndarray
            A 1D numpy array specifying the x-axis values for the heatmap.
        NcompressY : int, optional
            The compression factor along the y-axis. Default is 1 (no compression).
        cbar_Xpos : float, optional
            The x-position of the colorbar. Default is 1.0.

        Returns:
        --------
        None
        """

        fig = go.Figure()

        fig.add_trace(go.Heatmap(x = self.get_xList(), 
                                y = self.get_yList(), 
                                z = self.get_zList().transpose(), 
                                colorbar = cbar_dict)
                                )

        fig.add_annotation(text=f"Ionization Charge (log10 Q)",
                        xref="paper", yref="paper", xanchor="center", yanchor="middle",
                        x= 0.98, y= 1.03, textangle=0, showarrow=False, font_size = 12)

        fig.update_layout(
            #margin=dict(l=70, r=100, b=100, t = 110),
            font_family = 'serif',
            font_size   = 15)

        fig.update_layout(
        xaxis_title="Channel Number",
        yaxis_title="Time Tick",
        title_text="ProtoDUNE Anode Planes", title_x=0.5)

        return fig


if __name__ == "__main__":

    #####################################
    #####################################
    ##                                 ##
    ##     Run the code                ##
    ##                                 ##
    #####################################
    #####################################

    ## Insert the name of your .npz file
    source_name = "numpyarrays.npz"
    
    ## Insert the path to your .npz file
    data = np.load("./pathtonpz/"+ source_name + ".npz")

    Nxcompression = 1
    Nycompression = 1
    
    ## Get the frames after passing gauss filter.
    ## .pdf outputs provide more resolution to the image. They have bigger size though.
    for key in data:
        if "frame_gauss_" in key:
            ievent = int(key[len("frame_gauss_"):])
            inputData = data[f'frame_gauss_{ievent}']
            MyArray = SetupArray(inputData, xRange = [0,inputData.shape[0]], Nycompression= Nycompression, Nxcompression= Nxcompression,logScale = True)
            if Nxcompression == 1 and Nycompression == 1:
                MyArray.create_wirecell_plot().write_image(f"./nameoftheoutputpathofnotcompressedimages/nameofoutputfile_{ievent}.png", scale = 6)
            else: 
                MyArray.create_wirecell_plot().write_image(f"./nameoftheoutputpathofcompressedimages/nameofoutputfile_{ievent}.png", scale = 6)
            break
