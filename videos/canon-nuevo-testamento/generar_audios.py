import asyncio
import os
import subprocess
import sys

# Intentar importar edge-tts. Si no está instalado, instalarlo automáticamente.
try:
    import edge_tts
except ImportError:
    print("Instalando la biblioteca edge-tts para voz artificial premium...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
    import edge_tts

# Configuración de voz y rutas
VOICE = "es-MX-JorgeNeural" # Voz masculina, profunda y académica ideal para documentales
OUTPUT_DIR = "/Users/danielvazquez/.gemini/antigravity/scratch/youtube/videos/canon-nuevo-testamento/assets"

# Textos del guion traducidos y adaptados
SCENES = {
    "1": "Existe un mito popular moderno que afirma que un grupo de obispos, reunidos bajo el mandato del emperador Constantino en el Concilio de Nicea, decidió mediante votación qué libros formarían la Biblia cristiana, quemando los evangelios prohibidos.",
    
    "2": "Pero la realidad histórica es profundamente diferente. Las actas oficiales de Nicea demuestran que el concilio no dedicó ni una sola sesión a debatir la lista de los escritos sagrados. La formación de la Biblia no fue una decisión administrativa abrupta, sino un fascinante proceso de siglos.",
    
    "3": "Para comprender cómo llegó a cerrarse la lista de veintisiete libros que hoy componen el Nuevo Testamento, debemos adentrarnos en una historia de persecuciones, herejías, debates teológicos y descubrimientos arqueológicos que redefinen nuestra comprensión del cristianismo primitivo.",
    
    "4": "La palabra canon proviene del griego kanón, que a su vez se deriva de un término semítico que significa caña o vara de medir. En el mundo antiguo, denotaba una regla o criterio de excelencia. Pero en los siglos primero y segundo, los cristianos no usaban esta palabra para listas de libros. Clemente de Roma o Ireneo de Lyon hablaban del canon de la verdad para referirse a la doctrina de la fe, no a un catálogo cerrado de libros sagrados.",
    
    "5": "Por el contrario, el concepto de Escritura o graphé era mucho más fluido. Para los primeros cristianos, la Escritura era la Septuaginta heredada del judaísmo. Un escrito funcionaba como Escritura cuando la comunidad le reconocía autoridad divina y lo leía públicamente en el culto dominical. La función como texto sagrado precedió por siglos a la fijeza de una lista cerrada.",
    
    "6": "Las cartas de Pablo de Tarso y los Evangelios se escribieron originalmente en papiro, un material vegetal accesible importado de Egipto. Sin embargo, mientras el mundo judío y pagano continuaba usando rollos, las comunidades cristianas adoptaron masivamente una innovación tecnológica revolucionaria: el códice, el antepasado del libro moderno.",
    
    "7": "El códice permitía escribir por ambas caras de la hoja, optimizando el costo. Hacía posible compilar los cuatro evangelios en un solo volumen portátil y facilitaba la búsqueda rápida de pasajes bíblicos durante debates teológicos. Escribas cristianos incluso crearon las Nómina Sacra, abreviaturas de devoción para palabras sagradas como Dios o Señor.",
    
    "8": "Alrededor del año 140 después de Cristo, un rico armador llamado Marción de Sínope llegó a Roma con una teología radical: postulaba que el Dios del Antiguo Testamento era un dios de ira inferior, totalmente opuesto al Dios de amor revelado en Jesús. Para respaldar su teología, Marción creó la primera lista formalmente cerrada de escritos autoritativos de la historia.",
    
    "9": "Su catálogo, llamado Evangelikon, contenía únicamente un evangelio de Lucas mutilado, despojado de toda conexión con el judaísmo. Su Apostolikon constaba de diez cartas paulinas editadas. Esta audaz provocación forzó a la gran Iglesia ortodoxa a reaccionar y definir con urgencia los límites reales de sus propios libros sagrados.",
    
    "10": "En el siglo dieciocho, el bibliotecario Ludovico Muratori descubrió un manuscrito en latín vulgar que contenía la lista más antigua que se conserva de libros del Nuevo Testamento. La datación tradicional sitúa el texto original a finales del siglo segundo, lo que significaría que Roma ya poseía un catálogo casi idéntico al actual en el año 170.",
    
    "11": "Sin embargo, la investigación crítica moderna está dividida. Académicos como Albert Sundberg argumentan que el fragmento pertenece en realidad al siglo cuarto debido a su peculiar omisión de epístolas clave como Hebreos o Pedro y la inclusión de obras disputadas. Resolver este enigma define si la fijeza de la Biblia ocurrió de forma orgánica o tardía.",
    
    "12": "En el año 331 después de Cristo, el emperador Constantino encargó a Eusebio de Cesarea la producción de cincuenta copias de las Sagradas Escrituras en pergamino de alta calidad para las nuevas iglesias de Constantinopla. Aunque el Imperio financió la copia, no influyó en la doctrina; fue la Iglesia, basándose en el uso litúrgico continuado, la que dictó el contenido.",
    
    "13": "La fijeza definitiva llegó en el año 367 después de Cristo, cuando el arzobispo Atanasio de Alejandría enumeró en su Carta Festal anual los veintisiete libros exactos que componen el Nuevo Testamento actual. Pocos años después, los sínodos de Hipona y Cartago en Occidente ratificaron formalmente este catálogo bajo la influencia teológica de Agustín de Hipona.",
    
    "14": "La exclusión de los evangelios apócrifos y textos gnósticos, como los hallados en Nag Hammadi en 1945, no fue fruto de una imposición imperial dictatorial. Fue la consecuencia natural de su falta de conexión apostólica y su contradicción teológica con la regla de la fe que las comunidades cristianas habían vivido y defendido con su propia vida desde el primer siglo."
}

async def generate_tts(scene_id, text):
    output_file = os.path.join(OUTPUT_DIR, f"audio_escena_{scene_id}.mp3")
    print(f"Generando audio para Escena {scene_id} -> {output_file}...")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)

async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tasks = [generate_tts(sid, txt) for sid, txt in SCENES.items()]
    await asyncio.gather(*tasks)
    print("\n¡PROCESO COMPLETADO! Todos los audios de voz en off generados con éxito.")

if __name__ == "__main__":
    asyncio.run(main())
