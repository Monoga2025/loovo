# Entorno: Windows + Git Bash (problemas reales y soluciones)

- **Python:** `python3` es un alias de la Microsoft Store que no funciona. Usa `python`.
- **Codificación:** exporta `PYTHONIOENCODING=utf-8` y abre los JSON con `open(..., encoding="utf-8")`. Sin eso fallan las tildes y la ñ.
- **faster-whisper:**
  - con CUDA detectada pero sin `cublas64_12.dll` falla; usa `device="cpu"`;
  - `medium` en int8 falla con `mkl_malloc` si hay menos de unos 2 GB libres; usa `transcribe.py auto`, que cae a `small`;
  - aunque la RAM libre sea poca, el archivo de paginación puede bastar; medium funcionó con 1,3 GB libres y 7 GB de memoria comprometible.
- **ffmpeg y rutas en filtros:** Git Bash convierte `C:/...` dentro de `-vf "ass=...:fontsdir=C\:/Windows/Fonts"` y rompe el filtro. No pases `fontsdir`: libass usa DirectWrite y encuentra las fuentes del sistema solo.
- **ffmpeg 9:** `-vsync` ya no existe; usa `-fps_mode vfr`.
- **Fuentes:** Montserrat y Anton no suelen estar instaladas. Para subtítulos ASS usa Arial Black o Segoe UI Bold; en HyperFrames usa Inter, que va en su caché.
- **RAM:** es el cuello de botella; este equipo tenía 7,7 GB con 1–2 GB libres.
  - Antes de tareas pesadas, consulta la RAM y la memoria comprometible libres (`Get-CimInstance Win32_OperatingSystem`).
  - No cierres procesos del usuario (sus servidores de desarrollo) sin permiso explícito; el clasificador de seguridad lo bloquea.
  - Sí puedes cerrar los procesos huérfanos de **tus** renders.
- **Esperas:** no encadenes `sleep`, está bloqueado. Usa `run_in_background`, un bucle `until ...; do sleep N; done` con timeout de 600 s, o Monitor.
- **Tamaño:** cada versión de `motion/assets` ocupa unos 150 MB y el original copiado 1,1 GB. Avisa del espacio en disco si el usuario guarda versiones.
