
let closeDescButton = document.getElementById("closeDesc");
closeDescButton.addEventListener("click", () => {
  let description = document.querySelector(".description");
  if (description.style.display != "none") {
    description.style.display = "none";
    closeDescButton.innerText = "Show Description";
  } else {
    description.style.display = "block";
    closeDescButton.innerText = "Minimize Description";
  }
})
