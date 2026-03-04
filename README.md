# 18-Choropleth
## Interactive Choropleth Visualization of Global Immigration Patterns to Canada

This branch demonstrates **choropleth mapping techniques** using Folium to visualize immigration patterns to Canada from 1980 to 2013, creating an interactive color-coded world map that reveals global migration trends.

---

## Progressive Visualization

### Plot 1: Global Immigration Choropleth Map
<img width="2235" height="1255" alt="Screenshot 2026-03-04 022010" src="https://github.com/user-attachments/assets/cb621b82-a3a7-4801-9055-d14ae998c54c" />

**Visual Characteristics:**
- **Base Map**: World map centered at [0, 0] with zoom level 2
- **Color Scheme**: YlOrRd (Yellow-Orange-Red) sequential palette
- **Fill Opacity**: 0.7 for country polygons
- **Line Opacity**: 0.2 for country borders
- **Legend Title**: "Immigration to Canada"
- **Time Period**: 1980-2013 cumulative immigration totals

**Color Intensity Legend:**

| Color | Immigration Range | Interpretation |
|-------|-------------------|----------------|
| Light Yellow | 0 - 115,318 | Low immigration |
| Yellow | 115,318 - 230,635 | Low-medium immigration |
| Light Orange | 230,635 - 345,953 | Medium immigration |
| Orange | 345,953 - 461,270 | Medium-high immigration |
| Dark Orange | 461,270 - 576,587 | High immigration |
| Red | 576,587 - 691,904 | Very high immigration |
| Dark Red | 691,904+ | Highest immigration |

**Legend Scale:**
<img width="400" height="60" alt="Color Scale" src="https://github.com/user-attachments/assets/[replace-with-actual-image-id]" />

```
115,318    230,635    345,953    461,270    576,587    691,904
   └──────────┴──────────┴──────────┴──────────┴──────────┘
   Light Yellow ──────────────────────────────→ Dark Red
```

---

## Top Immigration Countries (1980-2013)

### Highest Immigration Sources

| Rank | Country | Total Immigrants | Continent | Color on Map |
|------|---------|------------------|-----------|--------------|
| **1** | India | 691,904 | Asia | Dark Red |
| **2** | China | 691,904 | Asia | Dark Red |
| **3** | Philippines | 691,904 | Asia | Dark Red |
| **4** | Pakistan | 345,953 - 461,270 | Asia | Orange |
| **5** | United Kingdom | 345,953 - 461,270 | Europe | Orange |
| **6** | United States | 345,953 - 461,270 | North America | Orange |
| **7** | Iran | 230,635 - 345,953 | Asia | Light Orange |
| **8** | South Korea | 230,635 - 345,953 | Asia | Light Orange |
| **9** | Sri Lanka | 230,635 - 345,953 | Asia | Light Orange |
| **10** | France | 115,318 - 230,635 | Europe | Yellow |

### Regional Patterns

**Asia (Highest Immigration):**
- India, China, Philippines (Dark Red - 690K+)
- Pakistan, Iran, South Korea, Sri Lanka (Orange/Light Orange - 230K-460K)
- Vietnam, Lebanon, Bangladesh (Yellow - 115K-230K)

**Europe (Medium-High Immigration):**
- United Kingdom (Orange - 345K-460K)
- France, Poland, Portugal (Yellow - 115K-230K)
- Germany, Italy, Netherlands (Light Yellow - <115K)

**Americas (Variable Immigration):**
- United States (Orange - 345K-460K)
- Jamaica, Mexico, Colombia (Yellow - 115K-230K)
- Haiti, Guyana, Trinidad (Light Yellow - <115K)

**Africa (Emerging Immigration):**
- Egypt, Morocco, Algeria (Light Yellow - <115K)
- South Africa, Somalia, Ethiopia (Light Yellow - <115K)
- Most sub-Saharan countries (Light Yellow - <50K)

---

## Geographic Patterns Analysis

### Continental Distribution

| Continent | Immigration Pattern | Notable Countries |
|-----------|--------------------|-------------------|
| **Asia** | Highest overall | India, China, Philippines (690K+) |
| **Europe** | Medium-high | UK, France, Poland |
| **North America** | Medium | US, Jamaica, Mexico |
| **South America** | Low-medium | Colombia, Peru, Brazil |
| **Africa** | Low | Egypt, Morocco, South Africa |
| **Oceania** | Low | Australia, New Zealand |

