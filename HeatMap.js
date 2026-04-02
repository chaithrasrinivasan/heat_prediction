import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, Circle } from "react-leaflet";
import "leaflet/dist/leaflet.css";

function HeatMap() {

  const [heatZones, setHeatZones] = useState([]);

  // Example heat data (later this will come from backend API)
  useEffect(() => {

    const data = [
      {
        area: "Anna Nagar",
        lat: 13.0850,
        lng: 80.2101,
        heat: "High",
        temperature: 38
      },
      {
        area: "T Nagar",
        lat: 13.0418,
        lng: 80.2337,
        heat: "Medium",
        temperature: 36
      },
      {
        area: "Adyar",
        lat: 13.0012,
        lng: 80.2565,
        heat: "Low",
        temperature: 33
      }
    ];

    setHeatZones(data);

  }, []);

  // Function to decide color
  const getColor = (level) => {

    if (level === "High") return "red";
    if (level === "Medium") return "orange";
    return "green";

  };

  return (

    <MapContainer
      center={[13.0827, 80.2707]}
      zoom={12}
      style={{ height: "500px", width: "100%" }}
    >

      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {heatZones.map((zone, index) => (

        <Circle
          key={index}
          center={[zone.lat, zone.lng]}
          radius={500}
          pathOptions={{
            color: getColor(zone.heat),
            fillColor: getColor(zone.heat),
            fillOpacity: 0.5
          }}
        >

          <Popup>
            <b>{zone.area}</b> <br />
            Temperature: {zone.temperature}°C <br />
            Heat Risk: {zone.heat}
          </Popup>

        </Circle>

      ))}

    </MapContainer>

  );
}

export default HeatMap;
