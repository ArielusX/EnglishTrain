import React, { useState } from "react";
import "./ExerciseStyles.css";

const Listening: React.FC = () => {
  const [selected, setSelected] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const correct = "B";

  const options = [
    { id: "A", text: "She went to the store." },
    { id: "B", text: "She had gone to the store." },
    { id: "C", text: "She is going to the store." },
  ];

  const playAudio = () => {
    new Audio("/audio/example.mp3").play(); // placeholder
  };

  return (
    <div className="exercise-container">
      <h2>Listening Exercise</h2>
      <p className="instruction">Listen carefully and choose the correct sentence.</p>

      <button className="btn-outline" onClick={playAudio}>🔊 Play Audio</button>

      <div className="options">
        {options.map((opt) => (
          <button
            key={opt.id}
            className={`option ${selected === opt.id ? "selected" : ""}`}
            onClick={() => setSelected(opt.id)}
          >
            {opt.text}
          </button>
        ))}
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answer</button>
      ) : (
        <p className="feedback">
          {selected === correct
            ? "✅ Correct!"
            : `❌ The correct answer was "${options.find(o => o.id === correct)?.text}".`}
        </p>
      )}
    </div>
  );
};

export default Listening;
