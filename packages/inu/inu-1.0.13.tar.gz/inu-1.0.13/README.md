# Inertial Navigation Utilities

*Distribution Statement A: Approved for public release; distribution unlimited.*

## Functions

This library provides forward mechanization of inertial measurement unit sensor
values (accelerometer and gyroscope readings) to get position, velocity, and
attitude as well as inverse mechanization to get sensor values from position,
velocity, and attitude. It also includes tools to calculate velocity from
geodetic position over time, to estimate attitude from velocity, and to estimate
wind velocity from ground-track velocity and yaw angle.

## Accuracy

The mechanization algorithms in this library make no simplifying assumptions.
The Earth is defined as an ellipsoid. Any deviations of the truth from this
simple shape can be captured by more complex gravity models. The algorithms use
a single frequency update structure which is much simpler than the common
two-frequency update structure and just as, if not more, accurate.

## Duality

The forward and inverse mechanization functions are perfect duals of each other.
This means that if you started with a profile of position, velocity, and
attitude and passed these into the inverse mechanization algorithm to get sensor
values and then passed those sensor values into the forward mechanization
algorithm, you would get back the original position, velocity, and attitude
profiles. The only error will be due to finite-precision rounding.

## Vectorization

When possible, the functions are vectorized in order to handle processing
batches of values. A set of scalars is a 1D array. A set of vectors is a 2D
array, with each vector in a column. So, a (3, 7) array is a set of seven
vectors, each with 3 elements. If an input matrix does not have 3 rows, it will
be assumed that the rows of the matrix are vectors.

## Extended Kalman Filter

An extended Kalman filter can be implemented using this library. The `mech_step`
function applies the mechanization equations to a single time step. It returns
the time derivatives of the states. The `jacobian` function calculates the
continuous-domain Jacobian of the dynamics function. While this does mean that
the user must then manually integrate the derivatives and discretize the
Jacobian, this gives the user greater flexibility to decide how to discretize
them.

The example code below is meant to run within a for loop stepping through time,
where `k` is the time index:

```python
# Inputs
fbbi = fbbi_t[:, k] # specific forces (m/s^2)
wbbi = wbbi_t[:, k] # rotation rates (rad/s)
z = z_t[:, k] # GPS position (rad, rad, m)

# Update
S = H @ Ph @ H.T + R # innovation covariance (3, 3)
Si = np.linalg.inv(S) # inverse (3, 3)
Kg = Ph @ H.T @ Si # Kalman gain (9, 3)
Ph -= Kg @ H @ Ph # update to state covariance (9, 9)
r = z - llh # innovation (3,)
dx = Kg @ r # changes to states (9,)
llh += dx[:3] # add change in position
vne += dx[3:6] # add change in velocity
# matrix exponential of skew-symmetric matrix
Psi = inu.rodrigues_rotation(dx[6:])
Cnb = Psi.T @ Cnb

# Save results.
tllh_t[:, k] = llh
tvne_t[:, k] = vne
trpy_t[:, k] = inu.dcm_to_rpy(Cnb.T)

# Get the Jacobian and propagate the state covariance.
F = inu.jacobian(fbbi, llh, vne, Cnb)
Phi = I + (F*T)@(I + (F*T/2)) # 2nd-order expm(F T)
Ph = Phi @ Ph @ Phi.T + Qd

# Get the state derivatives.
Dllh, Dvne, wbbn = inu.mech_step(fbbi, wbbi, llh, vne, Cnb)

# Integrate (forward Euler).
llh += Dllh * T # change applies linearly
vne += Dvne * T # change applies linearly
Cnb[:, :] = Cnb @ inu.rodrigues_rotation(wbbn * T)
inu.orthonormalize_dcm(Cnb)

# Update progress bar.
inu.progress(k, K, tic)
```

In the example above, `H` should be a (3, 9) matrix with ones along the
diagonal. The `Qd` should be the (9, 9) discretized dynamics noise covariance
matrix. The `R` should be the (3, 3) measurement noise covariance matrix.
