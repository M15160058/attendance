📍 Location-Based Attendance Verification (Streamlit + GPS + Microsoft Forms)

This project provides a location-restricted attendance system built with Streamlit.

Users must be physically present near the seminar/classroom to access the attendance form.
If they are inside the allowed GPS radius, they are automatically redirected to a Microsoft Form.
Otherwise, access is denied.

🚀 Live App

👉 Open here:
https://attendance-8avu5rhldpsugjrcgvx7qj.streamlit.app/

✅ How It Works

User opens the Streamlit page

Browser requests GPS permission

Distance is calculated using Haversine formula

If inside allowed radius → redirect to Microsoft Form

If outside → access denied

🔒 Logic
IF distance ≤ allowedRadius:
    redirect to MS Form
ELSE:
    block access

✨ Features

✅ Automatic GPS verification
✅ Distance calculation (meters)
✅ Microsoft Forms redirect
✅ No form shown before verification
✅ Works on mobile & desktop
✅ Simple, lightweight
✅ Easy deployment on Streamlit Cloud


📍 Configuration

Inside app.py you can change:

Target location
const targetLat = 39.132473;
const targetLng = -84.5170492;

Radius (meters)
const allowedRadius = 90;
