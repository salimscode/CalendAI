import logo from '../assets/logo.webp'; 

const Navbar = () => {
    return ( 
        <div className="navbar">
            <div className="companyInfo">
                <img className="logo" src={logo}></img>
                <h1>CalendAI</h1>
            </div>
            <div className="cta-section">
                <h2 className="link">Log In</h2>
            </div>
        </div>
     );
}
 
export default Navbar;