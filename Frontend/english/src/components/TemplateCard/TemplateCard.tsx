import React from "react";
import "./TemplateCard.css";

interface TemplateCardProps {
  title: string;
  description: string;
  category: string;
  exercises: number;
  onGenerate: () => void;
}

const TemplateCard: React.FC<TemplateCardProps> = ({
  title,
  description,
  category,
  exercises,
  onGenerate,
}) => {
  return (
    <div className="template-card">
      <div className="template-content">
        <h3 className="template-title">{title}</h3>
        <p>{description}</p>
        <div className="template-meta">
          <span>{category}</span>
          <span>{exercises} ejercicios</span>
        </div>
        <button className="btn" onClick={onGenerate}>
          Generar PDF
        </button>
      </div>
    </div>
  );
};

export default TemplateCard;
