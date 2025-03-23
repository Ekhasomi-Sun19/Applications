// Save theme preference in localStorage
const savedTheme = localStorage.getItem('theme');

if (savedTheme) {
    body.classList.add(savedTheme);
    themeToggleButton.textContent = savedTheme === 'dark-theme' ? 'Switch to Light Theme' : 'Switch to Dark Theme';
} else {
    body.classList.add('light-theme');
}

themeToggleButton.addEventListener('click', () => {
    const currentTheme = body.classList.contains('dark-theme') ? 'dark-theme' : 'light-theme';
    const newTheme = currentTheme === 'dark-theme' ? 'light-theme' : 'dark-theme';

    body.classList.replace(currentTheme, newTheme);
    localStorage.setItem('theme', newTheme);

    themeToggleButton.textContent = newTheme === 'dark-theme' ? 'Switch to Light Theme' : 'Switch to Dark Theme';
});

