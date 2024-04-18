# Run `pytest` in the terminal.

import time
import numpy as np
import scipy as sp
import inu
import trm


def fake_path(T, axis=1):
    # Define time.
    K = round(360.0/T) + 1
    t = np.arange(K)*T

    # Define a figure eight.
    R = 0.000156784 # radians
    theta = np.linspace(0, 2*np.pi, K)
    lat = (R/4)*np.sin(2*theta)
    lon = R*(np.cos(theta) - 1)
    hae = 50.0*(1 - np.cos(theta))
    llh_t = np.row_stack((lat, lon, hae))

    # Transpose.
    if axis == 0:
        llh_t = llh_t.T

    return t, llh_t


def test_somiliana():
    # lists
    llh_t = [[np.pi/4, 0, 0],
        [np.pi/5, 0.01, 100.0]]
    grav = inu.somigliana(llh_t)
    assert np.allclose(np.linalg.norm(grav, axis=1),
        np.array([9.80619777, 9.79788193]))
    # horizontal time variance
    grav = inu.somigliana(np.array(llh_t).T)
    assert np.allclose(np.linalg.norm(grav, axis=0),
        np.array([9.80619777, 9.79788193]))


def test_rpy_dcm():
    # multiple single duals
    N = 5
    RPY = np.zeros((3, N))
    RPY[0, :] = np.random.uniform(-np.pi, np.pi, N)
    RPY[1, :] = np.random.uniform(-np.pi/2 + 1e-15, np.pi/2 - 1e-15, N)
    RPY[2, :] = np.random.uniform(-np.pi, np.pi, N)
    for n in range(N):
        C = inu.rpy_to_dcm(RPY[:, n])
        rpy = inu.dcm_to_rpy(C)
        assert np.allclose(rpy, RPY[:, n])


def test_orthonormalize_dcm():
    # Run many random tests.
    K = 1000
    N = 10
    nn = np.zeros(K)
    for k in range(K):
        C = np.random.randn(3, 3)
        for n in range(N):
            inu.orthonormalize_dcm(C)
            Z = np.abs(C @ C.T - np.eye(3))
            if np.max(Z) < 1e-15:
                break
        nn[k] = n + 1
    n_max = np.max(nn)
    assert (n_max <= 2)


def test_rodrigues_rotation():
    N = 1000
    for n in range(N):
        # Build a proper rotation vector.
        theta = np.random.randn(3)
        nm = np.linalg.norm(theta)
        if nm > np.pi:
            theta = -theta*(2*np.pi - nm)/nm

        # Convert to a rotation matrix.
        Delta = inu.rodrigues_rotation(theta)

        # Convert back to a rotation vector.
        Theta = inu.inverse_rodrigues_rotation(Delta)
        assert np.allclose(theta, Theta)


def test_mech():
    # ------------------------------------
    # Test with time varying along axis 1.
    # ------------------------------------

    # Build path.
    T = 0.1
    t, llh = fake_path(T)
    vne = inu.llh_to_vne(llh, T)
    grav = inu.somigliana(llh)
    rpy = inu.vne_to_rpy(vne, grav[2, :], T)

    # Inverse and forward mechanize.
    hfbbi, hwbbi = inu.inv_mech(llh, vne, rpy, T, show_progress=False)
    tllh, tvne, trpy = inu.mech(hfbbi, hwbbi,
        llh[:, 0], vne[:, 0], rpy[:, 0], T, show_progress=False)

    assert np.allclose(llh, tllh)
    assert np.allclose(vne, tvne)
    assert np.allclose(rpy, trpy)

    # ------------------------------------
    # Test with time varying along axis 0.
    # ------------------------------------

    # Build path.
    T = 0.1
    t, llh = fake_path(T, axis=0)
    vne = inu.llh_to_vne(llh, T)
    grav = inu.somigliana(llh)
    rpy = inu.vne_to_rpy(vne, grav[:, 2], T)

    # Inverse and forward mechanize.
    hfbbi, hwbbi = inu.inv_mech(llh, vne, rpy, T, show_progress=False)
    tllh, tvne, trpy = inu.mech(hfbbi, hwbbi,
        llh[0, :], vne[0, :], rpy[0, :], T, show_progress=False)

    assert np.allclose(llh, tllh)
    assert np.allclose(vne, tvne)
    assert np.allclose(rpy, trpy)


