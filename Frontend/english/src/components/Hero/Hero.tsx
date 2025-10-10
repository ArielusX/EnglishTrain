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
          Master advanced English through focused exercises designed for the C1
          exam. Build confidence, accuracy, and fluency — one challenge at a
          time.
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
    </section>
  );
};

export default Hero;
