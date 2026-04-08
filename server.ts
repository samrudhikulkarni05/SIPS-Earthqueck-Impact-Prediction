import express from "express";
import { createServer as createViteServer } from "vite";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function startServer() {
  const app = express();
  const PORT = 3000;

  // API routes
  app.get("/api/health", (req, res) => {
    res.json({ status: "ok", message: "SIPS Backend is running" });
  });

  // Mock API for seismic alerts
  app.get("/api/alerts", (req, res) => {
    res.json([
      { loc: 'Hokkaido, Japan', mag: '5.2', time: '12m ago', risk: 'Medium' },
      { loc: 'Antofagasta, Chile', mag: '4.1', time: '45m ago', risk: 'Low' },
      { loc: 'Lombok, Indonesia', mag: '6.4', time: '2h ago', risk: 'High' },
      { loc: 'California, USA', mag: '3.8', time: '4h ago', risk: 'Low' },
      { loc: 'Athens, Greece', mag: '4.5', time: '6h ago', risk: 'Medium' },
      { loc: 'Sichuan, China', mag: '5.9', time: '8h ago', risk: 'High' },
    ]);
  });

  // Vite middleware for development
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath));
    app.get('*', (req, res) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`SIPS Server running on http://localhost:${PORT}`);
  });
}

startServer();
