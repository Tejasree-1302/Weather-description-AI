async function getDescription() {
  const weatherInput = document.getElementById("weather").value;

  const response = await fetch("http://127.0.0.1:7860/api/predict/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ data: [weatherInput] }),
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.data[0];
}
