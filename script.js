function handleSubmit(event) {
    // Prevent form submission
    event.preventDefault();

    // Check if the article textarea is empty
    var articleTextarea = document.getElementById("article");
    if (articleTextarea.value.trim() === "") {
        alert("The article should not be empty.");
        return; // Return without proceeding further
    }

    // Proceed with form submission
    event.target.submit();
}

function copyToClipboard() {
    var result = document.getElementsByClassName("answer")[0].textContent;
    navigator.clipboard.writeText(result).then(function () {
        alert("Copied to clipboard!");
    }, function () {
        alert("Copying failed, please manually copy the result!");
    });
}

function newEntry() {
    location.reload(); // Reload the page
}

// Check if the answer is empty, and hide the copy button if it is
var answer = document.getElementsByClassName("answer")[0];
var copyButton = document.getElementById("copyButton");
var refreshButton = document.getElementById("clearButton");

if (answer.textContent.trim() === "") {
    copyButton.style.display = "none";
    refreshButton.style.display = "none";
}