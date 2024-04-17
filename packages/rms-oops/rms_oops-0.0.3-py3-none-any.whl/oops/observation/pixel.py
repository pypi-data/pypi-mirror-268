################################################################################
# oops/observation/pixel.py: Subclass Pixel of class Observation
################################################################################

import numpy as np
from polymath import Scalar, Pair, Vector3

from oops.observation import Observation
from oops.cadence     import Cadence
from oops.event       import Event
from oops.frame       import Frame
from oops.path        import Path

class Pixel(Observation):
    """A subclass of Observation consisting of one or more measurements obtained
    from a single rectangular pixel.

    Generalization to other FOV shapes is TODO.
    """

    #===========================================================================
    def __init__(self, axes, cadence, fov, path, frame, **subfields):
        """Constructor for a Pixel observation.

        Input:
            axes        a list or tuple of strings, with one value for each axis
                        in the associated data array. A value of 't' should
                        appear at the location of the array's time-axis.

            cadence     a 1-D Cadence object defining the start time and
                        duration of each consecutive measurement. Note that it
                        also defines the number of measurements.
=
            fov         a FOV (field-of-view) object, which describes the field
                        of view including any spatial distortion. It maps
                        between spatial coordinates (u,v) and instrument
                        coordinates (x,y). For a Pixel object, both axes of the
                        FOV must have length 1.

            path        the path waypoint co-located with the instrument.

            frame       the wayframe of a coordinate frame fixed to the optics
                        of the instrument. This frame should have its Z-axis
                        pointing outward near the center of the line of sight,
                        with the X-axis pointing rightward and the y-axis
                        pointing downward.

            subfields   a dictionary containing all of the optional attributes.
                        Additional subfields may be included as needed.
        """

        # Basic properties
        self.path = Path.as_waypoint(path)
        self.frame = Frame.as_wayframe(frame)

        # FOV
        self.fov = fov
        if self.fov.uv_shape != (1,1):
          raise ValueError('Pixel observation FOV must have shape (1,1)')

        self.uv_shape = (1,1)

        # Axes
        self.axes = list(axes)
        self.u_axis = -1
        self.v_axis = -1
        self.swap_uv = False
        if 't' in self.axes:
            self.t_axis = self.axes.index('t')
        else:
            self.t_axis = -1

        # Cadence
        self.cadence = cadence
        if len(self.cadence.shape) != 1:
            raise ValueError('Pixel observation requires a 1-D cadence')

        samples = self.cadence.shape[0]

        # Shape / Size
        shape_list = len(axes) * [0]
        if self.t_axis >= 0:
            shape_list[self.t_axis] = samples
        self.shape = tuple(shape_list)

        # Timing
        self.time = self.cadence.time
        self.midtime = self.cadence.midtime
        self._scalar_time = (Scalar(self.time[0]), Scalar(self.time[1]))
        self._scalar_midtime = Scalar(self.cadence.midtime)

        # Optional subfields
        self.subfields = {}
        for key in subfields.keys():
            self.insert_subfield(key, subfields[key])

    def __getstate__(self):
        return (self.axes, self.cadence, self.fov, self.path, self.frame,
                self.subfields)

    def __setstate__(self, state):
        self.__init__(*state[:-1], **state[-1])

    #===========================================================================
    def uvt(self, indices, remask=False, derivs=True):
        """Coordinates (u,v) and time t for indices into the data array.

        This method supports non-integer index values.

        Input:
            indices     a Scalar or Vector of array indices.
            remask      True to mask values outside the field of view.
            derivs      True to include derivatives in the returned values.

        Return:         (uv, time)
            uv          a Pair defining the values of (u,v) within the FOV that
                        are associated with the array indices.
            time        a Scalar defining the time in seconds TDB associated
                        with the array indices.
        """

        # Works for a 1-D index or a multi-D index
        tstep = Observation.scalar_from_indices(indices, self.t_axis,
                                                derivs=derivs)

        if tstep is None:       # if t_axis < 0
            uv = Pair.filled(indices.shape, 0.5)
            return (uv, self._scalar_midtime)

        time = self.cadence.time_at_tstep(tstep, remask=remask)
        uv = Pair.filled(time.shape, 0.5, mask=time.mask)
        return (uv, time)

    #===========================================================================
    def uvt_range(self, indices, remask=False):
        """Ranges of (u,v) spatial coordinates and time for integer array
        indices.

        Input:
            indices     a Vector of array indices.
            remask      True to mask values outside the field of view.

        Return:         (uv_min, uv_max, time_min, time_max)
            uv_min      a Pair defining the minimum values of (u,v) associated
                        the pixel.
            uv_max      a Pair defining the maximum values of (u,v).
            time_min    a Scalar defining the minimum time associated with the
                        pixel. It is given in seconds TDB.
            time_max    a Scalar defining the maximum time value.
        """

        if self.t_axis < 0:
            return (Pair.INT00, self.fov.uv_shape) + self._scalar_time

        # Works for a 1-D index or a multi-D index
        tstep = Observation.scalar_from_indices(indices, self.t_axis)
        (time_min,
         time_max) = self.cadence.time_range_at_tstep(tstep, remask=remask)

        # uv pair
        uv_min = Pair.zeros(indices.shape, dtype='int', mask=time_min.mask)

        return (uv_min, uv_min + self.fov.uv_shape, time_min, time_max)

    #===========================================================================
    def time_range_at_uv(self, uv_pair, remask=False):
        """The start and stop times of the specified spatial pixel (u,v).

        The Pixel observation subclass has no spatial axes, so the inputs here
        are generally ignored, although they are expected to fall between 0 and
        1 inclusive.

        Input:
            uv_pair     a Pair of spatial (u,v) data array coordinates,
                        truncated to integers if necessary.
            remask      True to mask values outside the field of view.

        Return:         a tuple containing Scalars of the start time and stop
                        time of each (u,v) pair, as seconds TDB.
        """

        return self.time_range_at_uv_0d(uv_pair, remask=remask)

    #===========================================================================
    def uv_range_at_time(self, time, remask=False):
        """The (u,v) range of spatial pixels observed at the specified time.

        For the Pixel observation subclass, the (u,v) ranges are always (0,1).
        The time is largely ignored, although it is expected to fall within the
        time limits of the observation and will be masked if remask == True.

        Input:
            time        a Scalar of time values in seconds TDB.
            remask      True to mask values outside the time limits.

        Return:         (uv_min, uv_max)
            uv_min      the lower (u,v) corner Pair of the area observed at the
                        specified time.
            uv_max      the upper (u,v) corner Pair of the area observed at the
                        specified time.
        """

        return Observation.uv_range_at_time_0d(self, time,
                                               uv_shape=self.uv_shape,
                                               remask=remask)

    #===========================================================================
    def time_shift(self, dtime):
        """A copy of the observation object with a time-shift.

        Input:
            dtime       the time offset to apply to the observation, in units of
                        seconds. A positive value shifts the observation later.

        Return:         a (shallow) copy of the object with a new time.
        """

        obs = Pixel(axes=self.axes, cadence=self.cadence.time_shift(dtime),
                    fov=self.fov, path=self.path, frame=self.frame)

        for key in self.subfields.keys():
            obs.insert_subfield(key, self.subfields[key])

        return obs

    ############################################################################
    # Overrides of Observation class methods
    ############################################################################

    def event_at_grid(self, meshgrid, tfrac=0.5, time=None):
        """An event object describing the arrival of a photon at a set of
        locations defined by the given meshgrid. This version overrides the
        default definition to apply the timing for each pixel of a time-sequence
        by default.

        Input:
            meshgrid    a Meshgrid object describing the sampling of the field
                        of view.
            tfrac       Scalar of fractional times during the exposure, where
                        tfrac=0 at the beginning and 1 at the end. Default is
                        0.5.
            time        optional Scalar of absolute time in seconds. Only one of
                        tfrac and time can be specified.

        Return:         the corresponding event.
        """

        if time is None:
            tstep = np.arange(self.cadence.shape[0]) + tfrac
            time = self.cadence.time_at_tstep(tstep)
            time = time.append_axes(len(meshgrid.shape))

        event = Event(time, Vector3.ZERO, self.path, self.frame)

        # Insert the arrival directions
        event.neg_arr_ap = meshgrid.los

        return event

    #===========================================================================
    def gridless_event(self, meshgrid, tfrac=0.5, time=None,
                             shapeless=False):
        """An event object describing the arrival of a photon at a set of locations
        defined by the given meshgrid. This version overrides the default
        definition to apply the timing for each pixel of a time-sequence by
        default.

        Input:
            meshgrid    a Meshgrid object describing the sampling of the field
                        of view.
            tfrac       Scalar of fractional times during the exposure, where
                        tfrac=0 at the beginning and 1 at the end. Default is
                        0.5.
            time        optional Scalar of absolute time in seconds. Only one of
                        tfrac and time can be specified; the other must be None.
            shapeless   True to return a shapeless event, referring to the mean
                        of all the times.

        Return:         the corresponding event.
        """

        if tfrac is not None:
            if time is not None:
                raise ValueError('tfrac and time cannot both be defined')

            tstep = np.arange(self.cadence.shape[0]) + tfrac
            time = self.cadence.time_at_tstep(tstep)
            time = time.append_axes(len(meshgrid.shape))

        if shapeless:
            time = time.mean()

        event = Event(time, Vector3.ZERO, self.path, self.frame)

        return event

