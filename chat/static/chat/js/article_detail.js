document.addEventListener("DOMContentLoaded", function() {
    // Any custom JavaScript for the article detail page can go here
    console.log("Article Detail Page Loaded");

    // Example: Scroll to the comment form if there's a hash in the URL
    if(window.location.hash === "#comment-form") {
        document.querySelector('.comment-form').scrollIntoView({ behavior: 'smooth' });
    }
});
