# Kamraan Nazir OSINT Investigation

![Map Visualization](https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png "Target Map Visualization Placeholder") 
*(A screenshot of the interactive map `map.html` and `Target Triangulation Map.html` used to trace geolocation markers like Mohipora and Government Degree College Kulgam.)*

## Overview
This repository contains the findings and tools developed during the OSINT investigation of **Kamraan Nazir Khan** (alias: @midnighttdreamerr). The subject is based in Kulgam, Jammu & Kashmir.

The objective was to enumerate the subject's digital footprint across various platforms, gather publicly available intelligence, and map potential geolocations based on public interactions and education clues.

## Tools Used
- **Maigret:** For cross-platform username enumeration (found profiles on YouTube, Kaggle, Letterboxd, ArtStation, Hashnode, Spotify, OP.GG).
- **Advanced Dorking (Google/DuckDuckGo):** To discover non-obvious indexed files, such as civil engineering test scoresheets and tender documents.
- **Folium / Leaflet:** For creating the interactive triangulation map (`map.html` / `Target Triangulation Map.html`) marking locations of interest.
- **Instaloader / Custom IG Scripts:** Attempted data retrieval for Instagram.

## Methodology
1. **Initial Enumeration:** Started with the known alias (`@midnighttdreamerr`) and primary name.
2. **Cross-Platform Profiling:** Used `maigret` to verify the presence of the handle across 100+ sites. This expanded the target's footprint into gaming (OP.GG), arts (ArtStation), and technology (Kaggle/Hashnode).
3. **Deep Web & Document Searching:** Used Boolean dorking for "Kamraan Nazir Khan" and "Kamran Nazir Khan", yielding government PDFs, test scores, and university lists that were scraped and analyzed.
4. **Geospatial Mapping:** Aggregated identified locations (Pulse Medicare Kulgam, Govt Degree College Kulgam, Al Shameem Library) to generate a triangulation map.

## Shortcomings & Challenges
- **Instagram Aggressive Rate-Limiting:** Instagram's anti-bot mechanics and rate limits repeatedly blocked scraping attempts, even with session cookie injection.
- **Cloudflare Protections:** Attempts to scrape the subject's LibraryThing profile were heavily mitigated by Cloudflare's anti-bot challenges.
- **Name Collision / Dual Profile:** Dorking revealed significant discrepancies. While the digital footprint suggests a literature/arts background, document leaks (scoresheets, date sheets) point to a Civil Engineering background. This indicates either a complex dual-identity or a regional name collision.
- **Private Accounts:** Crucial platforms like Instagram are set to private, severely limiting passive collection without social engineering.

## Contents
- `consolidated_report.md` - The final structured intelligence report.
- `index.html` - A web-based presentation of the report.
- `map.html` - The generated interactive map of the subject's locations.
