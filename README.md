# 17-Maps with Markers
## Interactive Crime Incident Visualization in San Francisco with Folium Markers and Clustering

This branch demonstrates **interactive crime mapping techniques** using Folium to visualize San Francisco Police Department incident data, progressively enhancing visualizations from basic markers to sophisticated clustered representations with multiple zoom levels.

---

## Progressive Enhancement Sequence

### Plot 1: Base Map of San Francisco
<img width="800" height="600" alt="1" src="https://github.com/user-attachments/assets/4d81b595-52ca-48be-8f15-d48b69d44ece" />

**Visual Characteristics:**
- **Center Coordinates**: [37.77, -122.42] (downtown San Francisco)
- **Zoom Level**: 12 (city district level)
- **Visible Areas**: San Francisco Bay, Golden Gate Bridge, Bay Bridge, Alcatraz, Oakland, Berkeley
- **Neighborhoods Visible**: Presidio, Richmond District, Downtown, Tenderloin, Civic Center, Embarcadero, Financial District, Mission District, Bernal Heights, Sunset District, Golden Gate Park

**File Output**: `sanfran_map.html`

---

### Plot 2: Crime Incident Markers (Basic)
<img width="800" height="600" alt="2" src="https://github.com/user-attachments/assets/9cad0957-4549-4f99-932d-d3aaa3484656" />

**Visual Characteristics:**
- **100 red circle markers** (7.5px radius, black border)
- First 100 crime incidents from dataset
- Natural visual clustering begins to emerge
- High-density areas show marker overlap

**File Output**: `sanfran_crimes_map.html`

---

### Plot 3: Crime Incident Markers with Pop-up Labels
<img width="800" height="600" alt="3" src="https://github.com/user-attachments/assets/381ec44b-4bb6-4d96-9894-c45f47a6af2f" />

**Visual Characteristics:**
- **Red exclamation icon markers**
- **Clickable pop-ups** displaying crime category
- **Crime Types**: LARCENY/THEFT, ASSAULT, VEHICLE THEFT, BURGLARY, DRUG/NARCOTIC, VANDALISM, FRAUD, ROBBERY, WEAPON LAWS, TRESPASS

**File Output**: `sanfran_crimes_map_markers.html`

---

### Plot 4: Clustered Crime Markers (Base Zoom Level 4)
<img width="800" height="600" alt="4" src="https://github.com/user-attachments/assets/107b8ce9-6cbe-4a06-8f90-e685798f69e8" />

**Visual Characteristics:**
- **MarkerCluster plugin** groups nearby incidents
- **Major Clusters**: Downtown (30-40), Mission District (15-20), Richmond District (10-15), Sunset District (8-12), Bayview (5-8)
- **Color Coding**: Light green (1-5), Dark green (6-15), Yellow (16-30), Orange (31-50), Red (51+)

**File Output**: `sanfran_crimes_map_markers_clustered.html`

---

### Plot 4`: First Zoom Level (District Detail - Zoom 8)
<img width="800" height="600" alt="4`" src="https://github.com/user-attachments/assets/3fe4cc3b-d897-45de-84ac-e9162d500b6e" />

**Visible Neighborhoods and Landmarks:**
- **West Oakland** - East Bay neighborhood, industrial areas, port facilities
- **San Francisco** - City center, downtown skyline, Financial District
- **Oakland** - Major East Bay city, Port of Oakland, Lake Merritt
- **Bay Bridge** - Trans-bay connection, East span, Yerba Buena Island
- **West Span** - Bay Bridge western section, approach to San Francisco
- **Sunset District** - Western SF neighborhood, grid streets, Ocean Beach
- **CA 35** - Skyline Boulevard, coastal mountain route

---

### Plot 4``: Second Zoom Level (Street Detail - Zoom 12)
<img width="800" height="600" alt="4``" src="https://github.com/user-attachments/assets/6f19eb2f-e996-42f9-8d05-620255af5ec9" />

**Visible Neighborhoods and Streets:**

