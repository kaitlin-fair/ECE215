# Objective 3.7

| LO# | Description |
|----------|----------|
| 3.7 | I can calculate the maximum detection range from a radar antenna to a target using the Radar Range equation. | 

## RADAR Detection Range

Once you find an object with a RADAR, calculating its distance is easy.
The problem is actually finding the object -- aircraft or incoming
missile from over the horizon. In this lesson, we'll focus on how far
away RADAR can detect a target based on the same principles we used with
the Friis equation. Next lesson, we'll talk about more advanced RADAR
capabilities, which are used to detect multiple targets.

First, let's look at a RADAR's maximum range, which is a specific
application of the communications concepts we've already learned. In
order to detect a target, we need to have LOS to the object and then get
enough energy to the target so that, when the energy is reflected, it
can travel back to the RADAR's receiver where it will be detected and
processed. In the simplest RADAR scenario, we are considering the
receiver to be co-located with the transmitter.

Let's look at LOS range how it affects our RADAR's maximum range. This
follows the exact same process as determining whether two radios have
LOS. While there are RADARs that use RF propagation methods other than
LOS (e.g., forward scatter), most RADAR systems rely on LOS, so we must
first ensure our RADAR is within the maximum LOS range:

$r_{max,LOS} = \sqrt{2h_{radar}} + \sqrt{2h_{target}}$

Once the target is within the maximum LOS range, we also need to deliver
energy to the target and then collect the reflected energy. Since
electromagnetic energy from a RADAR makes a round trip (compared with
the one-way trip for a radio), we'll need to modify the Friis equation
to handle this new scenario. Using the same principles as with the
development of the Friis equation, the power density *reaching the
target* will be:

$$S = P_{T}G_{T}\frac{1}{4\pi R^{2}}$$

When we developed the Friis equation, we multiplied this power density
by the receiving antenna's effective area to find how much power was
received. In that case, we want the receiver to collect as much energy
as possible. However, with RADAR, the target is reflecting the energy
rather than receiving it. We use a parameter called *RADAR cross
section* (RCS) to quantify how much of the impinging signal is reflected
by an object. RCS is denoted by the Greek symbol σ and most often given
in units of m^2^, although it can also be given in units of dBsm
(dB/m^2^). As a side note, developing "stealthy" aircraft involves
employing a myriad of techniques to reduce the RCS as much as possible,
thereby making the aircraft look "small" (or invisible) to the RADAR.
These modifications range from structural changes that deflect signals
instead of reflecting them to special coatings which absorb the energy
instead of reflecting it. Even though a B-52 and a B-2 are roughly the
same size from head on, the B-2 is specifically designed not to reflect
energy back to the RADAR, so its RCS is much lower and the aircraft is
much harder to detect.

For this course, we will use a single "average" value to describe an
object's RCS, but in reality, this value changes depending on the
orientation of the object with respect to the RADAR.

Now, the power reflected from the target back to the RADAR receiver is:

$$P = \left( P_{T}G_{T}\frac{1}{4\pi R^{2}} \right)(RCS) = P_{T}G_{T}\frac{RCS}{4\pi R^{2}}$$

At this point, the reflected signal will travel back to the receiver at
the speed of light. Again, the energy will "spread out" on a spherical
surface, with the distance between the RADAR and target, $R$, being the
radius of that sphere. Therefore, the power at the receiver will be:

$$P = \left( P_{T}G_{T}\frac{RCS}{4\pi R^{2}} \right)\left( \frac{1}{4\pi R^{2}} \right) = P_{T}G_{T}\frac{RCS}{(4\pi)^{2}R^{4}}$$

We must then "catch" this power with the receiving antenna's effective
area which is:

$$A_{eff} = \frac{\lambda^{2}}{4\pi}G_{R}$$

Therefore, the received power at the RADAR is:

$$P_{R} = PA_{eff} = \left( P_{T}G_{T}\frac{RCS}{(4\pi)^{2}R^{4}} \right)\left( \frac{\lambda^{2}}{4\pi}G_{R} \right)$$

Combining and simplifying---and assuming we're using the same antenna
for both transmission and reception---we find the final form of the
RADAR equation.

