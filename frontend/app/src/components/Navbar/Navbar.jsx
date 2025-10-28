import {Link} from "react-router-dom"
import styles from "./styles.module.css"
import logoImg from "../../assets/logo-white.png"

function Navbar() {
    return <nav className={styles.Navbar}>
        <Link to="/" className={styles.Logo}>
            <img src={logoImg} alt="" className={styles.LogoImg} />
            <h1 className={styles.LogoText}>ClipNet</h1>
        </Link>
    </nav>
}

export default Navbar;