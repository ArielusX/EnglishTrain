import React, { useState } from "react";
import "./ExerciseStyles.css";

const Writing: React.FC = () => {
  const [text, setText] = useState("");
  const [submitted, setSubmitted] = useState(false);

  return (
    <div className="exercise-container">
      <h2>Writing Task</h2>
      <p className="instruction">Write about the following topic:</p>
      <p className="prompt">
        “Describe a time when you had to solve a difficult problem.”
      </p>

      <textarea
        className="writing-box"
        rows={6}
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type your response here..."
      />

      {!submitted ? (
        <button className="btn" onClick={() => setSubmitted(true)}>Submit</button>
      ) : (
        <p className="feedback">✅ Submitted! (Feedback coming soon)</p>
      )}
    </div>
  );
};

export default Writing;
