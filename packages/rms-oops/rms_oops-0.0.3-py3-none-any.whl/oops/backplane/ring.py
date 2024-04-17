################################################################################
# oops/backplanes/ring.py: Ring backplanes
################################################################################

import numpy as np
from polymath       import Pair, Qube, Scalar
from oops.backplane import Backplane
from oops.body      import Body
from oops.frame     import Frame

# Backplane names that can be "nested", such that the array mask propagates
# forward to each new backplane array that refers to it.
RING_BACKPLANES = ('ring_radius', 'radial_mode')

def ring_radius(self, event_key, rmin=None, rmax=None):
    """Radius of the ring intercept point in the observation.

    Input:
        event_key       key defining the ring surface event.
        rmin            minimum radius in km; None to allow it to be defined by
                        the event_key.
        rmax            maximum radius in km; None to allow it to be defined by
                        the event_key.
    """

    event_key = self.standardize_event_key(event_key, default='RING')
    key = ('ring_radius', event_key, rmin, rmax)
    if key in self.backplanes:
        return self.get_backplane(key)

    default_key = ('ring_radius', event_key, None, None)
    if default_key not in self.backplanes:
        self._fill_ring_intercepts(event_key)

    radius = self.get_backplane(default_key)
    if rmin is None and rmax is None:
        return radius

    new_mask = False
    if rmin is not None:
        new_mask = Qube.or_(new_mask, radius < rmin)
    if rmax is not None:
        new_mask = Qube.or_(new_mask, radius > rmax)

    if np.any(new_mask):
        radius = radius.remask_or(new_mask)

    return self.register_backplane(key, radius)

#===============================================================================
def ring_longitude(self, event_key, reference='node'):
    """Longitude of the ring intercept point in the image.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
        reference       defines the location of zero longitude.
                        'aries' for the First point of Aries;
                        'node'  for the J2000 ascending node;
                        'obs'   for the sub-observer longitude;
                        'sun'   for the sub-solar longitude;
                        'oha'   for the anti-observer longitude;
                        'sha'   for the anti-solar longitude, returning the
                                solar hour angle.
    """

    # Handle embedded backplane
    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_longitude', event_key, reference)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # Check inputs
    if reference not in ('aries', 'node', 'obs', 'oha', 'sun', 'sha'):
        raise ValueError('invalid longitude reference: ' + repr(reference))

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    # If it is not found with reference='node', fill in those backplanes
    default_key = ('ring_longitude', event_key, 'node')
    if default_key not in self.backplanes:
        self._fill_ring_intercepts(event_key)

    # Now apply the reference longitude
    longitude = self.get_backplane(default_key)
    if reference == 'node':
        return longitude

    if reference == 'aries':
        ref_lon = self._aries_ring_longitude(event_key)
    elif reference == 'sun':
        ref_lon = self._sub_solar_longitude(event_key)
    elif reference == 'sha':
        ref_lon = self._sub_solar_longitude(event_key) - Scalar.PI
    elif reference == 'obs':
        ref_lon = self._sub_observer_longitude(event_key)
    elif reference == 'oha':
        ref_lon = self._sub_observer_longitude(event_key) - Scalar.PI

    longitude = (longitude - ref_lon) % Scalar.TWOPI
    return self.register_backplane(key, longitude)

#===============================================================================
def radial_mode(self, backplane_key, cycles, epoch, amp, peri0, speed,
                      a0=0., dperi_da=0., reference='node'):
    """Radius shift based on a particular ring mode.

    Input:
        backplane_key   key defining a ring_radius or radial_mode backplane,
                        possibly with other radial modes.
        cycles          the number of radial oscillations in 360 degrees of
                        longitude.
        epoch           the time (seconds TDB) at which the mode parameters
                        apply.
        amp             radial amplitude of the mode in km.
        peri0           a longitude (radians) at epoch where the mode is at its
                        radial minimum at semimajor axis a0. For cycles == 0, it
                        is the phase at epoch, where a phase of 0 corresponds to
                        the minimum ring radius, with every particle at
                        pericenter.
        speed           local pattern speed in radians per second, as scaled by
                        the number of cycles.
        a0              the reference semimajor axis, used for slopes
        dperi_da        the rate of change of pericenter with semimajor axis,
                        measured at semimajor axis a0 in radians/km.
        reference       the reference longitude used to describe the mode; same
                        options as for ring_longitude
    """

    backplane_key = self.standardize_backplane_key(backplane_key)
    key = ('radial_mode', backplane_key, cycles, epoch, amp, peri0, speed,
                          a0, dperi_da, reference)

    if key in self.backplanes:
        return self.get_backplane(key)

    # Get original longitude, radius, and event time, ignoring modes
    ring_radius_key = backplane_key
    while ring_radius_key[0] == 'radial_mode':
        ring_radius_key = ring_radius_key[1]

    # Get the original ring_radius key; save rmin and rmax for later
    (backplane_type, event_key, rmin, rmax) = ring_radius_key
    if backplane_type != 'ring_radius':
        raise ValueError('radial modes only apply to ring_radius backplanes')

    # Get the referenced backplane without its mask
    if backplane_key[0] == 'ring_radius':
        radius = self.ring_radius(event_key, rmin=None, rmax=None)
    else:
        # We always save the unmasked version of each radial mode backplane
        unmasked_key = ('_unmasked_radial_mode',) + backplane_key[1:]
        radius = self.get_backplane(unmasked_key)

    # Evaluate the original unmasked ring backplanes
    a = self.ring_radius(event_key)
    time = self.event_time(event_key)

    # Apply the mode
    peri = peri0 + dperi_da * (a - a0) + speed * (time - epoch)
    if cycles == 0:
        mode = radius + amp * peri.cos()
    else:
        longitude = self.ring_longitude(event_key, reference)
        mode = radius + amp * (cycles * (longitude - peri)).cos()

    # Save the unmasked result
    unmasked_key = ('_unmasked_radial_mode',) + key[1:]
    self.register_backplane(unmasked_key, mode)

    # Update the mask if necessary
    if rmin is not None or rmax is not None:
        mask = False
        if rmin is not None:
            mask = Qube.or_(mask, mode.vals < rmin)
        if rmax is not None:
            mask = Qube.or_(mask, mode.vals > rmax)

        mode = mode.remask_or(mask)

    return self.register_backplane(key, mode)

