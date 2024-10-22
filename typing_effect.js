function typeWriter(text, elementId, speed) {
    let i = 0;
    const element = document.getElementById(elementId);
    if (!element) {
        console.error(`Element with id "${elementId}" not found`);
        return;
    }
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    element.innerHTML = ''; // Clear existing content
    type();
}

// Make sure the function is available globally
if (typeof window !== 'undefined') {
    window.typeWriter = typeWriter;
}
