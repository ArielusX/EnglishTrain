import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import TemplateCard from './components/TemplateCard/TemplateCard'
import Hero from './components/Hero/Hero'

function App() {
 

  return (
    <>

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
