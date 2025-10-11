import React, { useState } from "react";
import "./ExerciseStyles.css";

const Reading2: React.FC = () => {
  const [selectedAnswers, setSelectedAnswers] = useState<{[key: number]: string}>({});
  const [currentQuestion, setCurrentQuestion] = useState(1);
  
  const readingText = `Technology has revolutionized the way we communicate and access information. In the past two decades, we have witnessed an unprecedented transformation in how people connect with each other. Social media platforms, instant messaging applications, and video conferencing tools have made it possible to maintain relationships across great distances.

However, this digital revolution has also brought challenges. Many researchers argue that while technology has increased our global connectivity, it has simultaneously decreased the quality of face-to-face interactions. Studies show that people now spend more time looking at screens than engaging in personal conversations.

Furthermore, the constant stream of information can lead to cognitive overload. The ability to focus on complex tasks has become more difficult for many individuals. Despite these challenges, technology continues to evolve, offering new solutions to these very problems through digital wellness tools and mindful design approaches.`;

  const questions = [
    {
      id: 1,
      question: "What is the main topic of the passage?",
      options: [
        "A. The history of technology",
        "B. Impact of technology on communication",
        "C. Social media platforms",
        "D. Digital wellness tools"
      ],
      correct: "B"
    },
    {
      id: 2,
      question: "According to the text, what has technology increased?",
      options: [
        "A. Face-to-face interactions",
        "B. Global connectivity",
        "C. Personal conversations",
        "D. Cognitive abilities"
      ],
      correct: "B"
    },
    // Add 8 more questions...
  ];

  const handleSelect = (questionId: number, option: string) => {
    setSelectedAnswers(prev => ({
      ...prev,
      [questionId]: option
    }));
  };

  return (
    <div className="exercise-container reading-container">
      <div className="reading-layout">
        {/* Left Column - Reading Text */}
        <div className="reading-passage">
          <h3>Reading Passage</h3>
          <div className="passage-content">
            {readingText.split('\n').map((paragraph, index) => (
              <p key={index}>{paragraph}</p>
            ))}
          </div>
        </div>

        {/* Right Column - Questions */}
        <div className="questions-panel">
          <h3>Questions</h3>
          <div className="questions-navigation">
            {questions.map(q => (
              <button
                key={q.id}
                className={`nav-btn ${currentQuestion === q.id ? 'active' : ''} ${
                  selectedAnswers[q.id] ? 'answered' : ''
                }`}
                onClick={() => setCurrentQuestion(q.id)}
              >
                {q.id}
              </button>
            ))}
          </div>

          <div className="current-question">
            <p className="question-text">
              {currentQuestion}. {questions[currentQuestion - 1].question}
            </p>
            <div className="options-vertical">
              {questions[currentQuestion - 1].options.map(option => (
                <button
                  key={option}
                  className={`option-btn ${
                    selectedAnswers[currentQuestion] === option.charAt(0) ? 'selected' : ''
                  }`}
                  onClick={() => handleSelect(currentQuestion, option.charAt(0))}
                >
                  {option}
                </button>
              ))}
            </div>
          </div>

          <div className="reading-footer">
            <button 
              className="btn"
              disabled={Object.keys(selectedAnswers).length !== questions.length}
            >
              Complete Exercise
            </button>
            <div className="progress">
              {Object.keys(selectedAnswers).length}/{questions.length} answered
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Reading2;