import logo from '../assets/logo.png'; 
import { Link } from 'react-router-dom'; 

const Navbar = () => {
    return ( 
        <div className="navbar">
            <div className="companyInfo">
                <img className="logo" src={logo}></img>
                <Link className="link" to="/">
                    <h1>calendai</h1>
                </Link>
            </div>
            {/* <div className="cta-section">
                <h2 className="button">Log In</h2>
            </div> */}
        </div>
     );
}
 
export default Navbar;