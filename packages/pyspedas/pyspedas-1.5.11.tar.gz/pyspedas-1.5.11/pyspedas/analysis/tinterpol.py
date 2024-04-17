"""
Interpolates data specified in 'names' to time values found in 'interp_to'.

Notes
-----
Allowed wildcards are ? for a single character, * from multiple characters.
Similar to tinterpol.pro in IDL SPEDAS.

"""
import datetime
import logging
from pytplot import get_data, store, tnames
import numpy as np


def tinterpol(names, interp_to, method=None, newname=None, suffix=None):
    """
    Interpolate data to times in interp_to.

    Parameters
    ----------
    names: str/list of str
        List of variables to interpolate.
    interp_to: str,list, ndarray
        String containing the variable
            containing the time stamps to interpolate to
    method: str, optional
        Interpolation method. Default is ‘linear’.
        Specifies the kind of interpolation as a string (‘linear’, ‘nearest’,
        ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘previous’, ‘next’)
        where ‘zero’, ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline
        interpolation of zeroth, first, second or third order; ‘previous’ and
        ‘next’ simply return the previous or next value of the point) or
        as an integer specifying the order of the spline interpolator to use.
    newname: str/list of str, optional
        List of new names for pytplot variables.
        If '', then pytplot variables are replaced.
        If not given, then a suffix is applied.
    suffix: str, optional
        A suffix to apply. Default is '-itrp'.

    Returns
    -------
    None.

    """
    if not isinstance(names, list):
        names = [names]
    if not isinstance(newname, list):
        newname = [newname]

    old_names = tnames(names)

    if len(old_names) < 1:
        logging.error('tinterpol error: No pytplot names were provided.')
        return

    if suffix is None:
        suffix = '-itrp'

    if method is None:
        method = 'linear'

    if (newname is None) or (len(newname) == 1 and newname[0] is None):
        n_names = [s + suffix for s in old_names]
    else:
        n_names = newname

    if isinstance(interp_to, str):
        interp_to_data = get_data(interp_to, dt=True)

        if interp_to_data is None:
            logging.error('Error, tplot variable: ' + interp_to + ' not found.')
            return

        interp_to_times = interp_to_data[0]
    else:
        interp_to_times = interp_to

    for name_idx, name in enumerate(old_names):
        xdata = get_data(name, xarray=True)
        metadata = get_data(name, metadata=True)

        if isinstance(interp_to_times[0],(datetime.datetime,np.datetime64)):
            # Timezone-naive datetime or np.datetime64, use as-is
            interp_to_datetimes = interp_to_times
        elif isinstance(interp_to_times[0],(int,float,np.integer,np.float64)):
            # Assume seconds since Unix epoch, convert to np.datetime64 with nanosecond precision
            if isinstance(interp_to_times,np.ndarray):
                interp_to_datetimes = np.array(interp_to_times*1e09,dtype='datetime64[ns]')
            else:
                # We need to convert input to a numpy array before scaling to nanoseconds
                interp_to_datetimes = np.array(np.array(interp_to_times)*1e9,dtype='datetime64[ns]')
        elif isinstance(interp_to_times[0],str):
            # Interpret strings as timestamps, convert to np.datetime64 with nanosecond precision
            interp_to_datetimes = np.array(interp_to_times,dtype='datetime64[ns]')
        else:
            # Give up for any other type
            logging.error('tinterpol: Unable to convert type %s to timestamp.',type(interp_to_times[0]))
            return

        xdata_interpolated = xdata.interp({'time': interp_to_datetimes},
                                          method=method)

        if 'spec_bins' in xdata.coords:
            store(n_names[name_idx],
                  data={
                      'x': interp_to_times,
                      'y': xdata_interpolated.values,
                      'v': xdata_interpolated.coords['spec_bins'].values
                  },
                  metadata=metadata)
        else:
            store(n_names[name_idx], data={'x': interp_to_times,
                                           'y': xdata_interpolated.values}, metadata=metadata)

        logging.info('tinterpol (' + method + ') was applied to: ' + n_names[name_idx])
