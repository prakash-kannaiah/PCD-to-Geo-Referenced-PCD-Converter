import math

def calculate_angle(x1, y1, x2, y2, x3, y3, x4, y4):
    # Vector v1 = (x2 - x1, y2 - y1)
    v1x = x2 - x1
    v1y = y2 - y1

    # Vector v2 = (x4 - x3, y4 - y3)
    v2x = x4 - x3
    v2y = y4 - y3

    # Dot product of v1 and v2
    dot_product = v1x * v2x + v1y * v2y

    # Magnitudes of v1 and v2
    mag_v1 = math.sqrt(v1x**2 + v1y**2)
    mag_v2 = math.sqrt(v2x**2 + v2y**2)

    if mag_v1 == 0 or mag_v2 == 0:
        raise ValueError("One of the vectors has zero length.")

    # Cosine of angle
    cos_theta = dot_product / (mag_v1 * mag_v2)

    # Clamp value to avoid numerical issues
    cos_theta = max(min(cos_theta, 1), -1)

    # Angle in radians
    theta_rad = math.acos(cos_theta)

    # Convert to degrees
    theta_deg = math.degrees(theta_rad)

    return theta_deg

# Example input
x1, y1 = 1, 2
x2, y2 = 4, 6
x3, y3 = 1, 2
x4, y4 = 1, 0

angle = calculate_angle(x1, y1, x2, y2, x3, y3, x4, y4)
print(f"Angle between vectors: {angle:.2f} degrees")
