module.exports = {
  // Configuración de los archivos que Tailwind CSS debe analizar para purgar estilos no utilizados
  // En este caso, se analizan index.html y main.js para detectar clases CSS utilizadas
  content: [
    './templates/**/*.html',  // Añade todos los archivos HTML en templates
    './static/**/*.js'        // Añade todos los archivos JS en static
  ],
  
  // Configuración del modo oscuro
  // 'class' indica que el modo oscuro se activará mediante una clase CSS (.dark)
  // Esto permite controlar el tema oscuro mediante JavaScript o manualmente
  darkMode: 'class',
  
  // Configuración del tema de Tailwind
  // 'extend' permite extender las configuraciones por defecto de Tailwind
  // En este caso está vacío, pero aquí se podrían añadir colores personalizados, fuentes, etc.
  theme: {
    extend: {
      colors: {
        'custom-blue': '#1e40af',
        'custom-green': '#10b981',
      },
      fontFamily: {
        'sans': ['Inter', 'sans-serif'],
      },
      backgroundImage: {
        'custom-bg': "url('/static/images/background.jpg')"
      },
      objectFit: {
        'cover': 'cover',
        'contain': 'contain',
      },
    },
  },
  
  // Configuración de plugins de Tailwind
  // Aquí se pueden añadir plugins adicionales para extender funcionalidades
  plugins: [
    require('@tailwindcss/forms'),  // Añade el plugin de forms si lo necesitas
    require('@tailwindcss/typography'),
  ],
};