> **Key Concept -- RADAR Equation**
> 
> $$P_{R} = P_{T}G^{2}RCS\frac{\lambda^{2}}{(4\pi)^{3}R^{4}}$$

Let's look at the differences between received power for a RADAR versus
a communications link:

-   Doubling transmitted power also doubles the received power -- this
    is the same as before.

-   Doubling the RADAR antenna's gain, quadruples the received power,
    because we're effectively doubling both transmit and receive
    antennas at once.

-   Doubling the system's wavelength quadruples received power -- this
    is also the same before. Therefore, by using a lower frequency, more
    power arrives at the receiver. One challenge here is that reducing
    the RADAR's frequency also decreases the RADAR's accuracy, which
    we'll discuss shortly.

-   Doubling the distance between the RADAR and target reduces the power
    received by a factor of 16 -- this is the biggest difference between
    RADAR and communications.

This last fact makes building an effective RADAR system difficult. The
received power is almost always incredibly small. This requires RADARs
to have much more sensitive receivers than a radio. Also, most modern
RADAR receivers have the ability to integrate their received power over
the duration of the pulse width and extract all possible energy in the
pulse. Therefore, the longer the pulse duration, the more energy the
receiver can detect, giving a better signal-to-noise ratio.

In practice, aside from making smart design choices (stealthy materials
and sharp angles), we might ask what else can be done to help identify
when a RADAR wave impinges on your aircraft or weapon system.
Fortunately, a device called a RADAR Warning Receiver (RWR) can alert us
to the presence of RADAR wave. An RWR is basically a receiving radio
that "listens" for the electromagnetic waves generated by a RADAR.
Therefore, we can calculate the effective "listening" range of the RWR
using the Friis equation. In general, if we are trying to avoid RADAR
detection, we would like to know about a RADAR before it knows about us.
However, if we are designing a long range RADAR system, we want the
opposite to be true: we would like to detect the target before its RWR
can detect our signals.

### Example Problem 1
A B-52 with an RCS of 100 m^2^ is ingressing
hostile territory at 30,000' AGL. The enemy RADAR is on a 100' hill and
has the following parameters:

-   *P­<sub>T­</sub>* = 1 kW

-   *G* = 150

-   *f* = 300 MHz

-   Minimum *P­<sub>R­</sub>* = 12 fW

The B-52 has an RWR to detect enemy RADAR signals. Its parameters are:

-   G = 3.0

-   Minimum *P­<sub>R­</sub>* = 215 nW

Who sees who first (i.e., who is the first to establish positive
detection)?

**Understand**: Here, we have a friendly plane flying a sortie in the
vicinity of an enemy's RADAR. The friendly plane has an RWR with a given
sensitivity -- a *minimum* power needed to detect a signal. The
sensitivity will give us the *maximum* range (since power and range are
inversely proportional). We are asked to determine whether the RADAR
sees the plane first, or if the RWR does its job and alerts the B-52 to
the RADAR first.

**Identify Key Information**:

-   **Knowns:** We know the key parameters for both the RADAR and RWR.

-   **Unknowns:** We do not know the LOS or detection range for either
    the RADAR or RWR.

-   **Assumptions:** We assume the B-52's RCS is appropriate for its
    orientation to the RADAR. We also assume the gain for both antennas
    is representative of the orientations.

**Plan:** This problem uses almost all of the concepts from the last few
lessons. We need to solve for three separate ranges: the maximum LOS
range between the B-52 and the site, the maximum RADAR detection range
for the enemy's RADAR site, and the maximum communications range for the
B-52 warning receiver.

**Solve:** Let's solve the LOS piece first.

$$r_{max,\ \ total} = \sqrt{2h_{B - 52}} + \sqrt{2h_{radar}}\  = \sqrt{2*30,000'} + \ \sqrt{2*100'} = 259.1\ miles = 417.1\ km$$

The high altitude that the B-52 is at flying allows LOS to be
established at a long range.

Now, let's look at how far away the RADAR can detect the bomber. First,
we need to solve for the signal's wavelength

$$\lambda = \ \frac{c}{f}\  = \ \ \frac{3 \times 10^{8}\ m/s}{300 \times 10^{6}\ Hz}\  = 1\ m$$

