# Fase 8 — Producción con Higgsfield MCP

> Video, animaciones, voz, música, edición, subtítulos. Ver `CLAUDE.md` para el flujo recomendado de herramientas `mcp__HIGGSFIELD__*`.

> **Nota de alcance de esta fase:** al iniciar la Fase 8 se verificó el saldo de la cuenta Higgsfield conectada a este entorno: **110 créditos, plan Plus**. Generar los 43 assets del storyboard (video, imágenes, voz, música, SFX) consume muchos más créditos que ese saldo, y generarlos es una acción que gasta recursos reales y no es reversible. Por decisión explícita del usuario, este documento es el **plan de producción completo** — herramienta, prompt e input exactos para cada escena — listo para ejecutarse escena por escena cuando se autorice el gasto de créditos. **Ningún asset final ha sido generado todavía**; la columna "Resultado" queda marcada como pendiente en todas las filas.

## Voz de narración

**Voz elegida (`list_voices` / `create_voice`):** pendiente de audición final, pero preseleccionada a partir de `list_voices` (30 voces exploradas):

| Candidata | Voice ID | Género | Por qué se preselecciona |
|---|---|---|---|
| **Sterling** *(principal recomendada)* | `dc382508-c8bd-443c-8cb2-46e57b8d2e6f` | Masculino | Nombre y catálogo sugieren registro grave/serio, adecuado al tono "expediente" sobrio del guion — **a confirmar escuchando `preview_url` antes de generar cualquier locución final** |
| Arthur *(alternativa 1)* | `30fc8796-ceb6-4a66-b3a7-4a145ef7f346` | Masculino | Alternativa de registro clásico/documental |
| Harrison *(alternativa 2)* | `573e5163-59b3-4926-aab1-951ef2985f81` | Masculino | Alternativa si se busca un tono más cálido que "Sterling" |
| Vesper *(alternativa de género)* | `c3204739-4084-41a3-9dc5-c805b307ec18` | Femenino | Por si se decide narración femenina — registro sobrio sugerido por el catálogo |

**Herramienta de generación:** `text2speech_v2` con `variant: "elevenlabs"` (motor de mayor calidad percibida para narración documental larga) y `voice_type: "preset"` + el `voice_id` elegido. Alternativa: `generate_audio` con `seed_audio` si se prefiere ajustar `speech_rate`/`pitch_rate` finamente.

**Acción antes de generar:** escuchar los 4 `preview_url` listados arriba y confirmar la voz definitiva — no se genera narración final sin esta confirmación humana, dado que es la voz de toda la serie documental, no solo de este video.

**Segmentación de la narración:** se generará en 14 clips de audio independientes (uno por Hook, Actos 0–10, Conclusión y CTA), no en una sola toma continua, para poder ajustar ritmo/pausas por bloque sin regenerar el video completo si se necesita un cambio puntual.

## Assets por escena

> Convención de modelos usada abajo: **Seedance 2.0** (`seedance_2_0`) para los dos sets recurrentes con continuidad de identidad visual entre callbacks (sala de archivo, salón de Nicea); **Cinema Studio Video** (`cinematic_studio_video_v2`) para recreaciones históricas puntuales con movimiento de cámara sutil; **Nano Banana 2** (`nano_banana_2`) para fotogramas fijos fotorrealistas (manuscritos, artefactos) que luego alimentan a los modelos de video como `start_image`; **Recraft V4.1** (`recraft_v4_1`, `model_type: vector` o `utility`) para infografías, sellos y grafismos de texto. Todas las recreaciones de figuras históricas (Marción, Ireneo, Orígenes, Eusebio, Atanasio) se generan **explícitamente como siluetas/perfiles sin rasgos faciales inventados**, consistente con la nota de `05-storyboard.md`.

