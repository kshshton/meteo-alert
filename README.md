# 🌤️ MeteoAlert — Weather Alerts & Meteopathic Sensitivity Analysis

**MeteoAlert** is an analytical tool that monitors meteorological data (temperature, pressure, humidity, wind, etc.) to identify conditions that can affect **human well-being, focus, and cognitive performance** — especially for people sensitive to weather changes (known as *meteopaths*).

---

## 🚀 Overview

This project provides:
- Automatic weather data parsing from APIs (e.g., WeatherAPI)
- Analysis of short-term and long-term weather trends
- Detection of rapid atmospheric pressure drops and other discomfort triggers
- Visualization of daily and hourly trends
- Alert generation for conditions potentially affecting concentration and mood

---

## 🧠 Environmental Factors Affecting Concentration and Mental Clarity

Weather conditions can significantly influence the nervous system, vascular tone, and hormonal balance.  
Below are the main factors that may cause **mental fog, fatigue, or reduced focus** in weather-sensitive individuals.

---

### **1. Atmospheric Pressure (`pressure_mb`)**

Sudden or prolonged pressure drops are the **primary trigger** for cognitive slowing and headaches.

**Typical effects:**
- Headaches  
- Mental fatigue  
- Difficulty concentrating  

**Key metrics:**
- **Daily pressure range:** ΔP = P_max - P_min  
- **Rate of change:** ΔP / Δt (pressure change per hour)  
- **Sudden drop indicator:** decrease > 5 hPa within 3 hours  

📉 Rapid drops of >4–6 hPa within a few hours can cause vasodilation and reduced oxygen flow to the brain.

---

### **2. Temperature (`temp_c`, `feelslike_c`)**

Rapid thermal changes can cause **drowsiness** and **sluggishness**.

**Effects:**
- Sleepiness  
- Decreased alertness  
- Feeling drained  

**Metrics:**
- Daily temperature range (ΔT = T_max - T_min)  
- Variation in perceived temperature (`feelslike_c`)  
- Night vs. day temperature average  

---

### **3. Humidity (`humidity`)**

High humidity reduces comfort and increases fatigue; low humidity dries mucous membranes.

**Effects:**
- >80% → heavy, sticky feeling  
- <30% → irritability and discomfort  

**Metrics:**
- Average daily humidity  
- Hours above 80% humidity  

---

### **4. Cloudiness (`cloud`)**

Low sunlight exposure affects serotonin and melatonin balance, causing **mental fog**.

**Effects:**
- Fatigue  
- Lack of motivation  
- Decreased attention span  

**Metrics:**
- Average daily cloud cover  
- Hours with cloudiness > 80%  

---

### **5. Precipitation (`precip_mm`, `will_it_rain`)**

Rain or drizzle contributes to fatigue, especially when combined with low pressure.

**Metrics:**
- Total daily precipitation  
- Hours with rainfall  
- Intensity > 1 mm/h  

---

### **6. Wind (`wind_mph`, `gust_mph`)**

Strong gusts may contribute to irritability or mild fatigue.

**Metrics:**
- Average wind speed  
- Maximum gust speed  
- Hours with wind > 10 mph (16 km/h)  

---

### **Summary Table**

| Factor | Cognitive Impact | Typical Risk Thresholds |
|--------|------------------|--------------------------|
| **Pressure** | Very high | drop > 4–6 hPa in 3–6h or < 1005 hPa |
| **Cloudiness** | High | >80% for >3h |
| **Humidity** | Moderate | >80% or <30% |
| **Temperature** | Moderate | ΔT > 6°C in 3–6h |
| **Wind / Rain** | Low–moderate | gusts >30 km/h, heavy rain |