Next, we use the RADAR equation, recognizing that the minimum power
received gives the maximum range:

$$P_{R,min} = \frac{{P_{T}G^{2}\sigma\lambda}^{2}}{(4\pi)^{3}R_{\max}^{4}}\ $$

After some algebra machinations, we solve this equation

$$R_{\max} = \ \sqrt[4]{P_{T}G^{2}\sigma\frac{\lambda^{2}}{({4\pi)}^{3}P_{R,min}}}$$

Plugging in the values in the problem,

$$R_{RADAR,\ \ max} = \ \sqrt[4]{\frac{(1000\ W)(150)^{2}(100\ m^{2})(1\ m)^{2}}{({4\pi)}^{3}(12x10^{- 15}\ W)}\ } = 98.6\ km$$

Therefore, the RADAR will detect the bomber when it is 98.6 km away.

Finally, we can calculate how far away the bomber will be able to detect
the RADAR. Since the RWR on the bomber is a "listening" radio, we need
to use the Friis equation. As with the RADAR equation, we will need to
solve the Friis equation for *R*, again recognizing that the minimum
power received is the maximum range:

$$R_{RWR,\ max} = \ \sqrt{\frac{P_{T}G_{T}G_{R}\lambda^{2}}{{(4\pi)^{2}P}_{R,min}}} = \sqrt{\frac{(1000\ W)(150)(3)(1\ m)^{2}}{(4\pi)^{2}\left( 215x10^{- 9}\ W \right)}}\ \  = 115.1\ km\ $$

Since LOS is established at 417.1 km, both the RADAR site and the B-52
are capable of seeing each other at that range, but they don't have
enough power. Since the bomber's RWR can detect the RADAR at 115.1 km,
but the RADAR does not detect the bomber until 98.6 km, the bomber will
see the RADAR before the RADAR will see the bomber.

**Answer**: The B-52 is the first to detect.

### Example Problem 2
Given the previous scenario, but instead of a
B-52 at high altitude, let's use a B-1 (with a smaller RCS of 10 m^2^)
ingressing hostile territory at 200' AGL. All other parameters are the
same. What is the range that the RADAR will detect the B-1?

**Understand**: This is the same as the problem before, but now we have
changed the aircraft, which means we need to recalculate the LOS range
(since the altitude of the aircraft has changed) and the RADAR detection
range (since the RCS, σ, has changed).

**Identify Key Information**:

-   **Knowns:** We know the new altitude, the new RCS ($\sigma)$, and
    the RADAR parameters.

-   **Unknowns:** We do not know the new LOS range or the RADAR's
    detection range for the B-1.

-   **Assumptions:** As before, we assume the aircraft's RCS is
    appropriate for its orientation to the RADAR. We also assume the
    gain for both antennas is representative of the orientations.

**Plan:** We need to solve for two ranges: the maximum LOS range between
the B-1 and the RADAR site and the maximum RADAR detection range for the
enemy's RADAR site.

**Solve:** Let's solve for the new LOS range first:

$$r_{max,\ \ total} = \ \sqrt{2h_{B - 1}} + \sqrt{2h_{RADAR}}\  = \ \sqrt{2*200'} + \ \sqrt{2*100'\ } = \ 34.14\ miles = 54.97\ km$$

Now, let's look at how far away the RADAR can detect the bomber. First,
we start with the re-arranged RADAR equation,

$$R_{RADAR,max} = \ \sqrt[4]{P_{T}G^{2}\sigma\frac{\lambda^{2}}{({4\pi)}^{3}P_{R,min}}}$$

Plugging in the values in the problem,

$$R_{RADAR,\ max} = \ \sqrt[4]{\frac{(1000\ W)(150)^{2}(10\ m^{2})(1\ m)^{2}}{({4\pi)}^{3}(12x10^{- 15}\ W)}\ } = 55.4\ km$$

Using the same logic as before, we see that the RADAR can detect the
returned signal from the B-1 at 55.4km, but doesn't have LOS until 54.97
km.

**Answer:** The RADAR will detect the B-1 at 54.97 km.