def view_jacobian():

    # Build path.
    T = 0.1
    t, llh_t = fake_path(T)
    K = len(t)
    hae_t = llh_t[2]
    vne_t = inu.llh_to_vne(llh_t, T)
    grav_t = inu.somigliana(llh_t)
    rpy_t = inu.vne_to_rpy(vne_t, grav_t[2, :], T)

    # Inverse mechanize.
    fbbi_t, wbbi_t = inu.inv_mech(llh_t, vne_t, rpy_t,
            T, show_progress=False)

    # -------------------------------
    # Define the small delta vectors.
    # -------------------------------

    # position
    dang = 1e-7
    dh = 1e-1
    dlat = np.array([dang, 0, 0])
    dlon = np.array([0, dang, 0])
    dhae = np.array([0, 0, dh])

    # velocity
    dv = 1e-1
    dvN = np.array([dv, 0, 0])
    dvE = np.array([0, dv, 0])
    dvD = np.array([0, 0, dv])

    # tilt error
    psi = 1e-6
    psix = np.array([psi, 0, 0])
    psiy = np.array([0, psi, 0])
    psiz = np.array([0, 0, psi])
    Psix = np.array([
        [0, -psix[2], psix[1]],
        [psix[2], 0, -psix[0]],
        [-psix[1], psix[0], 0]])
    Psiy = np.array([
        [0, -psiy[2], psiy[1]],
        [psiy[2], 0, -psiy[0]],
        [-psiy[1], psiy[0], 0]])
    Psiz = np.array([
        [0, -psiz[2], psiz[1]],
        [psiz[2], 0, -psiz[0]],
        [-psiz[1], psiz[0], 0]])
    Delx = sp.linalg.expm(Psix.T)
    Dely = sp.linalg.expm(Psiy.T)
    Delz = sp.linalg.expm(Psiz.T)

    # ---------------------------------------
    # Initialize states and allocate storage.
    # ---------------------------------------

    # Initialize the states.
    llh = llh_t[:, 0]
    vne = vne_t[:, 0]
    Cnb = inu.rpy_to_dcm(rpy_t[:, 0]).T

    # Allocate storage.
    F_t = np.zeros((K, 9, 9))
    Fn_t = np.zeros((K, 9, 9))
    F60 = np.zeros(K)

    # -----------------
    # Process the data.
    # -----------------

    tic = time.perf_counter()
    for k in range(K):
        # Inputs
        fbbi = fbbi_t[:, k]
        wbbi = wbbi_t[:, k]

        # Override height and velocity for stability.
        llh[2] = hae_t[k]
        if k < K - 1:
            vne[2] = -(hae_t[k + 1] - hae_t[k])/T

        # Get the Jacobian.
        F_t[k, :, :] = inu.jacobian(fbbi, llh, vne, Cnb)

        # Get correct derivatives.
        Dllh, Dvne, wbbn = inu.mech_step(fbbi, wbbi, llh, vne, Cnb)
        E = inu.rodrigues_rotation(wbbn*T) # exp([w]x T)
        Dx = np.concatenate((Dllh, Dvne, np.zeros(3)))

        # Get partial of states with respect to position.
        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh + dlat, vne, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 0] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dang

        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh + dlon, vne, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 1] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dang

        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh + dhae, vne, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 2] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dh

        # Get partial of states with respect to velocity.
        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne + dvN, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 3] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dv

        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne + dvE, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 4] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dv

        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne + dvD, Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 5] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/dv

        # Get partial of states with respect to tilt errors.
        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne, Delx @ Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 6] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/psi

        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne, Dely @ Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 7] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/psi
        
        tDllh, tDvne, twbbn = inu.mech_step(fbbi, wbbi, llh, vne, Delz @ Cnb)
        tE = inu.rodrigues_rotation(twbbn*T) # exp([w~]x T)
        tDpsi = -inu.inverse_rodrigues_rotation(Cnb @ tE @ E.T @ Cnb.T)/T
        Fn_t[k, :, 8] = (np.concatenate((tDllh, tDvne, tDpsi)) - Dx)/psi

        # Integrate.
        llh += Dllh * T
        vne += Dvne * T
        Cnb[:, :] = Cnb @ inu.rodrigues_rotation(wbbn * T)
        inu.orthonormalize_dcm(Cnb)

        # Update progress bar.
        inu.progress(k, K, tic)

    # Build time.
    t = np.arange(K)*T

    # Plot the comparison of the results.
    names = ["lat", "lon", "hae", "vN", "vE", "vD", "ψx", "ψy", "ψz"]
    for row in range(9):
        for col in range(9):
            F = F_t[:, row, col]
            Fn = Fn_t[:, row, col]
            if (np.max(F) < 1e-16) and (np.min(F) > -1e-16):
                continue

            # Get the NMAE.
            er = F - Fn
            nmae = np.mean(np.abs(er))/np.abs(np.mean(F))

            #trm.plot(t, np.array([Fn, F]),
            #        label=f"{nmae*100}%   d{names[row]}/d{names[col]}",
            #        rows=0.333)
