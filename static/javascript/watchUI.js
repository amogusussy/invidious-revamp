function collapseDescription() {
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
  });
}

function collapseComments() {
  let collapseCommentButton = document.getElementById("commentCount");
  collapseCommentButton.addEventListener("click", () => {
    let comments = document.getElementById("comments");
    let buttonText = collapseCommentButton.innerText;

    if (comments.style.display == "none") {
      comments.style.display = "block";
      collapseCommentButton.innerText = buttonText.replace("Show", "Minimize");
    } else {
      comments.style.display = "none";
      collapseCommentButton.innerText = buttonText.replace("Minimize", "Show");
    }
  });
}

collapseDescription();
collapseComments();
