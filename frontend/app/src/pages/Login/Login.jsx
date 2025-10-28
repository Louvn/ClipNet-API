import { useLocation, useNavigate, Navigate } from "react-router-dom";
import { useState } from "react";
import styles from "./styles.module.css";
import Logo from "../../assets/logo-blue.png";
import config from "../../config.json"

function Login() {
    const location = useLocation();
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");

    if (localStorage.getItem("jwt")) {
        return <Navigate to="/" />;
    }
    
    const handleSubmit = async (event) => {
        event.preventDefault();
        
        const response = await fetch(config.apiUrl + "/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                username: username,
                password: password
            })
        });
    
        const data = await response.json();

        if (!response.ok) {
            setErrorMessage(data.detail);
            return;
        }
        
        localStorage.setItem("jwt", data.access_token);
        window.dispatchEvent(new CustomEvent("jwtChange", { detail: localStorage.getItem("jwt") }));
        const params = new URLSearchParams(location.search);
        return navigate(params.get("redirect") || "/", {replace: true});
    }

    return <div className={styles.LoginPage}>
        <form className={styles.LoginForm} onSubmit={handleSubmit}>
            
            <div className={styles.Heading}>
                <h1 className={styles.Logo}>
                    <img className={styles.LogoImg} src={Logo} alt="" />
                    <span className={styles.LogoText}>ClipNet</span>
                </h1>
                <p>This Website is private</p>
            </div>

            <input 
                className={`${styles.LoginInput} ${errorMessage ? styles.Error: ""}`}
                type="text" 
                name="username" 
                aria-label="username" 
                placeholder="username"
                required
                onChange={(e) => setUsername(e.target.value)}
                autoCapitalize="none"
                />

            <input 
                className={`${styles.LoginInput} ${errorMessage ? styles.Error: ""}`}
                type="password" 
                name="password" 
                aria-label="password" 
                placeholder="password" 
                required
                onChange={(e) => setPassword(e.target.value)}
                autoCapitalize="none"
                />

            {errorMessage && <span className={styles.ErrorMessage}>{errorMessage}</span>}

            <label className={styles.RememberMe}>
                <input type="checkbox" name="remember-me" value="false" className={styles.RememberMeInput} defaultChecked/>
                remember me
            </label>

            <button className={styles.LoginButton} type="submit">Login</button>
        </form>
    </div>
}

export default Login;