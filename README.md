
# PCD to Geo-Referenced PCD Converter

This program converts a local LiDAR point cloud (.pcd file) into a geo-referenced point cloud using:

- A known GPS starting and stopping position (latitude, longitude, altitude)
- A heading angle (rotation in degrees)

It does not require GNSS/IMU integration — only a .pcd file and basic GPS information. The program applies rotation and translation to align the point cloud with real-world geographic coordinates.

---

## 🧭 How It Works

1. Rotation: Rotates the point cloud around the Z-axis based on the heading angle.
2. Translation: Translates the rotated point cloud to the given GPS start location.

---

## 📁 Project Structure

```
├── main.py                 # Main Python script for PCD transformation
├── README.md               # This documentation file
├── requirements.txt        # Python dependencies
├── pointcloud_map.pcd      # Input point cloud file (user-provided)
└── output_transformed.pcd  # Output geo-referenced point cloud
```

---

## 📂 Input

- pointcloud_map.pcd : Local (non-referenced) point cloud file

---

## 📄 Output

- output_transformed.pcd : Geo-referenced PCD file after transformation

---

## 🔧 Requirements

Python 3.8 or higher.

Install required libraries with:

```
pip install -r requirements.txt
```

Dependencies:
- open3d
- numpy

---

## ▶️ Run the Program

### Step 1: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 2: Prepare Your Input File

- Make sure your point cloud file is named:
  pointcloud_map.pcd
- Place it in the same directory as main.py.

- Open main.py and update these values if needed:

```
tx = 42055.5884  # GPS latitude
ty = 41385.663   # GPS longitude
tz = 0           # GPS altitude
rz = -121.7      # Heading angle in degrees
```

---

### Step 3: Run the Script

```
python main.py
```

---

### Step 4: View and Save Output

- A 3D viewer will appear to show the transformed point cloud.
- To close the viewer and terminate the program, press **q** in the viewer window.
- A new file will be saved as:

  output_transformed.pcd

- Terminal output:

  Transformed point cloud saved as 'output_transformed.pcd'.

---

## 💡 Use Cases

- Outdoor LiDAR mapping
- GIS-ready transformation of point clouds
- Field robotics and AV research
- Preprocessing for SLAM or localization pipelines

---

## 👨‍💻 Author

Prakash Kannaiah  
LinkedIn: https://www.linkedin.com/in/prakash-kannaiah

