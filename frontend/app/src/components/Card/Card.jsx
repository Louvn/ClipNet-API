import styles from "./styles.module.css"

function SubWiki({image, name}) {
    return <div className={styles.SubWikiCard}>
        <img className={styles.SubWikiImage} src={image} alt="" />
        <h2 className={styles.SubWikiName}>{name}</h2>
        <button className={styles.SubWikiButton}>Open</button>
    </div>
}

export default SubWiki