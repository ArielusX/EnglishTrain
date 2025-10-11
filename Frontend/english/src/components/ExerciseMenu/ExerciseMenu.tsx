import React from "react";
import "./ExerciseMenu.css";

const exercises = [
  { icon: "🧩", title: "Grammar", desc: "Fill the blank, choose the correct option" },
  { icon: "🎧", title: "Listening", desc: "Listen and pick the right answer" },
  { icon: "📖", title: "Reading", desc: "Read and answer comprehension questions" },
  { icon: "✍️", title: "Writing", desc: "Practice writing structured answers" },
  { icon: "🎤", title: "Speaking", desc: "Talk and get instant feedback" },
];

const ExerciseMenu: React.FC = () => {
  return (
    <section className="exercise-menu" id="exercises">
      <h2>Choose your skill to practice</h2>
      <div className="exercise-grid">
        {exercises.map((ex) => (
          <div className="exercise-card" key={ex.title}>
            <span className="icon">{ex.icon}</span>
            <h3>{ex.title}</h3>
            <p>{ex.desc}</p>
            <button className="btn">Start</button>
          </div>
        ))}
      </div>
    </section>
  );
};

export default ExerciseMenu;
