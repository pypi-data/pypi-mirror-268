import numba
import numba.cuda as numba_driver
import numpy as np
import math

AVAIL_TORQUE = np.array([-1.0, 0.0, 1.0])

LINK_LENGTH_1 = 1.0  # [m]
LINK_LENGTH_2 = 1.0  # [m]
LINK_MASS_1 = 1.0  #: [kg] mass of link 1
LINK_MASS_2 = 1.0  #: [kg] mass of link 2
LINK_COM_POS_1 = 0.5  #: [m] position of the center of mass of link 1
LINK_COM_POS_2 = 0.5  #: [m] position of the center of mass of link 2
LINK_MOI = 1.0  #: moments of inertia for both links

pi = 3.1415926535897932384626433
MAX_VEL_1 = 12.566370614359172 # 4 * pi
MAX_VEL_2 = 28.274333882308138 # 9 * pi


@numba_driver.jit
def NumbaClassicControlAcrobotEnvStep(
        state_arr,
        action_arr,
        done_arr,
        reward_arr,
        observation_arr,
        env_timestep_arr,
        episode_length):

    kEnvId = numba_driver.blockIdx.x
    kThisAgentId = numba_driver.threadIdx.x

    TORQUE = numba_driver.const.array_like(AVAIL_TORQUE)

    assert kThisAgentId == 0, "We only have one agent per environment"

    env_timestep_arr[kEnvId] += 1

    assert 0 < env_timestep_arr[kEnvId] <= episode_length

    reward_arr[kEnvId, kThisAgentId] = -1.0

    action = action_arr[kEnvId, kThisAgentId, 0]

    torque = TORQUE[action]

    ns = numba_driver.local.array(shape=4, dtype=numba.float32)
    rk4(state_arr[kEnvId, kThisAgentId], torque, ns)

    ns[0] = wrap(ns[0], -pi, pi)
    ns[1] = wrap(ns[1], -pi, pi)
    ns[2] = bound(ns[2], -MAX_VEL_1, MAX_VEL_1)
    ns[3] = bound(ns[3], -MAX_VEL_2, MAX_VEL_2)

    for i in range(4):
        state_arr[kEnvId, kThisAgentId, i] = ns[i]

    terminated = _terminal(state_arr, kEnvId, kThisAgentId)
    if terminated:
        reward_arr[kEnvId, kThisAgentId] = 0.0

    _get_ob(state_arr, observation_arr, kEnvId, kThisAgentId)

    if env_timestep_arr[kEnvId] == episode_length or terminated:
        done_arr[kEnvId] = 1


@numba_driver.jit(device=True)
def _dsdt(state, torque, derivatives):
    m1 = LINK_MASS_1
    m2 = LINK_MASS_2
    l1 = LINK_LENGTH_1
    lc1 = LINK_COM_POS_1
    lc2 = LINK_COM_POS_2
    I1 = LINK_MOI
    I2 = LINK_MOI
    g = 9.8
    a = torque
    theta1 = state[0]
    theta2 = state[1]
    dtheta1 = state[2]
    dtheta2 = state[3]
    d1 = (
            m1 * lc1 ** 2
            + m2 * (l1 ** 2 + lc2 ** 2 + 2 * l1 * lc2 * math.cos(theta2))
            + I1
            + I2
    )
    d2 = m2 * (lc2 ** 2 + l1 * lc2 * math.cos(theta2)) + I2
    phi2 = m2 * lc2 * g * math.cos(theta1 + theta2 - pi / 2)
    phi1 = (
            -m2 * l1 * lc2 * dtheta2 ** 2 * math.sin(theta2)
            - 2 * m2 * l1 * lc2 * dtheta2 * dtheta1 * math.sin(theta2)
            + (m1 * lc1 + m2 * l1) * g * math.cos(theta1 - pi / 2)
            + phi2
    )

    ddtheta2 = (a + d2 / d1 * phi1 - m2 * l1 * lc2 * dtheta1 ** 2 * math.sin(theta2) - phi2
                ) / (m2 * lc2 ** 2 + I2 - d2 ** 2 / d1)
    ddtheta1 = -(d2 * ddtheta2 + phi1) / d1

    derivatives[0] = dtheta1
    derivatives[1] = dtheta2
    derivatives[2] = ddtheta1
    derivatives[3] = ddtheta2


@numba_driver.jit(device=True)
def rk4(state, torque, yout):
    dt = 0.2
    dt2 = 0.1
    k1 = numba_driver.local.array(shape=4, dtype=numba.float32)
    _dsdt(state, torque, k1)
    k1_update = numba_driver.local.array(shape=4, dtype=numba.float32)
    for i in range(4):
        k1_update[i] = state[i] + k1[i] * dt2
    k2 = numba_driver.local.array(shape=4, dtype=numba.float32)
    _dsdt(k1_update, torque, k2)
    k2_update = numba_driver.local.array(shape=4, dtype=numba.float32)
    for i in range(4):
        k2_update[i] = state[i] + k2[i] * dt2
    k3 = numba_driver.local.array(shape=4, dtype=numba.float32)
    _dsdt(k2_update, torque, k3)
    k3_update = numba_driver.local.array(shape=4, dtype=numba.float32)
    for i in range(4):
        k3_update[i] = state[i] + k3[i] * dt
    k4 = numba_driver.local.array(shape=4, dtype=numba.float32)
    _dsdt(k3_update, torque, k4)

    for i in range(4):
        yout[i] = state[i] + dt / 6.0 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])


@numba_driver.jit(device=True)
def wrap(x, m, M):
    diff = M - m
    while x > M:
        x = x - diff
    while x < m:
        x = x + diff
    return x


@numba_driver.jit(device=True)
def bound(x, m, M):
    return min(max(x, m), M)


@numba_driver.jit(device=True)
def _terminal(state_arr, kEnvId, kThisAgentId):
    state = state_arr[kEnvId, kThisAgentId]
    return bool(-math.cos(state[0]) - math.cos(state[1] + state[0]) > 1.0)


@numba_driver.jit(device=True)
def _get_ob(
        state_arr,
        observation_arr,
        kEnvId,
        kThisAgentId,):
    state = state_arr[kEnvId, kThisAgentId]
    observation_arr[kEnvId, kThisAgentId, 0] = math.cos(state[0])
    observation_arr[kEnvId, kThisAgentId, 1] = math.sin(state[0])
    observation_arr[kEnvId, kThisAgentId, 2] = math.cos(state[1])
    observation_arr[kEnvId, kThisAgentId, 3] = math.sin(state[1])
    observation_arr[kEnvId, kThisAgentId, 4] = state[2]
    observation_arr[kEnvId, kThisAgentId, 5] = state[3]
