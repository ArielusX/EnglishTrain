import React, { useState } from "react";
import "./ExerciseStyles.css";

const WordFormation = () => {
  const data = [
    { base: "CREATE", answer: "creative" },
    { base: "BEAUTY", answer: "beautiful" },
    { base: "DECIDE", answer: "decision" },
    { base: "MUSIC", answer: "musician" },
  ];

  const [answers, setAnswers] = useState(Array(data.length).fill(""));
  const [checked, setChecked] = useState(false);

  const correctCount = answers.filter((a, i) => a.trim().toLowerCase() === data[i].answer).length;

  return (
    <div className="exercise-container">
      <div className="progress-header">
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: `${(4 / 10) * 100}%` }}></div>
        </div>
        <span className="progress-text">4/10</span>
      </div>

      <h2>Part 3 — Word Formation</h2>
      <p className="instruction">Use the word given in capitals to form a word that fits the gap.</p>

      <div className="text-content">
        {data.map((item, i) => (
          <p key={i}>
            0{i + 1}. Her paintings are very{" "}
            <input
              type="text"
              value={answers[i]}
              onChange={(e) => {
                const copy = [...answers];
                copy[i] = e.target.value;
                setAnswers(copy);
              }}
              className={checked ? (answers[i].trim().toLowerCase() === item.answer ? "correct" : "wrong") : ""}
            />{" "}
            ( {item.base} )
          </p>
        ))}
      </div>

      {!checked ? (
        <button className="btn" onClick={() => setChecked(true)}>Check Answers</button>
      ) : (
        <div className={`feedback-box ${correctCount === data.length ? "success" : "error"}`}>
          <p className="feedback">
            {correctCount === data.length
              ? "✅ Perfect!"
              : `You got ${correctCount} out of ${data.length} correct.`}
          </p>
        </div>
      )}
    </div>
  );
};

export default WordFormation;
