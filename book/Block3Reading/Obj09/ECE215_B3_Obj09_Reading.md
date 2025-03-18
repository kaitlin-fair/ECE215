# Objective 3.9

| LO# | Description |
|----------|----------|
| 3.9 | I can calculate signal-to-noise ratio (SNR) and determine the affects on wireless communications. |

## Signal-to-Noise Ratio (SNR)

Imagine yourself trying to have a conversation with someone in a very noisy room. We can use the signal-to-noise ratio (SNR) to describe how well the other person can hear you:

$$SNR = \frac{signal}{noise} = \ \frac{how\ loud\ you\ are\ talking}{how\ loud\ everyone\ else\ is\ talking}$$

If the other person can understand you, then the SNR is acceptable. If
she can't hear you, the SNR is too low. In this case, you have two
options: either increase the signal (talk louder) or decrease the noise
(tell everyone else to be quiet). Either option will effectively
increase the SNR. In electrical engineering, we describe SNR in terms of
power:

$$SNR = \ \frac{P_{signal}}{P_{noise}}$$

In the above example, the noise came from everybody else talking. But,
in wireless transmissions, there are several sources of noice: jamming,
ambient noise from other signals, and thermal noise. We will discuss
jamming in the lesson on Electronic Warfare, and for our purposes, we
can assume the ambient noise is small compared to other sources.
*Thermal noise* is caused by the thermal agitation of charge carriers.

Recall that temperature is actually a measurement of the energy of
particles in a system. Inside a wireless system, this inherent particle
movement manifests as noise, and can interfere destructively as noise.
The equation to calculate the power of thermal noise is:

$$P_{noise} = k\left( T_{sys} \right)BW$$

In this equation,

-   *k* is the Boltzmann constant of 1.38 \* 10^-23^ J/K.

-   *T­<sub>sys­</sub>* is the effective noise temperature of the system in Kelvin.

-   *BW* is the bandwidth of the signal.

Since we know how to calculate the noise power, the signal-to-noise
ratio is therefore:

$$SNR = \ \frac{P_{signal}}{P_{noise}} = \ \frac{P_{R}}{k\left( T_{sys} \right)BW}$$

### Example Problem 1
A 500 mm-radius antenna receives 166.0 fW of
power. If the received signal has a bandwidth of 10 MHz and the system
has an effective temperature of 310 K, what is the signal-to-noise
ratio?

**Understand**: In this situation, we already know how much power
arrives at the reciver, but we want to know how the inherent thermal
noise of the system affects system performance. In other words, SNR
measures how hard we have to work to process the signal.

**Identify Key Information:**

-   **Knowns:** We know the received power, the radius of the antenna
    (which is irrelevant, since we already know the received power), the
    bandwidth of the signal, and the effective temperature of the
    system.

-   **Unknowns:** Signal-to-noise ratio (SNR).

-   **Assumptions:** Thermal noise is the only appreciable source of
    noise in the system. Although the effective noise temperature is 310
    K, which is equivalent to 98.3° F, this does not mean that the
    temperature of the antenna is necessarily 98.3°F. Instead, it means
    that all the energy in the system is equivalent to thermal noise at
    a temperature of 98.3°F.

**Plan:** We simply employ the SNR equation to calculate the SNR.

**Solve**: The SNR equation gives us,

$$SNR = \ \frac{P_{R}}{k\left( T_{sys} \right)BW} = \ \frac{166.0*\ 10^{- 15}W}{\left( 1.38*10^{- 23}\frac{J}{K} \right)(310\ K)(10\ MHz)} = 3.88$$

**Answer**: For the given system, the signal-to-noise ratio is 3.88,
which is very good.

### Example Problem 2
You are designing a communication system to
receive a signal with a bandwidth of 12 MHz. In order to process the
signal, your receiver requires a SNR of 3.5. Assuming the effective
noise temperature will not be higher than 320 K, what is the minimum
received power required by your system?

**Understand**: In earlier examples, we knew the minimum received power.
Now, however, we need to calculate it.

**Identify Key Information**:

-   **Knowns:** We know the required SNR, the maximum system
    temperature, and the bandwidth of the system.

-   **Unknowns:** The minimum received power required to process the
    signal.

-   **Assumptions:** Thermal noise is the only appreciable source of
    noise in the system.

**Plan:** We can rearrange the SNR equation to solve for the received
power, P­<sub>R­</sub>. Since we know the maximum system temperature and the
minimum required SNR, this gives us the worst case scenario, which is
the minimum required receive power.

**Solve**: First, we need to solve the SNR equation for P­<sub>R­</sub>:

$$P_{R} = SNR*k\left( T_{sys} \right)BW$$

$$P_{R} = \ 3.5*\left( 1.38*\frac{10^{- 23}J}{K} \right)(320\ K)*12\ MHz = \ 185.5\ fW$$

**Answer**: The minimum power required by the system is 185.5 fW.

### Example Problem 3

Consider a RADAR that transmits 1 kW of power at a frequency of
300 MHz using an antenna with a gain of 150 towards an aircraft with a
RADAR cross section (RCS) of 100 $m^2$, which is 86 km away. How much
power will the RADAR receive and what will be the signal to noise ratio
(SNR) at the RADAR's antenna? Solving for the received power, using the
RADAR equation, gives:

$$P_{R} = \ \frac{P_{T}G^{2}\sigma\left( \frac{c}{f} \right)^{2}}{({4\pi)}^{3}R^{4}} = \ \frac{(1000\ W)(150)^{2}(100\ m^{2})\left( \frac{3 \times 10^{8}\ m/s}{300 \times 10^{6}\ Hz} \right)^{2}}{({4\pi)}^{3}{(86,000\ m)}^{4}} = 20.73\ fW$$

Now for many ultra-sensitive receivers, 20.73 fW is an acceptable power.
However, what if the RADAR is still transmitting its 1 kW of power at
the same time? If we treat this transmitted power as noise, we can
calculate a signal to noise ratio of:

$$SNR = \ \frac{P_{signal}}{P_{noise}}\  = \ \ \frac{20.73\ fW}{1\ kW} = 20.73 \times 10^{- 18}$$

This number is unacceptably small -- no receiver will be able to
distinguish the returned signal from the "noise" of the transmitter.
There are two distinct ways to solve this problem: use separate antennas
for transmitting and receiving (this is called *bistatic*) or send
pulses of energy, instead of a continuous stream, with a *monostatic*
RADAR (aka pulse-Doppler RADAR!). 