| Location | Boundaries | Characteristics |
|----------|------------|------------------|
| **Tenderloin** | Market St to Geary St, Taylor St to Larkin St | High-density crime area, SRO hotels |
| **Richmond District** | North of Golden Gate Park | Clement Street shops, Asian restaurants |
| **Western Addition** | Divisadero St to Fillmore St | Fillmore Jazz District, Japantown |
| **Civic Center** | Van Ness to Market, McAllister to Grove | City Hall, Opera House, Library |
| **Fulton Street** | East-west through Richmond | Golden Gate Park northern border |
| **Hayes Valley** | Market St to Fell St | Boutiques, restaurants, Octavia Blvd |
| **Haight-Ashbury** | Stanyan to Masonic, Waller to Oak | Victorian houses, hippie culture |

---

## San Francisco Area Guide

### East Bay Cities
| City | Features |
|------|----------|
| **Oakland** | Port of Oakland, Lake Merritt, Jack London Square |
| **West Oakland** | Industrial areas, BART station |
| **Piedmont** | Wealthy residential enclave |
| **Berkeley** | UC Berkeley, Telegraph Avenue |
| **Alameda** | Naval Air Station, Victorian homes |
| **Orinda** | Affluent residential, BART station |

### Peninsula Cities
| City | Features |
|------|----------|
| **Daly City** | Suburban, Westlake shopping |
| **Brisbane** | Small industrial town, Sign Hill |
| **South San Francisco** | "The Industrial City", airport proximity |
| **Colma** | "City of the Dead" (many cemeteries) |

### Major Landmarks
| Landmark | Description |
|----------|-------------|
| **Golden Gate Bridge** | SF to Marin County connection |
| **Bay Bridge** | SF to Oakland connection |
| **Golden Gate Park** | Museums, gardens, lakes |
| **Presidio** | National park, forests |
| **Bay Audubon Sanctuary** | East Bay wetlands |
| **MLK Jr. Regional Shoreline** | Oakland park and trails |

---

## Crime Data Summary

### Police District Incidents (First 100)
| District | Incidents | Common Crimes |
|----------|-----------|---------------|
| SOUTHERN | 18 | Theft, assault, robbery |
| MISSION | 15 | Assault, drug, theft |
| TENDERLOIN | 14 | Drug, assault, theft |
| CENTRAL | 12 | Theft, vandalism, fraud |
| RICHMOND | 10 | Burglary, theft, vehicle theft |
| NORTHERN | 9 | Assault, robbery, weapons |
| BAYVIEW | 8 | Vehicle theft, burglary, assault |
| PARK | 7 | Theft, vandalism, drug |

### Time Patterns
| Day | Incidents | Peak Times |
|-----|-----------|------------|
| Friday | 22 | Afternoon/evening |
| Saturday | 19 | Late night |
| Sunday | 14 | Evening |
| Monday | 13 | Afternoon |

---

## Zoom Level Reference

| Level | Scale | Visible Area |
|-------|-------|--------------|
| **4** | City-wide | Entire SF + East Bay |
| **8** | District | Neighborhood clusters |
| **12** | Street | Block-level detail |
| **14** | Neighborhood | Individual buildings |
| **16** | Street | Building names |

---

## File Structure

```
17-maps-and-markers/
├── README.md
├── maps-and-markers.py
├── Police_Department_Incidents_-_Previous_Year__2016_.csv
├── outputs/
│   ├── 01-sanfran-base-map.html
│   ├── 02-sanfran-crimes-circle.html
│   ├── 03-sanfran-crimes-popup.html
│   └── 04-sanfran-crimes-clustered.html
├── data/
│   ├── san-francisco-neighborhoods.geojson
│   ├── police-districts.geojson
│   ├── crime-categories.csv
│   ├── landmark-coordinates.csv
│   ├── bridge-locations.csv
│   ├── highway-routes.csv
│   ├── zoom-level-examples/
│   │   ├── zoom-04-city-wide.png
│   │   ├── zoom-08-district.png
│   │   ├── zoom-12-street.png
│   │   └── zoom-16-building.png
│   └── cluster-behavior.md
└── requirements.txt
```
