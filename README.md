# Caso de Estudio – Validación de Auditorías con Alertas Smart

Este proyecto implementa un flujo completo para validar auditorías de campo en supermercados, simulando datos, generando alertas y mostrando los resultados en un dashboard con KPIs relevantes. Además, incluye la automatización de reportes y su envío por correo.

---

## 📌 Contexto y Objetivo
La empresa realiza auditorías en tiendas, donde cada cliente requiere un número mínimo de fotos (categorías auditadas + fotos de control).  
El objetivo es **automatizar la validación de auditorías**, identificar alertas cuando no se cumple el mínimo de fotos y generar reportes visuales y tabulares de los resultados.

---

## ⚙️ Enfoque de Solución
- **Generación de datos simulados** con un modelo generativo (LLM).
- **Procesamiento en Python** para calcular mínimos requeridos y detectar alertas.
- **Dashboard en Power BI** con KPIs y gráficas clave.
- **Automatización de reportes**: exportación del dashboard a PDF y envío de alertas por correo.
- **Diseño modular** para facilitar la escalabilidad y mantenibilidad.

---

## 📂 Estructura del Proyecto
- `auditory_market.ipynb` → Notebook con todo el flujo (simulación, validación, dashboard, reportes).
- `Caso_Estudio_AlertasSmart_DataEngineer_GENERATIVO.docx` → Documento con la descripción del caso.
- `dashboard.pdf` → Dashboard generado con KPIs y visualizaciones.
- `output/alertas_completo.xlsx`, `output/alertas_hoy.xlsx` → Reportes automáticos de auditorías con alertas (generado desde el notebook).

---

## 📊 Principales KPIs y Visualizaciones
El dashboard incluye:
- **Total de auditorías simuladas** y % en alerta.  
- **Auditorías con alertas por cliente**.  
- **Fotos esperadas vs fotos faltantes**.  
- **Cumplimiento anual y diario vs target**.  
- **Distribución de auditorías por fecha y por auditor**.  
- **Top de tiendas y categorías con alertas**.   

---

## 📦 Entregables
- Notebook con el flujo completo.  
- Dashboard en PDF.  
- Archivo Excel con alertas.  
- Flujo de envío automático por correo.  

---

## 🔎 Notas Finales
- Los datos utilizados son **simulados** y no corresponden a información real.  
- La solución fue diseñada de manera **modular**, lo que facilita su adaptación a entornos reales y nuevas fuentes de datos.  
