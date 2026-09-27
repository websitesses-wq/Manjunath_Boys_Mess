const http = require('http');
const fs = require('fs');
const path = require('path');

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

function handler(req, res) {
  try {
    let reqUrl = req.url || '/';
    let reqPath = reqUrl.split('?')[0];
    if (reqPath === '/' || reqPath === '') {
      reqPath = '/index.html';
    }

    const filePath = path.join(__dirname, reqPath);

    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath).toLowerCase();
      const contentType = MIME_TYPES[ext] || 'application/octet-stream';
      const fileData = fs.readFileSync(filePath);

      res.writeHead(200, {
        'Content-Type': contentType,
        'Cache-Control': 'public, max-age=3600'
      });
      res.end(fileData);
      return;
    }

    // Default fallback to index.html
    const indexPath = path.join(__dirname, 'index.html');
    if (fs.existsSync(indexPath)) {
      const indexData = fs.readFileSync(indexPath);
      res.writeHead(200, {
        'Content-Type': 'text/html; charset=UTF-8',
        'Cache-Control': 'public, max-age=3600'
      });
      res.end(indexData);
      return;
    }

    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  } catch (err) {
    console.error('Server error:', err);
    res.writeHead(500, { 'Content-Type': 'text/plain' });
    res.end('Server Error');
  }
}

if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  const server = http.createServer(handler);
  server.listen(PORT, () => {
    console.log(`Rajeshwari Boys Mess server running at http://localhost:${PORT}`);
  });
}

module.exports = handler;
