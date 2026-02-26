# 16-Folium Plot Branch
## Interactive Geographic Visualization of Immigration Patterns with Folium

This branch demonstrates **interactive map visualizations** using Folium to explore immigration patterns and geographic data, progressively enhancing map features from basic world views to specialized terrain representations of different regions.

---

## Progressive Enhancement Sequence

The branch showcases step-by-step improvements to interactive maps, with each iteration building upon the previous to create more sophisticated and targeted geographic visualizations:

### Plot 1: Basic World Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/0e8508ec-1128-44ac-b72c-6ebfa71b642e" />

**Map Configuration:**
```python
world_map = folium.Map()
```

**Visual Characteristics:**
- Default OpenStreetMap tile layer
- Global view centered at coordinates [0, 0]
- Zoom level 1 (world view)
- Basic interactive controls enabled
- Standard map styling with roads, labels, and terrain features
- Full pan and zoom functionality

---

### Plot 2: Canada-Centered World Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/17a234fa-661f-4696-8857-9671a77d7920" />

**Map Configuration:**
```python
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
```

**Visual Characteristics:**
- **Center Coordinates**: [56.130, -106.35] (central Canada)
- **Zoom Level**: 4 (regional view)
- North America prominently displayed
- Canada positioned at map center
- United States and Mexico visible in frame
- Default OpenStreetMap base layer maintained

**File Output**: `Canada_map.html`

---

### Plot 3: Higher Zoom Canada Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9a420b5a-f0c3-4a1a-b9ab-b7b9d02d49b7" />

**Map Configuration:**
```python
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)
```

**Visual Characteristics:**
- **Zoom Level**: 8 (detailed regional view)
- Greater detail of Canadian geography
- Provincial boundaries more visible
- Cities and towns appear with labels
- Major highway networks displayed
- Topographic features more pronounced

**File Output**: `world_map_higher_zoom.html`

---

### Plot 4: Mexico-Centered Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/0b8b8300-3267-41b5-8f45-112a71f6d05a" />

**Map Configuration:**
```python
mexico_latitude = 23.6345
mexico_longitude = -102.5528
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
```

**Visual Characteristics:**
- **Center Coordinates**: [23.6345, -102.5528] (central Mexico)
- **Zoom Level**: 4 (country view)
- Mexico positioned at map center
- Gulf of Mexico visible to the east
- Pacific Ocean visible to the west
- Southern United States border shown
- Central American countries partially visible

**File Output**: `Mexico_map.html`

---

### Plot 5: Toner Style World Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/917a9e00-cc7f-4a27-b8c6-2765b2f487c8" />

**Map Configuration:**
```python
world_map = folium.Map(
    location=[56.130, -106.35], 
    zoom_start=4, 
    tiles="CartoDB positron"
)
```

**Visual Characteristics:**
- **Tile Style**: CartoDB Positron (light toner)
- High-contrast monochromatic design
- Minimalist aesthetic with light backgrounds
- Dark text and road networks on light base
- Reduced visual clutter for data overlays
- Professional presentation appearance
- Excellent base layer for custom markers

**File Output**: `Toner_map.html`

---

### Plot 6: Terrain Style World Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/9ed7828f-637a-4340-b010-2c2b61bf6c6a" />

**Map Configuration:**
```python
world_map = folium.Map(
    location=[56.130, -106.35], 
    zoom_start=4, 
    tiles="CartoDB voyager"
)
```

**Visual Characteristics:**
- **Tile Style**: CartoDB Voyager (terrain)
- Enhanced topographic representation
- Green shading for lowland areas
- Brown/tan coloring for mountainous regions
- Blue water bodies with depth indication
- Road networks in muted colors
- Labels with improved readability
- Natural feature emphasis

**File Output**: `Terrain_map.html`

---

### Plot 7: Mexico Terrain Map
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/cfec5898-cad4-4d7b-af42-5d037de239ac" />

