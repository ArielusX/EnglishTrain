import React, { useState } from "react";
import "./ExerciseStyles.css";

const MultipleChoiceCloze = () => {
  const correctAnswers = ["C", "A", "D", "B"];
  const [answers, setAnswers] = useState(Array(4).fill(""));
  const [checked, setChecked] = useState(false);

  const handleSelect = (i: number, val: string) => {
    const copy = [...answers];
    copy[i] = val;
    setAnswers(copy);
  };

  const correctCount = answers.filter((a, i) => a === correctAnswers[i]).length;

  return (
    <div className="exercise-container">
      <div className="progress-header">
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${(4 / 10) * 100}%` }}></div>
        </div>
        <span className="progress-text">4/10</span>
      </div>

      <h2>Part 1 — Multiple Choice Cloze</h2>
      <p className="instruction">Choose the correct word (A, B, C or D) for each gap.</p>

      <div className="text-content">
        <p>
          Many people believe that success depends on talent, but in reality, determination plays a far more significant{" "}
          <strong>(1)</strong> role.{" "}
          <select
            value={answers[0]}
            onChange={(e) => handleSelect(0, e.target.value)}
            className={checked ? (answers[0] === correctAnswers[0] ? "correct" : "wrong") : ""}
          >
            <option value="">---</option>
            <option value="A">A) job</option>
            <option value="B">B) moment</option>
            <option value="C">C) part</option>
            <option value="D">D) duty</option>
          </select>
          .
        </p>
        <p>
          Research shows that those who work hard are often able to{" "}
          <strong>(2)</strong>{" "}
          <select
            value={answers[1]}
            onChange={(e) => handleSelect(1, e.target.value)}
            className={checked ? (answers[1] === correctAnswers[1] ? "correct" : "wrong") : ""}
          >
            <option value="">---</option>
            <option value="A">A) achieve</option>
            <option value="B">B) obtain</option>
            <option value="C">C) perform</option>
            <option value="D">D) manage</option>
          </select>{" "}
          better results.
        </p>
        <p>
          Talent can give an initial{" "}
          <strong>(3)</strong>{" "}
          <select
            value={answers[2]}
            onChange={(e) => handleSelect(2, e.target.value)}
            className={checked ? (answers[2] === correctAnswers[2] ? "correct" : "wrong") : ""}
          >
            <option value="">---</option>
            <option value="A">A) level</option>
            <option value="B">B) goal</option>
            <option value="C">C) start</option>
            <option value="D">D) advantage</option>
          </select>
          , but without effort, it rarely leads to excellence.
        </p>
        <p>
          In conclusion, success may not be about being born with the right skills but about{" "}
          <strong>(4)</strong>{" "}
          <select
            value={answers[3]}
            onChange={(e) => handleSelect(3, e.target.value)}
            className={checked ? (answers[3] === correctAnswers[3] ? "correct" : "wrong") : ""}
          >
            <option value="">---</option>
            <option value="A">A) staying</option>
            <option value="B">B) keeping</option>
            <option value="C">C) maintaining</option>
            <option value="D">D) holding</option>
          </select>{" "}
          consistent and focused.
        </p>
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answers</button>
      ) : (
        <div className={`feedback-box ${correctCount === 4 ? "success" : "error"}`}>
          <p className="feedback">
            {correctCount === 4 ? "✅ Perfect!" : `You got ${correctCount} out of 4 correct.`}
          </p>
        </div>
      )}
    </div>
  );
};

export default MultipleChoiceCloze;