#===============================================================================
def _aries_ring_longitude(self, event_key):
    """Gridless longitude of First Point of Aries from the ring ascending node.

    Primarily used internally. Longitudes are measured in the eastward
    (prograde) direction.
    """

    event_key = self.gridless_event_key(event_key, default='RING')
    key = ('_aries_ring_longitude', event_key)

    if key in self.backplanes:
        return self.get_backplane(key)

    event = self.get_gridless_event(event_key)
    frame = Frame.as_primary_frame(event.frame)
    longitude = (-frame.node_at_time(event.time)) % Scalar.TWOPI

    return self.register_backplane(key, longitude)

#===============================================================================
def ring_azimuth(self, event_key, direction='obs', apparent=True):
    """Angle from a photon direction to the local radial direction.

    The angle is measured in the prograde direction from the photon's direction
    to the local radial, as measured at the ring intercept point and projected
    into the ring plane. This value is 90 degrees at the left ansa and 270
    degrees at the right ansa.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
        direction       'obs'   for the apparent departing direction of the
                                photon to the observer;
                        'sun'   for the (negative) apparent direction of the
                                photon arriving from the Sun.
        apparent        True for the apparent azimuth in the surface frame,
                        allowing for the fact that ring particles are in orbital
                        motion around the planet center;
                        False for the actual azimuth.
    """

    if direction not in ('obs', 'sun'):
        raise ValueError('invalid azimuth direction: ' + repr(direction))

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_azimuth', event_key, direction, apparent)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    if direction == 'obs':
        event = self.get_surface_event(event_key)
        photon_los = event.dep_ap if apparent else event.dep
    else:
        event = self.get_surface_event(event_key, arrivals=True)
        photon_los = event.neg_arr_ap if apparent else event.neg_arr

    photon_angle = photon_los.longitude(recursive=self.ALL_DERIVS)
    radius_angle = event.pos.longitude(recursive=self.ALL_DERIVS)
    azimuth = (radius_angle - photon_angle) % Scalar.TWOPI

    return self.register_backplane(key, azimuth)

#===============================================================================
def ring_elevation(self, event_key, direction='obs', pole='prograde',
                                    apparent=True):
    """Angle from the ring plane to the photon direction, evaluated at the ring
    intercept point.

    It is equivalent to (PI/2 - incidence) if photon == 'obs', (PI/2 - emission)
    if photon == 'sun'.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
        direction       'obs'       for the apparent departing direction of the
                                    photon to the observer;
                        'sun'       for the (negative) apparent direction of the
                                    photon arriving from the Sun.
        pole            'sunward'   positive elevations on the illuminated face;
                        'observed'  positive elevations on the observed face;
                        'north'     positive elevations on the IAU north face;
                        'prograde'  positive elevations on the side of the rings
                                    defined by positive angular momentum;
                        'unsigned'  for positive elevations on both ring faces.
        apparent        True for the apparent elevation in the surface frame,
                        allowing for the fact that ring particles are in orbital
                        motion around the planet center;
                        False for the actual elevation.
    """

    if direction not in ('obs', 'sun'):
        raise ValueError('invalid elevation direction: ' + repr(direction))

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_elevation', event_key, direction, pole, apparent)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    # "unsigned" is the one option not explicitly supported by ring_incidence or
    # ring_emission
    if direction == 'obs':
        pole = pole.replace('unsigned', 'observed')
        alt_key = ('ring_emission_angle', event_key, pole, apparent)
    else:
        pole = pole.replace('unsigned', 'sunward')
        alt_key = ('ring_incidence_angle', event_key, pole, apparent)

    pole_angle = self.evaluate(alt_key)
    return self.register_backplane(key, Scalar.HALFPI - pole_angle)

#===============================================================================
def _fill_ring_intercepts(self, event_key):
    """Internal method to fill in the ring intercept geometry backplanes.

    Input:
        event_key       key defining the ring surface event.
    """

    # Validate the surface type
    surface = self.get_surface(event_key[1])
    if surface.COORDINATE_TYPE != 'polar':
        raise ValueError('invalid coordinate type for ring geometry: '
                         + surface.COORDINATE_TYPE)

    # Get the ring intercept coordinates
    event = self.get_surface_event(event_key)

    # Register the default ring_radius and ring_longitude backplanes
    self.register_backplane(('ring_radius', event_key, None, None),
                            event.coord1)
    self.register_backplane(('ring_longitude', event_key, 'node'),
                            event.coord2)

