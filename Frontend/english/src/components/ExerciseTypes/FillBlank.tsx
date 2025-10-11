import React, { useState } from "react";
import "./ExerciseStyles.css";

const FillBlank = () => {
  const correctAnswers = [
    "is",      // 0
    "because", // 9
    "such",    // 10
    "other",   // 11
    "may",     // 12
    "despite", // 13
    "if",      // 14
    "nothing", // 15
    "in"       // 16
  ];

  const [answers, setAnswers] = useState(Array(9).fill(""));
  const [isChecked, setIsChecked] = useState(false);

  const checkAnswers = () => setIsChecked(true);

  const handleAnswerChange = (index, value) => {
    const newAnswers = [...answers];
    newAnswers[index] = value;
    setAnswers(newAnswers);
  };

  const getInputClass = (index) => {
    if (!isChecked) return "";
    const isCorrect = answers[index].trim().toLowerCase() === correctAnswers[index];
    return isCorrect ? "correct" : "wrong";
  };

  const correctCount = answers.filter((ans, idx) => 
    ans.trim().toLowerCase() === correctAnswers[idx]
  ).length;

  return (
    <div className="exercise-container">
      <div className="progress-header">
        <div className="progress-bar">
          <div 
            className="progress-fill"
            style={{ width: `${(8 / 10) * 100}%` }}
          ></div>
        </div>
        <span className="progress-text">8/10</span>
      </div>

      <h2>Fill in the blank</h2>
      <p className="instruction">Complete the text with the correct words.</p>

      <div className="text-content">
        <p>
          The truth (0){" "}
          <input
            type="text"
            value={answers[0]}
            onChange={(e) => handleAnswerChange(0, e.target.value)}
            placeholder="..."
            className={getInputClass(0)}
          />{" "}
          nobody really knows how language first began. Did we all start talking at around the same time (9){" "}
          <input
            type="text"
            value={answers[1]}
            onChange={(e) => handleAnswerChange(1, e.target.value)}
            placeholder="..."
            className={getInputClass(1)}
          />{" "}
          of the manner in which our brains had begun to develop? Although there is a lack of clear evidence, people have come up with various theories about the origins of language. One recent theory is that human beings have evolved in (10){" "}
          <input
            type="text"
            value={answers[2]}
            onChange={(e) => handleAnswerChange(2, e.target.value)}
            placeholder="..."
            className={getInputClass(2)}
          />{" "}
          a way that we are programmed for language from the moment of birth. In (11){" "}
          <input
            type="text"
            value={answers[3]}
            onChange={(e) => handleAnswerChange(3, e.target.value)}
            placeholder="..."
            className={getInputClass(3)}
          />{" "}
          words, language came about as a result of an evolutionary change in our brains at some stage.
        </p>
        
        <p>
          Language (12){" "}
          <input
            type="text"
            value={answers[4]}
            onChange={(e) => handleAnswerChange(4, e.target.value)}
            placeholder="..."
            className={getInputClass(4)}
          />{" "}
          well be programmed into the brain but, (13){" "}
          <input
            type="text"
            value={answers[5]}
            onChange={(e) => handleAnswerChange(5, e.target.value)}
            placeholder="..."
            className={getInputClass(5)}
          />{" "}
          this, people still need stimulus from others around them. From studies, we know that (14){" "}
          <input
            type="text"
            value={answers[6]}
            onChange={(e) => handleAnswerChange(6, e.target.value)}
            placeholder="..."
            className={getInputClass(6)}
          />{" "}
          children are isolated from human contact and have not learnt to construct sentences before they are ten, it is doubtful they will ever do so. This research shows, if (15){" "}
          <input
            type="text"
            value={answers[7]}
            onChange={(e) => handleAnswerChange(7, e.target.value)}
            placeholder="..."
            className={getInputClass(7)}
          />{" "}
          else, that language is a social activity, not something invented (16){" "}
          <input
            type="text"
            value={answers[8]}
            onChange={(e) => handleAnswerChange(8, e.target.value)}
            placeholder="..."
            className={getInputClass(8)}
          />{" "}
          isolation.
        </p>
      </div>

      {!isChecked ? (
        <button className="btn" onClick={checkAnswers}>Check Answers</button>
      ) : (
        <div className={`feedback-box ${correctCount === 9 ? 'success' : 'error'}`}>
          <p className="feedback">
            {correctCount === 9
              ? "✅ Perfect! All answers are correct!"
              : `You got ${correctCount} out of 9 correct.`}
          </p>
        </div>
      )}
    </div>
  );
};

export default FillBlank;