import React, { useState } from "react";
import "./ExerciseStyles.css";

const Speaking: React.FC = () => {
  const [recording, setRecording] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const toggleRecording = () => {
    setRecording(!recording);
    // Aquí podrías integrar la API Web Speech o tu backend
  };

  return (
    <div className="exercise-container">
      <h2>Speaking Practice</h2>
      <p className="instruction">Talk for at least 30 seconds about this topic:</p>
      <p className="prompt">
        “What are the advantages and disadvantages of remote work?”
      </p>

      <button
        className={`mic-button ${recording ? "recording" : ""}`}
        onClick={toggleRecording}
      >
        🎙️ {recording ? "Recording..." : "Start Recording"}
      </button>

      {submitted ? (
        <p className="feedback">✅ Response submitted! Analyzing...</p>
      ) : (
        recording && (
          <button className="btn" onClick={() => setSubmitted(true)}>
            Stop & Submit
          </button>
        )
      )}
    </div>
  );
};

export default Speaking;