#===============================================================================
def ring_incidence_angle(self, event_key, pole='sunward', apparent=True):
    """Incidence angle of the arriving photons at the local ring surface.

    By default, angles are measured from the sunward pole and should always be
    <= pi/2. However, calculations for values relative to the IAU-defined north
    pole and relative to the prograde pole are also supported.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
        pole            'sunward'   for incidence < pi/2 on the illuminated
                                    face;
                        'observed'  for incidence < pi/2 on the observed face;
                        'north'     for incidence < pi/2 on the IAU-defined
                                    north face;
                        'prograde'  for incidence < pi/2 on the side of the ring
                                    plane defined by positive angular momentum.
        apparent        True for the apparent angle in the surface frame;
                        False for the actual.
    """

    if pole not in ('sunward', 'observed', 'north', 'prograde'):
        raise ValueError('invalid incidence angle pole: ' + repr(pole))

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_incidence_angle', event_key, pole, apparent)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    # See lighting.py for the standard definitions of incidence and emission.
    # A request for the standard definition always returns the sunward value,
    # but it also saves the "prograde" definition.
    sunward = self.incidence_angle(event_key, apparent=apparent)
    if pole == 'sunward':
        return self.register_backplane(key, sunward)

    prograde_key = key[:-2] + ('prograde', apparent)
    prograde = self.get_backplane(prograde_key)
    if pole == 'prograde':
        return prograde

    # Default emission angle is > pi/2 wherever the observed face of the rings
    # is different from the illuminated face.
    if pole == 'observed':
        flip = self.emission_angle(event_key, apparent) > Scalar.HALFPI
        incidence = Scalar.PI * flip + (1 - 2*flip) * sunward
        return self.register_backplane(key, incidence)

    # The remaining case is 'north'
    # If the ring is prograde, 'north' and 'prograde' are the same
    if self._ring_is_retrograde(event_key):
        incidence = Scalar.PI - prograde
    else:
        incidence = prograde

    return self.register_backplane(key, incidence)

#===============================================================================
def ring_emission_angle(self, event_key, pole='sunward', apparent=True):
    """Emission angle of the departing photons at the local ring surface.

    By default, angles are measured from the sunward pole, so the emission angle
    should be < pi/2 on the sunlit side and > pi/2 on the dark side of the
    rings. However, calculations for values relative to the IAU-defined north
    pole and relative to the prograde pole are also supported.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
        pole            'sunward'   for emission < pi/2 on the illuminated face;
                        'observed'  for emission < pi/2 on the observed face;
                        'north'     for emission < pi/2 on the IAU-defined north
                                    face;
                        'prograde'  for emission < pi/2 on the side of the ring
                                    plane defined by positive angular momentum.
        apparent        True for the apparent angle in the surface frame;
                        False for the actual.
    """

    if pole not in ('sunward', 'observed', 'north', 'prograde'):
        raise ValueError('invalid emission angle pole: ' + repr(pole))

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_emission_angle', event_key, pole, apparent)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    # See lighting.py for the standard definitions of incidence and emission.
    # A request for the standard definition always returns the sunward value,
    # but it also saves the "prograde" definition.
    sunward = self.emission_angle(event_key, apparent=apparent)
    if pole == 'sunward':
        return self.register_backplane(key, sunward)

    prograde_key = key[:-2] + ('prograde', apparent)
    prograde = self.get_backplane(prograde_key)
    if pole == 'prograde':
        return prograde

    # The "observed" emission is always <= pi/2
    if pole == 'observed':
        emission = Scalar.HALFPI - (Scalar.HALFPI - sunward).abs()
        return self.register_backplane(key, emission)

    # The remaining case is 'north'
    # If the ring is prograde, 'north' and 'prograde' are the same
    if self._ring_is_retrograde(event_key):
        emission = Scalar.PI - prograde
    else:
        emission = prograde

    return self.register_backplane(key, emission)

#===============================================================================
def ring_sub_observer_longitude(self, event_key, reference='node'):
    """Gridless sub-observer longitude in the ring plane.

    Input:
        event_key       key defining the event on the center of the ring's path.
        reference       defines the location of zero longitude.
                        'aries' for the First point of Aries;
                        'node'  for the J2000 ascending node;
                        'obs'   for the sub-observer longitude;
                        'sun'   for the sub-solar longitude;
                        'oha'   for the anti-observer longitude;
                        'sha'   for the anti-solar longitude, returning the
                                solar hour angle.
    """

    if reference not in ('aries', 'node', 'obs', 'oha', 'sun', 'sha'):
        raise ValueError('invalid longitude reference: ' + repr(reference))

    # Look up under the desired reference
    gridless_key = self.gridless_event_key(event_key, default='RING')
    key0 = ('ring_sub_observer_longitude', gridless_key)
    key = key0 + (reference,)
    if key in self.backplanes:
        return self.get_backplane(key)

    # Generate longitude values
    default_key = key0 + ('node',)
    if default_key in self.backplanes:
        longitude = self.get_backplane(default_key)
    else:
        longitude = self._sub_observer_longitude(gridless_key)
        longitude = self.register_backplane(default_key, longitude)

    if reference == 'node':
        return longitude

    # Now apply an alternative reference longitude
    if reference == 'aries':
        ref_lon = self._aries_ring_longitude(gridless_key)
    elif reference == 'sun':
        ref_lon = self._sub_solar_longitude(gridless_key)
    elif reference == 'sha':
        ref_lon = self._sub_solar_longitude(gridless_key) - np.pi
    elif reference == 'obs':
        ref_lon = self._sub_observer_longitude(gridless_key)
    elif reference == 'oha':
        ref_lon = self._sub_observer_longitude(gridless_key) - np.pi

    longitude = (longitude - ref_lon) % Scalar.TWOPI
    return self.register_backplane(key, longitude)

