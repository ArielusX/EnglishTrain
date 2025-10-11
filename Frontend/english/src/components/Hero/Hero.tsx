import React from "react";
import "./Hero.css";

const Hero: React.FC = () => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>
          C1 English Prep
          <br />
          <span>Practice & Improve</span>
        </h1>
        <p>
          Master advanced English through focused exercises designed for the
          Cambridge C1 exam. Build accuracy, fluency, and confidence — one
          challenge at a time.
        </p>

        <div className="hero-buttons">
          <a href="#exercises" className="btn">
            Start Practicing
          </a>
          <a href="#about" className="btn btn-outline">
            Learn More
          </a>
        </div>
      </div>

      {/* Minimalist section below Hero */}
      <div className="hero-exercises" id="exercises">
        <h2>Explore Skills</h2>
        <div className="exercise-types">
          <div className="type-card">
            <span>🧩</span>
            <p>Grammar</p>
          </div>
          <div className="type-card">
            <span>🎧</span>
            <p>Listening</p>
          </div>
          <div className="type-card">
            <span>📖</span>
            <p>Reading</p>
          </div>
          <div className="type-card">
            <span>✍️</span>
            <p>Writing</p>
          </div>
          <div className="type-card">
            <span>🎤</span>
            <p>Speaking</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
