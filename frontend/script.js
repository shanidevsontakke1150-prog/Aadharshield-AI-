
fetch("https://aadharshield-backend.onrender.com/health")
  .then(res => res.json())
  .then(data => {
    document.getElementById("status").innerText = "🟢 Backend Online";
    document.getElementById("status").className = "status ok";
  })
  .catch(() => {
    document.getElementById("status").innerText = "🔴 Backend Offline";
    document.getElementById("status").className = "status err";
  });
async function checkRisk() {
  const aadhaar = document.getElementById("aadhaar").value;
  const location = document.getElementById("location").value;
  const device = document.getElementById("device").value;
  const service = document.getElementById("service").value;

  const res = await fetch("https://aadharshield-backend.onrender.com/check", {
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
