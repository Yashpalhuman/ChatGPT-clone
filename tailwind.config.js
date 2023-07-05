/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        // chadblack: 'rgba(52,53,65,var(--tw-bg-opacity))',
        chadblack: {50:'#343541'}
      }

    },
  },
  plugins: [],
}