################################################################################
# UNIT TESTS
################################################################################

import unittest

class Test_Pixel(unittest.TestCase):

    def runTest(self):

        from oops.cadence.metronome import Metronome
        from oops.fov.flatfov import FlatFOV

        fov = FlatFOV((0.001,0.001), (1,1))
        cadence = Metronome(tstart=0., tstride=10., texp=10., steps=20)
        obs = Pixel(axes=('t'),
                    cadence=cadence, fov=fov, path='SSB', frame='J2000')

        indices = Scalar([(0,),(1,),(20,),(21,)])
        indices_ = indices.copy()
        indices_.vals[indices_.vals == 20] -= 1         # clip the top

        # uvt() with remask == False
        (uv, time) = obs.uvt(indices)

        self.assertFalse(np.any(uv.mask))
        self.assertFalse(np.any(time.mask))
        self.assertEqual(time, cadence.time_at_tstep(indices))
        self.assertEqual(uv, (0.5,0.5))

        # uvt() with remask == True
        (uv, time) = obs.uvt(indices, remask=True)

        self.assertTrue(np.all(uv.mask == np.array([3*[[False]] + [[True]]])))
        self.assertTrue(np.all(time.mask == uv.mask))
        self.assertEqual(time[:3], cadence.tstride * indices[:3])
        self.assertEqual(uv[:3], (0.5,0.5))

        # uvt_range() with remask == False
        (uv_min, uv_max, time_min, time_max) = obs.uvt_range(indices)

        self.assertFalse(np.any(uv_min.mask))
        self.assertFalse(np.any(uv_max.mask))
        self.assertFalse(np.any(time_min.mask))
        self.assertFalse(np.any(time_max.mask))

        self.assertEqual(uv_min, (0,0))
        self.assertEqual(uv_max, (1,1))

        self.assertEqual(time_min, cadence.time_range_at_tstep(indices_)[0])
        self.assertEqual(time_max, time_min + cadence.texp)

        # uvt_range() with remask == False, new indices
        non_ints = indices + 0.2
        (uv_min, uv_max, time_min, time_max) = obs.uvt_range(non_ints)

        self.assertFalse(np.any(uv_min.mask))
        self.assertFalse(np.any(uv_max.mask))
        self.assertFalse(np.any(time_min.mask))
        self.assertFalse(np.any(time_max.mask))

        self.assertEqual(uv_min, (0,0))
        self.assertEqual(uv_max, (1,1))

        self.assertEqual(time_min, cadence.time_range_at_tstep(non_ints)[0])
        self.assertEqual(time_max, time_min + cadence.texp)

        # uvt_range() with remask == True, new indices
        non_ints = indices + 0.2
        (uv_min, uv_max, time_min, time_max) = obs.uvt_range(non_ints, remask=True)

        self.assertTrue(np.all(uv_min.mask == np.array(2*[[False]] + 2*[[True]])))
        self.assertTrue(np.all(uv_max.mask == uv_min.mask))
        self.assertTrue(np.all(time_min.mask == uv_min.mask))
        self.assertTrue(np.all(time_max.mask == uv_min.mask))

        self.assertEqual(uv_min[:2], (0,0))
        self.assertEqual(uv_max[:2], (1,1))
        self.assertEqual(time_min[:2], indices[:2] * cadence.tstride)
        self.assertEqual(time_max[:2], time_min[:2] + cadence.texp)

        # time_range_at_uv() with remask == False
        uv = Pair([(0,0),(0,1),(1,0),(1,1),(1,2)])

        (time0, time1) = obs.time_range_at_uv(uv)

        self.assertEqual(time0, obs.time[0])
        self.assertEqual(time1, obs.time[1])

        # time_range_at_uv() with remask == True
        (time0, time1) = obs.time_range_at_uv(uv, remask=True)

        self.assertTrue(np.all(time0.mask == 4*[False] + [True]))
        self.assertTrue(np.all(time1.mask == time0.mask))
        self.assertEqual(time0[:4], obs.time[0])
        self.assertEqual(time1[:4], obs.time[1])

        ####################################

        # Alternative axis order ('a','t')

        fov = FlatFOV((0.001,0.001), (1,1))
        cadence = Metronome(tstart=0., tstride=10., texp=10., steps=20)
        obs = Pixel(axes=('a','t'),
                    cadence=cadence, fov=fov, path='SSB', frame='J2000')

        indices = Pair([(0,0),(1,1),(0,20,),(1,21)])
        indices_ = indices.copy()
        indices_.vals[indices_.vals == 20] -= 1         # clip the top

        # uvt() with remask == False
        (uv,time) = obs.uvt(indices)

        self.assertFalse(uv.mask)
        self.assertFalse(np.any(time.mask))
        self.assertEqual(time.without_mask(),
                         cadence.time_at_tstep(indices.to_scalar(1)))
        self.assertEqual(uv, (0.5,0.5))

        # uvt() with remask == True
        (uv,time) = obs.uvt(indices, remask=True)

        self.assertTrue(np.all(uv.mask == np.array(3*[False] + [True])))
        self.assertTrue(np.all(time.mask == uv.mask))
        self.assertEqual(time[:3], cadence.tstride * indices[:3].to_scalar(1))
        self.assertEqual(uv[:3], (0.5,0.5))

        # uvt_range() with remask == False
        (uv_min, uv_max, time_min, time_max) = obs.uvt_range(indices)

        self.assertFalse(uv_min.mask)
        self.assertFalse(uv_max.mask)
        self.assertFalse(time_min.mask)
        self.assertFalse(time_max.mask)

        self.assertEqual(uv_min, (0,0))
        self.assertEqual(uv_max, (1,1))

        self.assertEqual(time_min, cadence.time_range_at_tstep(indices.to_scalar(1))[0])
        self.assertEqual(time_max, time_min + cadence.texp)

        # uvt_range() with remask == False, new indices
        non_ints = indices + (0.2,0.9)
        (uv_min, uv_max, time_min, time_max) = obs.uvt_range(non_ints)

        self.assertFalse(uv_min.mask)
        self.assertFalse(uv_max.mask)
        self.assertFalse(time_min.mask)
        self.assertFalse(time_max.mask)

        self.assertEqual(uv_min, (0,0))
        self.assertEqual(uv_max, (1,1))

        self.assertEqual(time_min, cadence.time_range_at_tstep(indices.to_scalar(1))[0])
        self.assertEqual(time_max, time_min + cadence.texp)

        # uvt_range() with remask == True, new indices
        non_ints = indices + (0.2,0.2)
        (uv_min, uv_max, time_min,
                         time_max) = obs.uvt_range(non_ints, remask=True)

        self.assertTrue(np.all(uv_min.mask == np.array(2*[False] + 2*[True])))
        self.assertTrue(np.all(uv_max.mask == uv_min.mask))
        self.assertTrue(np.all(time_min.mask == uv_min.mask))
        self.assertTrue(np.all(time_max.mask == uv_min.mask))

        self.assertEqual(uv_min[:2], (0,0))
        self.assertEqual(uv_max[:2], (1,1))
        self.assertEqual(uv_min[2:], Pair.MASKED)
        self.assertEqual(uv_max[2:], Pair.MASKED)

        self.assertEqual(time_min[:2], indices.to_scalar(1)[:2] * cadence.tstride)
        self.assertEqual(time_max[:2], time_min[:2] + cadence.texp)

        # time_range_at_uv() with remask == False
        uv = Pair([(0,0),(0,1),(1,0),(1,1),(1,2)])

        (time0, time1) = obs.time_range_at_uv(uv)
        self.assertEqual(time0, obs.time[0])
        self.assertEqual(time1, obs.time[1])

        # time_range_at_uv() with remask == True
        (time0, time1) = obs.time_range_at_uv(uv, remask=True)

        self.assertTrue(np.all(time0.mask == 4*[False] + [True]))
        self.assertTrue(np.all(time1.mask == time0.mask))
        self.assertEqual(time0[:4], obs.time[0])
        self.assertEqual(time1[:4], obs.time[1])

########################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
################################################################################
