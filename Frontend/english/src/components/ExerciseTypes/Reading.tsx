import React, { useState } from "react";
import "./ExerciseStyles.css";

const Reading: React.FC = () => {
  const [selected, setSelected] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);
  const correct = "A";

  return (
    <div className="exercise-container">
      <h2>Reading Comprehension</h2>
      <p className="instruction">Read the passage and answer the question below.</p>

      <div className="reading-text">
        <p>
          Technology has changed the way we communicate. People now use instant
          messaging and video calls more than ever before, reducing face-to-face
          interactions but increasing global connectivity.
        </p>
      </div>

      <p className="question">
        What is one negative consequence mentioned in the text?
      </p>

      <div className="options">
        <button
          className={`option ${selected === "A" ? "selected" : ""}`}
          onClick={() => setSelected("A")}
        >
          Less face-to-face interaction
        </button>
        <button
          className={`option ${selected === "B" ? "selected" : ""}`}
          onClick={() => setSelected("B")}
        >
          Slow global communication
        </button>
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answer</button>
      ) : (
        <p className="feedback">
          {selected === correct ? "✅ Correct!" : "❌ Incorrect, it was A."}
        </p>
      )}
    </div>
  );
};

export default Reading;
