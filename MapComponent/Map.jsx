const LatitudeAndLongitude = (mapUrl) => {
    function extractLatLongFromGoogleMapsURL(url) {
      const regex = /@([-+]?\d+\.\d+),([-+]?\d+\.\d+)/;
      const match = url.match(regex);
      if (match && match.length >= 3) {
        const lat = parseFloat(match[1]);
        const lng = parseFloat(match[2]);
        return { lat, lng };
      }
      return null;
    }
  
    extractLatLongFromGoogleMapsURL(mapUrl);
  
    console.log("url: ", mapUrl);
  
    return (
      <div>
        <h1>Latitude and Longitude</h1>
      </div>
    );
  };
  
  export default LatitudeAndLongitude;
  