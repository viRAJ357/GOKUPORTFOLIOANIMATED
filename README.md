# 3Dfolio: Goku Portfolio Animated

## Description
This is an immersive, high-performance 3D portfolio website built with React, Three.js (@react-three/fiber), and Vite. It features a full-screen, pure-black design highlighting a high-fidelity holographic 3D character hero animation (Goku model) that tracks the user's mouse. The scene is illuminated by additive blending with a custom galaxy particle background and includes high-quality typography with smooth section transitions, heavily inspired by modern interactive aesthetic portfolios.

## Project Screenshot
![Project Preview](./app/src/assets/herobg.png)

## Project Structure
```text
PORTFOLIOGOKU/
├── app/
│   ├── public/              # Static public assets (e.g. 3D models like scene.gltf, logos)
│   ├── src/
│   │   ├── assets/          # Project images, textures, and icons
│   │   ├── components/      # React components (Contact, Experience, Works, Preloader, Hero, etc.)
│   │   │   └── canvas/      # Three.js specific 3D components (HoloModel, Galaxy, Earth, etc.)
│   │   ├── constants/       # User data and content
│   │   ├── utils/           # Helper scripts
│   │   ├── App.jsx          # Main App entry with all configured components
│   │   ├── index.css        # Global CSS + Tailwind config
│   │   └── main.jsx         # ReactDOM render entry point
│   ├── package.json         # Project dependencies and scripts
│   ├── tailwind.config.cjs  # Tailwind settings
│   └── vite.config.js       # Vite configurations
├── deploy_hf.py             # Script for HuggingFace deployment
└── README.md                # Project README details
```

## Technologies Used
- **React.js**: For component-driven architecture and state management.
- **Three.js & React Three Fiber/Drei**: For building and rendering the custom 3D HoloModel and Galaxy scene.
- **Tailwind CSS**: For custom, utility-first styling.
- **Framer Motion**: For elegant layout animations and micro-interactions.

## Setup and Installation

1. Clone the repository and navigate to the `app` directory:
   ```bash
   cd app
   ```
2. Install the necessary dependencies:
   ```bash
   npm install
   ```
3. Run the fast local development server:
   ```bash
   npm run dev
   ```

## Deployment
The project is set up to generate a highly optimized static build that can be hosted anywhere (Vercel, Netlify, GitHub Pages). 
A simple python script `deploy_hf.py` is included to easily deploy the built `app/dist` folder to HuggingFace spaces. Just ensure `HF_TOKEN` is passed via the environment variables.
