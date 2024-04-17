################################################################################
# oops/observation/all.py
################################################################################

# Import the Observation class and all its subclasses into a common name space

from oops.observation              import Observation
from oops.observation.insitu       import InSitu
from oops.observation.pixel        import Pixel
from oops.observation.pushbroom    import Pushbroom     # replaced by TimedImage
from oops.observation.pushframe    import Pushframe     # replaced by TimedImage
from oops.observation.rasterscan   import RasterScan    # replaced by TimedImage
from oops.observation.rasterslit   import RasterSlit    # replaced by TimedImage
from oops.observation.rasterslit1d import RasterSlit1D
from oops.observation.slit         import Slit          # replaced by TimedImage
from oops.observation.slit1d       import Slit1D
from oops.observation.snapshot     import Snapshot
from oops.observation.timedimage   import TimedImage

################################################################################
