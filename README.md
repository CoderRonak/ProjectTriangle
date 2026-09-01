# Triangle Solver 🔺

A comprehensive Python CLI application for computing and analyzing the properties of triangles using multiple input methods.

## Features

- **Flexible Input Methods**
  - Three sides (SSS)
  - Two sides + included angle (SAS)
  - One side + two angles (AAS)
  - 2D or 3D coordinates of vertices

- **Comprehensive Triangle Analysis**
  - Triangle classification (angle type & side type)
  - Perimeter and area calculation
  - All three angles (in degrees)
  - Inradius and circumradius
  - Medians and altitudes
  - Display all properties at once

- **Robust Validation**
  - Input validation for sides and angles
  - Triangle inequality check
  - Collinearity detection for coordinate input
  - Floating-point precision handling
  - Custom error messages

## Requirements

- Python 3.12+
- Standard library only (no external dependencies)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CoderRonak/ProjectTriangle.git
cd ProjectTriangle
```

2. Switch to the v1 branch:
```bash
git checkout v1
```

3. (Optional) Install dependencies using uv:
```bash
uv sync
```

## Usage

Run the application:
```bash
cd project
python main.py
```

### Interactive Menu

1. **Select Input Type**
   - Enter `1` for three sides (SSS)
   - Enter `2` for two sides + included angle (SAS)
   - Enter `3` for one side + two angles (AAS)
   - Enter `4` for 2D/3D coordinates
   - Enter `5` to exit

2. **Select Output**
   - View triangle type classification
   - Calculate perimeter or area
   - Display all angles
   - Calculate inradius/circumradius
   - Display medians or altitudes
   - View all properties at once

### Example Usage

#### Using Three Sides
```
Select Input Type → 1
Enter side 1: 3
Enter side 2: 4
Enter side 3: 5

Select Output → 9
Triangle Type      : right & scalene
Perimeter          : 12.00 units
Area               : 6.00 sq. units
Angles (deg)       : 36.87, 53.13, 90.00
Inradius           : 1.00 units
Circumradius       : 2.50 units
Medians            : 3.61, 4.27, 5.00 units
Altitudes          : 2.40, 3.00, 4.00 units
```

#### Using 2D Coordinates
```
Select Input Type → 4
Enter point 1: 0,0
Enter point 2: 3,0
Enter point 3: 0,4

Result: A 3-4-5 right triangle is calculated
```

## Project Structure

```
project/
├── main.py              # Main application loop
├── compute.py           # Triangle class & calculations
├── input_handle.py      # Input collection & validation
├── convert.py           # Convert between input formats
├── output.py            # CLI presentation & formatting
└── error_handling.py    # Custom exceptions & validation
```

## Mathematical Methods

- **Area**: Heron's formula
- **Angles**: Law of cosines
- **Inradius**: Area / semi-perimeter
- **Circumradius**: (a × b × c) / (4 × Area)
- **Medians**: Using median length formula
- **Altitudes**: 2 × Area / base
- **Coordinate Conversion**: Distance formula (2D & 3D)

## Error Handling

The application gracefully handles:
- Invalid numeric inputs
- Non-positive values
- Invalid angles (≥ 180°)
- Triangle inequality violations
- Collinear points (2D)
- Floating-point precision issues

## Author

**Ronak** - [CoderRonak](https://github.com/CoderRonak)

## License

This project is open source and available for educational use.
