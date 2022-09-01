const mobileWidth = 960;

function toggleSidebar() {
  const width = document.querySelector("body").offsetWidth;
  const toggler = document.querySelector("#toggler");
  if (width < mobileWidth) {
    toggler.checked = false;
  } else {
    toggler.checked = true;
  }
}

const mq = window.matchMedia(`(max-width: ${mobileWidth}px)`);
if (matchMedia) {
  mq.addListener(toggleSidebar);
}

document.addEventListener("DOMContentLoaded", function() {
  toggleSidebar();
});
