import React, { useState } from "react";
import "./ExerciseStyles.css";

const KeyWordTransformations = () => {
  const items = [
    {
      base: "able",
      question: "It’s impossible for me to finish this project today.",
      answer: "I am not able to finish this project today.",
    },
    {
      base: "used",
      question: "Living in a big city is strange for me.",
      answer: "I am not used to living in a big city.",
    },
  ];

  const [answers, setAnswers] = useState(Array(items.length).fill(""));
  const [checked, setChecked] = useState(false);

  const correctCount = answers.filter((a, i) =>
    a.trim().toLowerCase() === items[i].answer.toLowerCase()
  ).length;

  return (
    <div className="exercise-container">
      <div className="progress-header">
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${(2 / 10) * 100}%` }}></div>
        </div>
        <span className="progress-text">2/10</span>
      </div>

      <h2>Part 4 — Key Word Transformations</h2>
      <p className="instruction">
        Complete the second sentence so that it means the same as the first, using the word given. 
        You must use between two and five words.
      </p>

      <div className="text-content">
        {items.map((item, i) => (
          <div key={i} style={{ marginBottom: "24px" }}>
            <p>
              <strong>{i + 1}.</strong> {item.question}
            </p>
            <p>
              <strong>Keyword:</strong> {item.base.toUpperCase()}
            </p>
            <input
              type="text"
              placeholder="Type your transformed sentence..."
              value={answers[i]}
              onChange={(e) => {
                const copy = [...answers];
                copy[i] = e.target.value;
                setAnswers(copy);
              }}
              className={checked ? (answers[i].trim().toLowerCase() === item.answer.toLowerCase() ? "correct" : "wrong") : ""}
              style={{ width: "100%", marginTop: "6px" }}
            />
          </div>
        ))}
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answers</button>
      ) : (
        <div className={`feedback-box ${correctCount === items.length ? "success" : "error"}`}>
          <p className="feedback">
            {correctCount === items.length
              ? "✅ Perfect!"
              : `You got ${correctCount} out of ${items.length} correct.`}
          </p>
        </div>
      )}
    </div>
  );
};

export default KeyWordTransformations;
