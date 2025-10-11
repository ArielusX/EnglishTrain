
import './App.css'
import TemplateCard from './components/TemplateCard/TemplateCard'
import Hero from './components/Hero/Hero'
import ExerciseMenu from './components/ExerciseMenu/ExerciseMenu'
import FillBlank from './components/ExerciseTypes/FillBlank'
import Reading from './components/ExerciseTypes/Reading'
import Speaking from './components/ExerciseTypes/Speaking'
import Writing from './components/ExerciseTypes/Writing'
import MultipleChoiceCloze from './components/ExerciseTypes/MultipleChoiceCloze'
import KeyWordTransformations from './components/ExerciseTypes/KeyWordTransformations'
import OpenCloze from './components/ExerciseTypes/OpenCloze'
import WordFormation from './components/ExerciseTypes/WordFormation'

function App() {
 

  return (
    <>
    <FillBlank/>
    <MultipleChoiceCloze/>
    <KeyWordTransformations/>
    <OpenCloze/>
    <WordFormation/>
    <Reading/>
    <Speaking/>
    <Writing/>
    <ExerciseMenu/>

             <Hero />

<div className='flex'>   <TemplateCard
  title={"Grammar"}
  description={"Ejercicios de grammas"}
  category={"English"}
  exercises={6}
  onGenerate={() => console.log("Generar PDF")}
 />   <TemplateCard
  title={"Grammar"}
  description={"Ejercicios de grammas"}
  category={"English"}
  exercises={6}
  onGenerate={() => console.log("Generar PDF")}
 />   <TemplateCard
  title={"Grammar"}
  description={"Ejercicios de grammas"}
  category={"English"}
  exercises={6}
  onGenerate={() => console.log("Generar PDF")}
 /></div>
   

    </>
  )
}

export default App