**Map Configuration:**
```python
mexico_latitude = 23.6345
mexico_longitude = -102.5528
mexico_map = folium.Map(
    location=[mexico_latitude, mexico_longitude], 
    zoom_start=6, 
    tiles='CartoDB voyager'
)
```

**Visual Characteristics:**
- **Center Coordinates**: [23.6345, -102.5528] (central Mexico)
- **Zoom Level**: 6 (detailed country view)
- **Tile Style**: CartoDB Voyager (terrain)
- **Mexican Topography Displayed:**
  - Sierra Madre Oriental mountain range
  - Sierra Madre Occidental mountain range
  - Central Mexican Plateau
  - Gulf of Mexico coastal plains
  - Pacific coastal regions
  - Baja California peninsula
  - Yucatán Peninsula lowlands
- Major cities labeled (Mexico City, Guadalajara, Monterrey)
- State boundaries visible
- Detailed hydrography (rivers, lakes, reservoirs)

**File Output**: `mexico_Terrain_map_.html`

---

## Folium Map Components

### Core Elements
```python
import folium

# Basic map creation
map_object = folium.Map(
    location=[latitude, longitude],  # Center coordinates [lat, lon]
    zoom_start=zoom_level,           # Initial zoom (1=world, 18=street)
    tiles=tile_style,                 # Base map style
    control_scale=True                 # Show scale bar
)
```

**Component Breakdown:**

| Component | Description | Options |
|-----------|-------------|---------|
| **Location** | Center point coordinates | [latitude, longitude] in decimal degrees |
| **Zoom Start** | Initial zoom level | 1 (world) to 18 (street level) |
| **Tiles** | Base map styling | OpenStreetMap, CartoDB positron, CartoDB voyager, Stamen Terrain, Stamen Toner |
| **Control Scale** | Show/hide scale bar | True/False |
| **Zoom Control** | Enable/disable zoom buttons | True/False |
| **Prefer Canvas** | Rendering method | True/False |

---

## Tile Style Comparison

### Available Base Maps

| Tile Style | Provider | Visual Characteristics | Best Use Case |
|------------|----------|------------------------|---------------|
| **OpenStreetMap** | OpenStreetMap | Standard map with roads, labels, POIs | General purpose |
| **CartoDB Positron** | CartoDB | Light, minimal, high contrast | Data overlays, printing |
| **CartoDB Voyager** | CartoDB | Terrain-enhanced with natural features | Topographic visualization |
| **Stamen Terrain** | Stamen | Hill shading and natural colors | Outdoor recreation |
| **Stamen Toner** | Stamen | Black and white high contrast | Night mode, overlays |

### Style Characteristics

| Feature | OpenStreetMap | Positron | Voyager |
|---------|---------------|----------|---------|
| **Background** | Light gray | White | Variable by terrain |
| **Roads** | Yellow/muted | Gray | Muted gray |
| **Water** | Blue | Light blue | Blue with depth |
| **Forests** | Green | Not shown | Green shading |
| **Mountains** | Contour lines | Not shown | Brown shading |
| **Labels** | Black | Dark gray | Dark gray |
| **Contrast** | Medium | High | Medium |

---

## Geographic Coordinates Reference

### Key Locations in North America

| Location | Latitude | Longitude | Description |
|----------|----------|-----------|-------------|
| **Canada (central)** | 56.130 | -106.35 | Geographic center approximation |
| **Mexico (central)** | 23.6345 | -102.5528 | Geographic center approximation |
| **United States (central)** | 39.8283 | -98.5795 | Geographic center (Belle Fourche, SD) |
| **Toronto, Canada** | 43.6532 | -79.3832 | Largest Canadian city |
| **Mexico City, Mexico** | 19.4326 | -99.1332 | Capital of Mexico |
| **Vancouver, Canada** | 49.2827 | -123.1207 | Major Pacific port |
| **Cancún, Mexico** | 21.1619 | -86.8515 | Caribbean tourism hub |

### Zoom Level Reference