#===============================================================================
def ring_sub_solar_longitude(self, event_key, reference='node'):
    """Gridless sub-solar longitude in the ring plane.

    Input:
        event_key       key defining the event on the center of the ring's path.
        reference       defines the location of zero longitude.
                        'aries' for the First point of Aries;
                        'node'  for the J2000 ascending node;
                        'obs'   for the sub-observer longitude;
                        'sun'   for the sub-solar longitude;
                        'oha'   for the anti-observer longitude;
                        'sha'   for the anti-solar longitude, returning the
                                solar hour angle.
    """

    if reference not in ('aries', 'node', 'obs', 'oha', 'sun', 'sha'):
        raise ValueError('invalid longitude reference: ' + repr(reference))

    # Look up under the desired reference
    gridless_key = self.gridless_event_key(event_key, default='RING')
    key0 = ('ring_sub_solar_longitude', gridless_key)
    key = key0 + (reference,)
    if key in self.backplanes:
        return self.get_backplane(key)

    # If it is not found with reference='node', fill in those backplanes
    default_key = key0 + ('node',)
    if default_key in self.backplanes:
        longitude = self.get_backplane(default_key)
    else:
        longitude = self._sub_solar_longitude(gridless_key)
        longitude = self.register_backplane(default_key, longitude)

    if reference == 'node':
        return longitude

    # Now apply an alternative reference longitude
    if reference == 'aries':
        ref_lon = self._aries_ring_longitude(gridless_key)
    elif reference == 'sun':
        ref_lon = self._sub_solar_longitude(gridless_key)
    elif reference == 'sha':
        ref_lon = self._sub_solar_longitude(gridless_key) - np.pi
    elif reference == 'obs':
        ref_lon = self._sub_observer_longitude(gridless_key)
    elif reference == 'oha':
        ref_lon = self._sub_observer_longitude(gridless_key) - np.pi

    longitude = (longitude - ref_lon) % Scalar.TWOPI
    return self.register_backplane(key, longitude)

#===============================================================================
def ring_center_incidence_angle(self, event_key, pole='sunward', apparent=True):
    """Incidence angle of the arriving photons at the ring system center.

    Input:
        event_key       key defining the ring surface event.
        pole            'sunward'   for incidence < pi/2 on the illuminated
                                    face;
                        'observed'  for incidence < pi/2 on the observed face;
                        'north'     for incidence < pi/2 on the IAU-defined
                                    north face;
                        'prograde'  for incidence < pi/2 on the side of the ring
                                    plane defined by positive angular momentum.
        apparent        True for the apparent angle in the body frame;
                        False for the actual.
    """

    gridless_key = self.gridless_event_key(event_key, default='RING')
    return self.ring_incidence_angle(gridless_key, pole=pole, apparent=apparent)

#===============================================================================
def ring_center_emission_angle(self, event_key, pole='sunward', apparent=True):
    """Emission angle of departing photons at the center of the ring system.

    By default, angles are measured from the sunward pole, so the emission angle
    should be < pi/2 on the sunlit side and > pi/2 on the dark side of the
    rings. However, calculations for values relative to the IAU-defined north
    pole and relative to the prograde pole are also supported.

    Input:
        event_key       key defining the ring surface event.
        pole            'sunward'   for emission < pi/2 on the illuminated face;
                        'observed'  for emission < pi/2 on the observed face;
                        'north'     for emission < pi/2 on the IAU-defined north
                                    face;
                        'prograde'  for emission < pi/2 on the side of the ring
                                    plane defined by positive angular momentum.
        apparent        True for the apparent angle in the body frame;
                        False for the actual.
    """

    gridless_key = self.gridless_event_key(event_key, default='RING')
    return self.ring_emission_angle(gridless_key, pole=pole, apparent=apparent)

#===============================================================================
def ring_radial_resolution(self, event_key):
    """Projected radial resolution in km/pixel at the ring intercept point.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
    """

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_radial_resolution', event_key)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    if key in self.backplanes:
        return self.get_backplane(key)

    event = self.get_surface_event(event_key, derivs=True)
    if event.surface.COORDINATE_TYPE != 'polar':
        raise ValueError('invalid coordinate type for ring geometry: '
                         + event.surface.COORDINATE_TYPE)

    radius = event.coord1
    drad_duv = radius.d_dlos.chain(self.dlos_duv)
    resolution = drad_duv.join_items(Pair).norm()

    return self.register_backplane(key, resolution)

