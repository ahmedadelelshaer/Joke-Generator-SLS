import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import JokeGenerator from './jokemaker'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <JokeGenerator/>
    </div>
      
  )
}

export default App