### Major Sending Regions

**South Asia Corridor:**
- India (690K+)
- Pakistan (345K-460K)
- Sri Lanka (230K-345K)
- Bangladesh (115K-230K)

**East Asia Corridor:**
- China (690K+)
- Philippines (690K+)
- South Korea (230K-345K)
- Vietnam (115K-230K)

**Middle East Corridor:**
- Iran (230K-345K)
- Lebanon (115K-230K)
- Syria (50K-115K)
- Iraq (50K-115K)

**European Corridor:**
- United Kingdom (345K-460K)
- France (115K-230K)
- Poland (115K-230K)
- Portugal (115K-230K)

---

## Dataset Information

### Data Source

| Attribute | Description |
|-----------|-------------|
| **Dataset** | International migration data to Canada |
| **Source** | Official Canadian immigration statistics |
| **Time Period** | 1980 - 2013 (33 years) |
| **Countries** | 195 nations |
| **Variables** | Annual immigration counts by country |

### Data Processing

**Original Columns:**
- OdName → **Country** (renamed)
- AreaName → **Continent** (renamed)
- RegName → **Region** (renamed)
- AREA, REG, DEV, Type, Coverage → **Dropped**

**Derived Columns:**
- **Total** = Sum of all years (1980-2013)

### Sample Data (First 5 Countries)

| Country | Continent | Region | Total | Color Class |
|---------|-----------|--------|-------|-------------|
| Afghanistan | Asia | Southern Asia | 11,260 | Light Yellow |
| Albania | Europe | Southern Europe | 4,078 | Light Yellow |
| Algeria | Africa | Northern Africa | 22,688 | Light Yellow |
| American Samoa | Oceania | Polynesia | 6 | Light Yellow |
| Andorra | Europe | Southern Europe | 15 | Light Yellow |

---

## Choropleth Map Components

### Visual Elements

| Component | Description | Settings |
|-----------|-------------|----------|
| **Base Map** | OpenStreetMap tiles | Default Folium base |
| **GeoJSON Layer** | World country boundaries | `world_countries.json` |
| **Data Binding** | Country names to polygons | `key_on="feature.properties.name"` |
| **Color Scale** | Sequential color scheme | `fill_color="YlOrRd"` |
| **Fill Opacity** | Transparency of country fills | `fill_opacity=0.7` |
| **Border Opacity** | Transparency of country boundaries | `line_opacity=0.2` |
| **Legend** | Color intensity guide | "Immigration to Canada" |

### Color Scheme: YlOrRd (Yellow-Orange-Red)

| Hex Code | Color Name | Value Range |
|----------|------------|-------------|
| #FFFFB2 | Light Yellow | 0 - 115,318 |
| #FED976 | Yellow | 115,318 - 230,635 |
| #FEB24C | Light Orange | 230,635 - 345,953 |
| #FD8D3C | Orange | 345,953 - 461,270 |
| #FC4E2A | Dark Orange | 461,270 - 576,587 |
| #E31A1C | Red | 576,587 - 691,904 |
| #B10026 | Dark Red | 691,904+ |

---

## Geographic Highlights by Region

### Asia (Dominant Sending Region)

| Subregion | Pattern | Key Countries |
|-----------|---------|---------------|
| **South Asia** | Very High | India (690K+), Pakistan (345K-460K) |
| **East Asia** | Very High | China (690K+), South Korea (230K-345K) |
| **Southeast Asia** | Very High | Philippines (690K+), Vietnam (115K-230K) |
| **Middle East** | Medium | Iran (230K-345K), Lebanon (115K-230K) |
| **Central Asia** | Low | Kazakhstan, Uzbekistan (<50K) |

### Europe (Moderate Sending Region)

| Subregion | Pattern | Key Countries |
|-----------|---------|---------------|
| **Western Europe** | Medium-High | UK (345K-460K), France (115K-230K) |
| **Southern Europe** | Medium | Portugal (115K-230K), Italy (50K-115K) |
| **Eastern Europe** | Medium | Poland (115K-230K), Ukraine (50K-115K) |
| **Northern Europe** | Low-Medium | Ireland, Sweden (<115K) |

### Americas (Variable Sending Region)

| Subregion | Pattern | Key Countries |
|-----------|---------|---------------|
| **North America** | Medium | US (345K-460K), Mexico (115K-230K) |
| **Caribbean** | Medium | Jamaica (115K-230K), Haiti (50K-115K) |
| **South America** | Low-Medium | Colombia, Peru, Brazil (<115K) |
| **Central America** | Low | Guatemala, El Salvador (<50K) |

