import math as m


def get_distance(lat1, log1, lat2, log2) -> float:
    rad_log1 = m.radians(log1)
    rad_lat1 = m.radians(lat1)
    rad_log2 = m.radians(log2)
    rad_lat2 = m.radians(lat2)

    a = (m.sin((rad_lat2 - rad_lat1) / 2) ** 2) + m.cos(rad_lat1) * (
        m.cos(rad_lat2) * (m.sin((rad_log2 - rad_log1) / 2) ** 2)
    )

    c = 2 * m.atan2(m.sqrt(a), m.sqrt(1 - a))

    distance = float(6371000 * c)
    return distance


distance = get_distance(12.8608997, 74.8416703, 12.8635056, 74.8433197)
