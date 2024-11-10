import Navbar from "../components/Navbar";

const LoginPage = () => {
    return (
        <div className="main">
            <Navbar />
            <form className="loginForm">
                <h1>login</h1>
                <div className="formSection">
                    <label htmlFor="username">Username:</label>
                    <input type="text" name="username"/>
                </div>
                <div className="formSection">
                    <label htmlFor="password">Password:</label>
                    <input type="password" name="password"/>
                </div>
                <h3 className="button">log in</h3>
            </form>
        </div>
    );
}
 
export default LoginPage;