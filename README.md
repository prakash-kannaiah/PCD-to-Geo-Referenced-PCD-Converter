# PCD to Geo-Referenced PCD Converter

This tool converts a **local LiDAR point cloud (PCD file)** into a **geo-referenced point cloud** using:
- A known GPS starting position (latitude, longitude, altitude)
- A heading angle (in degrees)

It only uses LiDAR and two GPS positions (start and stop) to anchor the point cloud globally.

---

## 🧭 How It Works

1. **Rotation**: The point cloud is rotated around the Z-axis using the heading (yaw) angle to match the global orientation.
2. **Translation**: The point cloud is then translated to the given GPS starting location.

---

## 📁 Input

- `pointcloud_map.pcd`: Raw local PCD file.

## 📄 Output

- `output_transformed.pcd`: Transformed, geo-referenced PCD file.

---

## 🔧 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