| Escena (# del storyboard) | Herramienta usada | Prompt / input | Resultado (id/url) | Post-proceso aplicado |
|---|---|---|---|---|
| 1 | `nano_banana_2` (still base) → `seedance_2_0` (start_image = still) | "Minimalist reconstruction of the Council of Nicaea, 325 AD, wide frontal shot, bishops seated in semicircle, cold blue window light, no ornate decoration, restrained historical documentary style, no dramatization" · video: dolly-in muy sutil, 7s, 720p | PENDIENTE | Guardar como referencia de "set Nicea" para reusar en escenas 2 y 28 (continuidad visual vía `image_references`) |
| 2 | `recraft_v4_1` (`model_type: utility`) | Tipografía "NICEA, 325 d.C." → "LO QUE NO DEBATIÓ: QUÉ LIBROS IBAN EN TU BIBLIA.", fondo negro, alto contraste | PENDIENTE | Animación de aparición de texto en edición (corte seco, sin motion nativo) |
| 3 | `nano_banana_2` (still) → `seedance_2_0` | "Dark wooden archive table, ancient manuscripts and facsimiles arranged as case-file evidence, warm single lamp light, rest in shadow, top-down composition" · video: travelling cenital lento, 8s | PENDIENTE | Guardar como referencia de "set sala de archivo" para escenas 4, 5, 38, 40, 41 |
| 4 | `seedance_2_0` (image_references = still de escena 3) | "Same archive table, hands (no face) arranging documents next to five small stamp-icons representing evidence categories" · dolly lateral lento, 8s | PENDIENTE | — |
| 5 | `recraft_v4_1` (`model_type: vector`) | Cinco sellos minimalistas con las etiquetas HECHO / HIPÓTESIS / INTERPRETACIÓN / TRADICIÓN / CONSENSO ACADÉMICO, estilo sello de goma, paleta neutra | PENDIENTE | Secuencia de aparición (stamp-in) animada en edición |
| 6 | `nano_banana_2` → `cinematic_studio_video_v2` | "Animated-style map of the eastern Mediterranean, glowing gold trade routes connecting Ephesus, Corinth, Rome, Antioch, parchment-dark background" · push-in gradual, 8s | PENDIENTE | — |
| 7 | `nano_banana_2` | "Macro photo of ancient Greek papyrus fragment, warm side lighting, shallow depth of field, hand (no face) pointing at a line of text" | PENDIENTE | Reframe a 16:9 si se necesita recorte fino |
| 8 | `nano_banana_2` → `cinematic_studio_video_v2` | "Hands closing an archival manuscript case box, warm archive lighting" · dolly lento hacia atrás, 6s | PENDIENTE | — |
| 9 | `nano_banana_2` → `cinematic_studio_video_v2` | "Sealed clay jar in near-silhouette, very dim backlight, mysterious tone" · zoom lento in, 6s | PENDIENTE | — |
| 10 | `nano_banana_2` → `cinematic_studio_video_v2` | "Minimalist Roman interior recreation, 144 AD, silhouette of a man facing an unrolled scroll on a stand, candlelight" · travelling lateral, 8s | PENDIENTE | — |
| 11 | `nano_banana_2` → `cinematic_studio_video_v2` | "A door closing, a scroll left outside the frame, warm interior backlight through doorway" · cámara en mano controlada, 6s | PENDIENTE | — |
| 12 | `recraft_v4_1` (`model_type: vector`) | Infografía: lista del "Apostolikón" de Marción junto a la lista de 27 libros actuales, comparación visual clara | PENDIENTE | Overlay animado en edición |
| 13 | `recraft_v4_1` (`model_type: utility`) | Split screen con nombres/cita breve de McDonald y de Vinzent–BeDuhn, mismo peso visual, fondo neutro oscuro | PENDIENTE | — |
| 14 | `nano_banana_2` → `cinematic_studio_video_v2` | "Scriptorium interior in Lyon, 180 AD, bishop silhouette dictating to a scribe copying by candlelight, monastic atmosphere" · dolly-in lento, 8s | PENDIENTE | — |
| 15 | `nano_banana_2` | "Illuminated medieval-style manuscript page with the four evangelist symbols (lion, ox, man, eagle), warm golden lighting, macro" | PENDIENTE | Paneo lento aplicado en edición (Ken Burns) |
| 16 | `recraft_v4_1` (`model_type: vector`) | Infografía: brújula de 4 puntos cardinales transformándose en los 4 evangelios, minimalista | PENDIENTE | Animación de transformación en edición |
| 17 | `nano_banana_2` → `cinematic_studio_video_v2` | "Macro shot of a damaged ancient Latin manuscript fragment, forensic-style top lighting, evidence-table presentation" · cámara fija, push-in leve, 8s | PENDIENTE | Guardar como referencia para escenas 18, 20, 21 (continuidad del fragmento) |
| 18 | `recraft_v4_1` (overlay sobre still de escena 17) | Sello rojo "EN DISPUTA" estampado sobre la imagen congelada del fragmento | PENDIENTE | Freeze frame + overlay compuesto en edición |
| 19 | `recraft_v4_1` (`model_type: vector`) | Línea de tiempo bifurcada: "s. II — consenso mayoritario" vs. "s. IV — Sundberg/Hahneman", con nombres en pantalla | PENDIENTE | — |
| 20 | `seedance_2_0` (image_references = still de escena 17) | "Magnifying glass slowly moving across the Latin fragment text, forensic lighting" · push-in lento, 6s | PENDIENTE | — |
| 21 | `seedance_2_0` (image_references = still de escena 17) | "Full fragment shot, camera pulling back, forensic light warming to amber" · pull-out lento, 6s | PENDIENTE | — |
| 22 | `nano_banana_2` → `cinematic_studio_video_v2` | "Conceptual ancient library interior, Alexandria, shelves of scrolls, silhouette of a scholar sorting scrolls onto three tables, warm dust-lit atmosphere" · travelling lateral amplio, 8s | PENDIENTE | — |
| 23 | `nano_banana_2` | "Three tables with clearly distinct piles of scrolls, differentiated by texture/tag, warm golden light" | PENDIENTE | Paneo horizontal lento en edición |
| 24 | `nano_banana_2` → `cinematic_studio_video_v2` | "Ecclesiastical study interior in Caesarea, silhouette of a historian writing lists on parchment, side window light" · dolly-in, 6s | PENDIENTE | — |
| 25 | `recraft_v4_1` (`model_type: vector`) | Infografía de 3 categorías (homologoúmena / antilegómena / nótha) con libros asociados a cada una | PENDIENTE | — |
| 26 | `nano_banana_2` → `cinematic_studio_video_v2` | "Roman street, soldiers confiscating scrolls from a house, sober restrained treatment, no violence close-ups, harsh midday light" · cámara en mano controlada, 8s | PENDIENTE | — |
| 27 | `nano_banana_2` → `cinematic_studio_video_v2` (`sound: on` para el crepitar) | "A scroll burning, controlled framing, warm firelight, brief shot" · estático corto, 4s | PENDIENTE | — |
| 28 | `seedance_2_0` (image_references = still de escena 1) | Mismo set del Hook (salón de Nicea), repite el mismo movimiento de cámara del plano 1 para el callback | PENDIENTE | Verificar continuidad exacta de encuadre respecto al plano 1 |
| 29 | `recraft_v4_1` (`model_type: utility`) | Texto de actas conciliares resaltando "naturaleza de Cristo", "fecha de la Pascua", "Credo" — sin mención de canon | PENDIENTE | — |
| 30 | `recraft_v4_1` (`model_type: vector`) | Split screen: silueta genérica de portada de novela de ficción (sin logos/marcas reales) vs. facsímil de acta | PENDIENTE | Verificar que no se use ninguna marca/portada real con derechos de autor |
| 31 | `nano_banana_2` → `cinematic_studio_video_v2` | "Alexandria interior, 367 AD, bishop silhouette sealing a Paschal letter, warm candlelight" · dolly-in lento, 8s | PENDIENTE | — |
| 32 | `recraft_v4_1` (`model_type: vector`) | Lista numerada 1–27 apareciendo progresivamente, tipografía elegante, fondo oscuro | PENDIENTE | Animación de aparición secuencial en edición |
| 33 | `nano_banana_2` → `cinematic_studio_video_v2` | "Egyptian desert, 1945, two silhouetted figures digging near a rock formation, golden sunset light, aerial framing" · aéreo con push-in, 8s | PENDIENTE | — |
| 34 | `nano_banana_2` → `cinematic_studio_video_v2` | "Half-open clay jar with papyrus codices visible inside, warm dim backlight of sunset" · macro push-in, 5s | PENDIENTE | — |
| 35 | `nano_banana_2` → `cinematic_studio_video_v2` | "North African council hall, Hippo, assembly of bishops, warm Mediterranean light" · travelling lateral, 8s | PENDIENTE | — |
| 36 | `recraft_v4_1` (overlay) | Sello "RATIFICADO" estampándose sobre facsímil de acta conciliar | PENDIENTE | — |
| 37 | `recraft_v4_1` (`model_type: vector`) | Icono "lista ya existente" (izquierda) + icono de concilio (derecha) + flecha de confirmación, no de creación | PENDIENTE | — |
| 38 | `seedance_2_0` (image_references = still de escena 3) | Mismo set de sala de archivo, ahora con documentos ordenados cronológicamente sobre la mesa | PENDIENTE | — |
| 39 | `recraft_v4_1` (`model_type: utility`) | Split screen equilibrado: cita breve de Kruger y de Ehrman, mismo tamaño/peso tipográfico | PENDIENTE | — |
| 40 | `seedance_2_0` (image_references = still de escena 3) | Mesa de archivo completa, cámara alejándose revelando todos los documentos en orden cronológico | PENDIENTE | — |
| 41 | `recraft_v4_1` (`model_type: vector`) | Título del documental sobre la lista de 27 libros desenfocada de fondo | PENDIENTE | — |
| 42 | `recraft_v4_1` (`model_type: utility`) | Texto "Próximo expediente: los manuscritos" + miniatura sutil del siguiente documental | PENDIENTE | — |
| 43 | `recraft_v4_1` (`model_type: vector`) | Ícono minimalista de campana/suscripción + texto de pregunta para comentarios | PENDIENTE | — |

## Música y SFX

**Herramientas exploradas:** `models_explore(type: "audio")` devolvió, además de los modelos de voz, dos modelos específicos de música/SFX: **Sonilo Music** (`sonilo_music`, texto-a-música instrumental) y **Mirelo Text to Audio** (`mirelo_text_to_audio`, texto-a-SFX). **Ambos aparecen etiquetados en el catálogo como "Game pipeline only"** — antes de generar la banda sonora hay que confirmar si estas herramientas están disponibles fuera de flujos de creación de videojuegos en este entorno MCP, o si esa restricción bloquea su uso aquí. **Riesgo de producción a resolver antes de ejecutar esta sección:** si `sonilo_music`/`mirelo_text_to_audio` no están disponibles, la alternativa es una biblioteca de música/SFX libre de regalías fuera de Higgsfield (a definir).

**Plan de música (si `sonilo_music` está disponible):**
- Motivo principal ("leitmotiv Nicea"): cuerdas graves + drone de cello, usado en planos 1, 2 y 28 (callback).
- Motivo "sala de archivo": piano minimalista, usado en planos 3, 4, 5, 38, 40, 41.
- Motivo "expediente en disputa": cuerdas con tensión no resuelta, para planos 12, 13, 18, 19, 20.
- Resolución final: cuerdas + coro sutil en crescendo controlado, plano 40–41.

**Plan de SFX (si `mirelo_text_to_audio` está disponible):** sello de goma (planos 5, 18, 36), pluma rascando papel (planos 14, 24), fuego crepitando (plano 27), viento/puerto de fondo (plano 6), excavación en arena (plano 33).

## Subtítulos

**Idioma(s):** inglés como pista de subtítulos principal (coincide con la narración final decidida en Fase 6/público objetivo de Fase 1). Español como segunda pista, generada con la herramienta `dubbing` de Higgsfield MCP a partir del audio final en inglés — no se traduce el guion de nuevo desde cero, se dobla/subtitula desde el máster en inglés para evitar discrepancias entre versiones.

## Chequeo de virality (opcional, antes de publicar)

**Resultado de `virality_predictor`:** no ejecutado todavía — requiere un corte del video ya montado (aunque sea preliminar), y en esta fase no se ha generado ningún asset final. **Siguiente acción cuando exista un primer corte:** correr `virality_predictor` sobre el video montado y registrar aquí el resultado antes de publicar.

**Ajustes hechos en respuesta (si los hubo — nunca para sensacionalizar):** pendiente, se documentará cuando exista resultado.

**Siguiente paso:** completar `07-paquete-youtube.md`.