| Zoom Level | View Scale | Visible Area | Use Case |
|------------|------------|--------------|----------|
| **1** | Global | Entire world | World overview |
| **4** | Continental | North America | Regional context |
| **6** | Country | Mexico or Canada | Country analysis |
| **8** | Regional | Provinces/States | Regional detail |
| **10** | City | Major metropolitan | Urban analysis |
| **12** | District | City neighborhoods | Local context |

---

## Progressive Enhancement Philosophy

### Step-by-Step Map Development

1. **Plot 1: Basic Foundation**
   - Start with simplest possible map
   - Default settings, global view
   - Establish baseline functionality

2. **Plot 2: Geographic Targeting**
   - Center on specific region (Canada)
   - Adjust zoom for regional context
   - Begin geographic focus

3. **Plot 3: Detail Enhancement**
   - Increase zoom level
   - Reveal more geographic features
   - Show regional complexity

4. **Plot 4: Alternative Region**
   - Shift focus to Mexico
   - Maintain consistent zoom
   - Compare different geographies

5. **Plot 5: Style Variation - Toner**
   - Change base map styling
   - Explore minimalist aesthetic
   - Prepare for data overlays

6. **Plot 6: Style Variation - Terrain**
   - Enhance with topographic features
   - Show natural geography
   - Emphasize physical landscape

7. **Plot 7: Combined Optimization**
   - Target specific region (Mexico)
   - Optimal zoom for detail (6)
   - Terrain styling for context
   - Maximum geographic information

---

## Geographic Insights by Region

### Canada (Plots 2-3)

**Physical Geography:**
- Vast northern territories
- Rocky Mountains in the west
- Great Lakes in the southeast
- Hudson Bay lowlands
- Arctic archipelago

**Political Boundaries:**
- 10 provinces and 3 territories
- US border along 49th parallel
- Maritime provinces in the east
- Pacific coast in British Columbia

### Mexico (Plots 4, 7)

**Physical Geography:**
- **Sierra Madre Oriental**: Eastern mountain range
- **Sierra Madre Occidental**: Western mountain range
- **Mexican Plateau**: High central plain
- **Baja California**: Long peninsula in the west
- **Yucatán Peninsula**: Flat limestone lowlands
- **Trans-Mexican Volcanic Belt**: Active volcanoes including Popocatépetl

**Topographic Features at Zoom 6:**
- Mountain ranges clearly delineated
- Plateau elevation visible
- Coastal plain width distinguishable
- Peninsula formations recognizable
- Isthmus of Tehuantepec visible
- Gulf of California (Sea of Cortés) clearly shown

---

## File Structure

```
16-folium-plot/
├── README.md
├── folium-plot.py                          # Main visualization script with all 7 maps
├── Canada.xlsx                              # Primary immigration dataset (reference)
├── outputs/
│   ├── 01-world-map.html                     # Plot 1 - Basic world map
│   ├── 02-canada-map.html                     # Plot 2 - Canada-centered map
│   ├── 03-canada-higher-zoom.html              # Plot 3 - Higher zoom Canada map
│   ├── 04-mexico-map.html                       # Plot 4 - Mexico-centered map
│   ├── 05-toner-map.html                         # Plot 5 - Toner style world map
│   ├── 06-terrain-map.html                        # Plot 6 - Terrain style world map
│   └── 07-mexico-terrain-map.html                  # Plot 7 - Mexico terrain map
├── data/
│   ├── canada-coordinates.csv                      # Canadian cities and landmarks
│   ├── mexico-coordinates.csv                       # Mexican cities and landmarks
│   ├── north-america-bounds.csv                      # Continental bounding boxes
│   ├── topographic-features.csv                       # Mountain ranges, plateaus
│   ├── water-bodies.csv                                # Lakes, rivers, oceans
│   ├── zoom-level-reference.txt                         # Zoom level guide
│   └── tile-style-comparison.md                         # Base map style guide
└── requirements.txt                                   # folium, pandas, etc.
```
