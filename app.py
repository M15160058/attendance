import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Attendance Check", layout="centered")

FORM_URL = "https://forms.office.com/Pages/DesignPageV2.aspx?origin=NeoPortalPage&subpage=design&id=bC4i9cZf60iPA3PbGCA7Y3zURXDN2c1Mk8io1jX0SGNUMlVIUEtTQ0xaWEUxTDFZMjUzM0xLUFVJVC4u"

# If verified, redirect immediately
if "verified" in st.session_state and st.session_state.verified:
    st.markdown(
        f"""
        <meta http-equiv="refresh" content="0; url={FORM_URL}">
        """,
        unsafe_allow_html=True,
    )
    st.stop()

st.title("📍 Attendance Verification")
st.write("Checking your location... Please allow GPS access.")

result = components.html(
"""
<!DOCTYPE html>
<html>
<body style="text-align:center;font-family:Arial;color:white;">

<p id="status">Requesting location...</p>

<script>
const targetLat = 39.132473;
const targetLng = -84.5170492;
const allowedRadius = 3000;

function toRad(value){
  return value * Math.PI / 180;
}

function getDistance(lat1, lon1, lat2, lon2){
  const R = 6371000;
  const dLat = toRad(lat2-lat1);
  const dLon = toRad(lon2-lon1);

  const a = Math.sin(dLat/2)**2 +
            Math.cos(toRad(lat1)) *
            Math.cos(toRad(lat2)) *
            Math.sin(dLon/2)**2;

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R*c;
}

if(navigator.geolocation){

  navigator.geolocation.getCurrentPosition(function(position){

      const lat = position.coords.latitude;
      const lng = position.coords.longitude;
      const dist = getDistance(lat,lng,targetLat,targetLng);

      if(dist <= allowedRadius){
          document.getElementById("status").innerHTML =
          "✅ Location verified...";
          
          // Send success to Streamlit
          window.parent.postMessage("verified", "*");

      }else{
          document.getElementById("status").innerHTML =
          "❌ Access denied. You must be in seminar room.";
      }

  },
  function(error){
      document.getElementById("status").innerHTML =
      "❌ Please enable GPS.";
  });

}else{
  document.getElementById("status").innerHTML =
  "❌ Geolocation not supported.";
}
</script>

</body>
</html>
""",
height=200,
)

# Listen for JS message
if result == "verified":
    st.session_state.verified = True
    st.rerun()
