import React from "react";
import "./App.css"; // Assuming a separate CSS file for styles

function App() {
  return (
    <div className="app" style={styles.body}>
      <header style={styles.header}>
        <h2 style={styles.logo}>Football Fanatics</h2>
        <ul style={styles.menu}>
          <li style={styles.menuItem}><a href="#" style={styles.link}>Home</a></li>
          <li style={styles.menuItem}><a href="#" style={styles.link}>Contact Us</a></li>
          <li style={styles.menuItem}><a href="#" style={styles.link}>Get Started</a></li>
        </ul>
      </header>
      <main style={styles.content}>
        <h1>Welcome to Football Fanatics</h1>
        <p>Join the game, explore the thrill!</p>
        <button style={styles.button}>Get Started</button>
      </main>
      <footer style={styles.footer}>
        &copy; 2024 Football Fanatics. All rights reserved.
      </footer>
    </div>
  );
}

const styles = {
  body: {
    margin: 0,
    fontFamily: "Arial, sans-serif",
    background: "url('football-background.jpg') no-repeat center center fixed",
    backgroundSize: "cover",
    color: "white",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    height: "100vh",
  },
  header: {
    backgroundColor: "rgba(0, 0, 0, 0.7)",
    padding: "10px 20px",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  logo: {
    margin: 0,
  },
  menu: {
    listStyle: "none",
    display: "flex",
    margin: 0,
    padding: 0,
  },
  menuItem: {
    margin: "0 15px",
  },
  link: {
    textDecoration: "none",
    color: "white",
    fontWeight: "bold",
    transition: "color 0.3s",
  },
  content: {
    textAlign: "center",
    marginTop: "10%",
  },
  button: {
    padding: "10px 20px",
    fontSize: "1em",
    color: "white",
    backgroundColor: "red",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    transition: "background-color 0.3s",
  },
  footer: {
    backgroundColor: "rgba(0, 0, 0, 0.7)",
    textAlign: "center",
    padding: "10px 0",
    fontSize: "0.9em",
  },
};

export default App;
