import React from "react";
import FillBlank from "../ExerciseTypes/FillBlank";
import Listening from "../ExerciseTypes/Listening";
import Reading from "../ExerciseTypes/Reading";
import Writing from "../ExerciseTypes/Writing";
import Speaking from "../ExerciseTypes/Speaking";

interface Props {
  type: "grammar" | "listening" | "reading" | "writing" | "speaking";
}

const ExerciseView: React.FC<Props> = ({ type }) => {
  switch (type) {
    case "grammar":
      return <FillBlank />;
    case "listening":
      return <Listening />;
    case "reading":
      return <Reading />;
    case "writing":
      return <Writing />;
    case "speaking":
      return <Speaking />;
    default:
      return null;
  }
};

export default ExerciseView;
