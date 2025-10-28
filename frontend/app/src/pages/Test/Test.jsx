import Card from "../../components/Card"
import styles from "./styles.module.css"

function Test() {
    return <>
        <section className={styles.SubWikiSection}>
            {[1, 2, 3, 4, 5, 6].map((num) => (
                <Card name="Test" image="https://avatars.githubusercontent.com/u/190509242?v=4" />  
            ))}
        </section>
    </>
}

export default Test;