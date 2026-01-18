document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    const btn = document.getElementById('submitBtn');
    const clearBtn = document.getElementById('clearBtn');
    const reviewBox = document.getElementById('reviewBox');
    const resultBox = document.getElementById('resultBox');

    // Visual feedback for analysis
    form.onsubmit = function() {
        btn.value = "Analyzing... 🔍";
        btn.style.opacity = "0.7";
    };

    // Logic for Clear button
    clearBtn.addEventListener('click', function() {
        // Clear text box
        reviewBox.value = "";
        
        // Hide existing result box
        if (resultBox) {
            resultBox.style.display = 'none';
        }

        // Reset button text
        btn.value = "Analyze Now ✨";
        btn.style.opacity = "1";
    });
});