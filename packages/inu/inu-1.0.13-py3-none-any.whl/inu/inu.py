"""
--------------------------------------------------------------------------------
Copyright 2022 David Woodburn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Distribution Statement A. Approved for public release: distribution unlimited.
--------------------------------------------------------------------------------

Functions
---------
This library provides forward mechanization of inertial measurement unit sensor
values (accelerometer and gyroscope readings) to get position, velocity, and
attitude in the North, East, down (NED) local reference frame, as well as
inverse mechanization to get sensor values from position, velocity, and
attitude. It also includes tools to calculate velocity from geodetic position
over time, to estimate attitude from velocity, and to estimate wind velocity
from ground-track velocity and yaw angle.

Accuracy
--------
The mechanization algorithms in this library make no simplifying assumptions.
The Earth is defined as an ellipsoid. Any deviations of the truth from this
simple shape can be captured by more complex gravity models. The algorithms use
a single frequency update structure which is much simpler than the common
two-frequency update structure and just as, if not more, accurate.

Duality
-------
The forward and inverse mechanization functions are perfect duals of each other.
This means that if you started with a profile of position, velocity, and
attitude and passed these into the inverse mechanization algorithm to get sensor
values and then passed those sensor values into the forward mechanization
algorithm, you would get back the original position, velocity, and attitude
profiles. The only error would be due to finite-precision rounding.

Vectorization
-------------
When possible, the functions are vectorized in order to handle processing
batches of values. A set of scalars is a 1D array. A set of vectors is a 2D
array, with each vector in a column. So, a (3, 7) array is a set of seven
vectors, each with 3 elements. If an input matrix does not have 3 rows, it will
be assumed that the rows of the matrix are vectors.
--------------------------------------------------------------------------------
"""

__author__ = "David Woodburn"
__license__ = "MIT"
__date__ = "2024-04-15"
__maintainer__ = "David Woodburn"
__email__ = "david.woodburn@icloud.com"
__status__ = "Development"

import os
import math
import time
import numpy as np
import scipy as sp

# WGS84 constants (IS-GPS-200M and NIMA TR8350.2)
A_E = 6378137.0             # Earth's semi-major axis (m) (p. 109)
E2 = 6.694379990141317e-3   # Earth's eccentricity squared (ND) (derived)
W_EI = 7.2921151467e-5      # sidereal Earth rate (rad/s) (p. 106)

# -----------------
# Support Functions
# -----------------

class config:
    uni = True # flag to use Unicode characters
    cols = 60 # default column width
    rows = 20 # default row height


class persistent:
    t_last = None


