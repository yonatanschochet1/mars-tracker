from astropy.coordinates import get_body, EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt

#observer location (Tel Aviv as example)
location = EarthLocation(lat=32.0853*u.deg, lon=34.7818*u.deg, height=0*u.m)
#Time range in next 48 hours
times = Time.now() + np.linspace(0, 2, 100)*u.day

#Mars
mars_altitudes = []

for t in times:
    mars = get_body("mars", t, location)
    altaz = mars.transform_to(AltAz(obstime=t, location = location))
    mars_altitudes.append(altaz.alt.degree)

#Plot
plt.figure()
plt.plot(times.datetime, mars_altitudes)
plt.xlabel("Time")
plt.ylabel("Altitude (Degrees)")
plt.title("Mars Altitude Over Time")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/mars_altitude.png")
plt.show()