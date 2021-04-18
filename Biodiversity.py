import math

def CalculateDistance(Lat1, Lon1, Lat2, Lon2):

    Lat1 = float(Lat1)
    Lon1 = float(Lon1)
    Lat2 = float(Lat2)
    Lon2 = float(Lon2)

    nDLat = (Lat1 - Lat2) * 0.017453293
    nDLon = (Lon1 - Lon2) * 0.017453293

    Lat1 = Lat1 * 0.017453293
    Lat2 = Lat2 * 0.017453293

    nA = (math.sin(nDLat/2) ** 2) + math.cos(Lat1) * math.cos(Lat2) * (math.sin(nDLon/2) ** 2 )
    nC = 2 * math.atan2(math.sqrt(nA),math.sqrt( 1 - nA ))
    nD = 6372.797 * nC

    return nD

def LineToList(Str):
    Str = Str.rstrip()
    return Str.split("\t")