#===============================================================================
def ring_angular_resolution(self, event_key):
    """Projected angular resolution in radians/pixel at the ring intercept.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
    """

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_angular_resolution', event_key)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    event = self.get_surface_event(event_key, derivs=True)
    if event.surface.COORDINATE_TYPE != 'polar':
        raise ValueError('invalid coordinate type for ring geometry: '
                         + event.surface.COORDINATE_TYPE)

    longitude = event.coord2
    dlon_duv = longitude.d_dlos.chain(self.dlos_duv)
    resolution = dlon_duv.join_items(Pair).norm()

    return self.register_backplane(key, resolution)

#===============================================================================
def ring_gradient_angle(self, event_key):
    """Direction of the radius gradient at each pixel in the image.

    The angle is measured from the U-axis toward the V-axis.

    Input:
        event_key       key defining the ring surface event. Alternatively, a
                        ring_radius or radial_mode backplane key, in which case
                        this backplane inherits the mask of the given backplane
                        array.
    """

    (event_key,
     backplane_key) = self._event_and_backplane_keys(event_key, RING_BACKPLANES,
                                                     default='RING')

    key = ('ring_gradient_angle', event_key)
    if backplane_key:
        return self._remasked_backplane(key, backplane_key)

    # If this backplane array is already defined, return it
    if key in self.backplanes:
        return self.get_backplane(key)

    event = self.get_surface_event(event_key, derivs=True)
    if event.surface.COORDINATE_TYPE != 'polar':
        raise ValueError('invalid coordinate type for ring geometry: '
                         + event.surface.COORDINATE_TYPE)

    rad = event.coord1
    drad_duv = rad.d_dlos.chain(self.dlos_duv)
    (drad_du, drad_dv) = drad_duv.join_items(Pair).to_scalars()

    clock = drad_dv.arctan2(drad_du)
    return self.register_backplane(key, clock)

#===============================================================================
def ring_shadow_radius(self, event_key, ring_surface_key):
    """Radius in the ring plane that casts a shadow at each point on this body.
    """

    event_key = self.standardize_event_key(event_key)
    ring_surface_key = ring_surface_key.upper()

    key = ('ring_shadow_radius', event_key, ring_surface_key)
    if key in self.backplanes:
        return self.get_backplane(key)

    # Make sure the surface event is already defined
    _ = self.get_surface_event(event_key, arrivals=True)

    # Solve for the ring event
    ring_event_key = event_key[:1] + (ring_surface_key,) + event_key[1:]
    ring_event = self.get_surface_event(ring_event_key)
    radius = ring_event.coord1

    return self.register_backplane(key, radius)

#===============================================================================
def ring_shadow_incidence(self, event_key, ring_surface_key):
    """Incidence angle in the ring plane that casts a shadow at each point on
    this body.
    """

    event_key = self.standardize_event_key(event_key)
    ring_surface_key = ring_surface_key.upper()

    key = ('ring_shadow_incidence', event_key, ring_surface_key)
    if key in self.backplanes:
        return self.get_backplane(key)

    # Make sure the surface event is already defined
    _ = self.get_surface_event(event_key, arrivals=True)

    # Solve for the ring event
    ring_event_key = event_key[:1] + (ring_surface_key,) + event_key[1:]
    ring_event = self.get_surface_event(ring_event_key)

    # The departure vectors are defined in the ring event, but not the arrivals
    emission = ring_event.emission_angle(apparent=True, derivs=self.ALL_DERIVS)
    incidence = Scalar.HALFPI - (Scalar.HALFPI - emission).abs()

    return self.register_backplane(key, incidence)

#===============================================================================
def ring_radius_in_front(self, event_key, ring_surface_key):
    """Radius in the ring plane that obscures each point on this body."""

    event_key = self.standardize_event_key(event_key)
    ring_surface_key = ring_surface_key.upper()

    key = ('ring_radius_in_front', event_key, ring_surface_key)
    if key in self.backplanes:
        return self.get_backplane(key)

    ring_event_key = event_key[:1] + (ring_surface_key,)
    radius = self.ring_radius(ring_event_key)
    intercepted = self.where_intercepted(event_key, tvl=False)
    radius = radius.remask_or(intercepted.logical_not())

    return self.register_backplane(key, radius)

#===============================================================================
def _ring_is_retrograde(self, event_key):
    """True if this ring is retrograde."""

    body_name = event_key[1]
    if ':' in body_name:
        planet_name = body_name.partition(':')[0]
        parent = Body.lookup(planet_name)
    else:
        parent = Body.lookup(body_name).parent

    return parent.ring_is_retrograde

################################################################################

# Add these functions to the Backplane module
Backplane._define_backplane_names(globals().copy())

################################################################################
# GOLD MASTER TESTS
################################################################################

from oops.backplane.gold_master import register_test_suite
from oops.constants import DPR

