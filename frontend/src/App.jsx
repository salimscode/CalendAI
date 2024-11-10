import Navbar from './components/Navbar'
import HeroSection from './components/HeroSection'
import { Link } from 'react-router-dom'; 
import './App.css'

function App() {
  return (
    <div className="main">  
      <Navbar />
      <HeroSection /> 
      <div className="buttonContainer">
          <h3 className="heroButton">
            <Link className="link" to="/login">
              get started
            </Link>
          </h3>
      </div>
    </div>
  )
}

export default App
