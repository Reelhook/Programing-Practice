
// Function to remove YouTube Shorts elements
function removeShorts() {
  // If currently on a Shorts page, redirect to the main YouTube homepage.
  if (window.location.pathname.startsWith("/shorts")) {
    window.location.href = "https://www.youtube.com/";
    return;
  }

  // Select all links whose href contains "/shorts"
  let shortsLinks = document.querySelectorAll('a[href*="/shorts"]');
  shortsLinks.forEach(link => {
    // Try to find a common container for a video element.
    let container = link.closest('ytd-rich-item-renderer');
    if (container) {
      container.remove();
    } else {
      // If no parent container is found, remove the link directly.
      link.remove();
    }
  });
}

// Initial call on script load
removeShorts();

// Observe changes in the DOM in case new Shorts elements are loaded dynamically
const observer = new MutationObserver(mutations => {
  mutations.forEach(mutation => {
    if (mutation.addedNodes.length > 0) {
      removeShorts();
    }
  });
});

// Start observing the document body for added nodes.
observer.observe(document.body, { childList: true, subtree: true });
