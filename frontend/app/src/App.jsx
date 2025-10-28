import { Routes, Route, Navigate } from "react-router-dom"
import { useState, useEffect } from "react"
import Test from "./pages/Test"
import Login from "./pages/Login"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer"

function App() {
    const [isLoggedIn, setLoggedIn] = useState(localStorage.getItem("jwt") ? true : false);
    useEffect(() => {
        const handleStorageChange = (event) => {
            setLoggedIn(event.detail ? true: false);
        }

        window.addEventListener("jwtChange", handleStorageChange);
        return () => window.removeEventListener("jwtChange", handleStorageChange);
    }, []);

    const ProtectedRoutes = ({children}) => {
        if (isLoggedIn) {
            return children
        }
        return <Navigate to="/login" />
    }

    return <>
        {isLoggedIn && <Navbar />}
        <main>
            <Routes>

                {/* public Routes */}
                <Route path="/login" element={<Login />} />

                {/* private Routes */}
                <Route
                    path="/*"
                    element={
                        <ProtectedRoutes>
                            <Routes>
                                <Route path="/" element={<Test />} />
                            </Routes>
                        </ProtectedRoutes>
                    }
                />
            
            </Routes>
        </main>

        {isLoggedIn && <Footer />}
    </>
}

export default App;