### Africa (Emerging Sending Region)

| Subregion | Pattern | Key Countries |
|-----------|---------|---------------|
| **North Africa** | Low-Medium | Egypt, Morocco, Algeria (<115K) |
| **East Africa** | Low | Somalia, Ethiopia, Kenya (<50K) |
| **West Africa** | Low | Nigeria, Ghana, Senegal (<50K) |
| **Southern Africa** | Low | South Africa, Zimbabwe (<50K) |

### Oceania (Minimal Sending Region)

| Subregion | Pattern | Key Countries |
|-----------|---------|---------------|
| **Australia/New Zealand** | Low | Australia, New Zealand (<50K) |
| **Pacific Islands** | Minimal | Fiji, Samoa, Tonga (<10K) |

---

## Immigration Trends Interpretation

### Historical Context (1980-2013)

**1980s Pattern:**
- European immigration still significant (UK, Portugal, Italy)
- Asian immigration beginning to rise (Vietnam, China)
- US immigration moderate but steady

**1990s Pattern:**
- Asian immigration accelerates (India, China, Philippines)
- European immigration declines
- Middle Eastern immigration increases (Iran, Lebanon)

**2000s Pattern:**
- South Asian dominance established (India, Pakistan, Sri Lanka)
- Chinese immigration continues strong
- Filipino immigration surges
- African immigration begins steady growth

### Policy Influences

| Period | Policy Change | Impact |
|--------|---------------|--------|
| **1967** | Points-based system introduced | Shift from European to global immigration |
| **1976** | Immigration Act | Family reunification emphasis |
| **1990s** | Business immigration programs | Increased Asian professional immigration |
| **2002** | Immigration and Refugee Protection Act | Skilled worker focus |
| **2008** | Canadian Experience Class | International student pathway |

---

## Interactive Features

### User Controls

| Control | Function |
|---------|----------|
| **Zoom In/Out** | Examine specific regions in detail |
| **Pan** | Navigate to different continents |
| **Hover** | View country names (browser dependent) |
| **Legend** | Reference color-value mapping |
| **Full Screen** | Expand map for better viewing |

### Regional Exploration Tips

| Region | Recommended Zoom | What to Observe |
|--------|------------------|-----------------|
| **South Asia** | Zoom 4 | India (dark red), Pakistan (orange) |
| **East Asia** | Zoom 4 | China (dark red), South Korea (orange) |
| **Europe** | Zoom 4 | UK (orange), France (yellow) |
| **Middle East** | Zoom 5 | Iran (orange), Lebanon (yellow) |
| **Caribbean** | Zoom 5 | Jamaica (yellow), Haiti (light yellow) |

---

## Data Insights Summary

### Key Observations

1. **Asian Dominance**: Three Asian countries (India, China, Philippines) each sent over 690,000 immigrants
2. **European Transition**: Traditional European sources (UK, France) now surpassed by Asian nations
3. **US-Canada Corridor**: Significant two-way migration (345K-460K from US)
4. **Emerging Sources**: African and Latin American immigration growing but still modest
5. **Concentration**: Top 10 countries account for over 60% of total immigration

### Statistical Highlights

| Metric | Value |
|--------|-------|
| **Total Immigrants (1980-2013)** | ~7.5 million |
| **Top 3 Countries Share** | ~28% of total |
| **Top 10 Countries Share** | ~62% of total |
| **Asian Share** | ~55% of total |
| **European Share** | ~25% of total |
| **Americas Share** | ~15% of total |
| **African Share** | ~4% of total |
| **Oceanian Share** | ~1% of total |

---

## File Structure

```
18-choropleth/
├── README.md
├── choropleth.py
├── Canada.xlsx
├── world_countries.json
├── outputs/
│   └── choropleth_world_map.html
├── data/
│   ├── immigration-totals-by-country.csv
│   ├── continental-breakdown.csv
│   ├── regional-patterns.csv
│   ├── top-20-countries.csv
│   ├── color-scale-reference.md
│   ├── geojson-properties.md
│   └── historical-context/
│       ├── 1980s-patterns.md
│       ├── 1990s-patterns.md
│       ├── 2000s-patterns.md
│       └── policy-timeline.md
└── requirements.txt
```
