import os
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from scipy import interpolate

# cartopy related imports
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

class Plot:
    def __init__(self, data, instrument='HARP2'):
        self.data = data
        self.plotDPI = 240
        self.xAxis = 'scattering_angle'
        if instrument.lower() == 'harp2':
            self.instrument = 'HARP2'
            # by default set the band to blue
            self.band = 'blue'
            self.bandAngles = range(80, 90)
            self.wavIndex = 0

        elif instrument.lower() == 'spexone':
            self.instrument = 'SPEXone'
            self.wavIndex = range(0, self.data['intensity_wavelength'].shape[1], 40)
            self.wavIndexDolp = range(0, self.data['dolp'].shape[1], 5)

        elif instrument.lower() == 'oci':
            self.instrument = 'OCI'
            self.xAxis = 'intensity_wavelength'
            self.band = 'all'
            self.wavIndex = range(0, self.data['intensity_wavelength'].shape[1])
            # find the index of wavelengths closest to 440 nm
            self.bandAngles = range(0,2) # only two angles for OCI
        self.setInstrument(self.instrument)
        self.reflectance = False
        self.verbose = False
        self.setPlotStyle()


    def setPlotStyle(self,font=None):
        """Set the plot style for the plot.
        Args:
            None
        """
        plt.rcParams.update({
                    'xtick.direction': 'in',
                    'ytick.direction': 'in',
                    'ytick.right': 'True',
                    'xtick.top': 'True',
                    'mathtext.fontset': 'cm',
                    'figure.dpi': self.plotDPI,
                    'axes.unicode_minus': False,
        })

        if font:
            plt.rcParams.update({'font.family':font})


    def setBandAngles(self, band=None):
        """Set the band angles for the plot.
        Args:
            bandAngles (list): The band angles for the plot.

        Returns:
            None
        """
        band = self.band if band is None else band
        if self.instrument == 'HARP2':
            band_angle_ranges = {
                'blue': range(80, 90),
                'green': range(0, 10),
                'red': range(10, 70),
                'nir': range(70, 80)
            }
            self.bandAngles = band_angle_ranges.get(band, None)
        else:
            # Hard Coded for now
            self.bandAngles = range(0, 5) if self.instrument == 'SPEXone' else None


    def setBand(self, band, verbose=True):
        """Set the band for the plot.
        Args:
            band (str): The band for the plot.

        Returns:
            None
        """
        band_ = band.lower()
        assert band_ in ['blue', 'green', 'red', 'nir', 'swir1', 'swir2',  'all', 'harp2'], 'Invalid band'
        self.band = band_

        # set the angle specification based on the instrument
        self.setBandAngles(self.band) if self.instrument == 'HARP2' else None

        # for oci, set the wavelength index
        if self.instrument == 'OCI':
            if self.band == 'blue':
                self.wavIndex = np.argmin(np.abs(self.data['intensity_wavelength']-440)) 
            elif self.band == 'all':
                self.wavIndex = range(0, self.data['intensity_wavelength'].shape[1])
            # self.setBandAngles(band=self.band)
        elif self.instrument == 'SPEXone':
            if self.band == 'all':
                self.wavIndex = range(0, self.data['intensity_wavelength'].shape[1], 20)
            elif self.band.lower() == 'harp2':
                self.wavIndex = [63, 170, 285]
                self.wavIndexDolp = [10, 25, 39]
                self.bands = ['blue', 'green', 'red']
        else:
            self.wavIndex = 0

        print(f'...Band set to {self.band}') if verbose else None


    def setDPI(self, dpi):
        """Set the DPI for the plot.
        Args:
            dpi (int): The DPI for the plot.

        Returns:
            None
        """
        self.plotDPI = dpi if dpi is not None else None
        print('setting dpi to %d ppi' %self.plotDPI)
        plt.rcParams['figure.dpi'] = self.plotDPI


    def setInstrument(self, instrument=None):
        """Set the instrument for the plot.
        Args:
            instrument (str): The instrument for the plot.

        Returns:
            None
        """
        if instrument is None:
            instrument = self.instrument
        else:
            assert instrument.lower() in ['harp2', 'spexone', 'oci'], 'Invalid instrument'
            self.instrument = instrument

        if self.instrument == 'HARP2':
            self.bands = ['blue', 'green', 'red', 'nir']
            self.allBandAngles = [self.setBandAngles(band) for band in self.bands]

            # variable to plot
            self.vars2plot = ['i', 'q', 'u', 'dolp']
        
        elif self.instrument == 'SPEXone':
            self.bands = ['blue', 'green', 'red', 'nir']
            self.allBandAngles = [self.setBandAngles(band) for band in self.bands]

            # variable to plot
            self.vars2plot = ['i','q', 'u', 'q_over_i', 'u_over_i', 'dolp']

        elif self.instrument == 'OCI':
            self.bands = ['all']
            # self.allBandAngles = [self.setBandAngles(band) for band in self.bands]

            # variable to plot
            self.vars2plot = ['i']

        print(f'Instrument set to {self.instrument}')


    def plotPixel(self, x, y, dataVar='i', xAxis=None, xlim=None, ylim=None,
                  axis=None, axisLabel=True, returnHandle=False, title=True,
                  maskFlag=True,
                    **kwargs):
        """Plot the data for a pixel.

        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            dataVar (str): The variable to plot.
            xAxis (str): The x-axis variable.

        Returns:
            None
        """
        xAxis = self.xAxis if xAxis is None else xAxis
        assert xAxis in ['scattering_angle', 'view_angles', 'intensity_wavelength'], 'Invalid x-axis variable'
        xData_, dataVar_, unit_ = self.physicalQuantity(x, y, dataVar, xAxis=xAxis, maskFlag=maskFlag)

        # Plot the data
        fig_, ax_ = plt.subplots(figsize=(6, 4)) if axis is None else (None, axis)
        ax_.plot(xData_, dataVar_, **kwargs)
        if axisLabel:
            plt.xlabel(xAxis)
            if unit_:
                plt.ylabel(f'{dataVar}\n{unit_}')
            elif dataVar != 'dolp':
                plt.ylabel(r'R$_{%s}$' % dataVar)
            elif dataVar == 'dolp':
                plt.ylabel(dataVar)

        # if oci, plot linear+log  in x axis
        if self.instrument == 'OCI' and xAxis == 'intensity_wavelength':
            if xlim:
                ax_.set_xlim(xlim)
                ax_.set_xlim((xlim[0], xlim[1]))
                ax_.set_xticks([300, 400, 500, 600, 700, 800, 900])
        # set the limits
        if ylim:
            ax_.set_ylim(ylim)
            ax_.set_ylim((ylim[0], ylim[1]))

        if title:
            titleStr = f'{self.data["date_time"]} \nPixel ({x}, {y}) of the instrument {self.instrument}'
            plt.title(titleStr)

        plt.show()

        if returnHandle:
            return fig_, ax_
        
    def physicalQuantity(self, x=None, y=None, dataVar='i', xAxis='scattering_angle', maskFlag=True):
        """Get the physical quantity for the plot.

        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            dataVar (str): The variable to plot.
            xAxis (str): The x-axis variable.

        Returns:
            xData_ (np.ndarray): The x-axis data.
            dataVar_ (np.ndarray): The y-axis data.
            unit_ (str): The unit of the data.
        """

        if x is None and y is None:
            x, y = 100, 200 # default values

        # plot reflectance or radiance
        if self.instrument == 'HARP2':
            if self.reflectance and dataVar.lower() in self.vars2plot and dataVar.lower() not in ['dolp']:
                # πI/F0
                dataVar_ = self.data[dataVar][x, y, self.bandAngles,
                                                    self.wavIndex]*np.pi/self.data['F0'][self.bandAngles, self.wavIndex]
                unit_= ''
            else:
                dataVar_ = self.data[dataVar][x, y, self.bandAngles, self.wavIndex]
                unit_ = '('+self.data['_units'][dataVar]+')' if not dataVar == 'dolp' else ''

        elif self.instrument == 'OCI':
            # find if all values in a 2d array is masked
            if self.reflectance and dataVar in self.vars2plot:
                # πI/F0

                if self.bandAngles is not None:
                    for i in self.bandAngles:
                        if self.data[dataVar] is not None and not np.all(np.ma.getmask(self.data[dataVar][x, y, self.bandAngles[i], self.wavIndex])):
                            if maskFlag:
                                dataVar_ = np.ma.getdata(self.data[dataVar][x, y, self.bandAngles[i], self.wavIndex])*np.pi/self.data['F0'][self.bandAngles[i], self.wavIndex]
                            else:
                                dataVar_ = np.ma.getdata(self.data[dataVar][x, y, self.bandAngles[i], self.wavIndex])*np.pi/np.ma.getdata(self.data['F0'][self.bandAngles[i], self.wavIndex])
                            continue
                unit_= ''
            else:
                if self.bandAngles is not None:
                    for i in self.bandAngles:
                        # check if the data is masked, for the case of OCI only one viewing angle at a time
                        if not np.all(np.ma.getmask(self.data[dataVar][x, y, self.bandAngles[i], self.wavIndex])):
                            dataVar_ = self.data[dataVar][x, y, self.bandAngles[i], self.wavIndex]
                            continue
                # check any valid data found
                if 'dataVar_' not in locals():
                    print(f'...No valid data found for the variable {dataVar} at the pixel ({x}, {y})')
                    # end the script
                    return None, None, None
                unit_ = '('+self.data['_units'][dataVar]+')' if not dataVar == 'dolp' else ''
        elif self.instrument == 'SPEXone':
            waveIndex = self.wavIndex if dataVar in ['i'] else self.wavIndexDolp
            if self.reflectance and dataVar in self.vars2plot and dataVar.lower() not in ['dolp']:
                # πI/F0
                dataVar_ = self.data[dataVar][x, y, :, waveIndex].T*np.pi/self.data['F0'][:, waveIndex]
                unit_= ''
            else:
                dataVar_ = self.data[dataVar][x, y, :, waveIndex].T
                unit_ = '('+self.data['_units'][dataVar]+')' if not dataVar == 'dolp' else ''
        
        # for the scattering angle
        if xAxis == 'scattering_angle':
            xData_ = self.data[xAxis][x, y, self.bandAngles]
        # for the view angles
        elif xAxis == 'view_angles':
            xData_ = self.data[xAxis][self.bandAngles]
        elif xAxis == 'intensity_wavelength':
            xData_ = self.data[xAxis][self.bandAngles[i]] if self.instrument == 'OCI' else self.data[xAxis][self.bandAngles] # type: ignore

        return xData_, dataVar_, unit_

    def setFigure(self, figsize=(10, 5), **kwargs):
        """Set the figure size for the plot.
        Args:
            figsize (tuple): The figure size for the plot.

        Returns:
            None
        """

        if self.plotAll:
            # define the number of subplots
            print(f'...Setting the subplots with number of bands {len(self.bands2plot)} and number of variables {len(self.vars2plot)}')
            fig_, ax_ = plt.subplots(nrows = len(self.vars2plot), 
                                     ncols=len(self.bands2plot),
                                     figsize=figsize, sharex=True, **kwargs)
            
            return fig_, ax_


    
    # plot all bands in a single plot
    def plotPixelVars(self, x, y, xAxis='scattering_angle',
                     bands = None, saveFig=False,
                     axis=None, axisLabel=True, showUnit=True,
                    **kwargs):
        """
        Plot all bands for a pixel.

        Args:
            x (int): The x coordinate of the pixel.
            y (int): The y coordinate of the pixel.
            xAxis (str, optional): The x-axis variable. Defaults to 'scattering_angle'.
            bands (list, optional): List of bands to plot. If None, all bands are plotted. Defaults to None.
            saveFig (bool, optional): If True, the figure is saved. Defaults to False.
            axis (matplotlib.axes.Axes, optional): The axes object to draw the plot onto. If None, a new figure and axes are created. Defaults to None.
            axisLabel (bool, optional): If True, labels are added to the axes. Defaults to True.
            **kwargs: Variable length argument list to pass to the plot function.

        Returns:
            None
        """
        assert xAxis in ['scattering_angle', 'view_angles'], 'Invalid x-axis variable'
        if bands is None:
            self.plotAll = True
        self.bands2plot = self.bands if bands is None else bands
        tempBands = self.bands

        # based on the instrument, set the band angles 
        if axis is None:
            # Define the size of each subplot
            subplot_size = (2, 1.5)
            rows = len(self.vars2plot)
            cols = len(self.bands2plot)

            # Calculate the figure size to keep a good aspect ratio
            figsize = (subplot_size[0] * cols, subplot_size[1] * rows)
            figAll, axAll = self.setFigure(figsize=figsize) # type: ignore
        else:
            axAll = axis

        # define color strings based on the length of the bands try to preserve the color
        colors = ['C%d' %i for i in range(cols)]
        
        # plot the data over different bands and variables
        for i, vars in enumerate(self.vars2plot):
            for j, band in enumerate(self.bands2plot):
                # Set the title for the column
                axAll[i,j].set_title(band) if i == 0 else None

                # set the band and angles
                self.setBand(band, verbose=self.verbose)

                # get the physical quantity
                xData_, dataVar_, unit_ = self.physicalQuantity(x, y, vars, xAxis=xAxis)

                if self.instrument == 'SPEXone':
                    dataVar_ = dataVar_[:, j]

                # plot the data
                axAll[i,j].plot(xData_, dataVar_,
                                '%so-' %colors[j],
                                label= vars if j ==0 else None, **kwargs)
                
                # set the labels
                if axisLabel and j == 0:
                    if (unit_ and showUnit):
                        axAll[i,j].set_ylabel(f'{vars}\n{unit_}') 
                    elif self.reflectance:
                        axAll[i,j].set_ylabel(r'R$_%s$' %vars) if not vars == 'dolp' else axAll[i,j].set_ylabel(vars)
                    else:
                        axAll[i,j].set_ylabel(vars)
                    axAll[i,j].yaxis.set_label_coords(-0.25,0.5)

                if axisLabel and i == len(self.vars2plot)-1:
                    axAll[i,j].set_xlabel(xAxis)

        plt.suptitle(f'{self.data["date_time"]} \nPixel ({x}, {y}) of the instrument {self.instrument}')
        plt.tight_layout()
        plt.show()

        # if SPEXOne, change the band back to all
        if self.instrument == 'SPEXone':
            self.bands = tempBands

        # if saveFig is True, save the figure
        if saveFig:
            location = f'./{self.instrument}_pixel_{x}_{y}.png'
            figAll.savefig(location, dpi=self.plotDPI)

    def plotRGB(self, var='i', viewAngleIdx=[38, 4, 84],
                 scale= 1, normFactor=200, returnRGB=False, autoNorm=False,
                 plot=True, rgb_dolp=False, saveFig=False, **kwargs):
        """Plot the RGB image of the instrument.

        Args:
            var (str, optional): The variable to plot. Defaults to 'i'.
            viewAngleIdx (list, optional): The view angle indices. Defaults to [38, 4, 84].
            scale (int, optional): The scale factor. Defaults to 1.
            normFactor (int, optional): The normalization factor. Defaults to 200.
            returnRGB (bool, optional): If True, the RGB data is returned. Defaults to False.
            plot (bool, optional): If True, the RGB image is plotted. Defaults to True.
            **kwargs: Variable length argument list to pass to the plot function.

        Returns:
            None
        """

        # find the index to plot
        idx = viewAngleIdx

        # Check the number of indices
        if self.instrument == 'HARP2':
            assert len(idx) == 3, 'Invalid number of indices' 
        elif self.instrument == 'OCI':
            if not len(idx) == 3:
                assert len(idx) == 1, 'Invalid number of indices'
            else:
                if np.nanmean(self.data['latitude']) > 0:
                    viewAngleIdx = [1]
                else:
                    viewAngleIdx = [0]
                assert len(viewAngleIdx) == 1, 'Invalid number of indices'
        elif self.instrument == 'SPEXone':
            assert len(idx) == 3, 'Invalid number of indices'
            # the viewAngleIdx is the index of the wavelength should be between 0 to 5
            assert np.all(np.array(idx) < 5), 'Invalid viewAngleIdx'

        # Create a 3D array to store the RGB data
        rgb = np.zeros((self.data[var].shape[0], self.data[var].shape[1], 3), dtype=np.float16)

        # if the instrument is HARP2
        if self.instrument == 'HARP2':
            if rgb_dolp:
                rgb[:, :, 0] = self.data['i'][:,:,idx[0],0]*self.data[var][:,:,idx[0],0]
                rgb[:, :, 1] = self.data['i'][:,:,idx[1],0]*self.data[var][:,:,idx[1],0]
                rgb[:, :, 2] = self.data['i'][:,:,idx[2],0]*self.data[var][:,:,idx[2],0]
            else:
                rgb[:, :, 0] = self.data[var][:,:,idx[0],0]
                rgb[:, :, 1] = self.data[var][:,:,idx[1],0]
                rgb[:, :, 2] = self.data[var][:,:,idx[2],0]
        elif self.instrument == 'OCI' or self.instrument == 'SPEXone':
            # for the case of OCI, the variable is the intensity
            if self.instrument == 'SPEXone' and var == 'dolp':
                var_wav = 'polarization_wavelength'
            else:
                var_wav = 'intensity_wavelength'
            # find wavelength index close tor R, G, B
            #self.data['intensity_wavelength']-440
            idxB = np.argmin(np.abs(self.data[var_wav]-440))
            idxG = np.argmin(np.abs(self.data[var_wav]-550))
            idxR = np.argmin(np.abs(self.data[var_wav]-670))
            if var == 'dolp':
                rgb[:, :, 0] = self.data['i'][:,:,idx[0],idxR]*self.data[var][:,:,idx[0],idxR]
                rgb[:, :, 1] = self.data['i'][:,:,idx[1],idxG]*self.data[var][:,:,idx[1],idxG]
                rgb[:, :, 2] = self.data['i'][:,:,idx[2],idxB]*self.data[var][:,:,idx[2],idxB]
            else:
                
                if self.instrument == 'SPEXone':
                    rgb[:, :, 0] = self.data[var][:,:,idx[0],idxR]
                    rgb[:, :, 1] = self.data[var][:,:,idx[1],idxG]
                    rgb[:, :, 2] = self.data[var][:,:,idx[2],idxB]
                else: # for OCI
                    rgb[:, :, 0] = self.data[var][:,:,viewAngleIdx[0],idxR]
                    rgb[:, :, 1] = self.data[var][:,:,viewAngleIdx[0],idxG]
                    rgb[:, :, 2] = self.data[var][:,:,viewAngleIdx[0],idxB]

        # Normalize the RGB image
        if autoNorm:

            # calculate the normFactor for each band
            normFactor = np.zeros(3)

            # normalize the RGB to 0-1
            for rgbIdx in range(3):
                # normalize the RGB to 0-1 using nanmin and nanmax
                iMin = 10
                iMax = np.nanpercentile(rgb[:, :, rgbIdx], 99)
                rgb[:, :, rgbIdx] = (rgb[:, :, rgbIdx])/(iMax-iMin)
        else:
            # if normFactor is scalar, divide the RGB by the scalar else divide in a loop
            if not isinstance(normFactor, (int, float)):
                for i in range(3):
                    if isinstance(scale, (int, float)):
                        rgb[:, :, i] = rgb[:, :, i]/normFactor[i]*scale
        
            else:
                try:
                    if isinstance(scale, (int, float)):
                        rgb = rgb/normFactor*scale
                    else:
                        for i in range(3):
                            rgb[:, :, i] = rgb[:, :, i]/normFactor*scale[i]
                except Exception as e:
                    print(f'...Error in normalizing the RGB image {e}')
                    print('normFactor and scale shoulshould be an integer', normFactor)
        # Floor the rgb values to 0-1
        rgb = np.clip(rgb, 0, 1)

        # Plot the RGB image
        if plot:
            plt.imshow(rgb, origin='lower')
            if self.instrument == 'HARP2':
                plt.title(f'{self.data["date_time"]} \nRGB image of the instrument {self.instrument}\n using "{var}" variable at angles {idx[0]}, {idx[1]}, {idx[2]}', fontsize=8)
            elif self.instrument == 'OCI':
                plt.title(f'{self.data["date_time"]} \nRGB image of the instrument {self.instrument}\n using "{var}" variable at angle {viewAngleIdx[0]}', fontsize=8)
            elif self.instrument == 'SPEXone':
                plt.title(f'{self.data["date_time"]} \nRGB image of the instrument {self.instrument}\n using "{var}" variable at angles {idx[0]}, {idx[1]}, {idx[2]}', fontsize=8)
            plt.show()

        if returnRGB:
            self.rgb = rgb

        if saveFig:
            location = f'./{self.instrument}_RGB.png'
            plt.savefig(location, dpi=self.plotDPI)
            print(f'...RGB image saved at {location}')

    
    def projectVar(self, var='i', viewAngleIdx=None, viewAngle= 0,
                   proj='PlateCarree', colorbar=True, varAlpha=1,
                   stockImage=False, level='L1C',idx_=1, saveFig=False,
                   lakes=True, rivers=False, figsize_=None, ax=None, dpi=300,
                   highResStockImage=False,
                   **kwargs):
        """ Project a single variable of the data to the earth projection using Cartopy.
        
        Args:
            var (str, optional): The variable to plot. Defaults to 'i'.
            viewAngleIdx (list, optional): The view angle indices. Defaults to [38].
            proj (str, optional): The projection method. Defaults to 'PlateCarree'.
            colorbar (bool, optional): If True, the colorbar is added. Defaults to False.
            varAlpha (int, optional): The alpha value for the variable. Defaults to 1.
            stockImage (bool, optional): If True, the stock image is added. Defaults to False.
            level (str, optional): The level of the data. Defaults to 'L1C'.
            idx_ (int, optional): The index of the variable. Defaults to 1.
            saveFig (bool, optional): If True, the figure is saved. Defaults to False.            
            **kwargs: Variable length argument list to pass to the plot function.
            
        Returns:
            None
        """

        # Check the number of indices
        assert proj in ['PlateCarree', 'Orthographic'], 'Invalid projection method'
        assert var in self.data.keys(), 'Invalid variable, use one of the available variables %s' %self.data.keys()

        # Define which angle to plot
        if viewAngleIdx is None:
            # find the nadir in self.bandAngles where the difference with a reference angle is minimum
            viewAngleIdx = np.argmin(np.abs(self.data['view_angles'][self.bandAngles]-viewAngle))
            # viewAngleIdx = [np.where(self.data['view_angles'][self.bandAngles])]
        
        viewAngle = self.data['view_angles'][self.bandAngles][viewAngleIdx]

        # Get the latitude and longitude
        lat = self.data['latitude']
        lon = self.data['longitude']

        if level.lower() == 'l1b':
            lat = lat[viewAngleIdx, :, :]
            lon = lon[viewAngleIdx, :, :]

        # center of the plot
        lon_center = (lon.max() + lon.min()) / 2
        lat_center = (lat.max() + lat.min()) / 2

        # find if the longitude has a transition from -180 to 180
        transitionFlag = False
        if np.abs(lon.max() - lon.min()) > 180 :
            transitionFlag = True
            # use sine and cosine to find the center of the projection
            lon_center, ln_min, ln_max = self.average_longitude(lon.ravel())

        # default kwargs
        kwargs = dict()
        kwargs['linewidth'] = 1
        kwargs['color'] = 'y'
        kwargs['alpha'] = 0.25
        kwargs['linestyle'] = '-.'

        # default figsize
        figsize = (4, 5)  

        if kwargs:
            # check the kwargs keys and modify the default values
            for key, value in kwargs.items():
                if key in kwargs:
                    kwargs[key] = value
                if key in ['figsize']:
                    figsize = value

        # Prepare figure and axes
        figsize_ = figsize if figsize_ is None else figsize_
        if ax is None:
            fig = plt.figure(figsize=figsize_)
        
        if proj == 'PlateCarree':
            if ax is None:
                if transitionFlag:
                    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=lon_center))
                else:
                    ax = plt.axes(projection=ccrs.PlateCarree())
            else:
                ax = ax
            # Set up gridlines and labels
            gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                                **kwargs)
            gl.xlabels_top = False
            gl.ylabels_right = False
            gl.xlocator = mticker.FixedLocator(np.around(np.linspace(np.nanmin(lon),np.nanmax(lon),6),2))
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER

        elif proj == 'Orthographic':
            ax = plt.axes(projection=ccrs.Orthographic(central_longitude=lon_center, central_latitude=lat_center))
        else:
            print('Invalid projection method')
        
        # setup the gridlines
        if ax is not None:
            ax.coastlines()
            ax.set_global()
            ax.set_extent([lon.min(), lon.max(), lat.min(), lat.max()], crs=ccrs.PlateCarree())
            if not highResStockImage:
                ax.stock_img() if stockImage else ax.add_feature(cfeature.OCEAN, zorder=0)
                ax.add_feature(cfeature.LAND, zorder=0, edgecolor='black')
            else:
                ax.background_img(name='NaturalEarthRelief', resolution='high')
            # Add coastline feature
            ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1, alpha=0.5)
            ax.add_feature(cfeature.LAKES, edgecolor='black', linewidth=1, alpha=0.5) if lakes else None
            ax.add_feature(cfeature.RIVERS, edgecolor='black', linewidth=1, alpha=0.5) if rivers else None
        
        # plot the data with alpha value
        if varAlpha:
            kwargs['alpha'] = varAlpha

        # if reflectance is True, plot the reflectance
        if level.lower() == 'l1b':
            data_ = self.data[var][viewAngleIdx,:,:]

            plt.contourf(lon, lat,
                            data_, 60,
                            transform=ccrs.PlateCarree(), **kwargs)

        else:
            if self.reflectance and var in ['i', 'q', 'u']:
                # πI/F0
                data_ = self.data[var][:,:,viewAngleIdx,0]*np.pi/self.data['F0'][viewAngleIdx, 0]
            else:
                data_ = self.data[var][:,:,viewAngleIdx,0]

            plt.contourf(lon, lat,
                            data_, 60,
                            transform=ccrs.PlateCarree(), **kwargs)
        
        # select var and units
        var, unit_ = self.reflectanceChange(var) if self.reflectance else (var, self.data['_units'][var])
        # var = '%s_' %var
        # add colorbar with same size as the y axis length and set the label
        if ax is not None:
            ax.set_xmargin(0.05)
            ax.set_ymargin(0.05)

            # round the view angle to 2 decimal places
            ax.set_title(f'${var}{{({self.band})}}$ at {round(float(viewAngle), 2)}° viewing angle \nof the instrument {self.instrument}')
            plt.show()

            if saveFig:
                location = f'./{self.instrument}_viewAngle_{viewAngle}.png'
                fig.savefig(location, dpi=self.plotDPI)
                print(f'...Figure saved at {location}')

    def reflectanceChange(self, var):
        """Change the variable to reflectance if reflectance is True.

        Args:
            var (str): The variable to change.

        Returns:
            var (str): The variable to reflectance.
            units_ (str): The units of the variable.
        """

        # if reflectance is True, change the varstring to reflectance only for ['i', 'q', 'u']
        if self.reflectance and var in ['i', 'q', 'u']:
            var = 'R_%s' %var
            units_ = ''
        return var, units_



    # Plot projected RGB using Cartopy
    def projectedRGB(self, rgb=None, scale=1, ax=None, fig=None,
                     var='i', viewAngleIdx=[36, 4, 84],
                     normFactor=200, proj='PlateCarree',
                     saveFig=False, noShow=False, rivers=False, lakes=False,
                     rgb_dolp=False, figsize=None, savePath=None, dpi=None, setTitle=True,
                     returnRGB=False, lon_0=None, lat_0=None, black_background=True,
                     proj_size=None, returnTransitionFlag=False, highResStockImage=False,
                     **kwargs):
        """Plot the projected RGB image of the instrument using Cartopy.

        Args:
            rgb (np.ndarray, optional): The RGB data. Defaults to None.
            scale (int, optional): The scale factor. Defaults to 1.
            ax (matplotlib.axes.Axes, optional): The axes object to draw the plot onto. If None, a new figure and axes are created. Defaults to None.
            var (str, optional): The variable to plot. Defaults to 'i'.
            viewAngleIdx (list, optional): The view angle indices. Defaults to [38, 4, 84].
            normFactor (int, optional): The normalization factor. Defaults to 200.
            proj (str, optional): The projection method. Defaults to 'PlateCarree'.
            **kwargs: Variable length argument list to pass to the plot function.

        Returns:
            None
        """
        assert proj.lower() in ['platecarree', 'orthographic', 'none'], 'Invalid projection method currently only PlateCarree and Orthographic are supported'
        self.plotDPI = dpi if dpi is not None else self.plotDPI
        if self.instrument == 'OCI':
            if np.nanmean(self.data['latitude']) > 0:
                viewAngleIdx = [1]
            else:
                viewAngleIdx = [0]
            assert len(viewAngleIdx) == 1, 'Invalid number of indices'

        # if RGB does not exist, run the plotRGB method
        if rgb is None:
            self.plotRGB(var=var, viewAngleIdx=viewAngleIdx, scale=scale, normFactor=normFactor, returnRGB=True, plot=False, rgb_dolp=rgb_dolp,
                               **kwargs)

        # Check the shape of the RGB data
        assert self.rgb.shape[2] == 3, 'Invalid RGB data'

        # Get the latitude and longitude
        lat = self.data['latitude']
        lon = self.data['longitude']

        # find if the longitude has a transition from -180 to 180
        transitionFlag = False
        if np.abs(lon.max() - lon.min()) > 180 and lon_0 is None:
            transitionFlag = True
            # use sine and cosine to find the center of the projection
            lon_center, ln_min, ln_max = self.average_longitude(lon.ravel())
        else:
            lon_center = (lon.max() + lon.min()) / 2 if lon_0 is None else lon_0
        lat_center = (lat.max() + lat.min()) / 2 if lat_0 is None else lat_0
        print(f'...Centering the projection at lon:{round(lon_center, 3)}, lat:{round(lat_center,3)}')

        proj_size=(900,400) if proj_size is None else proj_size

        if transitionFlag:
            # Interpolate the RGB values onto a regular grid via function applying scale factor in advance
            rgb_new, rgb_extent = self.GridRGB(lon, lat, dateline=True, proj_size=proj_size)

        else:
            # rgb_new, rgb_extent = self.GridRGB(lon, lat, dateline=False, proj_size=proj_size)
            rgb_new, nlon, nlat = self.meshgridRGB(lon, lat, return_mapdata=False, proj_size=proj_size) #Created projection image
            rgb_extent = [nlon.min(), nlon.max(), nlat.min(), nlat.max()]         # type: ignore

        # Prepare figure and axes
        if ax is None and proj.lower() != 'none':
            print('...Creating a new figure')
            if figsize is None:
                fig = plt.figure(figsize=(4, 5), dpi=self.plotDPI) if fig is None else fig
                # print('...Setting the figure size to (4, 5)')
            else:
                if fig is None:
                    print(f'...Creating a new figure with figsize {figsize}')
                    print(f'...Setting the figure dpi to {self.plotDPI}')
                    fig = plt.figure(figsize=figsize, dpi=self.plotDPI)
                else:
                    fig = fig
                # print(f'...Setting the figure size to {figsize}')

        # Check the projection type
        if proj == 'Orthographic':
            # Create an Orthographic projection
            if ax is None:
                ax = plt.axes(projection=ccrs.Orthographic(lon_center, lat_center))
            else:
                ax = ax
            if highResStockImage:
                ax.background_img(name='BlueMarble', resolution='high')
            else:
                ax.stock_img()
            if fig is not None:
                fig.patch.set_facecolor('black')

            # mask the black pane
            rgb_new = np.ma.masked_where(rgb_new == 0, rgb_new)

            # Display the image in the projection
            ax.imshow(rgb_new, origin='lower',  extent=rgb_extent, transform=ccrs.PlateCarree(), **kwargs)
            ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=0.2, alpha=0.5)

        elif proj == 'PlateCarree':
            # Create a PlateCarree projection
            if ax is None:
                if transitionFlag:
                    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=lon_center))
                else:
                    ax = plt.axes(projection=ccrs.PlateCarree())
            else: 
                # print('...Using the existing axes')
                ax=ax
            # Set up gridlines and labels
            gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='white', alpha=0.2, linestyle='--')
            gl.xlabels_top = False
            gl.ylabels_right = False
            gl.xlocator = mticker.FixedLocator(np.around(np.linspace(rgb_extent[0],rgb_extent[1],6),2))
            gl.xformatter = LONGITUDE_FORMATTER
            gl.yformatter = LATITUDE_FORMATTER

            # mask the black pane
            rgb_new = np.ma.masked_where(rgb_new == 0, rgb_new)
            
            # Display the image in the projection
            ax.imshow(rgb_new, origin='lower', extent=rgb_extent, **kwargs)
            # Add coastline feature
            ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1, alpha=0.5)
            ax.add_feature(cfeature.LAKES, edgecolor='black', linewidth=1, alpha=0.5) if lakes else None
            ax.add_feature(cfeature.RIVERS, edgecolor='black', linewidth=1, alpha=0.5) if rivers else None

        else:
            # Handle invalid projection type
            if proj.lower() == 'none':
                print('...No projection method selected')
            else:
                print('Invalid projection method')

        # These operations are common to both projections but not needed for just getting the RGB interpolated data
        if proj.lower() != 'none':
            # set a margin around the data
            if ax is not None:
                ax.set_xmargin(0.05)
                ax.set_ymargin(0.05)

            if setTitle:
                # set the title using the date_time
                fontColor = 'tan' if black_background else 'black'
                if ax is not None:
                    ax.set_title(f'RGB image of the instrument {self.instrument}\n {self.data["date_time"]} at viewing angles {str(self.data["view_angles"][viewAngleIdx[0]])}', color=fontColor)

            plt.box(on=None)
            plt.show() if not noShow else None

            if saveFig:
                location = f'./{self.instrument}_RGB_{str(viewAngleIdx[0])}_proj_{proj}.png'
                if savePath is not None:
                    location = savePath
                if fig is not None:  # Check if fig is not None
                    fig.savefig(location, dpi=self.plotDPI)
                print(f'...Figure saved at {location}')

        # return the figure and axes and the projected RGB
        if returnRGB:
            if proj.lower() == 'none':
                if proj.lower() == 'none' and returnTransitionFlag:
                    return rgb_new, rgb_extent, transitionFlag
                
                return rgb_new, rgb_extent
            else:
                if returnTransitionFlag:
                    return fig, ax, rgb_new, rgb_extent, transitionFlag, lon_center, lat_center
                else:
                    return fig, ax, rgb_new, rgb_extent


    def meshgridRGB(self, LON, LAT, proj_size=(900,400), return_mapdata=False):
        """Project the RGB data using meshgrid.

        This function takes longitude and latitude data along with optional parameters and returns the projected RGB data.
        
        Args:
            self (object): The instance of the class.
            LON (np.ndarray): The longitude data.
            LAT (np.ndarray): The latitude data.
            proj_size (tuple, optional): The size of the projection. Defaults to (905,400).
            return_mapdata (bool, optional): If True, the map data is returned. Defaults to False.
                
        Returns:
            np.ndarray: The projected RGB data.
            
        Raises:
            None
            
        Examples:
            # Create an instance of the class
            plot = Plot()
            
            # Define longitude and latitude data
            lon_data = np.array([0, 1, 2, 3, 4])
            lat_data = np.array([0, 1, 2, 3, 4])
            
            # Call the meshgridRGB function
            rgb_data = plot.meshgridRGB(lon_data, lat_data)
        """
        # for each color channel, the code sets the border pixels of the image to 0. 
        rr = self.rgb[:,:,0]
        rr[0:-1,0] = 0
        rr[0:-1,-1] = 0
        rr[0,0:-1] = 0
        rr[-1,0:-1] = 0
        gg = self.rgb[:,:,1]
        gg[0:-1,0] = 0
        gg[0:-1,-1] = 0
        gg[0,0:-1] = 0
        gg[-1,0:-1] = 0
        bb = self.rgb[:,:,2]
        bb[0:-1,0] = 0
        bb[0:-1,-1] = 0
        bb[0,0:-1] = 0
        bb[-1,0:-1] = 0

        # The code calculates the maximum and minimum latitude (mx_lat and mn_lat)
        # and longitude (mx_lon and mn_lon) from the LAT and LON arrays. 
        # It then calculates the midpoint of the latitude (lat0) and longitude (lon0)
        
        # Calculate the maximum and minimum latitude and longitude
        mx_lat = np.max(LAT)
        mn_lat = np.min(LAT)
        mx_lon = np.max(LON)
        mn_lon = np.min(LON)

        # find if the longitude has a transition from -180 to 180
        transitionFlag = False
        if np.abs(mx_lon - mn_lon) > 180:
            transitionFlag = True
            # apply cosine conversion to the longitude and sine conversion latitude
            # LON = np.sin(np.radians(LON))
            # LAT = np.sin(np.radians(LAT))
            lon_center, ln_min, ln_max = self.average_longitude(LON.ravel())
            LON = np.where(LON < 0, -180 - LON, 180 - LON)
            mx_lon = LON.min() 
            mn_lon = LON.max()
            mx_lat = LAT.max()
            mn_lat = LAT.min()

        # Calculate the midpoint of the latitude and longitude
        lat0 = 1/2.*(mn_lat+mx_lat)
        # if the transitionFlag is True, calculate the midpoint of the longitude using the cosine of the longitude
        lon0 = 1/2.*(mn_lon+mx_lon)

        # Set the size of the new projected image
        x_new = proj_size[0]
        y_new = proj_size[0]

        # Create 1D arrays of evenly spaced values between the min and max longitude and latitude
        xx = np.linspace(mn_lon,mx_lon,x_new)
        yy = np.linspace(mn_lat,mx_lat,y_new)

        # Create a 2D grid of coordinates
        newxx, newyy = np.meshgrid(xx,yy)

        # Interpolate the red, green, and blue color channels at the new grid points
        newrr = interpolate.griddata( (LON.ravel(),LAT.ravel()), rr.ravel(), (newxx.ravel(), newyy.ravel()), method='nearest',fill_value=0 )
        newgg = interpolate.griddata( (LON.ravel(),LAT.ravel()), gg.ravel(), (newxx.ravel(), newyy.ravel()), method='nearest',fill_value=0 )
        newbb = interpolate.griddata( (LON.ravel(),LAT.ravel()), bb.ravel(), (newxx.ravel(), newyy.ravel()), method='nearest',fill_value=0 )

        # Reshape the color channels to the size of the new image
        newrr = newrr.reshape(x_new,y_new)
        newgg = newgg.reshape(x_new,y_new)
        newbb = newbb.reshape(x_new,y_new)

        # Clip the color values to the range [0, 1] and remove any pixels where any of the color channels are 0
        newrr[newrr>1] = 1
        newrr[newrr<0] = 0
        newrr[newbb==0] = 0
        newrr[newgg==0] = 0

        newgg[newgg>1] = 1
        newgg[newgg<0] = 0
        newgg[newbb==0] = 0
        newgg[newrr==0] = 0

        newbb[newbb>=1] = 1
        newbb[newbb<0] = 0
        newbb[newrr==0] = 0
        newbb[newgg==0] = 0

        # Create a new 3D array for the projected RGB image
        rgb_proj = np.zeros([np.shape(newrr)[0],np.shape(newrr)[1],3], dtype=np.float32)

        # Set the red, green, and blue channels of the new image
        rgb_proj[:,:,0] = newrr
        rgb_proj[:,:,1] = newgg
        rgb_proj[:,:,2] = newbb

        # If return_mapdata is True, return the map data
        if return_mapdata:
            return rgb_proj, (lon0,lat0), ((mn_lon,mx_lon),(mn_lat,mx_lat))
        else:
            return rgb_proj,xx,yy
        
    #------------------------------------------------------------------------------------------
    # Function to regrid RGB data
    # Noah Sienkiewicz created this function and has been modified by Anin to fit with the library
    #------------------------------------------------------------------------------------------
    def GridRGB(self, lon, lat, dateline=True, proj_size=(900,400)):
        """
        Interpolates RGB values onto a grid regularly spaced grid by longitude and latitude coordinates.

        Args:
            self (object): The instance of the class.
            lon (ndarray): 2-D array of longitude values from L1C.
            lat (ndarray): 2-D array of latitude values from L1C.
            dateline (bool, optional): Specifies whether the dateline is present in the longitude values. 
                Defaults to True.

        Returns:
            tuple: A rgb image array containing the interpolated RGB values as a 3-D array and the extent of the grid for imshow.

        """
        # Create a 3D array to store the RGB data
        tmp_r = self.rgb[:,:,0]
        tmp_g = self.rgb[:,:,1]
        tmp_b = self.rgb[:,:,2]
        
        if dateline:
            #When the dateline is bisecting the lon grid, we need to adjust the grid to be continuous
            #This means separating it into east and west halves according to the dateline. On the east
            #half where it's negative, shift all values by 360 to make them continuous with the west
            #half
            tmp_lon = np.unique(lon)
            west_lon = tmp_lon[tmp_lon>0]
            east_lon = tmp_lon[tmp_lon<0]
            lon_min = np.min(west_lon)
            lon_max = np.max(east_lon)
            lon_min = lon_min
            lon_max = 360+lon_max
        else: #if no datetline, do nothing special
            tmp_lon = np.unique(lon)
            lon_min = np.min(lon)
            lon_max = np.max(lat)

        lat_min = np.min(lat)
        lat_max = np.max(lat)

        # Imshow doesn't like arrays with irregularly shaped/spaced pixels. It tries to create
        # a simple rectangular box of regular squares, but because of our projection, we're
        # making some god awful shape. To fix that, I create a regular grid with the same start/end
        # points as the original grid. I create it as the same size as the original grid, but it doesn't
        # have to be. Using nearest neighbor interpolation means there's no real reason to go finer
        # but I didn't really play with it much to check
        new_lon, new_lat = np.meshgrid(np.linspace(lon_min,lon_max,proj_size[1]),
                                    np.linspace(lat_min,lat_max,proj_size[0]))
        
        tmp_lon = lon.flatten() #flatten the arrays for regridding
        if dateline: #if the dateline is present, again shift the values to be continuous
            tmp_lon[tmp_lon<0] = 360+tmp_lon[tmp_lon<0]
        else: #else do nothing
            tmp_lon = tmp_lon
        points = np.vstack([tmp_lon, lat.flatten()]).T #combine the lon and lat arrays into a 2D array according griddate spec
        new_points = np.vstack([new_lon.flatten(), new_lat.flatten()]).T #same for the new grid
        
        # Perform the interpolation RED
        to_grid = np.copy(tmp_r) #get a copy of the input red image data
        # Because we're using nearest neighbor, if I don't line the edges with 0, then those values get smeared
        # from the true image edge to the edge of the grid. We could mask them later with the alpha channel, but
        # for simplicity I use 0 values to help define the alpha mask, so it's not really worth trying
        to_grid[0,:] = 0  # top layer of the grid
        to_grid[-1,:] = 0 # bottom
        values = to_grid.flatten()  # replace 'values' with your image data array
        new_values = interpolate.griddata(points, values, new_points, method='nearest') #do interpolation (takes a few seconds)
        # Reshape the interpolated values to match the shape of the new grid
        new_r = new_values.reshape(new_lon.shape) #reshape result back to meshgrid expectations

        # Perform the interpolation GRN (same as red)
        to_grid = np.copy(tmp_g)
        to_grid[0,:] = 0
        to_grid[-1,:] = 0
        values = to_grid.flatten()  # replace 'values' with your data array
        new_values = interpolate.griddata(points, values, new_points, method='nearest')
        # Reshape the interpolated values to match the shape of the new grid
        new_g = new_values.reshape(new_lon.shape)

        # Perform the interpolation BLU (same as red)
        to_grid = np.copy(tmp_b)
        to_grid[0,:] = 0
        to_grid[-1,:] = 0
        values = to_grid.flatten()  # replace 'values' with your data array
        new_values = interpolate.griddata(points, values, new_points, method='nearest')
        # Reshape the interpolated values to match the shape of the new grid
        new_b = new_values.reshape(new_lon.shape)

        tmp_alpha = np.ones_like(new_b,dtype='float32')*1 #create an alpha channel (opacity) that is 1 (fully opaque) everywhere
        new_rgb = np.stack([new_r, new_g, new_b ,tmp_alpha], axis=-1) #stack into a new RGB on the last axis

        new_rgb[new_rgb[:,:,0] <= 0,-1] = 0 #set the alpha channel to 0 where the RGB is invalid making it full transparent
        ext = [lon_min, lon_max, lat_min, lat_max] #package the edges of the new retangular grid to give to imshow

        return new_rgb, ext
        
    def average_longitude(self, longitudes):
        # Convert longitudes to radians
        longitudes_rad = np.radians(longitudes)

        # Convert to Cartesian coordinates
        x = np.cos(longitudes_rad)
        y = np.sin(longitudes_rad)

        # Compute mean of Cartesian coordinates
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        # calculate the minimum and maximum of the longitudes
        x_min = np.min(x)
        x_max = np.max(x)
        y_min = np.min(y)
        y_max = np.max(y)

        min_lon = np.degrees(np.arctan2(y_min, x_min))
        max_lon = np.degrees(np.arctan2(y_max, x_max))

        # Convert mean coordinates back to longitude
        mean_longitude = np.degrees(np.arctan2(y_mean, x_mean))

        # Adjust the range of mean longitude to [-180, 180]
        mean_longitude = (mean_longitude + 180) % 360 - 180

        return mean_longitude, min_lon, max_lon
        
#---------------------------------------------------
# End of the class Plot
#---------------------------------------------------