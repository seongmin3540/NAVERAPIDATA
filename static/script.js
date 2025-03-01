let currentIndex = 0;
const slides = document.querySelectorAll('.ad-slide');
const totalSlides = slides.length;

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides;
    updateSliderPosition();
}

function updateSliderPosition() {
    const newTransformValue = -currentIndex * 100;
    document.querySelector('.ad-slider-wrapper').style.transform = `translateX(${newTransformValue}%)`;
}

// 자동으로 3초마다 슬라이드 전환
setInterval(nextSlide, 3500);
