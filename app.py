import streamlit as st
import streamlit.components.v1 as components

st.title("Attendance Check-In")

components.html(
"""
<!DOCTYPE html>
<html>
<body style="text-align:center;font-family:Arial;">

<h3>Checking your location...</h3>
<p id="status"></p>

<script>
const targetLat = 39.132473;
const targetLng = -84.5170492;
const allowedRadius = 50; // meters

function toRad(value) {
  return value * Math.PI / 180;
}

function getDistance(lat1, lon1, lat2, lon2) {
  const R = 6371000;
  const dLat = toRad(lat2-lat1);
  const dLon = toRad(lon2-lon1);

  const a = Math.sin(dLat/2)**2 +
            Math.cos(toRad(lat1)) *
            Math.cos(toRad(lat2)) *
            Math.sin(dLon/2)**2;

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R * c;
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position){

    const lat = position.coords.latitude;
    const lng = position.coords.longitude;

    const dist = getDistance(lat,lng,targetLat,targetLng);

    if(dist <= allowedRadius){
        document.getElementById("status").innerHTML =
          "✅ Location verified. Loading form...";

        // show form section
        window.parent.postMessage("ALLOW_FORM", "*");

    } else {
        document.getElementById("status").innerHTML =
          "❌ Access denied. You are outside allowed area.";
    }

  });
}
</script>
</body>
</html>
""",
height=200
)

# --------------------
# FORM SECTION
# --------------------

st.markdown("---")

name = st.text_input("Name")
email = st.text_input("Email")
speaker = st.text_input("Speaker Name")
question = st.text_area("Question")

if st.button("Submit Attendance"):
    st.success("Submitted successfully!")
