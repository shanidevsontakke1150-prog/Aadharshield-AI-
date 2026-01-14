async function checkRisk() {
  const aadhaar = document.getElementById("aadhaar").value;
  const location = document.getElementById("location").value;
  const device = document.getElementById("device").value;
  const service = document.getElementById("service").value;

  const res = await fetch("http://localhost:5000/check", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      aadhaar_id: aadhaar,
      location: location,
      device: device,
      service: service
    })
  });

  const data = await res.json();

  document.getElementById("result").innerText =
    "Risk: " + data.risk + " | Reason: " + data.reason;
}