def ring_test_suite(bpt):

    bp = bpt.backplane
    for (planet, name) in bpt.planet_ring_pairs:

        # Radius and resolution
        bpt.gmtest(bp.ring_radius(name),
                   name + ' radius (km)',
                   limit=0.1, radius=1)

        bpt.gmtest(bp.ring_radius(name) * bp.ring_angular_resolution(name),
                   name + ' angular resolution (km)',
                   limit=0.1, radius=1.5)

        bpt.gmtest(bp.ring_angular_resolution(name),
                   name + ' angular resolution (deg)',
                   method='degrees', limit=0.01, radius=1.5)

        # Longitude
        bpt.gmtest(bp.ring_longitude(name, reference='aries'),
                   name + ' longitude wrt Aries (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(bp.ring_longitude(name, reference='node'),
                   name + ' longitude wrt node (deg)',
                   method='mod360', limit=0.01, radius=1)

        longitude = bp.ring_longitude(name, reference='obs')
        bpt.gmtest(longitude,
                   name + ' longitude wrt observer (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(longitude - bp.ring_longitude(name, reference='oha'),
                    Scalar.PI,
                    name + ' longitude wrt observer minus wrt OHA (deg)',
                    method='mod360', limit=0.01)

        longitude = bp.ring_longitude(name, reference='sun')
        bpt.gmtest(longitude,
                   name + ' longitude wrt Sun (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(longitude - bp.ring_longitude(name, reference='sha'),
                    Scalar.PI,
                    name + ' longitude wrt Sun minus wrt SHA (deg)',
                    method='mod360', limit=1.e-13)

        # Azimuth
        apparent = bp.ring_azimuth(name, direction='obs', apparent=True)
        actual   = bp.ring_azimuth(name, direction='obs', apparent=False)
        bpt.gmtest(apparent,
                   name + ' azimuth to observer, apparent (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(actual,
                   name + ' azimuth to observer, actual (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(apparent - actual,
                    0.,
                    name + ' azimuth to observer, apparent minus actual (deg)',
                    method='mod360', limit=0.1)

        apparent = bp.ring_azimuth(name, direction='sun', apparent=True)
        actual   = bp.ring_azimuth(name, direction='sun', apparent=False)
        bpt.gmtest(apparent,
                   name + ' azimuth of Sun, apparent (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(actual,
                   name + ' azimuth of Sun, actual (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(apparent - actual,
                    0.,
                    name + ' azimuth of Sun, apparent minus actual (deg)',
                    method='mod360', limit=0.1)

        # Elevation
        apparent = bp.ring_elevation(name, direction='obs', apparent=True)
        actual   = bp.ring_elevation(name, direction='obs', apparent=False)
        bpt.gmtest(apparent,
                   name + ' elevation to observer, apparent (deg)',
                   method='degrees', limit=0.01, radius=1)
        bpt.gmtest(actual,
                   name + ' elevation to observer, actual (deg)',
                   method='degrees', limit=0.01, radius=1)
        bpt.compare(apparent - actual,
                    0.,
                    name + ' elevation to observer, apparent minus actual (deg)',
                    method='degrees', limit=0.1)

        apparent = bp.ring_elevation(name, direction='sun', apparent=True)
        actual   = bp.ring_elevation(name, direction='sun', apparent=False)
        bpt.gmtest(apparent,
                   name + ' elevation of Sun, apparent (deg)',
                   method='degrees', limit=0.01, radius=1)
        bpt.gmtest(actual,
                   name + ' elevation of Sun, actual (deg)',
                   method='degrees', limit=0.01, radius=1)
        bpt.compare(apparent - actual,
                    0.,
                    name + ' elevation of Sun, apparent minus actual (deg)',
                    method='degrees', limit=0.1)

        # Longitude & azimuth tests
        longitude = bp.ring_longitude(name, reference='obs')
        azimuth = bp.ring_azimuth(name, direction='obs')
        bpt.gmtest(azimuth - longitude,
                   name + ' azimuth minus longitude wrt observer (deg)',
                   method='mod360', limit=0.01, radius=1)

        longitude = bp.ring_longitude(name, reference='sun')
        azimuth = bp.ring_azimuth(name, direction='sun')
        bpt.compare(azimuth - longitude, 0.,
                    name + ' azimuth minus longitude wrt Sun (deg)',
                    method='mod360', limit=1.)

        # Sub-observer longitude
        bpt.gmtest(bp.ring_sub_observer_longitude(name, reference='aries'),
                   name + ' sub-observer longitude wrt Aries (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(bp.ring_sub_observer_longitude(name, reference='node'),
                   name + ' sub-observer longitude wrt node (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(bp.ring_sub_observer_longitude(name, reference='sun'),
                   name + ' sub-observer longitude wrt Sun (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(bp.ring_sub_observer_longitude(name, reference='obs'),
                    0.,
                    name + ' sub-observer longitude wrt observer (deg)',
                    method='mod360')

        # Sub-solar longitude
        bpt.gmtest(bp.ring_sub_solar_longitude(name, reference='aries'),
                   name + ' sub-solar longitude wrt Aries (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(bp.ring_sub_solar_longitude(name, reference='node'),
                   name + ' sub-solar longitude wrt node (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.gmtest(bp.ring_sub_solar_longitude(name, reference='obs'),
                   name + ' sub-solar longitude wrt observer (deg)',
                   method='mod360', limit=0.01, radius=1)
        bpt.compare(bp.ring_sub_solar_longitude(name, reference='sun'),
                    0.,
                    name + ' sub-solar longitude wrt Sun (deg)',
                    method='mod360')

        # Incidence, solar elevation
        incidence = bp.ring_center_incidence_angle(name, 'sunward')
        bpt.gmtest(incidence,
                   name + ' center incidence angle, sunward (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.compare(incidence - Scalar.HALFPI, 0.,
                    name + ' center incidence minus 90, sunward (deg)',
                    operator='<', method='degrees')
        bpt.gmtest(bp.ring_center_incidence_angle(name, 'north'),
                   name + ' center incidence angle, north (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.gmtest(bp.ring_center_incidence_angle(name, 'observed'),
                   name + ' center incidence angle, observed (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.gmtest(bp.ring_center_incidence_angle(name, 'prograde'),
                   name + ' center incidence angle, prograde (deg)',
                   limit=0.01, method='degrees', radius=1)

        sunward = bp.ring_incidence_angle(name, 'sunward')
        elevation = bp.ring_elevation(name, direction='sun', pole='sunward')
        generic = bp.incidence_angle(name)

        bpt.gmtest(sunward,
                   name + ' incidence angle, sunward (deg)',
                   limit=0.01, radius=1, method='degrees')
        bpt.compare(sunward - Scalar.HALFPI, 0.,
                    name + ' incidence angle minus 90, sunward (deg)',
                    operator='<=', method='degrees')
        bpt.compare(sunward + elevation, Scalar.HALFPI,
                    name + ' incidence plus solar elevation (deg)',
                    limit=1.e-13, method='degrees')
        bpt.compare(sunward - generic, 0.,
                    name + ' incidence angle, sunward minus generic (deg)',
                    limit=1.e-13, method='degrees')

        northward = bp.ring_incidence_angle(name, 'north')
        bpt.gmtest(northward,
                   name + ' incidence angle, north (deg)',
                   limit=0.01, radius=1, method='degrees')

        prograde = bp.ring_incidence_angle(name, 'prograde')
        if planet in ('JUPITER', 'SATURN', 'NEPTUNE'):
            bpt.compare(northward - prograde, 0.,
                        name + ' incidence angle, north minus prograde (deg)',
                        method='degrees')
        elif planet == 'URANUS':
            bpt.compare(northward + prograde, Scalar.PI,
                        name + ' incidence angle, north plus prograde (deg)',
                        limit=1.e-13, method='degrees')

        incidence0 = bp.ring_incidence_angle(name)
        incidence1 = bp.ring_center_incidence_angle(name)
        bpt.compare(incidence0 - incidence1, 0.,
                    name + ' incidence angle, ring minus center (deg)',
                    limit=0.1, method='degrees')

        # Emission, observer elevation
        bpt.gmtest(bp.ring_center_emission_angle(name, 'sunward'),
                   name + ' center emission angle, sunward (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.gmtest(bp.ring_center_emission_angle(name, 'north'),
                   name + ' center emission angle, north (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.gmtest(bp.ring_center_emission_angle(name, 'prograde'),
                   name + ' center emission angle, prograde (deg)',
                   limit=0.01, method='degrees', radius=1)

        emission = bp.ring_center_emission_angle(name, 'observed')
        bpt.gmtest(emission,
                   name + ' center emission angle, observed (deg)',
                   limit=0.01, method='degrees', radius=1)
        bpt.compare(emission - Scalar.HALFPI, 0.,
                    name + ' center emission minus 90, observed (deg)',
                    operator='<', method='degrees')

        emission = bp.ring_emission_angle(name, 'observed')
        elevation = bp.ring_elevation(name, direction='obs', pole='observed')
        generic = bp.emission_angle(name)

        bpt.gmtest(emission,
                   name + ' emission angle, observed (deg)',
                   limit=0.01, radius=1, method='degrees')
        bpt.compare(emission - Scalar.HALFPI, 0.,
                    name + ' emission angle minus 90, observed (deg)',
                    operator='<', method='degrees')
        bpt.compare(emission + elevation, Scalar.HALFPI,
                    name + ' emission plus observer elevation (deg)',
                    limit=1.e-13, method='degrees')

        sunward = bp.ring_emission_angle(name, 'sunward')
        bpt.compare(sunward - generic, 0.,
                    name + ' emission angle, sunward minus generic (deg)',
                    limit=1.e-13, method='degrees')

        northward = bp.ring_emission_angle(name, 'north')
        bpt.gmtest(northward,
                   name + ' emission angle, north (deg)',
                   limit=0.01, radius=1, method='degrees')

        prograde = bp.ring_emission_angle(name, 'prograde')
        if planet in ('JUPITER', 'SATURN', 'NEPTUNE'):
            bpt.compare(northward - prograde, 0.,
                        name + ' emission angle, north minus prograde (deg)',
                        limit=1.e-13, method='degrees')
        elif planet == 'URANUS':
            bpt.compare(northward + prograde, Scalar.PI,
                        name + ' emission angle, north plus prograde (deg)',
                        limit=1.e-13, method='degrees')

        emission0 = bp.ring_emission_angle(name)
        emission1 = bp.ring_center_emission_angle(name)
        bpt.compare(emission0 - emission1, 0.,
                    name + ' emission angle, ring minus center (deg)',
                    limit=5., method='degrees')

    # Mode tests, Saturn only
    for (planet, name) in bpt.planet_ring_pairs:
        if planet != 'SATURN':
            continue

        test0 = bp.ring_radius(name, 70.e3, 100.e3)
        bpt.gmtest(test0,
                   name + ' radius, modeless, 70-100 km',
                   limit=0.1, radius=1)

        test1 = bp.radial_mode(test0.key, 40, 0., 1000., 0., 0., 100.e3)
        bpt.gmtest(test1, name + ' radius, mode 1, 70-100 kkm',
                   limit=0.1, radius=1)

        test2 = bp.radial_mode(test1.key, 40, 0., -1000., 0., 0., 100.e3)
        bpt.gmtest(test2, name + ' radius, mode 1 canceled, 70-100 kkm',
                   limit=0.1, radius=1)

        bpt.compare(test0, test2,
                    name + ' radius, modeless vs. mode 1 canceled (km)',
                    limit=0.1, radius=1)

        test3 = bp.radial_mode(test1.key, 25, 0., 500., 0., 0., 100.e3)
        bpt.gmtest(test3,
                   name + ' radius, modes 1 and 2, 70-100 kkm',
                   limit=0.1, radius=1)
        bpt.gmtest(bp.ring_longitude(test3.key, 'node'),
                   name + ' longitude, modes 1 and 2, 70-100 kkm (deg)',
                   limit=0.01, method='mod360', radius=1)

    # Derivative tests
    if bpt.derivs:
      (bp, bp_u0, bp_u1, bp_v0, bp_v1) = bpt.backplanes
      pixel_uv = np.abs(bp.obs.fov.uv_scale.vals)

      for name in bpt.ring_names:

        # Get approximate ring spatial scale in km/pixel and deg/pixel
        km_per_los_radian = bp.distance(name) / bp.mu(name)
        if np.all(km_per_los_radian.mask):
            continue

        km_per_pixel = km_per_los_radian.max() * pixel_uv
        (ulimit_km, vlimit_km) = km_per_pixel * 0.001

        deg_per_los_radian = km_per_los_radian / bp.ring_radius(name) * DPR
        deg_per_pixel = deg_per_los_radian.max() * pixel_uv
        (ulimit_deg, vlimit_deg) = deg_per_pixel * 0.001

        # ring_radius
        rad = bp.ring_radius(name)
        drad_duv = rad.d_dlos.chain(bp.dlos_duv)
        (drad_du, drad_dv) = drad_duv.extract_denoms()

        drad = bp_u1.ring_radius(name) - bp_u0.ring_radius(name)
        bpt.compare(drad.wod/bpt.duv, drad_du,
                    name + ' radius d/du self-check (km/pix)',
                    limit=ulimit_km, radius=1)

        drad = bp_v1.ring_radius(name) - bp_v0.ring_radius(name)
        bpt.compare(drad.wod/bpt.duv, drad_dv,
                    name + ' radius d/dv self-check (km/pix)',
                    limit=vlimit_km, radius=1)

        # ring_longitude
        lon = bp.ring_longitude(name)
        dlon_duv = lon.d_dlos.chain(bp.dlos_duv)
        (dlon_du, dlon_dv) = dlon_duv.extract_denoms()

        dlon = (bp_u1.ring_longitude(name) - bp_u0.ring_longitude(name)).abs()
        dlon = Scalar.PI - (dlon - Scalar.PI).abs()
        bpt.compare((dlon.wod/bpt.duv - dlon_du).abs().median(), 0.,
                    name + ' longitude d/du self-check (deg/pix)',
                    limit=ulimit_deg, method='degrees')

        dlon = (bp_v1.ring_longitude(name) - bp_v0.ring_longitude(name)).abs()
        dlon = Scalar.PI - (dlon.wod - Scalar.PI).abs()
        bpt.compare((dlon.wod/bpt.duv - dlon_dv).abs().median(), 0.,
                    name + ' longitude d/dv self-check (deg/pix)',
                    limit=vlimit_deg, method='degrees')

        # ring_azimuth
        az = bp.ring_azimuth(name)
        daz_duv = az.d_dlos.chain(bp.dlos_duv)
        (daz_du, daz_dv) = daz_duv.extract_denoms()

        daz = (bp_u1.ring_azimuth(name) - bp_u0.ring_azimuth(name)).abs()
        daz = Scalar.PI - (daz - Scalar.PI).abs()
        bpt.compare((daz.wod/bpt.duv - daz_du).abs().median(), 0.,
                    name + ' azimuth d/du self-check (deg/pix)',
                    limit=ulimit_deg, method='degrees')

        daz = (bp_v1.ring_azimuth(name) - bp_v0.ring_azimuth(name)).abs()
        daz = Scalar.PI - (daz - Scalar.PI).abs()
        bpt.compare((daz.wod/bpt.duv - daz_dv).abs().median(), 0.,
                    name + ' azimuth d/dv self-check (deg/pix)',
                    limit=vlimit_deg, method='degrees')

        # ring_elevation is tested by incidence and emission

register_test_suite('ring', ring_test_suite)

################################################################################