def time_str(t_seconds):
    """ Convert time in seconds to a clock string of the form
    `HH:MM:SS.S`. """
    t_seconds = abs(t_seconds)
    hours = int(t_seconds/3600)
    minutes = int((t_seconds - hours*3600)//60)
    seconds = (t_seconds % 60)
    clock_str = "%02d:%02d:%04.1f" % (hours, minutes, seconds)
    return clock_str


def progress(k, K, t_init=None, width=None):
    """
    Output a simple progress bar with percent complete to the terminal. When `k`
    equals `K - 1`, the progress bar will complete and start a new line.

    Parameters
    ----------
    k : int
        Index which should grow monotonically from 0 to K - 1.
    K : int
        Final index value of `k` plus 1.
    t_init : float, default None
        Initial process time (s). If provided, an estimated time remaining will
        be displayed. If left as None, no time will be shown. When the progress
        bar completes, the total duration will be shown.
    width : int, default None
        Width of the full string, including the percent complete, the bar, and
        the clock. If not given, the width of the terminal window will be used.
    """

    # Skip this call if the bar is not done but not enough time has passed.
    t_now = time.perf_counter()
    if (k + 1 < K) and (persistent.t_last is not None) and \
            (t_now - persistent.t_last < 0.1):
        return
    persistent.t_last = t_now

    # Default the width to the terminal width or config.cols.
    if width is None:
        try: # Try to get the true size.
            width, _ = os.get_terminal_size()
            use_color = True
        except: # If getting terminal size fails, use default values.
            width = config.cols
            use_color = False

    # Get the ratio.
    ratio = (k + 1)/K

    # Get the clock string.
    if t_init is not None:
        t_elapsed = t_now - t_init
        if k + 1 == K:
            clk_str = "  " + time_str(t_elapsed)
        else:
            if ratio > 0:
                t_remaining = t_elapsed*(1.0 - ratio)/ratio
            else:
                t_remaining = 0.0
            clk_str = " -" + time_str(t_remaining)
    else:
        clk_str = ""

    # Define the color commands.
    if use_color:
        g_fgnd = "\x1b[38;5;244m"
        g_bgnd = "\x1b[48;5;244m"
        r_fgnd = "\x1b[39m"
        r_bgnd = "\x1b[49m"
    else:
        g_fgnd = ""
        g_bgnd = ""
        r_fgnd = ""
        r_bgnd = ""

    # Build the progress bar.
    if config.uni:
        N = width - 6 - len(clk_str) # maximum length of bar
        f = chr(0x2501) # full bar
        l = chr(0x2578) # left half
        r = chr(0x257A) # right half
        if k + 1 >= K:
            print(f"\r100% ", end='')
            for j in range(N):
                print(f, end='', flush=True)
            print(clk_str, flush=True)
        else:
            bar_len = int(N*ratio)
            spc_len = N - 1 - bar_len
            print(f"\r{int(100*ratio):3d}% ", end='')
            for j in range(bar_len):
                print(f, end='', flush=True)
            if ((N*ratio) % 1) < 0.5:
                print(f"{g_fgnd}{r}", end='')
            else:
                print(f"{l}{g_fgnd}", end='')
            for j in range(spc_len):
                print(f, end='', flush=True)
            print(f"{r_fgnd}{clk_str}", end='', flush=True)
    else:
        N = width - 6 - len(clk_str) # maximum length of bar within the brackets
        if k + 1 >= K:
            print(f"\r100% {'='*N}{clk_str}", flush=True)
        else:
            bar_len = int(N*ratio)
            print(f"\r{int(100*ratio):3d}% "
                + f"{'='*bar_len}{g_fgnd}"
                + f"{'-'*(N - bar_len)}{r_fgnd}{clk_str}", end='', flush=True)


def somigliana(llh_t):
    """
    Calculate the local acceleration of gravity vector in the navigation frame
    using the Somigliana equation. The navigation frame here has the North,
    East, Down (NED) orientation.

    Parameters
    ----------
    llh_t : (3,) or (3, K) or (K, 3) np.ndarray
        Geodetic position vector of latitude (radians), longitude (radians), and
        height above ellipsoid (meters) or matrix of such vectors.

    Returns
    -------
    gamma : (3,) or (3, K) or (K, 3) np.ndarray
        Acceleration of gravity in meters per second squared.
    """

    # Check input.
    if isinstance(llh_t, list):
        llh_t = np.array(llh_t)
    trs = (llh_t.ndim == 2 and llh_t.shape[0] != 3)

    # gravity coefficients
    ge = 9.7803253359
    k = 1.93185265241e-3
    f = 3.35281066475e-3
    m = 3.44978650684e-3

    # Transpose the input.
    if trs:
        llh_t = llh_t.T

    # Get local acceleration of gravity for height equal to zero.
    slat2 = np.sin(llh_t[0])**2
    klat = np.sqrt(1 - E2*slat2)
    grav_z0 = ge*(1 + k*slat2)/klat

    # Calculate gamma for the given height.
    grav_z = grav_z0*(1 + (3/A_E**2)*llh_t[2]**2
        - 2/A_E*(1 + f + m - 2*f*slat2)*llh_t[2])

    # Form vector.
    if isinstance(grav_z, np.ndarray):
        K = len(grav_z)
        grav = np.zeros((3, K))
        grav[2, :] = grav_z
        if trs:
            grav = grav.T
    else:
        grav = np.array([0.0, 0.0, grav_z])

    return grav


def rpy_to_dcm(rpy):
    """
    Convert roll, pitch, and yaw Euler angles to a direction cosine matrix that
    represents a zyx sequence of right-handed rotations.

    Parameters
    ----------
    rpy : (3,) list or np.ndarray
        Roll, pitch, and yaw Euler angle in radians.

    Returns
    -------
    C : (3, 3) np.ndarray
        Rotation matrix.
    """

    # Get the cosine and sine functions.
    r, p, y = rpy
    cr = math.cos(r)
    sr = math.sin(r)
    cp = math.cos(p)
    sp = math.sin(p)
    cy = math.cos(y)
    sy = math.sin(y)

    # Build the 3x3 matrix.
    C = np.array([
        [            cp*cy,             cp*sy,   -sp],
        [-cr*sy + sr*sp*cy,  cr*cy + sr*sp*sy, sr*cp],
        [ sr*sy + cr*sp*cy, -sr*cy + cr*sp*sy, cr*cp]])

    return C


def dcm_to_rpy(C):
    """
    Convert a direction cosine matrix (DCM) to roll, pitch, and yaw Euler
    angles. This DCM represents the zyx sequence of right-handed rotations.

    Parameters
    ----------
    C : (3, 3) list or np.ndarray
        Rotation matrix.

    Returns
    -------
    rpy : (3,) np.ndarray
        Roll, pitch, and yaw Euler angle in radians.
    """

    # Parse out the elements of the DCM that are needed.
    c11 = C[0, 0]
    c33 = C[2, 2]
    c12 = C[0, 1]
    c13 = C[0, 2]
    c23 = C[1, 2]

    # Get roll.
    rpy = np.zeros(3)
    rpy[0] = math.atan2(c23, c33)

    # Get pitch.
    sp = -c13
    pa = math.asin(sp)
    nm = math.sqrt(c11**2 + c12**2 + c23**2 + c33**2)
    pb = math.acos(nm/math.sqrt(2))
    rpy[1] = (1.0 - abs(sp))*pa + sp*pb

    # Get yaw.
    rpy[2] = math.atan2(c12, c11)

    return rpy


def orthonormalize_dcm(C):
    """
    Orthonormalize the rotation matrix using the Modified Gram-Schmidt
    algorithm. This function modifies the matrix in-place. Note that this
    algorithm only moves the matrix towards orthonormality; it does not
    guarantee that after one function call the returned matrix will be
    orthonormal. However, with a 1e-15 tolerance, orthonormality can be
    acheived typically within at most 2 function calls.

    Parameters
    ----------
    C : (3, 3) np.ndarray
        Square matrix.
    """

    # Orthonormalize a single matrix.
    C[:, 0] /= math.sqrt(C[0, 0]**2 + C[1, 0]**2 + C[2, 0]**2)
    C[:, 1] -= C[:, 0].dot(C[:, 1])*C[:, 0]
    C[:, 1] /= math.sqrt(C[0, 1]**2 + C[1, 1]**2 + C[2, 1]**2)
    C[:, 2] -= C[:, 0].dot(C[:, 2])*C[:, 0]
    C[:, 2] -= C[:, 1].dot(C[:, 2])*C[:, 1]
    C[:, 2] /= math.sqrt(C[0, 2]**2 + C[1, 2]**2 + C[2, 2]**2)


def rodrigues_rotation(theta):
    """
    Get the matrix exponential of the skew-symmetric matrix of the rotation
    vector `theta`.

        Delta = exp([theta] )
                           x

    The rotation vector should not have a norm greater than pi. If it does,
    scale the vector by `-(2 pi - n)/n`, where `n` is the norm of the rotation
    vector.

    Parameters
    ----------
    theta : (3,) list or np.ndarray
        Three-element vector of angles in radians.

    Returns
    -------
    Delta : (3, 3) np.ndarray
        Three-by-three matrix.
    """

    # Get the vector norm.
    x2 = theta[0]*theta[0]
    y2 = theta[1]*theta[1]
    z2 = theta[2]*theta[2]
    nm2 = x2 + y2 + z2
    nm = math.sqrt(nm2)

    # Get the sine and cosine factors.
    if nm < 0.04e-6:
        s = 1.0
    else:
        s = math.sin(nm)/nm
    if nm < 0.2e-3:
        c = 0.5
    else:
        c = (1 - math.cos(nm))/nm2

    # Get the rotation matrix.
    Delta = np.array([
        [1.0 - c*(y2 + z2),
            c*theta[0]*theta[1] - s*theta[2],
            c*theta[0]*theta[2] + s*theta[1]],
        [c*theta[0]*theta[1] + s*theta[2],
            1.0 - c*(x2 + z2),
            c*theta[1]*theta[2] - s*theta[0]],
        [c*theta[0]*theta[2] - s*theta[1],
            c*theta[1]*theta[2] + s*theta[0],
            1.0 - c*(x2 + y2)]])

    return Delta


def inverse_rodrigues_rotation(Delta):
    """
    Get the rotation vector `theta` from the skew-symmetric matrix that is the
    matrix logarithm of the rotation matrix `Delta`:

        [theta]  = ln(Delta)
               x

    The rotation vector will not have a norm greater than pi.

    Parameters
    ----------
    Delta : (3, 3) np.ndarray
        Three-by-three matrix.

    Returns
    -------
    theta : (3,) np.ndarray
        Three-element vector of angles in radians.
    """

    # Get the trace of the matrix and limit its value.
    q = Delta[0, 0] + Delta[1, 1] + Delta[2, 2]
    q_min = 2*np.cos(3.1415926) + 1
    q = max(min(q, 3.0), q_min)

    # Get the scaling factor of the vector.
    ang = math.acos((q-1)/2)
    s = ang/math.sqrt(3 + 2*q - q**2) if (q <= 2.9996) \
            else (q**2 - 11*q + 54)/60

    # Build the vector.
    theta = s*np.array([
        Delta[2, 1] - Delta[1, 2],
        Delta[0, 2] - Delta[2, 0],
        Delta[1, 0] - Delta[0, 1]])

    # Check the output.
    if q == q_min:
        raise ValueError("The provided output is incorrectly all zeros \n"
                + "because the input is very close to a 180 degree rotation.")

    return theta


def est_wind(vne_t, yaw_t):
    """
    Estimate the time-varying wind by comparing the ground travel velocity to
    the yaw (heading) angle.

    Parameters
    ----------
    vne_t : (3,) or (3, K) or (K, 3) np.ndarray
        North, East, and Down velocity vector of the navigation frame relative
        to the ECEF frame (meters per second).
    yaw_t : (K,) np.ndarray
        Yaw angle clockwise from north in radians.

    Returns
    -------
    wind_t : (2,) or (2, K) or (K, 2) np.ndarray
        North and East components of wind vector in meters per second.
    """

    # Check input.
    if isinstance(vne_t, list):
        vne_t = np.array(vne_t)
    if isinstance(yaw_t, list):
        yaw_t = np.array(yaw_t)
    trs = (vne_t.ndim == 2 and vne_t.shape[0] != 3)

    # Transpose input.
    if trs:
        vne_t = vne_t.T

    # Get the horizontal speed.
    sH_t = math.sqrt(vne_t[0]**2 + vne_t[1]**2)

    # Get the estimated wind.
    wind_t = np.array([
        vne_t[0] - sH_t*math.cos(yaw_t),
        vne_t[1] - sH_t*math.sin(yaw_t)])

    # Transpose output.
    if trs:
        wind_t = wind_t.T

    return wind_t


def wrap(Y):
    """
    Wrap angles to a -pi to pi range. This function is vectorized.
    """
    return Y - np.round(Y/math.tau)*math.tau


def ned_enu(Y):
    """
    Swap between North, East, Down (NED) orientation and East, North, Up (ENU)
    orientation. This operation changes the array in place.
    """
    Y[2] = -Y[2]
    x = Y[0].copy()
    Y[0] = Y[1].copy()
    Y[1] = x
    return Y


def vanloan(F, B=None, Q=None, T=None):
    """
    Discretize the dynamics, stochastic matrices in the equation

        .                 .--
        x = F x + B u + `/ Q  w

    where `F` is the dynamics matrix, `B` is the input matrix, and `Q` is the
    noise covariance matrix.

    Parameters
    ----------
    F : 2D np.ndarray
        Continuous-domain dynamics matrix.
    B : 2D np.ndarray, default None
        Continuous-domain dynamics input matrix.  To omit this input, provide
        `None`.
    Q : 2D np.ndarray, default None
        Continuous-domain dynamics noise covariance matrix.  To omit this input,
        provide `None`.
    T : float, default 1.0
        Sampling period in seconds.

    Returns
    -------
    Phi : 2D np.ndarray
        Discrete-domain dynamics matrix.
    Bd : 2D np.ndarray
        Discrete-domain dynamics input matrix.
    Qd : 2D np.ndarray
        Discrete-domain dynamics noise covariance matrix.

    Notes
    -----
    The Van Loan method, named after Charles Van Loan, is one way of
    discretizing the matrices of a state-space system.  Suppose that you have
    the following state-space system:

        .                 .--
        x = F x + B u + `/ Q  w

        y = C x + D u + R v

    where `x` is the state vector, `u` is the input vector, and `w` is a white,
    Gaussian noise vector with means of zero and variances of one.  Then, to get
    the discrete form of this equation, we would need to find `Phi`, `Bd`, and
    `Qd` such that

                             .--
        x = Phi x + Bd u + `/ Qd w

        y = C x + D u + Rd v

    `Rd` is simply `R`.  `C` and `D` are unaffected by the discretization
    process.  We can find `Phi` and `Qd` by doing the following:

            .-      -.                    .-          -.
            | -F  Q  |                    |  M11  M12  |
        L = |        |    M = expm(L T) = |            |
            |  0  F' |                    |  M21  M22  |
            '-      -'                    '-          -'
        Phi = M22'        Qd = Phi M12 .

    Note that `F` must be square and `Q` must have the same size as `F`.  To
    find `Bd`, we do the following:

            .-      -.                    .-         -.
            |  F  B  |                    |  Phi  Bd  |
        G = |        |    H = expm(G T) = |           |
            |  0  0  |                    |   0   I   |
            '-      -'                    '-         -'

    Note that for `Bd` to be calculated, `B` must have the same number of rows
    as `F`, but need not have the same number of columns.  For `Qd` to be
    calculated, `F` and `Q` must have the same shape.  If these conditions are
    not met, the function will fault.

    We can also express Phi and Bd in terms of their infinite series:

                         1   2  2    1   3  3
        Phi = I + F T + --- F  T  + --- F  T  + ...
                         2!          3!

                    1       2    1   2    3    1   3    4
        Bd = B T + --- F B T  + --- F  B T  + --- F  B T  + ...
                    2!           3!            4!

    The forward Euler method approximations to these are

        Phi = I + F T
        Bd  = B T
        Qd  = Q T

    The bilinear approximation to Phi is

                                         -1/2
        Phi = (I + 0.5 A T) (I - 0.5 A T)

    References
    ----------
    .. [1]  C. Van Loan, "Computing Integrals Involving the Matrix Exponential,"
            1976.
    .. [2]  Brown, R. and Phil Hwang. "Introduction to Random Signals and
            Applied Kalman Filtering (4th ed.)" (2012).
    .. [3]  https://en.wikipedia.org/wiki/Discretization
    """

    # Get Phi.
    N = F.shape[1] # number of states
    Phi = sp.linalg.expm(F*T)

    # Get Bd.
    if B is not None:
        M = B.shape[1] # number of inputs
        G = np.vstack(( np.hstack((F, B)), np.zeros((M, N + M)) ))
        H = sp.linalg.expm(G*T)
        Bd = H[0:N, N:(N + M)]
    else:
        Bd = None

    # Get Qd.
    if Q is not None:
        L = np.vstack((
                np.hstack((-F, Q)),
                np.hstack(( np.zeros((N, N)), F.T)) ))
        H = sp.linalg.expm(L*T)
        Qd = Phi @ H[0:N, N:(2*N)]
    else:
        Qd = None

    return Phi, Bd, Qd

# -------------
# Mechanization
# -------------

def llh_to_vne(llh_t, T):
    """
    Convert geodetic position over time to velocity of the navigation frame
    relative to the earth frame over time. Geodetic position is quadratically
    extrapolated by one sample.

    Parameters
    ----------
    llh_t : (3, K) or (K, 3) np.ndarray
        Matrix of geodetic position vectors of latitude (radians), longitude
        (radians), and height above ellipsoid (meters).
    T : float
        Sampling period in seconds.

    Returns
    -------
    vne_t : (3, K) or (K, 3) np.ndarray
        Matrix of velocity vectors.
    """

    # Check input.
    if isinstance(llh_t, list):
        llh_t = np.array(llh_t)
    trs = (llh_t.ndim == 2 and llh_t.shape[0] != 3)

    # Transpose the input.
    if trs:
        llh_t = llh_t.T

    # Parse geodetic position.
    lat = llh_t[0]
    lon = llh_t[1]
    hae = llh_t[2]

    # Extended derivatives
    lat_ext = 3*lat[-1] - 3*lat[-2] + lat[-3]
    lon_ext = 3*lon[-1] - 3*lon[-2] + lon[-3]
    hae_ext = 3*hae[-1] - 3*hae[-2] + hae[-3]
    Dlat = np.diff(np.append(lat, lat_ext))/T
    Dlon = np.diff(np.append(lon, lon_ext))/T
    Dhae = np.diff(np.append(hae, hae_ext))/T

    # Rotation rate of navigation frame relative to earth frame,
    # referenced in the navigation frame
    wnne_x = np.cos(lat)*Dlon
    wnne_y = -Dlat

    # Velocity of the navigation frame relative to the earth frame,
    # referenced in the navigation frame
    klat = np.sqrt(1 - E2*np.sin(lat)**2)
    Rm = (A_E/klat**3)*(1 - E2)
    Rt = A_E/klat
    vN = -wnne_y*(Rm + hae)
    vE =  wnne_x*(Rt + hae)
    vD = -Dhae
    if trs:
        vne_t = np.column_stack((vN, vE, vD))
    else:
        vne_t = np.row_stack((vN, vE, vD))

    return vne_t


def vne_to_rpy(vne_t, grav_t, T, alpha=0.0, wind=None):
    """
    Estimate the attitude angles in radians based on velocity.

    Parameters
    ----------
    vne_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of velocity of the navigation frame relative to the
        ECEF frame (meters per second).
    grav_t : float or (K,) np.ndarray
        Local acceleration of gravity magnitude in meters per second squared.
    T : float
        Sampling period in seconds.
    alpha : float, default 0.0
        Angle of attack in radians.
    wind : (2,) or (2, K) np.ndarray, default None
        Horizontal velocity vector of wind in meters per second.

    Returns
    -------
    rpy_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of attitude angles roll, pitch, and yaw, all in
        radians. These angles are applied in the context of a North, East, Down
        navigation frame to produce the body frame in a zyx sequence of passive
        rotations.
    """

    # Check input.
    if isinstance(vne_t, list):
        vne_t = np.array(vne_t)
    if isinstance(grav_t, list):
        grav_t = np.array(grav_t)
    trs = (vne_t.ndim == 2 and vne_t.shape[0] != 3)

    # Transpose input.
    if trs:
        vne_t = vne_t.T

    # Filter the velocity.
    vN, vE, vD = vne_t

    # Get the horizontal velocity.
    vH = np.sqrt(vN**2 + vE**2)

    # Estimate the yaw.
    if wind is None:
        yaw = np.arctan2(vE, vN)*(vH > 1e-6)
    else:
        yaw = np.arctan2(vE - wind[1], vN - wind[0])*(vH > 1e-6)

    # Estimate the pitch.
    pit = np.arctan(-vD/vH)*(vH > 1e-6) + alpha

    # Estimate the roll.
    aN = np.gradient(vN)/T # x-axis acceleration
    aE = np.gradient(vE)/T # y-axis acceleration
    ac = (vN*aE - vE*aN)/(vH + 1e-4) # cross product vH with axy
    rol = np.arctan(ac/grav_t)*(vH > 1e-6)

    # Assemble.
    rpy_t = np.row_stack((rol, pit, yaw))

    # Transpose output.
    if trs:
        rpy_t = rpy_t.T

    return rpy_t


def inv_mech(llh_t, vne_t, rpy_t, T, grav_model=somigliana, show_progress=True):
    """
    Compute the inverse mechanization of pose to get inertial measurement unit
    sensor values.

    Parameters
    ----------
    llh_t : (3, K) or (K, 3) np.ndarray
        Matrix of geodetic positions in terms of latitude (radians), longitude
        (radians), and height above ellipsoid (meters).
    vne_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of velocity of the navigation frame relative to the
        ECEF frame (meters per second).
    rpy_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of attitude angles roll, pitch, and yaw, all in
        radians. These angles are applied in the context of a North, East, Down
        navigation frame to produce the body frame in a zyx sequence of passive
        rotations.
    T : float
        Sampling period in seconds.
    grav_model : function, default somigliana
        The gravity model function to use. This function should take a position
        vector of latitude (radians), longitude (radians), and height above
        ellipsoid (meters) and return the local acceleration of gravity vector
        (meters per second squared) in the navigation frame with a North, East,
        Down (NED) orientation.
    show_progress : bool, default True
        Flag to show the progress bar in the terminal.

    Returns
    -------
    fbbi_t : (3, K) or (K, 3) np.ndarray
        Matrix of specific force vectors (meters per second squared) of the body
        frame relative to the inertial frame, referenced in the body frame.
    wbbi_t : (3, K) or (K, 3) np.ndarray
        Matrix of rotation rate vectors (radians per second) of the body frame
        relative to the inertial frame, referenced in the body frame.
    """

    # Check input.
    if isinstance(llh_t, list):
        llh_t = np.array(llh_t)
    if isinstance(vne_t, list):
        vne_t = np.array(vne_t)
    if isinstance(rpy_t, list):
        rpy_t = np.array(rpy_t)
    trs = (llh_t.ndim == 2 and llh_t.shape[0] != 3)

    # Transpose input.
    if trs:
        llh_t = llh_t.T
        vne_t = vne_t.T
        rpy_t = rpy_t.T

    # Extrapolate inputs by one sample.
    llh_ext = 3*llh_t[:, -1] - 3*llh_t[:, -2] + llh_t[:, -3]
    vne_ext = 3*vne_t[:, -1] - 3*vne_t[:, -2] + vne_t[:, -3]
    rpy_ext = 3*rpy_t[:, -1] - 3*rpy_t[:, -2] + rpy_t[:, -3]
    llh_t = np.column_stack((llh_t, llh_ext))
    vne_t = np.column_stack((vne_t, vne_ext))
    rpy_t = np.column_stack((rpy_t, rpy_ext))

    # storage
    K = llh_t.shape[1]
    fbbi_t = np.zeros((3, K - 1))
    wbbi_t = np.zeros((3, K - 1))

    # time loop
    for k in range(K - 1):
        # inputs
        llh = llh_t[:, k]
        llh_p = llh_t[:, k + 1]
        vne = vne_t[:, k]
        vne_p = vne_t[:, k + 1]
        rpy = rpy_t[:, k]
        rpy_p = rpy_t[:, k + 1]

        # position and velocity
        Dllh = (llh_p - llh)/T
        Dvne = (vne_p - vne)/T

        # rotation matrix
        Cnb = rpy_to_dcm(rpy).T
        Cnb_p = rpy_to_dcm(rpy_p).T
        wbbn = inverse_rodrigues_rotation(Cnb.T @ Cnb_p)/T

        # rotation rates
        clat = math.cos(llh[0])
        slat = math.sin(llh[0])
        wnne = np.array([
            clat*Dllh[1],
            -Dllh[0],
            -slat*Dllh[1]])
        wnei = np.array([
            W_EI*clat,
            0.0,
            -W_EI*slat])
        wbbi = wbbn + Cnb.T @ (wnne + wnei)

        # specific force
        grav = grav_model(llh)
        fbbi = Cnb.T @ (Dvne + np.cross(2*wnei + wnne, vne) - grav)

        # results storage
        fbbi_t[:, k] = fbbi
        wbbi_t[:, k] = wbbi

        # progress bar
        if show_progress:
            progress(k, K - 1)

    # Transpose output.
    if trs:
        fbbi_t = fbbi_t.T
        wbbi_t = wbbi_t.T

    return fbbi_t, wbbi_t


def mech(fbbi_t, wbbi_t, llh0, vne0, rpy0, T, hae_t=None,
        grav_model=somigliana, show_progress=True):
    """
    Compute the forward mechanization of inertial measurement unit sensor values
    to get pose.

    Parameters
    ----------
    fbbi_t : (3, K) or (K, 3) np.ndarray
        Matrix of specific force vectors (meters per second squared) of the body
        frame relative to the inertial frame, referenced in the body frame.
    wbbi_t : (3, K) or (K, 3) np.ndarray
        Matrix of rotation rate vectors (radians per second) of the body frame
        relative to the inertial frame, referenced in the body frame.
    llh0 : (3,) np.ndarray
        Initial geodetic position of latitude (radians), longitude (radians),
        and height above ellipsoid (meters).
    vne0 : (3,) np.ndarray
        Initial velocity vector (meters per second) in North, East, and Down
        (NED) directions.
    rpy0 : (3,) np.ndarray
        Initial roll, pitch, and yaw angles in radians. These angles are applied
        in the context of a North, East, Down (NED) navigation frame to produce
        the body frame in a zyx sequence of passive rotations.
    T : float
        Sampling period in seconds.
    hae_t : (K,) np.ndarray, default None
        Overrides height with this array of values if given.
    grav_model : function, default somigliana
        The gravity model function to use. This function should take a position
        vector of latitude (radians), longitude (radians), and height above
        ellipsoid (meters) and return the local acceleration of gravity vector
        (meters per second squared) in the navigation frame with a North, East,
        Down (NED) orientation.
    show_progress : bool, default True
        Flag to show the progress bar in the terminal.

    Returns
    -------
    llh_t : (3, K) or (K, 3) np.ndarray
        Matrix of geodetic positions in terms of latitude (radians), longitude
        (radians), and height above ellipsoid (meters).
    vne_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of velocity of the navigation frame relative to the
        ECEF frame (meters per second).
    rpy_t : (3, K) or (K, 3) np.ndarray
        Matrix of vectors of attitude angles roll, pitch, and yaw, all in
        radians. These angles are applied in the context of a North, East, Down
        navigation frame to produce the body frame in a zyx sequence of passive
        rotations.
    """

    # Check the inputs.
    if isinstance(fbbi_t, list):
        fbbi_t = np.array(fbbi_t)
    if isinstance(wbbi_t, list):
        wbbi_t = np.array(wbbi_t)
    if isinstance(llh0, list):
        llh0 = np.array(llh0)
    if isinstance(vne0, list):
        vne0 = np.array(vne0)
    if isinstance(rpy0, list):
        rpy0 = np.array(rpy0)
    trs = (fbbi_t.ndim == 2 and fbbi_t.shape[0] != 3)

    # Initialize states.
    llh = llh0.copy()
    vne = vne0.copy()
    Cnb = rpy_to_dcm(rpy0).T

    # Transpose input.
    if trs:
        fbbi_t = fbbi_t.T
        wbbi_t = wbbi_t.T

    # Storage
    K = fbbi_t.shape[1]
    llh_t = np.zeros((3, K))
    vne_t = np.zeros((3, K))
    rpy_t = np.zeros((3, K))

    # Time loop
    for k in range(K):
        # Inputs
        fbbi = fbbi_t[:, k]
        wbbi = wbbi_t[:, k]

        # Override height and velocity if height is provided.
        if hae_t is not None:
            llh[2] = hae_t[k]
            if k < K - 1:
                vne[2] = -(hae_t[k + 1] - hae_t[k])/T

        # Results storage
        llh_t[:, k] = llh
        vne_t[:, k] = vne
        rpy_t[:, k] = dcm_to_rpy(Cnb.T)

        # Get the derivatives.
        Dllh, Dvne, wbbn = mech_step(fbbi, wbbi, llh, vne, Cnb, grav_model)

        # Integrate.
        llh += Dllh * T
        vne += Dvne * T
        Cnb[:, :] = Cnb @ rodrigues_rotation(wbbn * T)
        orthonormalize_dcm(Cnb)

        # Progress bar
        if show_progress:
            progress(k, K)

    # Transpose output.
    if trs:
        llh_t = llh_t.T
        vne_t = vne_t.T
        rpy_t = rpy_t.T

    return llh_t, vne_t, rpy_t


def mech_step(fbbi, wbbi, llh, vne, Cnb, grav_model=somigliana):
    """
    Get the derivatives of position, velocity, and attitude for one time step.

    Parameters
    ----------
    fbbi : (3,) np.ndarray
        Vector of specific forces (meters per second squared) of the body frame
        relative to the inertial frame, referenced in the body frame.
    wbbi : (3,) np.ndarray
        Vector of rotation rates (radians per second) of the body frame relative
        to the inertial frame, referenced in the body frame.
    llh : (3,) np.ndarray
        Vector of geodetic position in terms of latitude (radians), longitude
        (radians), and height above ellipsoid (meters).
    vne : (3,) np.ndarray
        Vector of velocity of the navigation frame relative to the ECEF frame
        (meters per second).
    Cnb : (3, 3) np.ndarray
        Passive rotation matrix from the body frame to the NED navigation frame.
    grav_model : function, default somigliana
        The gravity model function to use. This function should take a position
        vector of latitude (radians), longitude (radians), and height above
        ellipsoid (meters) and return the local acceleration of gravity vector
        (meters per second squared) in the navigation frame with a North, East,
        Down (NED) orientation.

    Returns
    -------
    Dllh : (3,) np.ndarray
        Derivative of the vector of the geodetic position.
    Dvne : (3,) np.ndarray
        Derivative of the vector of the navigation frame velocity.
    wbbn : (3,) np.ndarray
        Derivative of the vector of the rotation rate of the body frame relative
        to the navigation frame.
    """

    # Trig of latitude
    clat = math.cos(llh[0])
    slat = math.sin(llh[0])
    tlat = math.tan(llh[0])

    # Rotation rate of earth relative to inertial
    wneix = W_EI*clat
    wneiz = -W_EI*slat

    # Rotation rate of navigation relative to earth
    klat = math.sqrt(1 - E2*slat**2)
    Rt = A_E/klat
    Rm = (Rt/klat**2)*(1 - E2)
    wnnex = vne[1]/(Rt + llh[2])
    wnney = -vne[0]/(Rm + llh[2])
    wnnez = -vne[1]*tlat/(Rt + llh[2])

    # Rotation rate of body relative to navigation
    wx = wnnex + wneix
    wy = wnney
    wz = wnnez + wneiz
    Dllh = np.array([wx, wy, wz])
    wbbn = wbbi - Cnb.T @ Dllh

    # Position derivatives
    Dllh[0] = -wnney
    Dllh[1] = wnnex/clat
    Dllh[2] = -vne[2]

    # Velocity derivatives
    wx += wneix
    wz += wneiz
    Dvne = Cnb @ fbbi + grav_model(llh)
    Dvne[0] -= wy * vne[2] - wz * vne[1]
    Dvne[1] -= wz * vne[0] - wx * vne[2]
    Dvne[2] -= wx * vne[1] - wy * vne[0]

    return Dllh, Dvne, wbbn


def jacobian(fbbi, llh, vne, Cnb):
    """
    Calculate the continuous-domain Jacobian matrix of the propagation function.
    The attitude change is handled via a tilt error vector. Note that this
    matrix must be discretized along with the dynamics noise covariance matrix.
    This can be done with the Van Loan method:

        Phi, _, Qd = inu.vanloan(F, None, Q)

    where `F` is the Jacobian returned by this function and `Q` is the dynamics
    noise covariance matrix. The `Phi` and `Qd` matrices are then the matrices
    you would use in your Bayesian estimation filter.

    Parameters
    ----------
    fbbi : (3,) np.ndarray
        Vector of specific forces (meters per second squared) of the body frame
        relative to the inertial frame, referenced in the body frame.
    llh : (3,) np.ndarray
        Vector of geodetic position in terms of latitude (radians), longitude
        (radians), and height above ellipsoid (meters).
    vne : (3,) np.ndarray
        Vector of velocity of the navigation frame relative to the ECEF frame
        (meters per second).
    Cnb : (3, 3) np.ndarray
        Passive rotation matrix from the body frame to the NED navigation frame.

    Returns
    -------
    F : (9, 9) np.ndarray
        Jacobian matrix.

    Notes
    -----
    The order of states are

        latitude, longitude, height above ellipsoid,
        North velocity, East velocity, down velocity,
        x tilt error, y tilt error, z tilt error

    The tilt error vector, psi, is applied to a true body to NED navigation
    frame rotation matrix, Cnb, to produce a tilted rotation matrix:

        ~              T 
        Cnb = exp([psi] ) Cnb
                       x 
    """

    # Parse the forces, positions, and velocities.
    fN, fE, fD = Cnb @ fbbi
    lat, _, hae = llh
    vN, vE, vD = vne

    # Trig of latitude
    clat = math.cos(lat)
    slat = math.sin(lat)
    slat2 = slat**2
    tlat = math.tan(lat)

    # Rotation rate of earth relative to inertial
    wneix = W_EI*clat
    wneiz = -W_EI*slat

    # Distance from Earth
    klat = math.sqrt(1 - E2*slat2)
    Rt = A_E/klat
    Rm = (Rt/klat**2)*(1 - E2)
    lt = Rt + hae
    lm = Rm + hae

    # Get the partial derivatives with respect to latitude and height.
    Dyl = (5.18595e-2 + 4.4e-9*hae)*np.sin(2*lat) \
            - 1.1475e-4*np.sin(4*lat)
    y0 = (9.7803253359 + 0.01889414744159113919*slat2)/klat
    Dyh = y0 * (-3.1570428705799e-7 + 2.10268965044e-9*slat2
            + 1.4749034e-13*hae)

    # Define the Jacobian matrix.
    F = np.zeros((9, 9))
    F[0, 2] = -vN/lm**2
    F[0, 3] = 1/lm
    F[1, 0] = vE*tlat/(lt*clat)
    F[1, 2] = -vE/(lt**2*clat)
    F[1, 4] = 1/(lt*clat)
    F[2, 5] = -1
    F[3, 0] = -2*vE*wneix - vE**2/(lt*clat**2)
    F[3, 2] = vE**2*tlat/lt**2 - vN*vD/lm**2
    F[3, 3] = vD/lm
    F[3, 4] = 2*wneiz - 2*vE*tlat/lt
    F[3, 5] = vN/lm
    F[3, 7] = -fD
    F[3, 8] = fE
    F[4, 0] = 2*vN*wneix + 2*vD*wneiz \
        + vN*vE/(lt*clat**2)
    F[4, 2] = -vE*(vN*tlat + vD)/lt**2
    F[4, 3] = -2*wneiz + vE*tlat/lt
    F[4, 4] = (vN*tlat + vD)/lt
    F[4, 5] = 2*wneix + vE/lt
    F[4, 6] = fD
    F[4, 8] = -fN
    F[5, 0] = -2*vE*wneiz + Dyl
    F[5, 2] = (vN/lm)**2 + (vE/lt)**2 + Dyh
    F[5, 3] = -2*vN/lm
    F[5, 4] = -2*wneix - 2*vE/lt
    F[5, 6] = -fE
    F[5, 7] = fN
    F[6, 0] = wneiz
    F[6, 2] = -vE/lt**2
    F[6, 4] = 1/lt
    F[6, 7] = wneiz - vE*tlat/lt
    F[6, 8] = vN/lm
    F[7, 2] = vN/lm**2
    F[7, 3] = -1/lm
    F[7, 6] = -wneiz + vE*tlat/lt
    F[7, 8] = wneix + vE/lt
    F[8, 0] = -wneix - vE/(lt*clat**2)
    F[8, 2] = vE*tlat/lt**2
    F[8, 4] = -tlat/lt
    F[8, 6] = -vN/lm
    F[8, 7] = -wneix - vE/lt

    return F
