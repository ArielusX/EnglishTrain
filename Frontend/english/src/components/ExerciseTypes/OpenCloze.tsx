import React, { useState } from "react";
import "./ExerciseStyles.css";

const OpenCloze = () => {
  const correctAnswers = ["is", "because", "such", "other", "may"];
  const [answers, setAnswers] = useState(Array(correctAnswers.length).fill(""));
  const [checked, setChecked] = useState(false);

  const update = (i: number, v: string) => {
    const copy = [...answers];
    copy[i] = v;
    setAnswers(copy);
  };

  const correctCount = answers.filter((a, i) => a.trim().toLowerCase() === correctAnswers[i]).length;

  return (
    <div className="exercise-container">
      <div className="progress-header">
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${(5 / 10) * 100}%` }}></div>
        </div>
        <span className="progress-text">5/10</span>
      </div>

      <h2>Part 2 — Open Cloze</h2>
      <p className="instruction">Write one word in each gap.</p>

      <div className="text-content">
        <p>
          The truth (0){" "}
          <input type="text" placeholder="..." value={answers[0]} onChange={(e) => update(0, e.target.value)} className={checked ? (answers[0] === "is" ? "correct" : "wrong") : ""}/> nobody really knows how language began.
          Did we all start talking at around the same time (1){" "}
          <input type="text" placeholder="..." value={answers[1]} onChange={(e) => update(1, e.target.value)} className={checked ? (answers[1] === "because" ? "correct" : "wrong") : ""}/> of the way our brains developed?
        </p>
        <p>
          People suggest (2){" "}
          <input type="text" placeholder="..." value={answers[2]} onChange={(e) => update(2, e.target.value)} className={checked ? (answers[2] === "such" ? "correct" : "wrong") : ""}/> theories, but one says language is built into our brains.
          In (3){" "}
          <input type="text" placeholder="..." value={answers[3]} onChange={(e) => update(3, e.target.value)} className={checked ? (answers[3] === "other" ? "correct" : "wrong") : ""}/> words, it’s part of evolution and (4){" "}
          <input type="text" placeholder="..." value={answers[4]} onChange={(e) => update(4, e.target.value)} className={checked ? (answers[4] === "may" ? "correct" : "wrong") : ""}/> be in all of us.
        </p>
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answers</button>
      ) : (
        <div className={`feedback-box ${correctCount === correctAnswers.length ? "success" : "error"}`}>
          <p className="feedback">
            {correctCount === correctAnswers.length
              ? "✅ Perfect!"
              : `You got ${correctCount} out of ${correctAnswers.length} correct.`}
          </p>
        </div>
      )}
    </div>
  );
};

export default OpenCloze;
