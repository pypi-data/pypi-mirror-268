# Inertial Navigation Utilities

Functions
---------
This library provides forward mechanization of inertial measurement unit sensor
values (accelerometer and gyroscope readings) to get position, velocity, and
attitude as well as inverse mechanization to get sensor values from position,
velocity, and attitude. It also includes tools to calculate velocity from
geodetic position over time, to estimate attitude from velocity, and to estimate
wind velocity from ground-track velocity and yaw angle.

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
profiles. The only error will be due to finite-precision rounding.

Vectorization
-------------
When possible, the functions are vectorized in order to handle processing
batches of values. A set of scalars is a 1D array. A set of vectors is a 2D
array, with each vector in a column. So, a (3, 7) array is a set of seven
vectors, each with 3 elements. If an input matrix does not have 3 rows, it will
be assumed that the rows of the matrix are vectors.

*Distribution Statement A: Approved for public release; distribution unlimited.*
