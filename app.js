async function verify() {
  let file = document.getElementById("file").files[0];
  let formData = new FormData();
  formData.append("file", file);

  let res = await fetch("http://127.0.0.1:8000/verify", {
    method: "POST",
    body: formData
  });

  let data = await res.json();
  document.getElementById("result").innerText =
    JSON.stringify(data, null, 2);
}
