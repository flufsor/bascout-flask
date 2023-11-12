document.addEventListener("DOMContentLoaded", function () {
    const targetField = document.getElementById("target");
    const addScanButton = document.getElementById("add_scan");

    function checkField() {
        if (targetField.value.trim() === "") {
            addScanButton.disabled = true;
        } else {
            addScanButton.disabled = false;
        }
    }

    targetField.addEventListener("input", checkField);


    checkField();
});
